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
    'GetVirtualNetworkResourceResult',
    'AwaitableGetVirtualNetworkResourceResult',
    'get_virtual_network_resource',
]

@pulumi.output_type
class GetVirtualNetworkResourceResult:
    """
    A virtual network.
    """
    def __init__(__self__, allowed_subnets=None, description=None, external_provider_resource_id=None, id=None, location=None, name=None, provisioning_state=None, subnet_overrides=None, tags=None, type=None):
        if allowed_subnets and not isinstance(allowed_subnets, list):
            raise TypeError("Expected argument 'allowed_subnets' to be a list")
        pulumi.set(__self__, "allowed_subnets", allowed_subnets)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if external_provider_resource_id and not isinstance(external_provider_resource_id, str):
            raise TypeError("Expected argument 'external_provider_resource_id' to be a str")
        pulumi.set(__self__, "external_provider_resource_id", external_provider_resource_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if subnet_overrides and not isinstance(subnet_overrides, list):
            raise TypeError("Expected argument 'subnet_overrides' to be a list")
        pulumi.set(__self__, "subnet_overrides", subnet_overrides)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="allowedSubnets")
    def allowed_subnets(self) -> Optional[Sequence['outputs.SubnetResponse']]:
        """
        The allowed subnets of the virtual network.
        """
        return pulumi.get(self, "allowed_subnets")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the virtual network.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="externalProviderResourceId")
    def external_provider_resource_id(self) -> Optional[str]:
        """
        The Microsoft.Network resource identifier of the virtual network.
        """
        return pulumi.get(self, "external_provider_resource_id")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The identifier of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[str]:
        """
        The provisioning status of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="subnetOverrides")
    def subnet_overrides(self) -> Optional[Sequence['outputs.SubnetOverrideResponse']]:
        """
        The subnet overrides of the virtual network.
        """
        return pulumi.get(self, "subnet_overrides")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetVirtualNetworkResourceResult(GetVirtualNetworkResourceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualNetworkResourceResult(
            allowed_subnets=self.allowed_subnets,
            description=self.description,
            external_provider_resource_id=self.external_provider_resource_id,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            subnet_overrides=self.subnet_overrides,
            tags=self.tags,
            type=self.type)


def get_virtual_network_resource(lab_name: Optional[str] = None,
                                 name: Optional[str] = None,
                                 resource_group_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualNetworkResourceResult:
    """
    A virtual network.


    :param str lab_name: The name of the lab.
    :param str name: The name of the virtual network.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['labName'] = lab_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:devtestlab/v20150521preview:getVirtualNetworkResource', __args__, opts=opts, typ=GetVirtualNetworkResourceResult).value

    return AwaitableGetVirtualNetworkResourceResult(
        allowed_subnets=__ret__.allowed_subnets,
        description=__ret__.description,
        external_provider_resource_id=__ret__.external_provider_resource_id,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        subnet_overrides=__ret__.subnet_overrides,
        tags=__ret__.tags,
        type=__ret__.type)
