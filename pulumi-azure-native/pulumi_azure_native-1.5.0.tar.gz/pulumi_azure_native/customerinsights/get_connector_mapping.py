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
    'GetConnectorMappingResult',
    'AwaitableGetConnectorMappingResult',
    'get_connector_mapping',
]

@pulumi.output_type
class GetConnectorMappingResult:
    """
    The connector mapping resource format.
    """
    def __init__(__self__, connector_mapping_name=None, connector_name=None, connector_type=None, created=None, data_format_id=None, description=None, display_name=None, entity_type=None, entity_type_name=None, id=None, last_modified=None, mapping_properties=None, name=None, next_run_time=None, run_id=None, state=None, tenant_id=None, type=None):
        if connector_mapping_name and not isinstance(connector_mapping_name, str):
            raise TypeError("Expected argument 'connector_mapping_name' to be a str")
        pulumi.set(__self__, "connector_mapping_name", connector_mapping_name)
        if connector_name and not isinstance(connector_name, str):
            raise TypeError("Expected argument 'connector_name' to be a str")
        pulumi.set(__self__, "connector_name", connector_name)
        if connector_type and not isinstance(connector_type, str):
            raise TypeError("Expected argument 'connector_type' to be a str")
        pulumi.set(__self__, "connector_type", connector_type)
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if data_format_id and not isinstance(data_format_id, str):
            raise TypeError("Expected argument 'data_format_id' to be a str")
        pulumi.set(__self__, "data_format_id", data_format_id)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if entity_type and not isinstance(entity_type, str):
            raise TypeError("Expected argument 'entity_type' to be a str")
        pulumi.set(__self__, "entity_type", entity_type)
        if entity_type_name and not isinstance(entity_type_name, str):
            raise TypeError("Expected argument 'entity_type_name' to be a str")
        pulumi.set(__self__, "entity_type_name", entity_type_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_modified and not isinstance(last_modified, str):
            raise TypeError("Expected argument 'last_modified' to be a str")
        pulumi.set(__self__, "last_modified", last_modified)
        if mapping_properties and not isinstance(mapping_properties, dict):
            raise TypeError("Expected argument 'mapping_properties' to be a dict")
        pulumi.set(__self__, "mapping_properties", mapping_properties)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if next_run_time and not isinstance(next_run_time, str):
            raise TypeError("Expected argument 'next_run_time' to be a str")
        pulumi.set(__self__, "next_run_time", next_run_time)
        if run_id and not isinstance(run_id, str):
            raise TypeError("Expected argument 'run_id' to be a str")
        pulumi.set(__self__, "run_id", run_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="connectorMappingName")
    def connector_mapping_name(self) -> str:
        """
        The connector mapping name
        """
        return pulumi.get(self, "connector_mapping_name")

    @property
    @pulumi.getter(name="connectorName")
    def connector_name(self) -> str:
        """
        The connector name.
        """
        return pulumi.get(self, "connector_name")

    @property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> Optional[str]:
        """
        Type of connector.
        """
        return pulumi.get(self, "connector_type")

    @property
    @pulumi.getter
    def created(self) -> str:
        """
        The created time.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="dataFormatId")
    def data_format_id(self) -> str:
        """
        The DataFormat ID.
        """
        return pulumi.get(self, "data_format_id")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the connector mapping.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        Display name for the connector mapping.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> str:
        """
        Defines which entity type the file should map to.
        """
        return pulumi.get(self, "entity_type")

    @property
    @pulumi.getter(name="entityTypeName")
    def entity_type_name(self) -> str:
        """
        The mapping entity name.
        """
        return pulumi.get(self, "entity_type_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> str:
        """
        The last modified time.
        """
        return pulumi.get(self, "last_modified")

    @property
    @pulumi.getter(name="mappingProperties")
    def mapping_properties(self) -> 'outputs.ConnectorMappingPropertiesResponse':
        """
        The properties of the mapping.
        """
        return pulumi.get(self, "mapping_properties")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nextRunTime")
    def next_run_time(self) -> str:
        """
        The next run time based on customer's settings.
        """
        return pulumi.get(self, "next_run_time")

    @property
    @pulumi.getter(name="runId")
    def run_id(self) -> str:
        """
        The RunId.
        """
        return pulumi.get(self, "run_id")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        State of connector mapping.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The hub name.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetConnectorMappingResult(GetConnectorMappingResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConnectorMappingResult(
            connector_mapping_name=self.connector_mapping_name,
            connector_name=self.connector_name,
            connector_type=self.connector_type,
            created=self.created,
            data_format_id=self.data_format_id,
            description=self.description,
            display_name=self.display_name,
            entity_type=self.entity_type,
            entity_type_name=self.entity_type_name,
            id=self.id,
            last_modified=self.last_modified,
            mapping_properties=self.mapping_properties,
            name=self.name,
            next_run_time=self.next_run_time,
            run_id=self.run_id,
            state=self.state,
            tenant_id=self.tenant_id,
            type=self.type)


def get_connector_mapping(connector_name: Optional[str] = None,
                          hub_name: Optional[str] = None,
                          mapping_name: Optional[str] = None,
                          resource_group_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConnectorMappingResult:
    """
    The connector mapping resource format.
    API Version: 2017-04-26.


    :param str connector_name: The name of the connector.
    :param str hub_name: The name of the hub.
    :param str mapping_name: The name of the connector mapping.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['connectorName'] = connector_name
    __args__['hubName'] = hub_name
    __args__['mappingName'] = mapping_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:customerinsights:getConnectorMapping', __args__, opts=opts, typ=GetConnectorMappingResult).value

    return AwaitableGetConnectorMappingResult(
        connector_mapping_name=__ret__.connector_mapping_name,
        connector_name=__ret__.connector_name,
        connector_type=__ret__.connector_type,
        created=__ret__.created,
        data_format_id=__ret__.data_format_id,
        description=__ret__.description,
        display_name=__ret__.display_name,
        entity_type=__ret__.entity_type,
        entity_type_name=__ret__.entity_type_name,
        id=__ret__.id,
        last_modified=__ret__.last_modified,
        mapping_properties=__ret__.mapping_properties,
        name=__ret__.name,
        next_run_time=__ret__.next_run_time,
        run_id=__ret__.run_id,
        state=__ret__.state,
        tenant_id=__ret__.tenant_id,
        type=__ret__.type)
