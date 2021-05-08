from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Type, TypeVar, Generic, Tuple, Optional

from paiargparse import pai_dataclass
from tensorflow import keras


@pai_dataclass
@dataclass
class IntVec2D:
    x: int
    y: int

    def to_tuple(self) -> Tuple[int, int]:
        return self.x, self.y


@pai_dataclass
@dataclass
class LayerParams(ABC):
    name: Optional[str] = None

    @classmethod
    @abstractmethod
    def cls(cls) -> Type['Layer']:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def name_prefix(cls) -> str:
        raise NotImplementedError

    def create(self) -> 'Layer':
        return self.cls()(self)

    def downscale(self, size: IntVec2D) -> IntVec2D:
        return size

    def downscale_factor(self, factor: IntVec2D) -> IntVec2D:
        return factor


TLayerParams = TypeVar("TLayerParams", bound=LayerParams)


class Layer(Generic[TLayerParams], keras.layers.Layer, ABC):
    def __init__(self, params: TLayerParams, **kwargs):
        super().__init__(name=params.name, **kwargs)
        self.params = params

    @abstractmethod
    def input_dims(self) -> int:
        raise NotImplementedError

    def call(self, inputs, **kwargs):
        if self.input_dims() != -1 and self.input_dims() != len(inputs.shape):
            if self.input_dims() == 3:
                # lstm like, TxBxF
                ds = keras.backend.shape(inputs)
                ss = inputs.shape
                inputs = keras.backend.reshape(inputs, (ds[0], ds[1], ss[2] * ss[3]))
            elif self.input_dims() == 4:
                # cnn like, BxTxHxW
                raise NotImplementedError
            else:
                raise NotImplementedError
        return self._call(inputs, **kwargs)

    @abstractmethod
    def _call(self, inputs, **kwargs):
        raise NotImplementedError
