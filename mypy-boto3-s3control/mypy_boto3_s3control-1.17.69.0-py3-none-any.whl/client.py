"""
Type annotations for s3control service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_s3control import S3ControlClient

    client: S3ControlClient = boto3.client("s3control")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_s3control.literals import BucketCannedACL, JobStatus, RequestedJobStatus
from mypy_boto3_s3control.paginator import ListAccessPointsForObjectLambdaPaginator
from mypy_boto3_s3control.type_defs import (
    CreateAccessPointForObjectLambdaResultTypeDef,
    CreateAccessPointResultTypeDef,
    CreateBucketConfigurationTypeDef,
    CreateBucketResultTypeDef,
    CreateJobResultTypeDef,
    DescribeJobResultTypeDef,
    GetAccessPointConfigurationForObjectLambdaResultTypeDef,
    GetAccessPointForObjectLambdaResultTypeDef,
    GetAccessPointPolicyForObjectLambdaResultTypeDef,
    GetAccessPointPolicyResultTypeDef,
    GetAccessPointPolicyStatusForObjectLambdaResultTypeDef,
    GetAccessPointPolicyStatusResultTypeDef,
    GetAccessPointResultTypeDef,
    GetBucketLifecycleConfigurationResultTypeDef,
    GetBucketPolicyResultTypeDef,
    GetBucketResultTypeDef,
    GetBucketTaggingResultTypeDef,
    GetJobTaggingResultTypeDef,
    GetPublicAccessBlockOutputTypeDef,
    GetStorageLensConfigurationResultTypeDef,
    GetStorageLensConfigurationTaggingResultTypeDef,
    JobManifestTypeDef,
    JobOperationTypeDef,
    JobReportTypeDef,
    LifecycleConfigurationTypeDef,
    ListAccessPointsForObjectLambdaResultTypeDef,
    ListAccessPointsResultTypeDef,
    ListJobsResultTypeDef,
    ListRegionalBucketsResultTypeDef,
    ListStorageLensConfigurationsResultTypeDef,
    ObjectLambdaConfigurationTypeDef,
    PublicAccessBlockConfigurationTypeDef,
    S3TagTypeDef,
    StorageLensConfigurationTypeDef,
    StorageLensTagTypeDef,
    TaggingTypeDef,
    UpdateJobPriorityResultTypeDef,
    UpdateJobStatusResultTypeDef,
    VpcConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("S3ControlClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    BucketAlreadyExists: Type[BotocoreClientError]
    BucketAlreadyOwnedByYou: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    IdempotencyException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    JobStatusException: Type[BotocoreClientError]
    NoSuchPublicAccessBlockConfiguration: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]


class S3ControlClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#can-paginate)
        """

    def create_access_point(
        self,
        AccountId: str,
        Name: str,
        Bucket: str,
        VpcConfiguration: "VpcConfigurationTypeDef" = None,
        PublicAccessBlockConfiguration: "PublicAccessBlockConfigurationTypeDef" = None,
    ) -> CreateAccessPointResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.create_access_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#create-access-point)
        """

    def create_access_point_for_object_lambda(
        self, AccountId: str, Name: str, Configuration: "ObjectLambdaConfigurationTypeDef"
    ) -> CreateAccessPointForObjectLambdaResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.create_access_point_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#create-access-point-for-object-lambda)
        """

    def create_bucket(
        self,
        Bucket: str,
        ACL: BucketCannedACL = None,
        CreateBucketConfiguration: CreateBucketConfigurationTypeDef = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWrite: str = None,
        GrantWriteACP: str = None,
        ObjectLockEnabledForBucket: bool = None,
        OutpostId: str = None,
    ) -> CreateBucketResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.create_bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#create-bucket)
        """

    def create_job(
        self,
        AccountId: str,
        Operation: "JobOperationTypeDef",
        Report: "JobReportTypeDef",
        ClientRequestToken: str,
        Manifest: "JobManifestTypeDef",
        Priority: int,
        RoleArn: str,
        ConfirmationRequired: bool = None,
        Description: str = None,
        Tags: List["S3TagTypeDef"] = None,
    ) -> CreateJobResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.create_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#create-job)
        """

    def delete_access_point(self, AccountId: str, Name: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.delete_access_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete-access-point)
        """

    def delete_access_point_for_object_lambda(self, AccountId: str, Name: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.delete_access_point_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete-access-point-for-object-lambda)
        """

    def delete_access_point_policy(self, AccountId: str, Name: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.delete_access_point_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete-access-point-policy)
        """

    def delete_access_point_policy_for_object_lambda(self, AccountId: str, Name: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.delete_access_point_policy_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete-access-point-policy-for-object-lambda)
        """

    def delete_bucket(self, AccountId: str, Bucket: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.delete_bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete-bucket)
        """

    def delete_bucket_lifecycle_configuration(self, AccountId: str, Bucket: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.delete_bucket_lifecycle_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete-bucket-lifecycle-configuration)
        """

    def delete_bucket_policy(self, AccountId: str, Bucket: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.delete_bucket_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete-bucket-policy)
        """

    def delete_bucket_tagging(self, AccountId: str, Bucket: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.delete_bucket_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete-bucket-tagging)
        """

    def delete_job_tagging(self, AccountId: str, JobId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.delete_job_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete-job-tagging)
        """

    def delete_public_access_block(self, AccountId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.delete_public_access_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete-public-access-block)
        """

    def delete_storage_lens_configuration(self, ConfigId: str, AccountId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.delete_storage_lens_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete-storage-lens-configuration)
        """

    def delete_storage_lens_configuration_tagging(
        self, ConfigId: str, AccountId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.delete_storage_lens_configuration_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete-storage-lens-configuration-tagging)
        """

    def describe_job(self, AccountId: str, JobId: str) -> DescribeJobResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.describe_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#describe-job)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#generate-presigned-url)
        """

    def get_access_point(self, AccountId: str, Name: str) -> GetAccessPointResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.get_access_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get-access-point)
        """

    def get_access_point_configuration_for_object_lambda(
        self, AccountId: str, Name: str
    ) -> GetAccessPointConfigurationForObjectLambdaResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.get_access_point_configuration_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get-access-point-configuration-for-object-lambda)
        """

    def get_access_point_for_object_lambda(
        self, AccountId: str, Name: str
    ) -> GetAccessPointForObjectLambdaResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.get_access_point_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get-access-point-for-object-lambda)
        """

    def get_access_point_policy(
        self, AccountId: str, Name: str
    ) -> GetAccessPointPolicyResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.get_access_point_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get-access-point-policy)
        """

    def get_access_point_policy_for_object_lambda(
        self, AccountId: str, Name: str
    ) -> GetAccessPointPolicyForObjectLambdaResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.get_access_point_policy_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get-access-point-policy-for-object-lambda)
        """

    def get_access_point_policy_status(
        self, AccountId: str, Name: str
    ) -> GetAccessPointPolicyStatusResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.get_access_point_policy_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get-access-point-policy-status)
        """

    def get_access_point_policy_status_for_object_lambda(
        self, AccountId: str, Name: str
    ) -> GetAccessPointPolicyStatusForObjectLambdaResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.get_access_point_policy_status_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get-access-point-policy-status-for-object-lambda)
        """

    def get_bucket(self, AccountId: str, Bucket: str) -> GetBucketResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.get_bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get-bucket)
        """

    def get_bucket_lifecycle_configuration(
        self, AccountId: str, Bucket: str
    ) -> GetBucketLifecycleConfigurationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.get_bucket_lifecycle_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get-bucket-lifecycle-configuration)
        """

    def get_bucket_policy(self, AccountId: str, Bucket: str) -> GetBucketPolicyResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.get_bucket_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get-bucket-policy)
        """

    def get_bucket_tagging(self, AccountId: str, Bucket: str) -> GetBucketTaggingResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.get_bucket_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get-bucket-tagging)
        """

    def get_job_tagging(self, AccountId: str, JobId: str) -> GetJobTaggingResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.get_job_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get-job-tagging)
        """

    def get_public_access_block(self, AccountId: str) -> GetPublicAccessBlockOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.get_public_access_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get-public-access-block)
        """

    def get_storage_lens_configuration(
        self, ConfigId: str, AccountId: str
    ) -> GetStorageLensConfigurationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.get_storage_lens_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get-storage-lens-configuration)
        """

    def get_storage_lens_configuration_tagging(
        self, ConfigId: str, AccountId: str
    ) -> GetStorageLensConfigurationTaggingResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.get_storage_lens_configuration_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get-storage-lens-configuration-tagging)
        """

    def list_access_points(
        self, AccountId: str, Bucket: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListAccessPointsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.list_access_points)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#list-access-points)
        """

    def list_access_points_for_object_lambda(
        self, AccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAccessPointsForObjectLambdaResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.list_access_points_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#list-access-points-for-object-lambda)
        """

    def list_jobs(
        self,
        AccountId: str,
        JobStatuses: List[JobStatus] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListJobsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.list_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#list-jobs)
        """

    def list_regional_buckets(
        self, AccountId: str, NextToken: str = None, MaxResults: int = None, OutpostId: str = None
    ) -> ListRegionalBucketsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.list_regional_buckets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#list-regional-buckets)
        """

    def list_storage_lens_configurations(
        self, AccountId: str, NextToken: str = None
    ) -> ListStorageLensConfigurationsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.list_storage_lens_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#list-storage-lens-configurations)
        """

    def put_access_point_configuration_for_object_lambda(
        self, AccountId: str, Name: str, Configuration: "ObjectLambdaConfigurationTypeDef"
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.put_access_point_configuration_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put-access-point-configuration-for-object-lambda)
        """

    def put_access_point_policy(self, AccountId: str, Name: str, Policy: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.put_access_point_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put-access-point-policy)
        """

    def put_access_point_policy_for_object_lambda(
        self, AccountId: str, Name: str, Policy: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.put_access_point_policy_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put-access-point-policy-for-object-lambda)
        """

    def put_bucket_lifecycle_configuration(
        self,
        AccountId: str,
        Bucket: str,
        LifecycleConfiguration: LifecycleConfigurationTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.put_bucket_lifecycle_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put-bucket-lifecycle-configuration)
        """

    def put_bucket_policy(
        self, AccountId: str, Bucket: str, Policy: str, ConfirmRemoveSelfBucketAccess: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.put_bucket_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put-bucket-policy)
        """

    def put_bucket_tagging(self, AccountId: str, Bucket: str, Tagging: TaggingTypeDef) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.put_bucket_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put-bucket-tagging)
        """

    def put_job_tagging(
        self, AccountId: str, JobId: str, Tags: List["S3TagTypeDef"]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.put_job_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put-job-tagging)
        """

    def put_public_access_block(
        self,
        PublicAccessBlockConfiguration: "PublicAccessBlockConfigurationTypeDef",
        AccountId: str,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.put_public_access_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put-public-access-block)
        """

    def put_storage_lens_configuration(
        self,
        ConfigId: str,
        AccountId: str,
        StorageLensConfiguration: "StorageLensConfigurationTypeDef",
        Tags: List["StorageLensTagTypeDef"] = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.put_storage_lens_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put-storage-lens-configuration)
        """

    def put_storage_lens_configuration_tagging(
        self, ConfigId: str, AccountId: str, Tags: List["StorageLensTagTypeDef"]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.put_storage_lens_configuration_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put-storage-lens-configuration-tagging)
        """

    def update_job_priority(
        self, AccountId: str, JobId: str, Priority: int
    ) -> UpdateJobPriorityResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.update_job_priority)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#update-job-priority)
        """

    def update_job_status(
        self,
        AccountId: str,
        JobId: str,
        RequestedJobStatus: RequestedJobStatus,
        StatusUpdateReason: str = None,
    ) -> UpdateJobStatusResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Client.update_job_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#update-job-status)
        """

    def get_paginator(
        self, operation_name: Literal["list_access_points_for_object_lambda"]
    ) -> ListAccessPointsForObjectLambdaPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/s3control.html#S3Control.Paginator.ListAccessPointsForObjectLambda)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/paginators.html#listaccesspointsforobjectlambdapaginator)
        """
