"""
Type annotations for synthetics service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_synthetics import SyntheticsClient

    client: SyntheticsClient = boto3.client("synthetics")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_synthetics.type_defs import (
    CanaryCodeInputTypeDef,
    CanaryRunConfigInputTypeDef,
    CanaryScheduleInputTypeDef,
    CreateCanaryResponseTypeDef,
    DescribeCanariesLastRunResponseTypeDef,
    DescribeCanariesResponseTypeDef,
    DescribeRuntimeVersionsResponseTypeDef,
    GetCanaryResponseTypeDef,
    GetCanaryRunsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    VpcConfigInputTypeDef,
)

__all__ = ("SyntheticsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class SyntheticsClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/synthetics.html#Synthetics.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/synthetics.html#Synthetics.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#can-paginate)
        """

    def create_canary(
        self,
        Name: str,
        Code: CanaryCodeInputTypeDef,
        ArtifactS3Location: str,
        ExecutionRoleArn: str,
        Schedule: CanaryScheduleInputTypeDef,
        RuntimeVersion: str,
        RunConfig: CanaryRunConfigInputTypeDef = None,
        SuccessRetentionPeriodInDays: int = None,
        FailureRetentionPeriodInDays: int = None,
        VpcConfig: VpcConfigInputTypeDef = None,
        Tags: Dict[str, str] = None,
    ) -> CreateCanaryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/synthetics.html#Synthetics.Client.create_canary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#create-canary)
        """

    def delete_canary(self, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/synthetics.html#Synthetics.Client.delete_canary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#delete-canary)
        """

    def describe_canaries(
        self, NextToken: str = None, MaxResults: int = None
    ) -> DescribeCanariesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/synthetics.html#Synthetics.Client.describe_canaries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#describe-canaries)
        """

    def describe_canaries_last_run(
        self, NextToken: str = None, MaxResults: int = None
    ) -> DescribeCanariesLastRunResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/synthetics.html#Synthetics.Client.describe_canaries_last_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#describe-canaries-last-run)
        """

    def describe_runtime_versions(
        self, NextToken: str = None, MaxResults: int = None
    ) -> DescribeRuntimeVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/synthetics.html#Synthetics.Client.describe_runtime_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#describe-runtime-versions)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/synthetics.html#Synthetics.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#generate-presigned-url)
        """

    def get_canary(self, Name: str) -> GetCanaryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/synthetics.html#Synthetics.Client.get_canary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#get-canary)
        """

    def get_canary_runs(
        self, Name: str, NextToken: str = None, MaxResults: int = None
    ) -> GetCanaryRunsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/synthetics.html#Synthetics.Client.get_canary_runs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#get-canary-runs)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/synthetics.html#Synthetics.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#list-tags-for-resource)
        """

    def start_canary(self, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/synthetics.html#Synthetics.Client.start_canary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#start-canary)
        """

    def stop_canary(self, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/synthetics.html#Synthetics.Client.stop_canary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#stop-canary)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/synthetics.html#Synthetics.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#tag-resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/synthetics.html#Synthetics.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#untag-resource)
        """

    def update_canary(
        self,
        Name: str,
        Code: CanaryCodeInputTypeDef = None,
        ExecutionRoleArn: str = None,
        RuntimeVersion: str = None,
        Schedule: CanaryScheduleInputTypeDef = None,
        RunConfig: CanaryRunConfigInputTypeDef = None,
        SuccessRetentionPeriodInDays: int = None,
        FailureRetentionPeriodInDays: int = None,
        VpcConfig: VpcConfigInputTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/synthetics.html#Synthetics.Client.update_canary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#update-canary)
        """
