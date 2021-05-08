# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetRemoteRenderingAccountResult',
    'AwaitableGetRemoteRenderingAccountResult',
    'get_remote_rendering_account',
]

@pulumi.output_type
class GetRemoteRenderingAccountResult:
    """
    RemoteRenderingAccount Response.
    """
    def __init__(__self__, account_domain=None, account_id=None, id=None, identity=None, location=None, name=None, tags=None, type=None):
        if account_domain and not isinstance(account_domain, str):
            raise TypeError("Expected argument 'account_domain' to be a str")
        pulumi.set(__self__, "account_domain", account_domain)
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="accountDomain")
    def account_domain(self) -> str:
        """
        Correspond domain name of certain Spatial Anchors Account
        """
        return pulumi.get(self, "account_domain")

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        """
        unique id of certain account.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.IdentityResponse']:
        """
        The identity associated with this account
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetRemoteRenderingAccountResult(GetRemoteRenderingAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRemoteRenderingAccountResult(
            account_domain=self.account_domain,
            account_id=self.account_id,
            id=self.id,
            identity=self.identity,
            location=self.location,
            name=self.name,
            tags=self.tags,
            type=self.type)


def get_remote_rendering_account(account_name: Optional[str] = None,
                                 resource_group_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRemoteRenderingAccountResult:
    """
    RemoteRenderingAccount Response.


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
    __ret__ = pulumi.runtime.invoke('azure-native:mixedreality/v20191202preview:getRemoteRenderingAccount', __args__, opts=opts, typ=GetRemoteRenderingAccountResult).value

    return AwaitableGetRemoteRenderingAccountResult(
        account_domain=__ret__.account_domain,
        account_id=__ret__.account_id,
        id=__ret__.id,
        identity=__ret__.identity,
        location=__ret__.location,
        name=__ret__.name,
        tags=__ret__.tags,
        type=__ret__.type)
