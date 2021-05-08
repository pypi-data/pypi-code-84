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
    'ListJobRemoteLoginInformationResult',
    'AwaitableListJobRemoteLoginInformationResult',
    'list_job_remote_login_information',
]

@pulumi.output_type
class ListJobRemoteLoginInformationResult:
    """
    Values returned by the List operation.
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
    def next_link(self) -> str:
        """
        The continuation token.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Sequence['outputs.RemoteLoginInformationResponse']:
        """
        The collection of returned remote login details.
        """
        return pulumi.get(self, "value")


class AwaitableListJobRemoteLoginInformationResult(ListJobRemoteLoginInformationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListJobRemoteLoginInformationResult(
            next_link=self.next_link,
            value=self.value)


def list_job_remote_login_information(experiment_name: Optional[str] = None,
                                      job_name: Optional[str] = None,
                                      resource_group_name: Optional[str] = None,
                                      workspace_name: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListJobRemoteLoginInformationResult:
    """
    Values returned by the List operation.
    API Version: 2018-05-01.


    :param str experiment_name: The name of the experiment. Experiment names can only contain a combination of alphanumeric characters along with dash (-) and underscore (_). The name must be from 1 through 64 characters long.
    :param str job_name: The name of the job within the specified resource group. Job names can only contain a combination of alphanumeric characters along with dash (-) and underscore (_). The name must be from 1 through 64 characters long.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    :param str workspace_name: The name of the workspace. Workspace names can only contain a combination of alphanumeric characters along with dash (-) and underscore (_). The name must be from 1 through 64 characters long.
    """
    __args__ = dict()
    __args__['experimentName'] = experiment_name
    __args__['jobName'] = job_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:batchai:listJobRemoteLoginInformation', __args__, opts=opts, typ=ListJobRemoteLoginInformationResult).value

    return AwaitableListJobRemoteLoginInformationResult(
        next_link=__ret__.next_link,
        value=__ret__.value)
