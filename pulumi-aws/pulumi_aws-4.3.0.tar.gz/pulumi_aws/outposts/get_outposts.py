# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetOutpostsResult',
    'AwaitableGetOutpostsResult',
    'get_outposts',
]

@pulumi.output_type
class GetOutpostsResult:
    """
    A collection of values returned by getOutposts.
    """
    def __init__(__self__, arns=None, availability_zone=None, availability_zone_id=None, id=None, ids=None, site_id=None):
        if arns and not isinstance(arns, list):
            raise TypeError("Expected argument 'arns' to be a list")
        pulumi.set(__self__, "arns", arns)
        if availability_zone and not isinstance(availability_zone, str):
            raise TypeError("Expected argument 'availability_zone' to be a str")
        pulumi.set(__self__, "availability_zone", availability_zone)
        if availability_zone_id and not isinstance(availability_zone_id, str):
            raise TypeError("Expected argument 'availability_zone_id' to be a str")
        pulumi.set(__self__, "availability_zone_id", availability_zone_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if site_id and not isinstance(site_id, str):
            raise TypeError("Expected argument 'site_id' to be a str")
        pulumi.set(__self__, "site_id", site_id)

    @property
    @pulumi.getter
    def arns(self) -> Sequence[str]:
        """
        Set of Amazon Resource Names (ARNs).
        """
        return pulumi.get(self, "arns")

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> str:
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> str:
        return pulumi.get(self, "availability_zone_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        """
        Set of identifiers.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="siteId")
    def site_id(self) -> str:
        return pulumi.get(self, "site_id")


class AwaitableGetOutpostsResult(GetOutpostsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOutpostsResult(
            arns=self.arns,
            availability_zone=self.availability_zone,
            availability_zone_id=self.availability_zone_id,
            id=self.id,
            ids=self.ids,
            site_id=self.site_id)


def get_outposts(availability_zone: Optional[str] = None,
                 availability_zone_id: Optional[str] = None,
                 site_id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOutpostsResult:
    """
    Provides details about multiple Outposts.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.outposts.get_outposts(site_id=data["aws_outposts_site"]["id"])
    ```


    :param str availability_zone: Availability Zone name.
    :param str availability_zone_id: Availability Zone identifier.
    :param str site_id: Site identifier.
    """
    __args__ = dict()
    __args__['availabilityZone'] = availability_zone
    __args__['availabilityZoneId'] = availability_zone_id
    __args__['siteId'] = site_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:outposts/getOutposts:getOutposts', __args__, opts=opts, typ=GetOutpostsResult).value

    return AwaitableGetOutpostsResult(
        arns=__ret__.arns,
        availability_zone=__ret__.availability_zone,
        availability_zone_id=__ret__.availability_zone_id,
        id=__ret__.id,
        ids=__ret__.ids,
        site_id=__ret__.site_id)
