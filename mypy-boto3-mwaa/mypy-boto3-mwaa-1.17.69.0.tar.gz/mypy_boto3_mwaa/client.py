"""
Type annotations for mwaa service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_mwaa import MWAAClient

    client: MWAAClient = boto3.client("mwaa")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_mwaa.literals import WebserverAccessMode
from mypy_boto3_mwaa.paginator import ListEnvironmentsPaginator
from mypy_boto3_mwaa.type_defs import (
    CreateCliTokenResponseTypeDef,
    CreateEnvironmentOutputTypeDef,
    CreateWebLoginTokenResponseTypeDef,
    GetEnvironmentOutputTypeDef,
    ListEnvironmentsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    LoggingConfigurationInputTypeDef,
    MetricDatumTypeDef,
    NetworkConfigurationTypeDef,
    UpdateEnvironmentOutputTypeDef,
    UpdateNetworkConfigurationInputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MWAAClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class MWAAClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mwaa.html#MWAA.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mwaa.html#MWAA.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#can-paginate)
        """

    def create_cli_token(self, Name: str) -> CreateCliTokenResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mwaa.html#MWAA.Client.create_cli_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#create-cli-token)
        """

    def create_environment(
        self,
        DagS3Path: str,
        ExecutionRoleArn: str,
        Name: str,
        NetworkConfiguration: "NetworkConfigurationTypeDef",
        SourceBucketArn: str,
        AirflowConfigurationOptions: Dict[str, str] = None,
        AirflowVersion: str = None,
        EnvironmentClass: str = None,
        KmsKey: str = None,
        LoggingConfiguration: LoggingConfigurationInputTypeDef = None,
        MaxWorkers: int = None,
        MinWorkers: int = None,
        PluginsS3ObjectVersion: str = None,
        PluginsS3Path: str = None,
        RequirementsS3ObjectVersion: str = None,
        RequirementsS3Path: str = None,
        Tags: Dict[str, str] = None,
        WebserverAccessMode: WebserverAccessMode = None,
        WeeklyMaintenanceWindowStart: str = None,
    ) -> CreateEnvironmentOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mwaa.html#MWAA.Client.create_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#create-environment)
        """

    def create_web_login_token(self, Name: str) -> CreateWebLoginTokenResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mwaa.html#MWAA.Client.create_web_login_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#create-web-login-token)
        """

    def delete_environment(self, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mwaa.html#MWAA.Client.delete_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#delete-environment)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mwaa.html#MWAA.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#generate-presigned-url)
        """

    def get_environment(self, Name: str) -> GetEnvironmentOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mwaa.html#MWAA.Client.get_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#get-environment)
        """

    def list_environments(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListEnvironmentsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mwaa.html#MWAA.Client.list_environments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#list-environments)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mwaa.html#MWAA.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#list-tags-for-resource)
        """

    def publish_metrics(
        self, EnvironmentName: str, MetricData: List[MetricDatumTypeDef]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mwaa.html#MWAA.Client.publish_metrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#publish-metrics)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mwaa.html#MWAA.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#tag-resource)
        """

    def untag_resource(self, ResourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mwaa.html#MWAA.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#untag-resource)
        """

    def update_environment(
        self,
        Name: str,
        AirflowConfigurationOptions: Dict[str, str] = None,
        AirflowVersion: str = None,
        DagS3Path: str = None,
        EnvironmentClass: str = None,
        ExecutionRoleArn: str = None,
        LoggingConfiguration: LoggingConfigurationInputTypeDef = None,
        MaxWorkers: int = None,
        MinWorkers: int = None,
        NetworkConfiguration: UpdateNetworkConfigurationInputTypeDef = None,
        PluginsS3ObjectVersion: str = None,
        PluginsS3Path: str = None,
        RequirementsS3ObjectVersion: str = None,
        RequirementsS3Path: str = None,
        SourceBucketArn: str = None,
        WebserverAccessMode: WebserverAccessMode = None,
        WeeklyMaintenanceWindowStart: str = None,
    ) -> UpdateEnvironmentOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mwaa.html#MWAA.Client.update_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#update-environment)
        """

    def get_paginator(
        self, operation_name: Literal["list_environments"]
    ) -> ListEnvironmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mwaa.html#MWAA.Paginator.ListEnvironments)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/paginators.html#listenvironmentspaginator)
        """
