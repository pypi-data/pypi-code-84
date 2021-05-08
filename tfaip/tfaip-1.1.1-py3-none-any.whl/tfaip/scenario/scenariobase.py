# Copyright 2021 The tfaip authors. All Rights Reserved.
#
# This file is part of tfaip.
#
# tfaip is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# tfaip is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# tfaip. If not, see http://www.gnu.org/licenses/.
# ==============================================================================
"""Definition of ScenarioBase"""
import importlib
import inspect
import json
import logging
import os
import re
import tempfile
from abc import ABC
from collections import Counter
from contextlib import ExitStack
from dataclasses import dataclass
from itertools import chain
from typing import Type, TYPE_CHECKING, Tuple, List, Optional, Iterable, Dict, TypeVar, Generic, \
    NoReturn

import numpy as np
import tensorflow as tf
import tensorflow.keras as keras
from paiargparse import pai_dataclass
from tensorflow.python.keras.metrics import MeanMetricWrapper

from tfaip import DataGeneratorParams, ScenarioBaseParams
from tfaip import PipelineMode
from tfaip import EvaluatorParams
from tfaip import TrainerPipelineParamsBase
from tfaip.data.data import DataBase
from tfaip.evaluator.evaluator import EvaluatorBase
from tfaip.lav.multilav import MultiLAV
from tfaip.model.modelbase import ModelBase
from tfaip.scenario.scenariobaseparams import NetConfigParamsBase, NetConfigNodeSpec
from tfaip.scenario.util.keras_debug_model import KerasDebugModel
from tfaip.scenario.util.outputholder import OutputHolderMetricWrapper
from tfaip.scenario.util.print_evaluate_layer import PrintEvaluateLayer
from tfaip.scenario.util.print_model_structure import print_all_layers
from tfaip.util.generic_meta import CollectGenericTypes
from tfaip.util.tfaipargparse import post_init
from tfaip.util.tftyping import AnyTensor

if TYPE_CHECKING:
    from tfaip.imports import LAVParams, LAV, TrainerParams, Predictor, PredictorParams, MultiModelPredictor, \
    Trainer

logger = logging.getLogger(__name__)


def list_scenarios_in_module(module) -> List[Tuple[str, Type['ScenarioBase']]]:
    return inspect.getmembers(module, lambda member: inspect.isclass(member)
                                                     and member.__module__ == module.__name__
                                                     and issubclass(member, ScenarioBase)
                                                     and member != ScenarioBase
                                                     and 'ScenarioBase' not in member.__name__)


@pai_dataclass
@dataclass
class KerasModelData:
    """
    Utility structure to hold shared information about the model
    """
    extended_loss_names: List[str]
    extended_metric_names: List[str]
    tensorboard_output_names: List[str]


TData = TypeVar('TData', bound=DataBase)
TModel = TypeVar('TModel', bound=ModelBase)
TScenarioParams = TypeVar('TScenarioParams', bound=ScenarioBaseParams)
TTrainerPipelineParams = TypeVar('TTrainerPipelineParams', bound=TrainerPipelineParamsBase)


class ScenarioBaseMeta(CollectGenericTypes):
    pass


class ScenarioBase(Generic[TData, TModel, TScenarioParams, TTrainerPipelineParams], ABC, metaclass=ScenarioBaseMeta):
    """
    The scenario base handles the setup of the scenario including training and model exporting.

    Several abstract methods must be overridden that define how to create the Model, and Data for this scenario.
    If your scenario requires different default params in contrast to the values defined in the respective dataclasses,
    override default_params().
    Furthermore it is possible to change the Trainer or LAV class which is usually not required!

    A typical Scenario only requires to implement get_meta() and get_param_cls()
    To set scenario specific (hidden) parameters use the subclasses __init__ or override create_model()
    or create_data(). Note that create_model() will be called after create_data()!

    The metaclass of the Scenario (ScenarioBaseMeta) will track the types of the Generics which is then use to create
    instances of the actual types automatically (see, e.g., model_cls(), data_cls(), ...).

    Attributes:
        data (DataBase):  After setup() was called, the DataBase of the scenario
        model (ModelBase):  After setup() was called, the ModelBase of the scenario

    """

    @classmethod
    def default_params(cls) -> TScenarioParams:
        """
        Override to change the default parameters for this scenario.

        Returns: ScenarioParams with adapted defaults of the respective Scenario
        """
        scenario_params = cls.params_cls()()
        scenario_params.scenario_base_path = inspect.getfile(cls)
        scenario_params.scenario_id = cls.__module__ + ':' + cls.__name__
        scenario_params.model = cls.model_cls().params_cls()()
        scenario_params.data = cls.data_cls().default_params()
        scenario_params.evaluator = cls.evaluator_cls().default_params()
        return scenario_params

    @classmethod
    def default_trainer_params(cls) -> 'TrainerParams[TScenarioParams, TTrainerPipelineParams]':
        """
        Override to change the default trainer params for this scenario.

        Use this to override hyperparameters such as the learning rate.

        Returns: TrainerParams with adapted defaults
        """
        trainer_params = cls.trainer_cls().params_cls()()
        trainer_params.scenario = cls.default_params()
        trainer_params.gen = cls.trainer_pipeline_params_cls()()
        return trainer_params

    @classmethod
    def params_from_dict(cls, d: dict) -> TScenarioParams:
        """
        Instantiate ScenarioParams from a dict. Not that since all dataclasses are a pai_dataclass the actual
        ScenarioParams will be read from the __cls__ arg within the dict.

        See also:
            ScenarioBaseParams.from_dict
        Args:
            d: trainer or scenario params dict

        Returns: ScenarioParams of the respective Scenario
        """
        # Support to also pass trainer params
        if 'scenario' in d:
            d = d['scenario']
        return cls.params_cls().from_dict(d)

    @classmethod
    def params_from_path(cls, path: str) -> TScenarioParams:
        """
        Read params from a file path and construct the stored ScenarioParams

        See Also:
            params_from_dict, read_params_dict_from_path
        Args:
            path: path to the file or to the directory containin a trainer_params.json or scenario_params.json

        Returns:
            Parsed ScenarioParams
        """
        return cls.params_from_dict(cls.read_params_dict_from_path(path))

    @classmethod
    def read_params_dict_from_path(cls, path: str) -> dict:
        """
        Read a params dict from a path (or dictionary)

        See Also:
            params_from_path

        Args:
            path: path to the file or to the directory containin a trainer_params.json or scenario_params.json

        Returns:
            dict of ScenarioParams

        """
        path = os.path.abspath(path)  # make abspath
        if os.path.isfile(path):
            # already pointing to a file
            with open(path) as f:
                d = json.load(f)
                if 'scenario' in d:
                    scenario_params_dict = d['scenario']
                else:
                    scenario_params_dict = d

        else:
            # Search for trainer_params.json or scenario_params.json
            trainer_params_json_path = os.path.join(path, 'trainer_params.json')
            scenario_params_json_path = os.path.join(path, 'scenario_params.json')
            if os.path.exists(trainer_params_json_path):
                with open(trainer_params_json_path) as f:
                    scenario_params_dict = json.load(f)['scenario']
            elif os.path.exists(scenario_params_json_path):
                with open(scenario_params_json_path) as f:
                    scenario_params_dict = json.load(f)
            else:
                raise FileNotFoundError(f'Either {trainer_params_json_path} or {scenario_params_json_path} must exist!')

        # Adapt resource path. Resources are detected relative to the location of the params file
        scenario_params_dict['data']['resource_base_path'] = path
        return scenario_params_dict

    @classmethod
    def from_path(cls, path: str) -> Tuple[Type['ScenarioBase'], TScenarioParams]:
        """
        Instantiate a scenario from a path.

        Args:
            path: Path to the scenario_params.json or dictionary containing them

        Returns:
            Tuple of the actual Scenario class and the parsed Scenario params
        """
        if cls != ScenarioBase:
            raise ValueError('You are calling this method from a real Scenario class. Call params_from_path instead')
        return cls.from_dict(cls.read_params_dict_from_path(path))

    @classmethod
    def from_dict(cls, d: dict) -> Tuple[Type['ScenarioBase'], TScenarioParams]:
        """
        Instantiate a scenario from a dict.

        Args:
            d: Dict of the scenario_params.json or dictionary containing them

        Returns:
            Tuple of the actual Scenario class and the parsed Scenario params
        """
        if cls != ScenarioBase:
            raise ValueError('You are calling this method from a real Scenario class. Call params_from_dict instead')
        scenario_params: ScenarioBaseParams = ScenarioBaseParams.from_dict(d)
        return scenario_params.cls(), scenario_params

    @classmethod
    def data_cls(cls) -> Type[TData]:
        return cls.__generic_types__[TData.__name__]

    @classmethod
    def model_cls(cls) -> Type[TModel]:
        return cls.__generic_types__[TModel.__name__]

    @classmethod
    def trainer_cls(cls) -> Type['Trainer[TrainerParams]']:
        from tfaip.trainer.trainer import Trainer  # pylint: disable=import-outside-toplevel
        return Trainer

    @classmethod
    def lav_cls(cls) -> Type['LAV']:
        from tfaip.lav.lav import LAV  # pylint: disable=import-outside-toplevel
        return LAV

    @classmethod
    def multi_lav_cls(cls) -> Type['MultiLAV']:
        return MultiLAV

    @classmethod
    def predictor_cls(cls) -> Type['Predictor']:
        from tfaip.predict.predictor import Predictor  # pylint: disable=import-outside-toplevel
        return Predictor

    @classmethod
    def evaluator_cls(cls) -> Type['EvaluatorBase']:
        return EvaluatorBase

    @classmethod
    def multi_predictor_cls(cls) -> Type['MultiModelPredictor']:
        from tfaip.predict.multimodelpredictor import \
            MultiModelPredictor  # pylint: disable=import-outside-toplevel
        return MultiModelPredictor

    @classmethod
    def create_trainer(cls, trainer_params: 'TrainerParams', restore=False) -> 'Trainer':
        post_init(trainer_params)
        return cls.trainer_cls()(trainer_params, cls(trainer_params.scenario), restore)

    @classmethod
    def create_lav(cls, lav_params: 'LAVParams', scenario_params: TScenarioParams) -> 'LAV':
        post_init(lav_params)
        post_init(scenario_params)
        return cls.lav_cls()(lav_params,
                             data_fn=lambda: cls.data_cls()(scenario_params.data),
                             model_fn=lambda: cls.model_cls()(scenario_params.model),
                             predictor_fn=cls.predictor_cls(),
                             evaluator_fn=lambda: cls.create_evaluator(scenario_params.evaluator),
                             )

    @classmethod
    def create_multi_lav(cls, lav_params: 'LAVParams', scenario_params: TScenarioParams,
                         predictor_params: Optional['PredictorParams'] = None):
        post_init(lav_params)
        post_init(scenario_params)
        post_init(predictor_params)
        return MultiLAV(
            lav_params,
            cls.create_multi_predictor,
            cls.create_evaluator(scenario_params.evaluator),
            predictor_params=predictor_params or cls.multi_predictor_cls().params_cls()(),
        )

    @classmethod
    def create_predictor(cls, model: str, params: 'PredictorParams') -> 'Predictor':
        post_init(params)
        data_params = cls.params_from_path(model).data
        post_init(data_params)
        predictor = cls.predictor_cls()(params, cls.data_cls()(data_params))
        if isinstance(model, str):
            model = keras.models.load_model(os.path.join(model, 'serve'),
                                            compile=False,
                                            custom_objects=cls.model_cls().all_custom_objects(),
                                            )

        predictor.set_model(model)
        return predictor

    @classmethod
    def create_multi_predictor(cls, paths: List[str], params: 'PredictorParams') -> 'MultiModelPredictor':
        post_init(params)
        predictor_cls = cls.multi_predictor_cls()
        return predictor_cls.from_paths(paths, params, cls)

    @classmethod
    def create_evaluator(cls, params: EvaluatorParams) -> EvaluatorBase:
        post_init(params)
        if cls.evaluator_cls() is None:
            raise NotImplementedError
        return cls.evaluator_cls()(params)

    @classmethod
    def params_cls(cls) -> Type[TScenarioParams]:
        return cls.__generic_types__[TScenarioParams.__name__]

    @classmethod
    def trainer_pipeline_params_cls(cls) -> Type[TTrainerPipelineParams]:
        return cls.__generic_types__[TTrainerPipelineParams.__name__]

    @classmethod
    def predict_generator_params_cls(cls) -> Type[DataGeneratorParams]:
        return cls.trainer_pipeline_params_cls().val_cls()

    @staticmethod
    def net_config_cls() -> Type[NetConfigParamsBase]:
        return NetConfigParamsBase

    def __init__(self, params: TScenarioParams):
        self._params = params
        self._keras_model_data = KerasModelData([], [], [])
        self._keras_train_model: Optional[keras.Model] = None
        self._export_graphs: Dict[str, keras.Model] = {}
        self._keras_predict_model: Optional[keras.Model] = None
        self.data: Optional[TData] = None
        self.model: Optional[TModel] = None

    @property
    def params(self) -> TScenarioParams:
        return self._params

    @property
    def keras_train_model(self):
        return self._keras_train_model

    @property
    def keras_predict_model(self):
        return self._keras_predict_model

    def setup(self):
        if not self.data:
            self.data = self.create_data()

        if not self.model:
            self.model = self.create_model()

    def create_data(self) -> TData:
        return self.__class__.data_cls()(self._params.data)

    def create_model(self) -> TModel:
        return self.__class__.model_cls()(self._params.model)

    def print_params(self) -> NoReturn:
        """
        Print the ScenarioParams to logger.info
        """
        logger.info(f'scenario_params={self._params.to_json(indent=2)}')

    def best_logging_settings(self) -> Tuple[str, str]:
        """
        Returns: See ModelBase.best_logging_settings()
        """
        return self.model.best_logging_settings()

    def export(self, path: str, trainer_params: Optional['TrainerParams'] = None,
               export_resources: bool = True) -> NoReturn:
        """
        Export the prediction model to a given path

        Args:
            path: Directory where to export the model to
            trainer_params: if given export the full trainer params instead of the scenario params
            export_resources: Set to true (default) to also export the resources
        """
        trainer_params_dict = trainer_params.to_dict() if trainer_params else None
        scenario_params_dict = trainer_params_dict['scenario'] if trainer_params_dict else self._params.to_dict()
        if export_resources:
            self._export_resources(path, scenario_params_dict)

        # Export serve models
        if self._params.export_serve:
            for label, export_graph in self._export_graphs.items():
                if label == 'default':
                    path_serve = os.path.join(path, self._params.default_serve_dir)  # default model handled separately
                else:
                    path_serve = os.path.join(path, self._params.additional_serve_dir, label)
                os.makedirs(os.path.dirname(path_serve), exist_ok=True)
                export_graph.save(path_serve, include_optimizer=False)

        # Export the NetConfigBaseParams
        if self._params.export_net_config:
            with open(os.path.join(path, self._params.net_config_filename), 'w') as f:
                json.dump(self.net_config().to_dict(), f, indent=2)

        # Export the training or scenario params
        if trainer_params_dict:
            params_path = os.path.join(path, self._params.trainer_params_filename)
            logger.debug(f'Storing trainer params to {params_path}')
            with open(params_path, 'w') as f:
                json.dump(trainer_params_dict, f, indent=2)
        else:
            params_path = os.path.join(path, self._params.scenario_params_filename)
            with open(params_path, 'w') as f:
                json.dump(scenario_params_dict, f, indent=2)

    def _export_resources(self, root_path: str, scenario_params_dict: dict) -> NoReturn:
        """
        Export/Dump all resources of the scenario to an export dir.

        Args:
            root_path: Path where to export
            scenario_params_dict: parameters of the exported dir. Adapt paths within the dict to be relative
        """
        os.makedirs(os.path.join(root_path), exist_ok=True)
        self.data.dump_resources(root_path, scenario_params_dict['data'])  # export the data resources

    def _print_all_layer(self) -> NoReturn:
        """
        Print all model params in detail

        Note: the implementation was tested for Tensorflow 2.3 und 2.4 and might need updates in the future
        since private functions are used that are not part of the official API.

        Args:
        """
        print_all_layers(self._keras_train_model, logger.info)

    def _set_no_train_scope(self, regex: Optional[str]) -> NoReturn:
        """
        Internal function to disable training of some layers by setting layer.trainable = False

        Note: the implementation was tested for Tensorflow 2.3 und 2.4 and might need updates in the future
        since private functions are used that are not part of the official API.

        Args:
            regex: The regex to match on layer names which shall be excluded
        """
        if not regex:
            return

        logger.info(f'Setting no train scope to {regex}')
        no_train_scope = re.compile(regex)

        try:
            def _set_for_layer(layer, prefix):
                # Recursively loop through all layers, check if the full layer name (separated by /) matches the regex.
                for sub_layer in layer._flatten_layers(False, False):  # pylint: disable=protected-access
                    full_layer_name = prefix + '/' + sub_layer.name if prefix else sub_layer.name
                    if no_train_scope.fullmatch(full_layer_name):
                        logger.info(f'Excluding layer "{full_layer_name}" from training')
                        sub_layer.trainable = False
                    else:
                        # Only call recursively of it is trainable, since if the parent layer is not trainable
                        # all child layers are non-trainable automatically
                        _set_for_layer(sub_layer, full_layer_name)

            _set_for_layer(self._keras_train_model, '')
        except Exception as e:
            raise Exception('Setting no train scopes was designed for TF 2.4.0. '
                            'Maybe you use an incompatible version') from e

    def setup_training(self, optimizer, skip_model_load_test=False, run_eagerly=False,
                       no_train_scope: Optional[str] = None) -> NoReturn:
        """
        Set training by constructing the training and prediction keras Models.

        Args:
            optimizer: The optimizer to use for training
            skip_model_load_test: Skip the test checking if the prediction model can be stored and loaded
            run_eagerly: Run the model in eager mode
            no_train_scope: Regex to match layers to exclude from training
        """
        self.setup()

        real_inputs = self.data.create_input_layers()
        real_targets = self.data.create_target_as_input_layers()
        real_meta = self.data.create_meta_as_input_layers()

        if self._params.debug_graph_construction:
            # Debugging the construction of a graph
            #  - Create the prediction graph as actual keras Model (non-Functional API), see KerasDebugModel
            #  - Construct a training pipeline and compute the metrics and losses for one batch
            if not run_eagerly:
                raise ValueError(
                    'Setting debug_graph_construction requires --train_params force_eager=True')
            logger.info('Debugging Graph Construction. Breakpoints during construction are supported')
            # process one example in KerasDebugModel which builds the graph based on this example
            keras_debug_model = KerasDebugModel(self.model)
            with self.data.pipeline_by_mode(PipelineMode.TRAINING) as train_data:
                prev = tf.config.functions_run_eagerly()
                tf.config.run_functions_eagerly(run_eagerly)
                keras_debug_model({**real_inputs,
                                   **real_targets,
                                   **real_meta,
                                   'step': tf.keras.layers.Input(shape=[1], dtype=tf.int32),
                                   'epoch': tf.keras.layers.Input(shape=[1], dtype=tf.int32),
                                   })
                out = keras_debug_model.predict(
                    self._wrap_data(train_data.input_dataset(), steps_per_epoch=1,
                                    is_debug_data=True).take(
                        self._params.debug_graph_n_examples))
                tf.config.run_functions_eagerly(
                    prev)  # reset to allow for multiple calls with different mode
            logger.info('Mean values of debug model output: {}', {k: np.mean(v) for k, v in out.items()})

        # This regroups all inputs/targets as input to allow to access the complete data during training
        # This is required to allow for custom loss functions that require multiple inputs (e.g., ctc)
        # This code does:
        # * regroup all inputs/targets as inputs
        # * create loss based on all inputs (includes the gt) and the outputs of the network
        # * the loss itself is handled as "output" of the network, the actual loss function (.compile) just
        #   forwards the "output" loss, this requires to create empty dummy outputs for the loss
        # * see fit()
        #

        def assert_unique_keys(keys):
            non_unique = [k for k, v in Counter(keys).items() if v > 1]
            if len(non_unique) > 0:
                raise KeyError('Keys of input, outputs, and targets must be unique. '
                               f'The following keys occurr more than once: {set(non_unique)}')

        all_keys = list(chain(real_inputs.keys(), real_targets.keys(), real_meta.keys()))
        assert_unique_keys(all_keys)

        # all inputs (step and epoch shall have a dimension of [1])
        inputs_targets = {**real_inputs, **real_targets, **real_meta,
                          'step': keras.layers.Input([1], name='step', dtype='int32'),
                          'epoch': keras.layers.Input([1], name='epoch', dtype='int32')}

        # Inputs have already correct names (checked by data) for exporting
        # real_inputs = {k: v if v.op.name == k else keras.layers.Layer(name=k)(v) for k, v in real_inputs.items()}
        # network outputs (ignores the targets)
        logger.info('Building training graph')
        real_outputs = self.model.build(inputs_targets)
        assert_unique_keys(all_keys + list(real_outputs.keys()))

        logger.info('Building prediction graph')
        pred_outputs = self.model.build(real_inputs)
        assert_unique_keys(all_keys + list(real_outputs.keys()))

        # inject the evaluate layer to the first output.
        # Note, if the first output is not used in the graph, nothing will be printed
        pel_key = next(iter(real_outputs.keys()))
        logger.debug(f'Injecting print evaluate layer to output {pel_key}')
        if self._params.print_eval_limit != 0:
            pel = PrintEvaluateLayer(self, self._params.print_eval_limit)
            real_outputs[pel_key] = tf.identity(
                pel((real_outputs[pel_key], real_inputs, real_outputs, real_targets, real_meta)),
                name=pel_key + '_')

        # loss as "output" of the network but called separately for logic
        additional_outputs = self.model.additional_outputs(real_inputs, real_outputs)
        extended_outputs = {**real_outputs, **self.model.additional_outputs(real_inputs, real_outputs)}
        extended_losses = self.model.extended_loss(inputs_targets, extended_outputs)
        simple_losses = self.model.loss()
        extended_metrics = self.model.extended_metric(inputs_targets, extended_outputs)
        simple_metrics = self.model.metric()
        outputs = {
            **real_outputs, **extended_losses, **extended_metrics, **additional_outputs,
            **{k: extended_outputs[v.output] for k, v in simple_metrics.items()},
            **{k: extended_outputs[v.output] for k, v in simple_losses.items()}
        }
        tensorboard_outputs = self.model.tensorboard_handler.setup(real_inputs, real_outputs)

        # Store the information about the node names to wrap the dataset for (see fit())
        self._keras_model_data = KerasModelData(
            list(extended_losses.keys()),
            list(extended_metrics.keys()),
            list(tensorboard_outputs.keys()),
        )

        # create the model (and a second one for exporting)
        logger.info('Building training keras model')
        self._keras_train_model = keras.Model(inputs=inputs_targets, outputs=outputs)
        logger.info('Attempting to set no train scope')
        self._set_no_train_scope(no_train_scope)  # exclude layers from training
        logger.info('Building prediction/export keras model (for export and decoding)')
        self._export_graphs = self.model.export_graphs(real_inputs, pred_outputs, real_targets)
        self._keras_predict_model = self._export_graphs['default']

        # compile the model but with a dummy loss that just returns the 'output' loss
        # the same goes for the metric
        def wrap_loss(_, p):
            return p

        logger.info('Compiling training model including optimization')
        loss_weights = self.model.loss_weights()
        loss_names = list(extended_losses.keys()) + list(simple_losses.keys())
        if loss_weights is not None:
            for k in loss_weights.keys():
                if k not in loss_names:
                    raise KeyError(
                        f'Loss weight {k} specified but not used in losses (available {loss_names}).')

        # Compile the actual model
        # - the loss comprises the actual (joined) losses of the model
        # - the weighted metrics comprises the actual (joined) metrics of the model
        # - the "metrics" are abused for additional tensorboard output (NOT ACTUAL METRICS)
        #   The additional outputs (as defined in the model) will be treated as a metric so that they are written to
        #   the logs. Callbacks will extract these "metrics" and pass them to the Tensorboard-handler
        self._keras_train_model.compile(
            optimizer=optimizer,
            loss={
                **{k: wrap_loss for k, _ in extended_losses.items()},
                **{k: v.loss for k, v in simple_losses.items()},
            },
            loss_weights=self.model.loss_weights(),
            metrics={
                k: OutputHolderMetricWrapper(v.shape, v.dtype, self._params.tensorboard_logger_history_size, name=k) for
                k, v in tensorboard_outputs.items()
            },
            weighted_metrics={
                **{k: MeanMetricWrapper(lambda t, p: p, name=k) for k, _ in extended_metrics.items()},
                **{k: v.metric for k, v in simple_metrics.items()}
            },
            run_eagerly=run_eagerly,
        )
        logger.info('Compiling prediction model graph')
        self._keras_predict_model.compile(run_eagerly=True)
        logger.info('Models successfully constructed')

        # check if loading/saving of model works (before actual training)
        if not skip_model_load_test:
            logger.info('Checking if model can be saved')
            with tempfile.TemporaryDirectory() as tmp:
                self._keras_predict_model.save(tmp)
                logger.info('Prediction model successfully saved. Attempting to load it')
                keras.models.load_model(tmp)
            logger.info('Model can be successfully loaded')

    def _wrap_data(self, dataset: Optional[tf.data.Dataset], steps_per_epoch: int, is_debug_data: bool = False) -> \
            Optional[tf.data.Dataset]:
        """
        Wrap the tf.data.Dataset:
          - add step and epoch as input node
          - Comprise inputs and targets as "full input" of the model
          - Add dummy nodes for losses and metrics
          - Wrap the sample weights similarly (third output)

        Args:
            dataset:  The dataset to wrap.
            steps_per_epoch: the number of steps per epoch
            is_debug_data: Wrapping is modified for the debugging of the graph construction
        Returns:
            the wrapped tf.data.Dataset or None if dataset was already None
        """
        if dataset is None:
            return None

        # wrapper for model fit (allows for other arguments)
        def regroup(inputs: Dict[str, AnyTensor], targets: Dict[str, AnyTensor], meta: Dict[str, AnyTensor]):
            # meta is unused for training
            batch_size = tf.shape(next(iter(inputs.values() if len(inputs) > 0 else targets.values())))[0]
            # see setup_training
            # regroup data for training into all as input, and only loss and metrics as output
            # this is required to allow for custom losses with multiple inputs
            zeros = tf.repeat(tf.constant(0, dtype=tf.int64), batch_size)
            if self._keras_train_model:
                step_epoch = {'step': zeros + self._keras_train_model.optimizer.iterations,
                              'epoch': zeros + self._keras_train_model.optimizer.iterations // steps_per_epoch}
            else:
                # No train model exists, this happens on model debug
                step_epoch = {'step': zeros,
                              'epoch': zeros}
            wrapped_inputs = {**inputs, **targets, **meta, **step_epoch}
            wrapped_targets = {**{l: zeros for l in
                                  self._keras_model_data.extended_loss_names +
                                  self._keras_model_data.extended_metric_names +
                                  self._keras_model_data.tensorboard_output_names
                                  },
                               **{k: targets[v.target] for k, v in self.model.metric().items() if v.target in targets},
                               **{k: targets[v.target] for k, v in self.model.loss().items() if v.target in targets},
                               }
            if is_debug_data:
                wrapped_weights = None
            else:
                wrapped_weights = self.model.sample_weights(inputs, targets)
                for k in wrapped_weights.keys():
                    if k not in wrapped_targets.keys():
                        raise KeyError(f'Sample weight {k} given but not found in targets (metric). '
                                       f'Available: {list(wrapped_targets.keys())}')
            return wrapped_inputs, wrapped_targets, wrapped_weights

        return dataset.map(regroup)

    def fit(self,
            epochs,
            callbacks,
            steps_per_epoch,
            initial_epoch=0,
            **kwargs) -> NoReturn:
        """
        Train the scenario.

        This function will create the training and optionally validation pipelines, and call fit of the keras model.

        Args:
            epochs: The number of epochs to train
            callbacks: Callbacks of training
            steps_per_epoch: Number of steps per epoch
            initial_epoch: Initial epoch (use if resuming the training)
            **kwargs: Additional args passed to keras.Model.fit
        """
        self._print_all_layer()

        with ExitStack() as stack:
            # Fill the exit stack that collects `__enter__` of all pipelines that are created.
            # This ensures that all subthreads are joined when training is finished.
            train_dataset = stack.enter_context(self.data.pipeline_by_mode(PipelineMode.TRAINING)).input_dataset()
            if self.data.pipeline_by_mode(PipelineMode.EVALUATION) is not None:
                val_dataset = stack.enter_context(self.data.pipeline_by_mode(PipelineMode.EVALUATION)).input_dataset()
            else:
                logger.warning('Training without validation.')
                val_dataset = None

            # Train the model
            self._keras_train_model.fit(self._wrap_data(train_dataset, steps_per_epoch),
                                        epochs=epochs,
                                        callbacks=callbacks,
                                        steps_per_epoch=steps_per_epoch,
                                        initial_epoch=initial_epoch,
                                        validation_data=self._wrap_data(val_dataset, steps_per_epoch),
                                        shuffle=False,
                                        **kwargs
                                        )

    def net_config(self) -> NetConfigParamsBase:
        """
        Create the NetConfigParams for this scenario.

        Usually a custom Scenario should override net_config_cls() and _fill_net_config()
        instead of overwriting this function.

        Returns:
            NetConfigParamsBase
        """

        def parse_spec(nodes, is_input):
            # TODO Evaluate whether the naming of in/out tensors could be inferred somehow...
            # For keras model no idea yet... even dir(XY) didn't helped
            # However, this 'solution' should work for NOW
            res = dict()
            if is_input:
                base_name_serve = 'serving_default_'
            else:
                base_name_serve = 'StatefulPartitionedCall:'

            for idx, k in enumerate(sorted(nodes.keys())):
                v = nodes[k]
                node_serve = base_name_serve
                if is_input:
                    node_serve += k + ':0'
                else:
                    node_serve += str(idx)

                res[k] = NetConfigNodeSpec(
                    shape=list(map(str, v.shape.dims)) if isinstance(v.shape.dims, Iterable) else [],
                    dtype=v.dtype.name,
                    node_serve=node_serve
                )
            return res

        # Create the actual class with the parsed spects
        net_config = self.__class__.net_config_cls()(
            id_model=self.params.id,
            id_serve='serve',
            in_nodes=parse_spec(self._keras_predict_model.input, True),
            out_nodes=parse_spec(self._keras_predict_model.output, False),
            tf_version=tf.__version__,
        )

        self._fill_net_config(net_config)  # Fill the net config with custom parameters
        return net_config

    def _fill_net_config(self, net_config: NetConfigParamsBase) -> NoReturn:
        """
        Overwrite to set additional net config params
        Args:
            net_config: NotConfigParamsBase (of possibly custom type) to fill
        """
        pass


def import_scenario(module_name: str) -> Type['ScenarioBase']:
    """
    module_name can either be:
    - module and class name separated by a ':', e.g.: tfaip.scenarios.tutorial.min.scenario:TutorialScenario
    - module containing one class inheriting ScenarioBase, e.g.: tfaip.scenarios.tutorial.min.scenario
    - module containing containing a scenario module that contains one class inheriting ScenarioBase, e.g.: tfaip.scenarios.tutorial.min
    """
    def import_module(module_path_or_name: str):
        import sys
        import os
        if os.getcwd() not in sys.path:
            sys.path.append(os.getcwd())
        try:
            return importlib.import_module(module_path_or_name.replace('/', '.'))
        except ModuleNotFoundError:
            raise ModuleNotFoundError(f"No module named '{module_path_or_name}'. Please specify the full module to "
                                      f"import or a relative path of the working directory. "
                                      f"E.g.: tfaip.scenario.tutorial.full")

    if ':' in module_name:
        module_path, scenario_class_name = module_name.split(':')
        module = import_module(module_path.replace('/', '.'))
        return getattr(module, scenario_class_name)

    module = import_module(module_name.replace('/', '.'))
    all_scenario_cls = list_scenarios_in_module(module)
    if len(all_scenario_cls) == 0:
        # No scenarios found, try module_name + '.scenario'
        if module_name.endswith('.scenario'):
            raise ModuleNotFoundError(f"No scenario found in module {module_name}")
        else:
            return import_scenario(module_name + '.scenario')
    else:
        if len(all_scenario_cls) > 1:
            raise ValueError(f"Multiple scenarios found in module {module_name}. Append the Scenario name to select "
                             f"one specific ({module_name}:NAME_OF_SCENARIO). "
                             f"Found scenarios: {', '.join([s[0] for s in all_scenario_cls])}")

        return all_scenario_cls[0][1]
