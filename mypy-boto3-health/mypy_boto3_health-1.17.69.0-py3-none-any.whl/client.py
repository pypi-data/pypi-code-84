"""
Type annotations for health service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_health import HealthClient

    client: HealthClient = boto3.client("health")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_health.paginator import (
    DescribeAffectedAccountsForOrganizationPaginator,
    DescribeAffectedEntitiesForOrganizationPaginator,
    DescribeAffectedEntitiesPaginator,
    DescribeEventAggregatesPaginator,
    DescribeEventsForOrganizationPaginator,
    DescribeEventsPaginator,
    DescribeEventTypesPaginator,
)
from mypy_boto3_health.type_defs import (
    DescribeAffectedAccountsForOrganizationResponseTypeDef,
    DescribeAffectedEntitiesForOrganizationResponseTypeDef,
    DescribeAffectedEntitiesResponseTypeDef,
    DescribeEntityAggregatesResponseTypeDef,
    DescribeEventAggregatesResponseTypeDef,
    DescribeEventDetailsForOrganizationResponseTypeDef,
    DescribeEventDetailsResponseTypeDef,
    DescribeEventsForOrganizationResponseTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeEventTypesResponseTypeDef,
    DescribeHealthServiceStatusForOrganizationResponseTypeDef,
    EntityFilterTypeDef,
    EventAccountFilterTypeDef,
    EventFilterTypeDef,
    EventTypeFilterTypeDef,
    OrganizationEventFilterTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("HealthClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    InvalidPaginationToken: Type[BotocoreClientError]
    UnsupportedLocale: Type[BotocoreClientError]


class HealthClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/health.html#Health.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/health.html#Health.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/client.html#can-paginate)
        """

    def describe_affected_accounts_for_organization(
        self, eventArn: str, nextToken: str = None, maxResults: int = None
    ) -> DescribeAffectedAccountsForOrganizationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/health.html#Health.Client.describe_affected_accounts_for_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/client.html#describe-affected-accounts-for-organization)
        """

    def describe_affected_entities(
        self,
        filter: EntityFilterTypeDef,
        locale: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeAffectedEntitiesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/health.html#Health.Client.describe_affected_entities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/client.html#describe-affected-entities)
        """

    def describe_affected_entities_for_organization(
        self,
        organizationEntityFilters: List[EventAccountFilterTypeDef],
        locale: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeAffectedEntitiesForOrganizationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/health.html#Health.Client.describe_affected_entities_for_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/client.html#describe-affected-entities-for-organization)
        """

    def describe_entity_aggregates(
        self, eventArns: List[str] = None
    ) -> DescribeEntityAggregatesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/health.html#Health.Client.describe_entity_aggregates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/client.html#describe-entity-aggregates)
        """

    def describe_event_aggregates(
        self,
        aggregateField: Literal["eventTypeCategory"],
        filter: EventFilterTypeDef = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> DescribeEventAggregatesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/health.html#Health.Client.describe_event_aggregates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/client.html#describe-event-aggregates)
        """

    def describe_event_details(
        self, eventArns: List[str], locale: str = None
    ) -> DescribeEventDetailsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/health.html#Health.Client.describe_event_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/client.html#describe-event-details)
        """

    def describe_event_details_for_organization(
        self, organizationEventDetailFilters: List[EventAccountFilterTypeDef], locale: str = None
    ) -> DescribeEventDetailsForOrganizationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/health.html#Health.Client.describe_event_details_for_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/client.html#describe-event-details-for-organization)
        """

    def describe_event_types(
        self,
        filter: EventTypeFilterTypeDef = None,
        locale: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeEventTypesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/health.html#Health.Client.describe_event_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/client.html#describe-event-types)
        """

    def describe_events(
        self,
        filter: EventFilterTypeDef = None,
        nextToken: str = None,
        maxResults: int = None,
        locale: str = None,
    ) -> DescribeEventsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/health.html#Health.Client.describe_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/client.html#describe-events)
        """

    def describe_events_for_organization(
        self,
        filter: OrganizationEventFilterTypeDef = None,
        nextToken: str = None,
        maxResults: int = None,
        locale: str = None,
    ) -> DescribeEventsForOrganizationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/health.html#Health.Client.describe_events_for_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/client.html#describe-events-for-organization)
        """

    def describe_health_service_status_for_organization(
        self,
    ) -> DescribeHealthServiceStatusForOrganizationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/health.html#Health.Client.describe_health_service_status_for_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/client.html#describe-health-service-status-for-organization)
        """

    def disable_health_service_access_for_organization(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/health.html#Health.Client.disable_health_service_access_for_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/client.html#disable-health-service-access-for-organization)
        """

    def enable_health_service_access_for_organization(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/health.html#Health.Client.enable_health_service_access_for_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/client.html#enable-health-service-access-for-organization)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/health.html#Health.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/client.html#generate-presigned-url)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_affected_accounts_for_organization"]
    ) -> DescribeAffectedAccountsForOrganizationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/health.html#Health.Paginator.DescribeAffectedAccountsForOrganization)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/paginators.html#describeaffectedaccountsfororganizationpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_affected_entities"]
    ) -> DescribeAffectedEntitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/health.html#Health.Paginator.DescribeAffectedEntities)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/paginators.html#describeaffectedentitiespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_affected_entities_for_organization"]
    ) -> DescribeAffectedEntitiesForOrganizationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/health.html#Health.Paginator.DescribeAffectedEntitiesForOrganization)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/paginators.html#describeaffectedentitiesfororganizationpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_event_aggregates"]
    ) -> DescribeEventAggregatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/health.html#Health.Paginator.DescribeEventAggregates)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/paginators.html#describeeventaggregatespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_event_types"]
    ) -> DescribeEventTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/health.html#Health.Paginator.DescribeEventTypes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/paginators.html#describeeventtypespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_events"]) -> DescribeEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/health.html#Health.Paginator.DescribeEvents)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/paginators.html#describeeventspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_events_for_organization"]
    ) -> DescribeEventsForOrganizationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/health.html#Health.Paginator.DescribeEventsForOrganization)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/paginators.html#describeeventsfororganizationpaginator)
        """
