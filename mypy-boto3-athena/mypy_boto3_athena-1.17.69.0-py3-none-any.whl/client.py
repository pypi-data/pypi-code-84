"""
Type annotations for athena service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_athena import AthenaClient

    client: AthenaClient = boto3.client("athena")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_athena.literals import DataCatalogType, WorkGroupState
from mypy_boto3_athena.paginator import (
    GetQueryResultsPaginator,
    ListDatabasesPaginator,
    ListDataCatalogsPaginator,
    ListNamedQueriesPaginator,
    ListQueryExecutionsPaginator,
    ListTableMetadataPaginator,
    ListTagsForResourcePaginator,
)
from mypy_boto3_athena.type_defs import (
    BatchGetNamedQueryOutputTypeDef,
    BatchGetQueryExecutionOutputTypeDef,
    CreateNamedQueryOutputTypeDef,
    GetDatabaseOutputTypeDef,
    GetDataCatalogOutputTypeDef,
    GetNamedQueryOutputTypeDef,
    GetPreparedStatementOutputTypeDef,
    GetQueryExecutionOutputTypeDef,
    GetQueryResultsOutputTypeDef,
    GetTableMetadataOutputTypeDef,
    GetWorkGroupOutputTypeDef,
    ListDatabasesOutputTypeDef,
    ListDataCatalogsOutputTypeDef,
    ListEngineVersionsOutputTypeDef,
    ListNamedQueriesOutputTypeDef,
    ListPreparedStatementsOutputTypeDef,
    ListQueryExecutionsOutputTypeDef,
    ListTableMetadataOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListWorkGroupsOutputTypeDef,
    QueryExecutionContextTypeDef,
    ResultConfigurationTypeDef,
    StartQueryExecutionOutputTypeDef,
    TagTypeDef,
    WorkGroupConfigurationTypeDef,
    WorkGroupConfigurationUpdatesTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AthenaClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    MetadataException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]


class AthenaClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_get_named_query(self, NamedQueryIds: List[str]) -> BatchGetNamedQueryOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.batch_get_named_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#batch-get-named-query)
        """

    def batch_get_query_execution(
        self, QueryExecutionIds: List[str]
    ) -> BatchGetQueryExecutionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.batch_get_query_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#batch-get-query-execution)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#can-paginate)
        """

    def create_data_catalog(
        self,
        Name: str,
        Type: DataCatalogType,
        Description: str = None,
        Parameters: Dict[str, str] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.create_data_catalog)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#create-data-catalog)
        """

    def create_named_query(
        self,
        Name: str,
        Database: str,
        QueryString: str,
        Description: str = None,
        ClientRequestToken: str = None,
        WorkGroup: str = None,
    ) -> CreateNamedQueryOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.create_named_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#create-named-query)
        """

    def create_prepared_statement(
        self, StatementName: str, WorkGroup: str, QueryStatement: str, Description: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.create_prepared_statement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#create-prepared-statement)
        """

    def create_work_group(
        self,
        Name: str,
        Configuration: "WorkGroupConfigurationTypeDef" = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.create_work_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#create-work-group)
        """

    def delete_data_catalog(self, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.delete_data_catalog)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#delete-data-catalog)
        """

    def delete_named_query(self, NamedQueryId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.delete_named_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#delete-named-query)
        """

    def delete_prepared_statement(self, StatementName: str, WorkGroup: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.delete_prepared_statement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#delete-prepared-statement)
        """

    def delete_work_group(
        self, WorkGroup: str, RecursiveDeleteOption: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.delete_work_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#delete-work-group)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#generate-presigned-url)
        """

    def get_data_catalog(self, Name: str) -> GetDataCatalogOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.get_data_catalog)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#get-data-catalog)
        """

    def get_database(self, CatalogName: str, DatabaseName: str) -> GetDatabaseOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.get_database)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#get-database)
        """

    def get_named_query(self, NamedQueryId: str) -> GetNamedQueryOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.get_named_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#get-named-query)
        """

    def get_prepared_statement(
        self, StatementName: str, WorkGroup: str
    ) -> GetPreparedStatementOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.get_prepared_statement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#get-prepared-statement)
        """

    def get_query_execution(self, QueryExecutionId: str) -> GetQueryExecutionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.get_query_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#get-query-execution)
        """

    def get_query_results(
        self, QueryExecutionId: str, NextToken: str = None, MaxResults: int = None
    ) -> GetQueryResultsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.get_query_results)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#get-query-results)
        """

    def get_table_metadata(
        self, CatalogName: str, DatabaseName: str, TableName: str
    ) -> GetTableMetadataOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.get_table_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#get-table-metadata)
        """

    def get_work_group(self, WorkGroup: str) -> GetWorkGroupOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.get_work_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#get-work-group)
        """

    def list_data_catalogs(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListDataCatalogsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.list_data_catalogs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#list-data-catalogs)
        """

    def list_databases(
        self, CatalogName: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDatabasesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.list_databases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#list-databases)
        """

    def list_engine_versions(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListEngineVersionsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.list_engine_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#list-engine-versions)
        """

    def list_named_queries(
        self, NextToken: str = None, MaxResults: int = None, WorkGroup: str = None
    ) -> ListNamedQueriesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.list_named_queries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#list-named-queries)
        """

    def list_prepared_statements(
        self, WorkGroup: str, NextToken: str = None, MaxResults: int = None
    ) -> ListPreparedStatementsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.list_prepared_statements)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#list-prepared-statements)
        """

    def list_query_executions(
        self, NextToken: str = None, MaxResults: int = None, WorkGroup: str = None
    ) -> ListQueryExecutionsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.list_query_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#list-query-executions)
        """

    def list_table_metadata(
        self,
        CatalogName: str,
        DatabaseName: str,
        Expression: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListTableMetadataOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.list_table_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#list-table-metadata)
        """

    def list_tags_for_resource(
        self, ResourceARN: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTagsForResourceOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#list-tags-for-resource)
        """

    def list_work_groups(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListWorkGroupsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.list_work_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#list-work-groups)
        """

    def start_query_execution(
        self,
        QueryString: str,
        ClientRequestToken: str = None,
        QueryExecutionContext: "QueryExecutionContextTypeDef" = None,
        ResultConfiguration: "ResultConfigurationTypeDef" = None,
        WorkGroup: str = None,
    ) -> StartQueryExecutionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.start_query_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#start-query-execution)
        """

    def stop_query_execution(self, QueryExecutionId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.stop_query_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#stop-query-execution)
        """

    def tag_resource(self, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#tag-resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#untag-resource)
        """

    def update_data_catalog(
        self,
        Name: str,
        Type: DataCatalogType,
        Description: str = None,
        Parameters: Dict[str, str] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.update_data_catalog)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#update-data-catalog)
        """

    def update_prepared_statement(
        self, StatementName: str, WorkGroup: str, QueryStatement: str, Description: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.update_prepared_statement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#update-prepared-statement)
        """

    def update_work_group(
        self,
        WorkGroup: str,
        Description: str = None,
        ConfigurationUpdates: WorkGroupConfigurationUpdatesTypeDef = None,
        State: WorkGroupState = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Client.update_work_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/client.html#update-work-group)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_query_results"]
    ) -> GetQueryResultsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Paginator.GetQueryResults)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators.html#getqueryresultspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_catalogs"]
    ) -> ListDataCatalogsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Paginator.ListDataCatalogs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators.html#listdatacatalogspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_databases"]) -> ListDatabasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Paginator.ListDatabases)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators.html#listdatabasespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_named_queries"]
    ) -> ListNamedQueriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Paginator.ListNamedQueries)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators.html#listnamedqueriespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_query_executions"]
    ) -> ListQueryExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Paginator.ListQueryExecutions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators.html#listqueryexecutionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_table_metadata"]
    ) -> ListTableMetadataPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Paginator.ListTableMetadata)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators.html#listtablemetadatapaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/athena.html#Athena.Paginator.ListTagsForResource)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators.html#listtagsforresourcepaginator)
        """
