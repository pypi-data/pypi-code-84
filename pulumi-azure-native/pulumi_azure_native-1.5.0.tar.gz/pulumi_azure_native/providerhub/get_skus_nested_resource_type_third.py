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
    'GetSkusNestedResourceTypeThirdResult',
    'AwaitableGetSkusNestedResourceTypeThirdResult',
    'get_skus_nested_resource_type_third',
]

@pulumi.output_type
class GetSkusNestedResourceTypeThirdResult:
    def __init__(__self__, id=None, name=None, properties=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.SkuResourceResponseProperties':
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetSkusNestedResourceTypeThirdResult(GetSkusNestedResourceTypeThirdResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSkusNestedResourceTypeThirdResult(
            id=self.id,
            name=self.name,
            properties=self.properties,
            type=self.type)


def get_skus_nested_resource_type_third(nested_resource_type_first: Optional[str] = None,
                                        nested_resource_type_second: Optional[str] = None,
                                        nested_resource_type_third: Optional[str] = None,
                                        provider_namespace: Optional[str] = None,
                                        resource_type: Optional[str] = None,
                                        sku: Optional[str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSkusNestedResourceTypeThirdResult:
    """
    API Version: 2020-11-20.


    :param str nested_resource_type_first: The first child resource type.
    :param str nested_resource_type_second: The second child resource type.
    :param str nested_resource_type_third: The third child resource type.
    :param str provider_namespace: The name of the resource provider hosted within ProviderHub.
    :param str resource_type: The resource type.
    :param str sku: The SKU.
    """
    __args__ = dict()
    __args__['nestedResourceTypeFirst'] = nested_resource_type_first
    __args__['nestedResourceTypeSecond'] = nested_resource_type_second
    __args__['nestedResourceTypeThird'] = nested_resource_type_third
    __args__['providerNamespace'] = provider_namespace
    __args__['resourceType'] = resource_type
    __args__['sku'] = sku
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:providerhub:getSkusNestedResourceTypeThird', __args__, opts=opts, typ=GetSkusNestedResourceTypeThirdResult).value

    return AwaitableGetSkusNestedResourceTypeThirdResult(
        id=__ret__.id,
        name=__ret__.name,
        properties=__ret__.properties,
        type=__ret__.type)
