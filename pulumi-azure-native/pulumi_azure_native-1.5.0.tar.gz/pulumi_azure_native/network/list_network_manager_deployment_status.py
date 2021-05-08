# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'ListNetworkManagerDeploymentStatusResult',
    'AwaitableListNetworkManagerDeploymentStatusResult',
    'list_network_manager_deployment_status',
]

@pulumi.output_type
class ListNetworkManagerDeploymentStatusResult:
    """
    A list of Network Manager Deployment Status
    """
    def __init__(__self__, skip_token=None, value=None):
        if skip_token and not isinstance(skip_token, str):
            raise TypeError("Expected argument 'skip_token' to be a str")
        pulumi.set(__self__, "skip_token", skip_token)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="skipToken")
    def skip_token(self) -> Optional[str]:
        """
        When present, the value can be passed to a subsequent query call (together with the same query and scopes used in the current request) to retrieve the next page of data.
        """
        return pulumi.get(self, "skip_token")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.NetworkManagerDeploymentStatusResponse']]:
        """
        Gets a page of Network Manager Deployment Status
        """
        return pulumi.get(self, "value")


class AwaitableListNetworkManagerDeploymentStatusResult(ListNetworkManagerDeploymentStatusResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListNetworkManagerDeploymentStatusResult(
            skip_token=self.skip_token,
            value=self.value)


def list_network_manager_deployment_status(deployment_types: Optional[Sequence[Union[str, 'ConfigurationType']]] = None,
                                           network_manager_name: Optional[str] = None,
                                           regions: Optional[Sequence[str]] = None,
                                           resource_group_name: Optional[str] = None,
                                           skip_token: Optional[str] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListNetworkManagerDeploymentStatusResult:
    """
    A list of Network Manager Deployment Status
    API Version: 2021-02-01-preview.


    :param Sequence[Union[str, 'ConfigurationType']] deployment_types: List of deployment types.
    :param str network_manager_name: The name of the network manager.
    :param Sequence[str] regions: List of locations.
    :param str resource_group_name: The name of the resource group.
    :param str skip_token: Continuation token for pagination, capturing the next page size and offset, as well as the context of the query.
    """
    __args__ = dict()
    __args__['deploymentTypes'] = deployment_types
    __args__['networkManagerName'] = network_manager_name
    __args__['regions'] = regions
    __args__['resourceGroupName'] = resource_group_name
    __args__['skipToken'] = skip_token
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:network:listNetworkManagerDeploymentStatus', __args__, opts=opts, typ=ListNetworkManagerDeploymentStatusResult).value

    return AwaitableListNetworkManagerDeploymentStatusResult(
        skip_token=__ret__.skip_token,
        value=__ret__.value)
