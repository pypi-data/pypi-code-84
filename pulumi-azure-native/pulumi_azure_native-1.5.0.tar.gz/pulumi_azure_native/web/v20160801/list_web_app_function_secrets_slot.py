# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'ListWebAppFunctionSecretsSlotResult',
    'AwaitableListWebAppFunctionSecretsSlotResult',
    'list_web_app_function_secrets_slot',
]

@pulumi.output_type
class ListWebAppFunctionSecretsSlotResult:
    """
    Function secrets.
    """
    def __init__(__self__, id=None, key=None, kind=None, name=None, trigger_url=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key and not isinstance(key, str):
            raise TypeError("Expected argument 'key' to be a str")
        pulumi.set(__self__, "key", key)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if trigger_url and not isinstance(trigger_url, str):
            raise TypeError("Expected argument 'trigger_url' to be a str")
        pulumi.set(__self__, "trigger_url", trigger_url)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        """
        Secret key.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="triggerUrl")
    def trigger_url(self) -> Optional[str]:
        """
        Trigger URL.
        """
        return pulumi.get(self, "trigger_url")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableListWebAppFunctionSecretsSlotResult(ListWebAppFunctionSecretsSlotResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListWebAppFunctionSecretsSlotResult(
            id=self.id,
            key=self.key,
            kind=self.kind,
            name=self.name,
            trigger_url=self.trigger_url,
            type=self.type)


def list_web_app_function_secrets_slot(function_name: Optional[str] = None,
                                       name: Optional[str] = None,
                                       resource_group_name: Optional[str] = None,
                                       slot: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListWebAppFunctionSecretsSlotResult:
    """
    Function secrets.


    :param str function_name: Function name.
    :param str name: Site name.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    :param str slot: Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
    """
    __args__ = dict()
    __args__['functionName'] = function_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['slot'] = slot
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:web/v20160801:listWebAppFunctionSecretsSlot', __args__, opts=opts, typ=ListWebAppFunctionSecretsSlotResult).value

    return AwaitableListWebAppFunctionSecretsSlotResult(
        id=__ret__.id,
        key=__ret__.key,
        kind=__ret__.kind,
        name=__ret__.name,
        trigger_url=__ret__.trigger_url,
        type=__ret__.type)
