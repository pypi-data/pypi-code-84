# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'ListSpatialAnchorsAccountKeysResult',
    'AwaitableListSpatialAnchorsAccountKeysResult',
    'list_spatial_anchors_account_keys',
]

@pulumi.output_type
class ListSpatialAnchorsAccountKeysResult:
    """
    Developer Keys of account
    """
    def __init__(__self__, primary_key=None, secondary_key=None):
        if primary_key and not isinstance(primary_key, str):
            raise TypeError("Expected argument 'primary_key' to be a str")
        pulumi.set(__self__, "primary_key", primary_key)
        if secondary_key and not isinstance(secondary_key, str):
            raise TypeError("Expected argument 'secondary_key' to be a str")
        pulumi.set(__self__, "secondary_key", secondary_key)

    @property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> str:
        """
        value of primary key.
        """
        return pulumi.get(self, "primary_key")

    @property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> str:
        """
        value of secondary key.
        """
        return pulumi.get(self, "secondary_key")


class AwaitableListSpatialAnchorsAccountKeysResult(ListSpatialAnchorsAccountKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListSpatialAnchorsAccountKeysResult(
            primary_key=self.primary_key,
            secondary_key=self.secondary_key)


def list_spatial_anchors_account_keys(account_name: Optional[str] = None,
                                      resource_group_name: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListSpatialAnchorsAccountKeysResult:
    """
    Developer Keys of account


    :param str account_name: Name of an Mixed Reality Account.
    :param str resource_group_name: Name of an Azure resource group.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:mixedreality/v20200501:listSpatialAnchorsAccountKeys', __args__, opts=opts, typ=ListSpatialAnchorsAccountKeysResult).value

    return AwaitableListSpatialAnchorsAccountKeysResult(
        primary_key=__ret__.primary_key,
        secondary_key=__ret__.secondary_key)
