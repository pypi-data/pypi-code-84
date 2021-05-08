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
    'GetAnalyticsItemResult',
    'AwaitableGetAnalyticsItemResult',
    'get_analytics_item',
]

@pulumi.output_type
class GetAnalyticsItemResult:
    """
    Properties that define an Analytics item that is associated to an Application Insights component.
    """
    def __init__(__self__, content=None, id=None, name=None, properties=None, scope=None, time_created=None, time_modified=None, type=None, version=None):
        if content and not isinstance(content, str):
            raise TypeError("Expected argument 'content' to be a str")
        pulumi.set(__self__, "content", content)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if scope and not isinstance(scope, str):
            raise TypeError("Expected argument 'scope' to be a str")
        pulumi.set(__self__, "scope", scope)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_modified and not isinstance(time_modified, str):
            raise TypeError("Expected argument 'time_modified' to be a str")
        pulumi.set(__self__, "time_modified", time_modified)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def content(self) -> Optional[str]:
        """
        The content of this item
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Internally assigned unique id of the item definition.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The user-defined name of the item.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.ApplicationInsightsComponentAnalyticsItemPropertiesResponse':
        """
        A set of properties that can be defined in the context of a specific item type. Each type may have its own properties.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def scope(self) -> Optional[str]:
        """
        Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        Date and time in UTC when this item was created.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeModified")
    def time_modified(self) -> str:
        """
        Date and time in UTC of the last modification that was made to this item.
        """
        return pulumi.get(self, "time_modified")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        Enum indicating the type of the Analytics item.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        This instance's version of the data model. This can change as new features are added.
        """
        return pulumi.get(self, "version")


class AwaitableGetAnalyticsItemResult(GetAnalyticsItemResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAnalyticsItemResult(
            content=self.content,
            id=self.id,
            name=self.name,
            properties=self.properties,
            scope=self.scope,
            time_created=self.time_created,
            time_modified=self.time_modified,
            type=self.type,
            version=self.version)


def get_analytics_item(id: Optional[str] = None,
                       name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       resource_name: Optional[str] = None,
                       scope_path: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAnalyticsItemResult:
    """
    Properties that define an Analytics item that is associated to an Application Insights component.
    API Version: 2015-05-01.


    :param str id: The Id of a specific item defined in the Application Insights component
    :param str name: The name of a specific item defined in the Application Insights component
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the Application Insights component resource.
    :param str scope_path: Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    __args__['scopePath'] = scope_path
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:insights:getAnalyticsItem', __args__, opts=opts, typ=GetAnalyticsItemResult).value

    return AwaitableGetAnalyticsItemResult(
        content=__ret__.content,
        id=__ret__.id,
        name=__ret__.name,
        properties=__ret__.properties,
        scope=__ret__.scope,
        time_created=__ret__.time_created,
        time_modified=__ret__.time_modified,
        type=__ret__.type,
        version=__ret__.version)
