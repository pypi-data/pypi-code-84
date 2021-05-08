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
    'GetJobResult',
    'AwaitableGetJobResult',
    'get_job',
]

@pulumi.output_type
class GetJobResult:
    """
    A Job resource type. The progress and state can be obtained by polling a Job or subscribing to events using EventGrid.
    """
    def __init__(__self__, created=None, description=None, id=None, input=None, last_modified=None, name=None, outputs=None, priority=None, state=None, type=None):
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if input and not isinstance(input, dict):
            raise TypeError("Expected argument 'input' to be a dict")
        pulumi.set(__self__, "input", input)
        if last_modified and not isinstance(last_modified, str):
            raise TypeError("Expected argument 'last_modified' to be a str")
        pulumi.set(__self__, "last_modified", last_modified)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if outputs and not isinstance(outputs, list):
            raise TypeError("Expected argument 'outputs' to be a list")
        pulumi.set(__self__, "outputs", outputs)
        if priority and not isinstance(priority, str):
            raise TypeError("Expected argument 'priority' to be a str")
        pulumi.set(__self__, "priority", priority)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def created(self) -> str:
        """
        The UTC date and time when the Job was created, in 'YYYY-MM-DDThh:mm:ssZ' format.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Optional customer supplied description of the Job.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def input(self) -> Any:
        """
        The inputs for the Job.
        """
        return pulumi.get(self, "input")

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> str:
        """
        The UTC date and time when the Job was last updated, in 'YYYY-MM-DDThh:mm:ssZ' format.
        """
        return pulumi.get(self, "last_modified")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def outputs(self) -> Sequence['outputs.JobOutputAssetResponse']:
        """
        The outputs for the Job.
        """
        return pulumi.get(self, "outputs")

    @property
    @pulumi.getter
    def priority(self) -> Optional[str]:
        """
        Priority with which the job should be processed. Higher priority jobs are processed before lower priority jobs. If not set, the default is normal.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the job.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetJobResult(GetJobResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetJobResult(
            created=self.created,
            description=self.description,
            id=self.id,
            input=self.input,
            last_modified=self.last_modified,
            name=self.name,
            outputs=self.outputs,
            priority=self.priority,
            state=self.state,
            type=self.type)


def get_job(account_name: Optional[str] = None,
            job_name: Optional[str] = None,
            resource_group_name: Optional[str] = None,
            transform_name: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetJobResult:
    """
    A Job resource type. The progress and state can be obtained by polling a Job or subscribing to events using EventGrid.


    :param str account_name: The Media Services account name.
    :param str job_name: The Job name.
    :param str resource_group_name: The name of the resource group within the Azure subscription.
    :param str transform_name: The Transform name.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['jobName'] = job_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['transformName'] = transform_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:media/v20180330preview:getJob', __args__, opts=opts, typ=GetJobResult).value

    return AwaitableGetJobResult(
        created=__ret__.created,
        description=__ret__.description,
        id=__ret__.id,
        input=__ret__.input,
        last_modified=__ret__.last_modified,
        name=__ret__.name,
        outputs=__ret__.outputs,
        priority=__ret__.priority,
        state=__ret__.state,
        type=__ret__.type)
