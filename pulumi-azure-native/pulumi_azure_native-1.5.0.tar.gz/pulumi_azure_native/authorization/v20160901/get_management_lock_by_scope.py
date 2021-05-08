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
    'GetManagementLockByScopeResult',
    'AwaitableGetManagementLockByScopeResult',
    'get_management_lock_by_scope',
]

@pulumi.output_type
class GetManagementLockByScopeResult:
    """
    The lock information.
    """
    def __init__(__self__, id=None, level=None, name=None, notes=None, owners=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if level and not isinstance(level, str):
            raise TypeError("Expected argument 'level' to be a str")
        pulumi.set(__self__, "level", level)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if notes and not isinstance(notes, str):
            raise TypeError("Expected argument 'notes' to be a str")
        pulumi.set(__self__, "notes", notes)
        if owners and not isinstance(owners, list):
            raise TypeError("Expected argument 'owners' to be a list")
        pulumi.set(__self__, "owners", owners)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource ID of the lock.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def level(self) -> str:
        """
        The level of the lock. Possible values are: NotSpecified, CanNotDelete, ReadOnly. CanNotDelete means authorized users are able to read and modify the resources, but not delete. ReadOnly means authorized users can only read from a resource, but they can't modify or delete it.
        """
        return pulumi.get(self, "level")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the lock.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def notes(self) -> Optional[str]:
        """
        Notes about the lock. Maximum of 512 characters.
        """
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter
    def owners(self) -> Optional[Sequence['outputs.ManagementLockOwnerResponse']]:
        """
        The owners of the lock.
        """
        return pulumi.get(self, "owners")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The resource type of the lock - Microsoft.Authorization/locks.
        """
        return pulumi.get(self, "type")


class AwaitableGetManagementLockByScopeResult(GetManagementLockByScopeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagementLockByScopeResult(
            id=self.id,
            level=self.level,
            name=self.name,
            notes=self.notes,
            owners=self.owners,
            type=self.type)


def get_management_lock_by_scope(lock_name: Optional[str] = None,
                                 scope: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagementLockByScopeResult:
    """
    The lock information.


    :param str lock_name: The name of lock.
    :param str scope: The scope for the lock. 
    """
    __args__ = dict()
    __args__['lockName'] = lock_name
    __args__['scope'] = scope
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:authorization/v20160901:getManagementLockByScope', __args__, opts=opts, typ=GetManagementLockByScopeResult).value

    return AwaitableGetManagementLockByScopeResult(
        id=__ret__.id,
        level=__ret__.level,
        name=__ret__.name,
        notes=__ret__.notes,
        owners=__ret__.owners,
        type=__ret__.type)
