"""
Type annotations for lakeformation service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_lakeformation import LakeFormationClient

    client: LakeFormationClient = boto3.client("lakeformation")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_lakeformation.literals import DataLakeResourceType, Permission, ResourceShareType
from mypy_boto3_lakeformation.type_defs import (
    AddLFTagsToResourceResponseTypeDef,
    BatchGrantPermissionsResponseTypeDef,
    BatchPermissionsRequestEntryTypeDef,
    BatchRevokePermissionsResponseTypeDef,
    DataLakePrincipalTypeDef,
    DataLakeSettingsTypeDef,
    DescribeResourceResponseTypeDef,
    FilterConditionTypeDef,
    GetDataLakeSettingsResponseTypeDef,
    GetEffectivePermissionsForPathResponseTypeDef,
    GetLFTagResponseTypeDef,
    GetResourceLFTagsResponseTypeDef,
    LFTagPairTypeDef,
    LFTagTypeDef,
    ListLFTagsResponseTypeDef,
    ListPermissionsResponseTypeDef,
    ListResourcesResponseTypeDef,
    RemoveLFTagsFromResourceResponseTypeDef,
    ResourceTypeDef,
    SearchDatabasesByLFTagsResponseTypeDef,
    SearchTablesByLFTagsResponseTypeDef,
)

__all__ = ("LakeFormationClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    AlreadyExistsException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    EntityNotFoundException: Type[BotocoreClientError]
    GlueEncryptionException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    OperationTimeoutException: Type[BotocoreClientError]
    ResourceNumberLimitExceededException: Type[BotocoreClientError]


class LakeFormationClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/lakeformation.html#LakeFormation.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_lf_tags_to_resource(
        self, Resource: "ResourceTypeDef", LFTags: List["LFTagPairTypeDef"], CatalogId: str = None
    ) -> AddLFTagsToResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/lakeformation.html#LakeFormation.Client.add_lf_tags_to_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#add-lf-tags-to-resource)
        """

    def batch_grant_permissions(
        self, Entries: List["BatchPermissionsRequestEntryTypeDef"], CatalogId: str = None
    ) -> BatchGrantPermissionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/lakeformation.html#LakeFormation.Client.batch_grant_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#batch-grant-permissions)
        """

    def batch_revoke_permissions(
        self, Entries: List["BatchPermissionsRequestEntryTypeDef"], CatalogId: str = None
    ) -> BatchRevokePermissionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/lakeformation.html#LakeFormation.Client.batch_revoke_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#batch-revoke-permissions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/lakeformation.html#LakeFormation.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#can-paginate)
        """

    def create_lf_tag(
        self, TagKey: str, TagValues: List[str], CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/lakeformation.html#LakeFormation.Client.create_lf_tag)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#create-lf-tag)
        """

    def delete_lf_tag(self, TagKey: str, CatalogId: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/lakeformation.html#LakeFormation.Client.delete_lf_tag)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#delete-lf-tag)
        """

    def deregister_resource(self, ResourceArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/lakeformation.html#LakeFormation.Client.deregister_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#deregister-resource)
        """

    def describe_resource(self, ResourceArn: str) -> DescribeResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/lakeformation.html#LakeFormation.Client.describe_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#describe-resource)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/lakeformation.html#LakeFormation.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#generate-presigned-url)
        """

    def get_data_lake_settings(self, CatalogId: str = None) -> GetDataLakeSettingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/lakeformation.html#LakeFormation.Client.get_data_lake_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#get-data-lake-settings)
        """

    def get_effective_permissions_for_path(
        self, ResourceArn: str, CatalogId: str = None, NextToken: str = None, MaxResults: int = None
    ) -> GetEffectivePermissionsForPathResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/lakeformation.html#LakeFormation.Client.get_effective_permissions_for_path)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#get-effective-permissions-for-path)
        """

    def get_lf_tag(self, TagKey: str, CatalogId: str = None) -> GetLFTagResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/lakeformation.html#LakeFormation.Client.get_lf_tag)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#get-lf-tag)
        """

    def get_resource_lf_tags(
        self, Resource: "ResourceTypeDef", CatalogId: str = None, ShowAssignedLFTags: bool = None
    ) -> GetResourceLFTagsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/lakeformation.html#LakeFormation.Client.get_resource_lf_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#get-resource-lf-tags)
        """

    def grant_permissions(
        self,
        Principal: "DataLakePrincipalTypeDef",
        Resource: "ResourceTypeDef",
        Permissions: List[Permission],
        CatalogId: str = None,
        PermissionsWithGrantOption: List[Permission] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/lakeformation.html#LakeFormation.Client.grant_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#grant-permissions)
        """

    def list_lf_tags(
        self,
        CatalogId: str = None,
        ResourceShareType: ResourceShareType = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListLFTagsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/lakeformation.html#LakeFormation.Client.list_lf_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#list-lf-tags)
        """

    def list_permissions(
        self,
        CatalogId: str = None,
        Principal: "DataLakePrincipalTypeDef" = None,
        ResourceType: DataLakeResourceType = None,
        Resource: "ResourceTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListPermissionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/lakeformation.html#LakeFormation.Client.list_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#list-permissions)
        """

    def list_resources(
        self,
        FilterConditionList: List[FilterConditionTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListResourcesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/lakeformation.html#LakeFormation.Client.list_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#list-resources)
        """

    def put_data_lake_settings(
        self, DataLakeSettings: "DataLakeSettingsTypeDef", CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/lakeformation.html#LakeFormation.Client.put_data_lake_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#put-data-lake-settings)
        """

    def register_resource(
        self, ResourceArn: str, UseServiceLinkedRole: bool = None, RoleArn: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/lakeformation.html#LakeFormation.Client.register_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#register-resource)
        """

    def remove_lf_tags_from_resource(
        self, Resource: "ResourceTypeDef", LFTags: List["LFTagPairTypeDef"], CatalogId: str = None
    ) -> RemoveLFTagsFromResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/lakeformation.html#LakeFormation.Client.remove_lf_tags_from_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#remove-lf-tags-from-resource)
        """

    def revoke_permissions(
        self,
        Principal: "DataLakePrincipalTypeDef",
        Resource: "ResourceTypeDef",
        Permissions: List[Permission],
        CatalogId: str = None,
        PermissionsWithGrantOption: List[Permission] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/lakeformation.html#LakeFormation.Client.revoke_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#revoke-permissions)
        """

    def search_databases_by_lf_tags(
        self,
        Expression: List["LFTagTypeDef"],
        NextToken: str = None,
        MaxResults: int = None,
        CatalogId: str = None,
    ) -> SearchDatabasesByLFTagsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/lakeformation.html#LakeFormation.Client.search_databases_by_lf_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#search-databases-by-lf-tags)
        """

    def search_tables_by_lf_tags(
        self,
        Expression: List["LFTagTypeDef"],
        NextToken: str = None,
        MaxResults: int = None,
        CatalogId: str = None,
    ) -> SearchTablesByLFTagsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/lakeformation.html#LakeFormation.Client.search_tables_by_lf_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#search-tables-by-lf-tags)
        """

    def update_lf_tag(
        self,
        TagKey: str,
        CatalogId: str = None,
        TagValuesToDelete: List[str] = None,
        TagValuesToAdd: List[str] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/lakeformation.html#LakeFormation.Client.update_lf_tag)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#update-lf-tag)
        """

    def update_resource(self, RoleArn: str, ResourceArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/lakeformation.html#LakeFormation.Client.update_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/client.html#update-resource)
        """
