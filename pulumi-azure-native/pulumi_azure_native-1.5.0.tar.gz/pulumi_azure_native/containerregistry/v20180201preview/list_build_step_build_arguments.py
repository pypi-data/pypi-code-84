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
    'ListBuildStepBuildArgumentsResult',
    'AwaitableListBuildStepBuildArgumentsResult',
    'list_build_step_build_arguments',
]

@pulumi.output_type
class ListBuildStepBuildArgumentsResult:
    """
    The list of build arguments for a build step.
    """
    def __init__(__self__, next_link=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[str]:
        """
        The URI that can be used to request the next set of paged results.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.BuildArgumentResponse']]:
        """
        The collection value.
        """
        return pulumi.get(self, "value")


class AwaitableListBuildStepBuildArgumentsResult(ListBuildStepBuildArgumentsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListBuildStepBuildArgumentsResult(
            next_link=self.next_link,
            value=self.value)


def list_build_step_build_arguments(build_task_name: Optional[str] = None,
                                    registry_name: Optional[str] = None,
                                    resource_group_name: Optional[str] = None,
                                    step_name: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListBuildStepBuildArgumentsResult:
    """
    The list of build arguments for a build step.


    :param str build_task_name: The name of the container registry build task.
    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group to which the container registry belongs.
    :param str step_name: The name of a build step for a container registry build task.
    """
    __args__ = dict()
    __args__['buildTaskName'] = build_task_name
    __args__['registryName'] = registry_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['stepName'] = step_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:containerregistry/v20180201preview:listBuildStepBuildArguments', __args__, opts=opts, typ=ListBuildStepBuildArgumentsResult).value

    return AwaitableListBuildStepBuildArgumentsResult(
        next_link=__ret__.next_link,
        value=__ret__.value)
