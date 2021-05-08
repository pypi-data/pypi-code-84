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
    'GetSoftwareUpdateConfigurationByNameResult',
    'AwaitableGetSoftwareUpdateConfigurationByNameResult',
    'get_software_update_configuration_by_name',
]

@pulumi.output_type
class GetSoftwareUpdateConfigurationByNameResult:
    """
    Software update configuration properties.
    """
    def __init__(__self__, created_by=None, creation_time=None, error=None, id=None, last_modified_by=None, last_modified_time=None, name=None, provisioning_state=None, schedule_info=None, tasks=None, type=None, update_configuration=None):
        if created_by and not isinstance(created_by, str):
            raise TypeError("Expected argument 'created_by' to be a str")
        pulumi.set(__self__, "created_by", created_by)
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if error and not isinstance(error, dict):
            raise TypeError("Expected argument 'error' to be a dict")
        pulumi.set(__self__, "error", error)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_modified_by and not isinstance(last_modified_by, str):
            raise TypeError("Expected argument 'last_modified_by' to be a str")
        pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_time and not isinstance(last_modified_time, str):
            raise TypeError("Expected argument 'last_modified_time' to be a str")
        pulumi.set(__self__, "last_modified_time", last_modified_time)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if schedule_info and not isinstance(schedule_info, dict):
            raise TypeError("Expected argument 'schedule_info' to be a dict")
        pulumi.set(__self__, "schedule_info", schedule_info)
        if tasks and not isinstance(tasks, dict):
            raise TypeError("Expected argument 'tasks' to be a dict")
        pulumi.set(__self__, "tasks", tasks)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if update_configuration and not isinstance(update_configuration, dict):
            raise TypeError("Expected argument 'update_configuration' to be a dict")
        pulumi.set(__self__, "update_configuration", update_configuration)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> str:
        """
        CreatedBy property, which only appears in the response.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> str:
        """
        Creation time of the resource, which only appears in the response.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def error(self) -> Optional['outputs.ErrorResponseResponse']:
        """
        Details of provisioning error
        """
        return pulumi.get(self, "error")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> str:
        """
        LastModifiedBy property, which only appears in the response.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> str:
        """
        Last time resource was modified, which only appears in the response.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state for the software update configuration, which only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="scheduleInfo")
    def schedule_info(self) -> 'outputs.SUCSchedulePropertiesResponse':
        """
        Schedule information for the Software update configuration
        """
        return pulumi.get(self, "schedule_info")

    @property
    @pulumi.getter
    def tasks(self) -> Optional['outputs.SoftwareUpdateConfigurationTasksResponse']:
        """
        Tasks information for the Software update configuration.
        """
        return pulumi.get(self, "tasks")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updateConfiguration")
    def update_configuration(self) -> 'outputs.UpdateConfigurationResponse':
        """
        update specific properties for the Software update configuration
        """
        return pulumi.get(self, "update_configuration")


class AwaitableGetSoftwareUpdateConfigurationByNameResult(GetSoftwareUpdateConfigurationByNameResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSoftwareUpdateConfigurationByNameResult(
            created_by=self.created_by,
            creation_time=self.creation_time,
            error=self.error,
            id=self.id,
            last_modified_by=self.last_modified_by,
            last_modified_time=self.last_modified_time,
            name=self.name,
            provisioning_state=self.provisioning_state,
            schedule_info=self.schedule_info,
            tasks=self.tasks,
            type=self.type,
            update_configuration=self.update_configuration)


def get_software_update_configuration_by_name(automation_account_name: Optional[str] = None,
                                              resource_group_name: Optional[str] = None,
                                              software_update_configuration_name: Optional[str] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSoftwareUpdateConfigurationByNameResult:
    """
    Software update configuration properties.


    :param str automation_account_name: The name of the automation account.
    :param str resource_group_name: Name of an Azure Resource group.
    :param str software_update_configuration_name: The name of the software update configuration to be created.
    """
    __args__ = dict()
    __args__['automationAccountName'] = automation_account_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['softwareUpdateConfigurationName'] = software_update_configuration_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:automation/v20190601:getSoftwareUpdateConfigurationByName', __args__, opts=opts, typ=GetSoftwareUpdateConfigurationByNameResult).value

    return AwaitableGetSoftwareUpdateConfigurationByNameResult(
        created_by=__ret__.created_by,
        creation_time=__ret__.creation_time,
        error=__ret__.error,
        id=__ret__.id,
        last_modified_by=__ret__.last_modified_by,
        last_modified_time=__ret__.last_modified_time,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        schedule_info=__ret__.schedule_info,
        tasks=__ret__.tasks,
        type=__ret__.type,
        update_configuration=__ret__.update_configuration)
