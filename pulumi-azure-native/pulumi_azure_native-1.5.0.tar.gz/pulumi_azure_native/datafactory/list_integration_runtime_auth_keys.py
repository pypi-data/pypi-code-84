# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'ListIntegrationRuntimeAuthKeysResult',
    'AwaitableListIntegrationRuntimeAuthKeysResult',
    'list_integration_runtime_auth_keys',
]

@pulumi.output_type
class ListIntegrationRuntimeAuthKeysResult:
    """
    The integration runtime authentication keys.
    """
    def __init__(__self__, auth_key1=None, auth_key2=None):
        if auth_key1 and not isinstance(auth_key1, str):
            raise TypeError("Expected argument 'auth_key1' to be a str")
        pulumi.set(__self__, "auth_key1", auth_key1)
        if auth_key2 and not isinstance(auth_key2, str):
            raise TypeError("Expected argument 'auth_key2' to be a str")
        pulumi.set(__self__, "auth_key2", auth_key2)

    @property
    @pulumi.getter(name="authKey1")
    def auth_key1(self) -> Optional[str]:
        """
        The primary integration runtime authentication key.
        """
        return pulumi.get(self, "auth_key1")

    @property
    @pulumi.getter(name="authKey2")
    def auth_key2(self) -> Optional[str]:
        """
        The secondary integration runtime authentication key.
        """
        return pulumi.get(self, "auth_key2")


class AwaitableListIntegrationRuntimeAuthKeysResult(ListIntegrationRuntimeAuthKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListIntegrationRuntimeAuthKeysResult(
            auth_key1=self.auth_key1,
            auth_key2=self.auth_key2)


def list_integration_runtime_auth_keys(factory_name: Optional[str] = None,
                                       integration_runtime_name: Optional[str] = None,
                                       resource_group_name: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListIntegrationRuntimeAuthKeysResult:
    """
    The integration runtime authentication keys.
    API Version: 2018-06-01.


    :param str factory_name: The factory name.
    :param str integration_runtime_name: The integration runtime name.
    :param str resource_group_name: The resource group name.
    """
    __args__ = dict()
    __args__['factoryName'] = factory_name
    __args__['integrationRuntimeName'] = integration_runtime_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:datafactory:listIntegrationRuntimeAuthKeys', __args__, opts=opts, typ=ListIntegrationRuntimeAuthKeysResult).value

    return AwaitableListIntegrationRuntimeAuthKeysResult(
        auth_key1=__ret__.auth_key1,
        auth_key2=__ret__.auth_key2)
