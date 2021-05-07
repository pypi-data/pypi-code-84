"""
Type annotations for cloudtrail service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudtrail import CloudTrailClient

    client: CloudTrailClient = boto3.client("cloudtrail")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_cloudtrail.paginator import (
    ListPublicKeysPaginator,
    ListTagsPaginator,
    ListTrailsPaginator,
    LookupEventsPaginator,
)
from mypy_boto3_cloudtrail.type_defs import (
    AdvancedEventSelectorTypeDef,
    CreateTrailResponseTypeDef,
    DescribeTrailsResponseTypeDef,
    EventSelectorTypeDef,
    GetEventSelectorsResponseTypeDef,
    GetInsightSelectorsResponseTypeDef,
    GetTrailResponseTypeDef,
    GetTrailStatusResponseTypeDef,
    InsightSelectorTypeDef,
    ListPublicKeysResponseTypeDef,
    ListTagsResponseTypeDef,
    ListTrailsResponseTypeDef,
    LookupAttributeTypeDef,
    LookupEventsResponseTypeDef,
    PutEventSelectorsResponseTypeDef,
    PutInsightSelectorsResponseTypeDef,
    TagTypeDef,
    UpdateTrailResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CloudTrailClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    CloudTrailARNInvalidException: Type[BotocoreClientError]
    CloudTrailAccessNotEnabledException: Type[BotocoreClientError]
    CloudTrailInvalidClientTokenIdException: Type[BotocoreClientError]
    CloudWatchLogsDeliveryUnavailableException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InsightNotEnabledException: Type[BotocoreClientError]
    InsufficientDependencyServiceAccessPermissionException: Type[BotocoreClientError]
    InsufficientEncryptionPolicyException: Type[BotocoreClientError]
    InsufficientS3BucketPolicyException: Type[BotocoreClientError]
    InsufficientSnsTopicPolicyException: Type[BotocoreClientError]
    InvalidCloudWatchLogsLogGroupArnException: Type[BotocoreClientError]
    InvalidCloudWatchLogsRoleArnException: Type[BotocoreClientError]
    InvalidEventCategoryException: Type[BotocoreClientError]
    InvalidEventSelectorsException: Type[BotocoreClientError]
    InvalidHomeRegionException: Type[BotocoreClientError]
    InvalidInsightSelectorsException: Type[BotocoreClientError]
    InvalidKmsKeyIdException: Type[BotocoreClientError]
    InvalidLookupAttributesException: Type[BotocoreClientError]
    InvalidMaxResultsException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidParameterCombinationException: Type[BotocoreClientError]
    InvalidS3BucketNameException: Type[BotocoreClientError]
    InvalidS3PrefixException: Type[BotocoreClientError]
    InvalidSnsTopicNameException: Type[BotocoreClientError]
    InvalidTagParameterException: Type[BotocoreClientError]
    InvalidTimeRangeException: Type[BotocoreClientError]
    InvalidTokenException: Type[BotocoreClientError]
    InvalidTrailNameException: Type[BotocoreClientError]
    KmsException: Type[BotocoreClientError]
    KmsKeyDisabledException: Type[BotocoreClientError]
    KmsKeyNotFoundException: Type[BotocoreClientError]
    MaximumNumberOfTrailsExceededException: Type[BotocoreClientError]
    NotOrganizationMasterAccountException: Type[BotocoreClientError]
    OperationNotPermittedException: Type[BotocoreClientError]
    OrganizationNotInAllFeaturesModeException: Type[BotocoreClientError]
    OrganizationsNotInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceTypeNotSupportedException: Type[BotocoreClientError]
    S3BucketDoesNotExistException: Type[BotocoreClientError]
    TagsLimitExceededException: Type[BotocoreClientError]
    TrailAlreadyExistsException: Type[BotocoreClientError]
    TrailNotFoundException: Type[BotocoreClientError]
    TrailNotProvidedException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]


class CloudTrailClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/cloudtrail.html#CloudTrail.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_tags(self, ResourceId: str, TagsList: List["TagTypeDef"] = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/cloudtrail.html#CloudTrail.Client.add_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#add-tags)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/cloudtrail.html#CloudTrail.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#can-paginate)
        """

    def create_trail(
        self,
        Name: str,
        S3BucketName: str,
        S3KeyPrefix: str = None,
        SnsTopicName: str = None,
        IncludeGlobalServiceEvents: bool = None,
        IsMultiRegionTrail: bool = None,
        EnableLogFileValidation: bool = None,
        CloudWatchLogsLogGroupArn: str = None,
        CloudWatchLogsRoleArn: str = None,
        KmsKeyId: str = None,
        IsOrganizationTrail: bool = None,
        TagsList: List["TagTypeDef"] = None,
    ) -> CreateTrailResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/cloudtrail.html#CloudTrail.Client.create_trail)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#create-trail)
        """

    def delete_trail(self, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/cloudtrail.html#CloudTrail.Client.delete_trail)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#delete-trail)
        """

    def describe_trails(
        self, trailNameList: List[str] = None, includeShadowTrails: bool = None
    ) -> DescribeTrailsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/cloudtrail.html#CloudTrail.Client.describe_trails)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#describe-trails)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/cloudtrail.html#CloudTrail.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#generate-presigned-url)
        """

    def get_event_selectors(self, TrailName: str) -> GetEventSelectorsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/cloudtrail.html#CloudTrail.Client.get_event_selectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#get-event-selectors)
        """

    def get_insight_selectors(self, TrailName: str) -> GetInsightSelectorsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/cloudtrail.html#CloudTrail.Client.get_insight_selectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#get-insight-selectors)
        """

    def get_trail(self, Name: str) -> GetTrailResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/cloudtrail.html#CloudTrail.Client.get_trail)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#get-trail)
        """

    def get_trail_status(self, Name: str) -> GetTrailStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/cloudtrail.html#CloudTrail.Client.get_trail_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#get-trail-status)
        """

    def list_public_keys(
        self, StartTime: datetime = None, EndTime: datetime = None, NextToken: str = None
    ) -> ListPublicKeysResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/cloudtrail.html#CloudTrail.Client.list_public_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#list-public-keys)
        """

    def list_tags(
        self, ResourceIdList: List[str], NextToken: str = None
    ) -> ListTagsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/cloudtrail.html#CloudTrail.Client.list_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#list-tags)
        """

    def list_trails(self, NextToken: str = None) -> ListTrailsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/cloudtrail.html#CloudTrail.Client.list_trails)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#list-trails)
        """

    def lookup_events(
        self,
        LookupAttributes: List[LookupAttributeTypeDef] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        EventCategory: Literal["insight"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> LookupEventsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/cloudtrail.html#CloudTrail.Client.lookup_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#lookup-events)
        """

    def put_event_selectors(
        self,
        TrailName: str,
        EventSelectors: List["EventSelectorTypeDef"] = None,
        AdvancedEventSelectors: List["AdvancedEventSelectorTypeDef"] = None,
    ) -> PutEventSelectorsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/cloudtrail.html#CloudTrail.Client.put_event_selectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#put-event-selectors)
        """

    def put_insight_selectors(
        self, TrailName: str, InsightSelectors: List["InsightSelectorTypeDef"]
    ) -> PutInsightSelectorsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/cloudtrail.html#CloudTrail.Client.put_insight_selectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#put-insight-selectors)
        """

    def remove_tags(self, ResourceId: str, TagsList: List["TagTypeDef"] = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/cloudtrail.html#CloudTrail.Client.remove_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#remove-tags)
        """

    def start_logging(self, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/cloudtrail.html#CloudTrail.Client.start_logging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#start-logging)
        """

    def stop_logging(self, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/cloudtrail.html#CloudTrail.Client.stop_logging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#stop-logging)
        """

    def update_trail(
        self,
        Name: str,
        S3BucketName: str = None,
        S3KeyPrefix: str = None,
        SnsTopicName: str = None,
        IncludeGlobalServiceEvents: bool = None,
        IsMultiRegionTrail: bool = None,
        EnableLogFileValidation: bool = None,
        CloudWatchLogsLogGroupArn: str = None,
        CloudWatchLogsRoleArn: str = None,
        KmsKeyId: str = None,
        IsOrganizationTrail: bool = None,
    ) -> UpdateTrailResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/cloudtrail.html#CloudTrail.Client.update_trail)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#update-trail)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_public_keys"]) -> ListPublicKeysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/cloudtrail.html#CloudTrail.Paginator.ListPublicKeys)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators.html#listpublickeyspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tags"]) -> ListTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTags)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators.html#listtagspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_trails"]) -> ListTrailsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTrails)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators.html#listtrailspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["lookup_events"]) -> LookupEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/cloudtrail.html#CloudTrail.Paginator.LookupEvents)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators.html#lookupeventspaginator)
        """
