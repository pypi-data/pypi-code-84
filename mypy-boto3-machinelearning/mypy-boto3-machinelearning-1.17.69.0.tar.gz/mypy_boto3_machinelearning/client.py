"""
Type annotations for machinelearning service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_machinelearning import MachineLearningClient

    client: MachineLearningClient = boto3.client("machinelearning")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_machinelearning.literals import (
    BatchPredictionFilterVariable,
    DataSourceFilterVariable,
    EvaluationFilterVariable,
    MLModelFilterVariable,
    MLModelType,
    SortOrder,
    TaggableResourceType,
)
from mypy_boto3_machinelearning.paginator import (
    DescribeBatchPredictionsPaginator,
    DescribeDataSourcesPaginator,
    DescribeEvaluationsPaginator,
    DescribeMLModelsPaginator,
)
from mypy_boto3_machinelearning.type_defs import (
    AddTagsOutputTypeDef,
    CreateBatchPredictionOutputTypeDef,
    CreateDataSourceFromRDSOutputTypeDef,
    CreateDataSourceFromRedshiftOutputTypeDef,
    CreateDataSourceFromS3OutputTypeDef,
    CreateEvaluationOutputTypeDef,
    CreateMLModelOutputTypeDef,
    CreateRealtimeEndpointOutputTypeDef,
    DeleteBatchPredictionOutputTypeDef,
    DeleteDataSourceOutputTypeDef,
    DeleteEvaluationOutputTypeDef,
    DeleteMLModelOutputTypeDef,
    DeleteRealtimeEndpointOutputTypeDef,
    DeleteTagsOutputTypeDef,
    DescribeBatchPredictionsOutputTypeDef,
    DescribeDataSourcesOutputTypeDef,
    DescribeEvaluationsOutputTypeDef,
    DescribeMLModelsOutputTypeDef,
    DescribeTagsOutputTypeDef,
    GetBatchPredictionOutputTypeDef,
    GetDataSourceOutputTypeDef,
    GetEvaluationOutputTypeDef,
    GetMLModelOutputTypeDef,
    PredictOutputTypeDef,
    RDSDataSpecTypeDef,
    RedshiftDataSpecTypeDef,
    S3DataSpecTypeDef,
    TagTypeDef,
    UpdateBatchPredictionOutputTypeDef,
    UpdateDataSourceOutputTypeDef,
    UpdateEvaluationOutputTypeDef,
    UpdateMLModelOutputTypeDef,
)
from mypy_boto3_machinelearning.waiter import (
    BatchPredictionAvailableWaiter,
    DataSourceAvailableWaiter,
    EvaluationAvailableWaiter,
    MLModelAvailableWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MachineLearningClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    IdempotentParameterMismatchException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    InvalidTagException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    PredictorNotMountedException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TagLimitExceededException: Type[BotocoreClientError]


class MachineLearningClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_tags(
        self, Tags: List["TagTypeDef"], ResourceId: str, ResourceType: TaggableResourceType
    ) -> AddTagsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.add_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#add-tags)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#can-paginate)
        """

    def create_batch_prediction(
        self,
        BatchPredictionId: str,
        MLModelId: str,
        BatchPredictionDataSourceId: str,
        OutputUri: str,
        BatchPredictionName: str = None,
    ) -> CreateBatchPredictionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.create_batch_prediction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#create-batch-prediction)
        """

    def create_data_source_from_rds(
        self,
        DataSourceId: str,
        RDSData: RDSDataSpecTypeDef,
        RoleARN: str,
        DataSourceName: str = None,
        ComputeStatistics: bool = None,
    ) -> CreateDataSourceFromRDSOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.create_data_source_from_rds)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#create-data-source-from-rds)
        """

    def create_data_source_from_redshift(
        self,
        DataSourceId: str,
        DataSpec: RedshiftDataSpecTypeDef,
        RoleARN: str,
        DataSourceName: str = None,
        ComputeStatistics: bool = None,
    ) -> CreateDataSourceFromRedshiftOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.create_data_source_from_redshift)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#create-data-source-from-redshift)
        """

    def create_data_source_from_s3(
        self,
        DataSourceId: str,
        DataSpec: S3DataSpecTypeDef,
        DataSourceName: str = None,
        ComputeStatistics: bool = None,
    ) -> CreateDataSourceFromS3OutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.create_data_source_from_s3)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#create-data-source-from-s3)
        """

    def create_evaluation(
        self,
        EvaluationId: str,
        MLModelId: str,
        EvaluationDataSourceId: str,
        EvaluationName: str = None,
    ) -> CreateEvaluationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.create_evaluation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#create-evaluation)
        """

    def create_ml_model(
        self,
        MLModelId: str,
        MLModelType: MLModelType,
        TrainingDataSourceId: str,
        MLModelName: str = None,
        Parameters: Dict[str, str] = None,
        Recipe: str = None,
        RecipeUri: str = None,
    ) -> CreateMLModelOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.create_ml_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#create-ml-model)
        """

    def create_realtime_endpoint(self, MLModelId: str) -> CreateRealtimeEndpointOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.create_realtime_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#create-realtime-endpoint)
        """

    def delete_batch_prediction(self, BatchPredictionId: str) -> DeleteBatchPredictionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.delete_batch_prediction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#delete-batch-prediction)
        """

    def delete_data_source(self, DataSourceId: str) -> DeleteDataSourceOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.delete_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#delete-data-source)
        """

    def delete_evaluation(self, EvaluationId: str) -> DeleteEvaluationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.delete_evaluation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#delete-evaluation)
        """

    def delete_ml_model(self, MLModelId: str) -> DeleteMLModelOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.delete_ml_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#delete-ml-model)
        """

    def delete_realtime_endpoint(self, MLModelId: str) -> DeleteRealtimeEndpointOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.delete_realtime_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#delete-realtime-endpoint)
        """

    def delete_tags(
        self, TagKeys: List[str], ResourceId: str, ResourceType: TaggableResourceType
    ) -> DeleteTagsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.delete_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#delete-tags)
        """

    def describe_batch_predictions(
        self,
        FilterVariable: BatchPredictionFilterVariable = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: SortOrder = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> DescribeBatchPredictionsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.describe_batch_predictions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#describe-batch-predictions)
        """

    def describe_data_sources(
        self,
        FilterVariable: DataSourceFilterVariable = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: SortOrder = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> DescribeDataSourcesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.describe_data_sources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#describe-data-sources)
        """

    def describe_evaluations(
        self,
        FilterVariable: EvaluationFilterVariable = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: SortOrder = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> DescribeEvaluationsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.describe_evaluations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#describe-evaluations)
        """

    def describe_ml_models(
        self,
        FilterVariable: MLModelFilterVariable = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: SortOrder = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> DescribeMLModelsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.describe_ml_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#describe-ml-models)
        """

    def describe_tags(
        self, ResourceId: str, ResourceType: TaggableResourceType
    ) -> DescribeTagsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.describe_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#describe-tags)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#generate-presigned-url)
        """

    def get_batch_prediction(self, BatchPredictionId: str) -> GetBatchPredictionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.get_batch_prediction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#get-batch-prediction)
        """

    def get_data_source(
        self, DataSourceId: str, Verbose: bool = None
    ) -> GetDataSourceOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.get_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#get-data-source)
        """

    def get_evaluation(self, EvaluationId: str) -> GetEvaluationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.get_evaluation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#get-evaluation)
        """

    def get_ml_model(self, MLModelId: str, Verbose: bool = None) -> GetMLModelOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.get_ml_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#get-ml-model)
        """

    def predict(
        self, MLModelId: str, Record: Dict[str, str], PredictEndpoint: str
    ) -> PredictOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.predict)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#predict)
        """

    def update_batch_prediction(
        self, BatchPredictionId: str, BatchPredictionName: str
    ) -> UpdateBatchPredictionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.update_batch_prediction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#update-batch-prediction)
        """

    def update_data_source(
        self, DataSourceId: str, DataSourceName: str
    ) -> UpdateDataSourceOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.update_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#update-data-source)
        """

    def update_evaluation(
        self, EvaluationId: str, EvaluationName: str
    ) -> UpdateEvaluationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.update_evaluation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#update-evaluation)
        """

    def update_ml_model(
        self, MLModelId: str, MLModelName: str = None, ScoreThreshold: float = None
    ) -> UpdateMLModelOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Client.update_ml_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#update-ml-model)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_batch_predictions"]
    ) -> DescribeBatchPredictionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeBatchPredictions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/paginators.html#describebatchpredictionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_data_sources"]
    ) -> DescribeDataSourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeDataSources)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/paginators.html#describedatasourcespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_evaluations"]
    ) -> DescribeEvaluationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeEvaluations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/paginators.html#describeevaluationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_ml_models"]
    ) -> DescribeMLModelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeMLModels)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/paginators.html#describemlmodelspaginator)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["batch_prediction_available"]
    ) -> BatchPredictionAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Waiter.batch_prediction_available)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/waiters.html#batchpredictionavailablewaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["data_source_available"]
    ) -> DataSourceAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Waiter.data_source_available)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/waiters.html#datasourceavailablewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["evaluation_available"]) -> EvaluationAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Waiter.evaluation_available)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/waiters.html#evaluationavailablewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["ml_model_available"]) -> MLModelAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/machinelearning.html#MachineLearning.Waiter.ml_model_available)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/waiters.html#mlmodelavailablewaiter)
        """
