# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetServiceAccountResult',
    'AwaitableGetServiceAccountResult',
    'get_service_account',
]

@pulumi.output_type
class GetServiceAccountResult:
    """
    A collection of values returned by getServiceAccount.
    """
    def __init__(__self__, arn=None, id=None, region=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        The ARN of the AWS CloudTrail service account in the selected region.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        return pulumi.get(self, "region")


class AwaitableGetServiceAccountResult(GetServiceAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceAccountResult(
            arn=self.arn,
            id=self.id,
            region=self.region)


def get_service_account(region: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServiceAccountResult:
    """
    Use this data source to get the Account ID of the [AWS CloudTrail Service Account](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-supported-regions.html)
    in a given region for the purpose of allowing CloudTrail to store trail data in S3.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    main = aws.cloudtrail.get_service_account()
    bucket = aws.s3.Bucket("bucket",
        force_destroy=True,
        policy=f\"\"\"{{
      "Version": "2008-10-17",
      "Statement": [
        {{
          "Sid": "Put bucket policy needed for trails",
          "Effect": "Allow",
          "Principal": {{
            "AWS": "{main.arn}"
          }},
          "Action": "s3:PutObject",
          "Resource": "arn:aws:s3:::tf-cloudtrail-logging-test-bucket/*"
        }},
        {{
          "Sid": "Get bucket policy needed for trails",
          "Effect": "Allow",
          "Principal": {{
            "AWS": "{main.arn}"
          }},
          "Action": "s3:GetBucketAcl",
          "Resource": "arn:aws:s3:::tf-cloudtrail-logging-test-bucket"
        }}
      ]
    }}

    \"\"\")
    ```


    :param str region: Name of the region whose AWS CloudTrail account ID is desired.
           Defaults to the region from the AWS provider configuration.
    """
    __args__ = dict()
    __args__['region'] = region
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:cloudtrail/getServiceAccount:getServiceAccount', __args__, opts=opts, typ=GetServiceAccountResult).value

    return AwaitableGetServiceAccountResult(
        arn=__ret__.arn,
        id=__ret__.id,
        region=__ret__.region)
