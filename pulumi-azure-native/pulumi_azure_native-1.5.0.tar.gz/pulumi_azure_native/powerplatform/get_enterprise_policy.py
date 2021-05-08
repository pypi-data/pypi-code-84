# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetEnterprisePolicyResult',
    'AwaitableGetEnterprisePolicyResult',
    'get_enterprise_policy',
]

@pulumi.output_type
class GetEnterprisePolicyResult:
    """
    Definition of the EnterprisePolicy.
    """
    def __init__(__self__, encryption=None, id=None, identity=None, location=None, lockbox=None, name=None, network_injection=None, system_data=None, tags=None, type=None):
        if encryption and not isinstance(encryption, dict):
            raise TypeError("Expected argument 'encryption' to be a dict")
        pulumi.set(__self__, "encryption", encryption)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if lockbox and not isinstance(lockbox, dict):
            raise TypeError("Expected argument 'lockbox' to be a dict")
        pulumi.set(__self__, "lockbox", lockbox)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_injection and not isinstance(network_injection, dict):
            raise TypeError("Expected argument 'network_injection' to be a dict")
        pulumi.set(__self__, "network_injection", network_injection)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def encryption(self) -> Optional['outputs.PropertiesResponseEncryption']:
        """
        The encryption settings for a configuration store.
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.EnterprisePolicyIdentityResponse']:
        """
        The identity of the EnterprisePolicy.
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
    def lockbox(self) -> Optional['outputs.PropertiesResponseLockbox']:
        """
        Settings concerning lockbox.
        """
        return pulumi.get(self, "lockbox")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkInjection")
    def network_injection(self) -> Optional['outputs.PropertiesResponseNetworkInjection']:
        """
        Settings concerning network injection.
        """
        return pulumi.get(self, "network_injection")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

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


class AwaitableGetEnterprisePolicyResult(GetEnterprisePolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEnterprisePolicyResult(
            encryption=self.encryption,
            id=self.id,
            identity=self.identity,
            location=self.location,
            lockbox=self.lockbox,
            name=self.name,
            network_injection=self.network_injection,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_enterprise_policy(enterprise_policy_name: Optional[str] = None,
                          resource_group_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEnterprisePolicyResult:
    """
    Definition of the EnterprisePolicy.
    API Version: 2020-10-30-preview.


    :param str enterprise_policy_name: The EnterprisePolicy name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['enterprisePolicyName'] = enterprise_policy_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:powerplatform:getEnterprisePolicy', __args__, opts=opts, typ=GetEnterprisePolicyResult).value

    return AwaitableGetEnterprisePolicyResult(
        encryption=__ret__.encryption,
        id=__ret__.id,
        identity=__ret__.identity,
        location=__ret__.location,
        lockbox=__ret__.lockbox,
        name=__ret__.name,
        network_injection=__ret__.network_injection,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type)
