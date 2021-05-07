"""
Type annotations for mq service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_mq import MQClient

    client: MQClient = boto3.client("mq")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_mq.literals import (
    AuthenticationStrategy,
    BrokerStorageType,
    DeploymentMode,
    EngineType,
)
from mypy_boto3_mq.paginator import ListBrokersPaginator
from mypy_boto3_mq.type_defs import (
    ConfigurationIdTypeDef,
    CreateBrokerResponseTypeDef,
    CreateConfigurationResponseTypeDef,
    DeleteBrokerResponseTypeDef,
    DescribeBrokerEngineTypesResponseTypeDef,
    DescribeBrokerInstanceOptionsResponseTypeDef,
    DescribeBrokerResponseTypeDef,
    DescribeConfigurationResponseTypeDef,
    DescribeConfigurationRevisionResponseTypeDef,
    DescribeUserResponseTypeDef,
    EncryptionOptionsTypeDef,
    LdapServerMetadataInputTypeDef,
    ListBrokersResponseTypeDef,
    ListConfigurationRevisionsResponseTypeDef,
    ListConfigurationsResponseTypeDef,
    ListTagsResponseTypeDef,
    ListUsersResponseTypeDef,
    LogsTypeDef,
    UpdateBrokerResponseTypeDef,
    UpdateConfigurationResponseTypeDef,
    UserTypeDef,
    WeeklyStartTimeTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MQClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]


class MQClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mq.html#MQ.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mq.html#MQ.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#can-paginate)
        """

    def create_broker(
        self,
        AuthenticationStrategy: AuthenticationStrategy = None,
        AutoMinorVersionUpgrade: bool = None,
        BrokerName: str = None,
        Configuration: "ConfigurationIdTypeDef" = None,
        CreatorRequestId: str = None,
        DeploymentMode: DeploymentMode = None,
        EncryptionOptions: "EncryptionOptionsTypeDef" = None,
        EngineType: EngineType = None,
        EngineVersion: str = None,
        HostInstanceType: str = None,
        LdapServerMetadata: LdapServerMetadataInputTypeDef = None,
        Logs: "LogsTypeDef" = None,
        MaintenanceWindowStartTime: "WeeklyStartTimeTypeDef" = None,
        PubliclyAccessible: bool = None,
        SecurityGroups: List[str] = None,
        StorageType: BrokerStorageType = None,
        SubnetIds: List[str] = None,
        Tags: Dict[str, str] = None,
        Users: List[UserTypeDef] = None,
    ) -> CreateBrokerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mq.html#MQ.Client.create_broker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#create-broker)
        """

    def create_configuration(
        self,
        AuthenticationStrategy: AuthenticationStrategy = None,
        EngineType: EngineType = None,
        EngineVersion: str = None,
        Name: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mq.html#MQ.Client.create_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#create-configuration)
        """

    def create_tags(self, ResourceArn: str, Tags: Dict[str, str] = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mq.html#MQ.Client.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#create-tags)
        """

    def create_user(
        self,
        BrokerId: str,
        Username: str,
        ConsoleAccess: bool = None,
        Groups: List[str] = None,
        Password: str = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mq.html#MQ.Client.create_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#create-user)
        """

    def delete_broker(self, BrokerId: str) -> DeleteBrokerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mq.html#MQ.Client.delete_broker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#delete-broker)
        """

    def delete_tags(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mq.html#MQ.Client.delete_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#delete-tags)
        """

    def delete_user(self, BrokerId: str, Username: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mq.html#MQ.Client.delete_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#delete-user)
        """

    def describe_broker(self, BrokerId: str) -> DescribeBrokerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mq.html#MQ.Client.describe_broker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#describe-broker)
        """

    def describe_broker_engine_types(
        self, EngineType: str = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeBrokerEngineTypesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mq.html#MQ.Client.describe_broker_engine_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#describe-broker-engine-types)
        """

    def describe_broker_instance_options(
        self,
        EngineType: str = None,
        HostInstanceType: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        StorageType: str = None,
    ) -> DescribeBrokerInstanceOptionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mq.html#MQ.Client.describe_broker_instance_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#describe-broker-instance-options)
        """

    def describe_configuration(self, ConfigurationId: str) -> DescribeConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mq.html#MQ.Client.describe_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#describe-configuration)
        """

    def describe_configuration_revision(
        self, ConfigurationId: str, ConfigurationRevision: str
    ) -> DescribeConfigurationRevisionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mq.html#MQ.Client.describe_configuration_revision)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#describe-configuration-revision)
        """

    def describe_user(self, BrokerId: str, Username: str) -> DescribeUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mq.html#MQ.Client.describe_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#describe-user)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mq.html#MQ.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#generate-presigned-url)
        """

    def list_brokers(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListBrokersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mq.html#MQ.Client.list_brokers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#list-brokers)
        """

    def list_configuration_revisions(
        self, ConfigurationId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListConfigurationRevisionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mq.html#MQ.Client.list_configuration_revisions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#list-configuration-revisions)
        """

    def list_configurations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListConfigurationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mq.html#MQ.Client.list_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#list-configurations)
        """

    def list_tags(self, ResourceArn: str) -> ListTagsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mq.html#MQ.Client.list_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#list-tags)
        """

    def list_users(
        self, BrokerId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListUsersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mq.html#MQ.Client.list_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#list-users)
        """

    def reboot_broker(self, BrokerId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mq.html#MQ.Client.reboot_broker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#reboot-broker)
        """

    def update_broker(
        self,
        BrokerId: str,
        AuthenticationStrategy: AuthenticationStrategy = None,
        AutoMinorVersionUpgrade: bool = None,
        Configuration: "ConfigurationIdTypeDef" = None,
        EngineVersion: str = None,
        HostInstanceType: str = None,
        LdapServerMetadata: LdapServerMetadataInputTypeDef = None,
        Logs: "LogsTypeDef" = None,
        SecurityGroups: List[str] = None,
    ) -> UpdateBrokerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mq.html#MQ.Client.update_broker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#update-broker)
        """

    def update_configuration(
        self, ConfigurationId: str, Data: str = None, Description: str = None
    ) -> UpdateConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mq.html#MQ.Client.update_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#update-configuration)
        """

    def update_user(
        self,
        BrokerId: str,
        Username: str,
        ConsoleAccess: bool = None,
        Groups: List[str] = None,
        Password: str = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mq.html#MQ.Client.update_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#update-user)
        """

    def get_paginator(self, operation_name: Literal["list_brokers"]) -> ListBrokersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/mq.html#MQ.Paginator.ListBrokers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/paginators.html#listbrokerspaginator)
        """
