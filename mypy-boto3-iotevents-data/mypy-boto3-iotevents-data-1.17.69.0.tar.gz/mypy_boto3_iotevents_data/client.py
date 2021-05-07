"""
Type annotations for iotevents-data service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_iotevents_data import IoTEventsDataClient

    client: IoTEventsDataClient = boto3.client("iotevents-data")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_iotevents_data.type_defs import (
    BatchPutMessageResponseTypeDef,
    BatchUpdateDetectorResponseTypeDef,
    DescribeDetectorResponseTypeDef,
    ListDetectorsResponseTypeDef,
    MessageTypeDef,
    UpdateDetectorRequestTypeDef,
)

__all__ = ("IoTEventsDataClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]


class IoTEventsDataClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iotevents-data.html#IoTEventsData.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_put_message(self, messages: List[MessageTypeDef]) -> BatchPutMessageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iotevents-data.html#IoTEventsData.Client.batch_put_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client.html#batch-put-message)
        """

    def batch_update_detector(
        self, detectors: List[UpdateDetectorRequestTypeDef]
    ) -> BatchUpdateDetectorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iotevents-data.html#IoTEventsData.Client.batch_update_detector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client.html#batch-update-detector)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iotevents-data.html#IoTEventsData.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client.html#can-paginate)
        """

    def describe_detector(
        self, detectorModelName: str, keyValue: str = None
    ) -> DescribeDetectorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iotevents-data.html#IoTEventsData.Client.describe_detector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client.html#describe-detector)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iotevents-data.html#IoTEventsData.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client.html#generate-presigned-url)
        """

    def list_detectors(
        self,
        detectorModelName: str,
        stateName: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListDetectorsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iotevents-data.html#IoTEventsData.Client.list_detectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client.html#list-detectors)
        """
