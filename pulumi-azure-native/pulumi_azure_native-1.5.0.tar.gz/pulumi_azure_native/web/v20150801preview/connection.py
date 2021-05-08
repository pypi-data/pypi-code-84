# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['ConnectionArgs', 'Connection']

@pulumi.input_type
class ConnectionArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 api: Optional[pulumi.Input['ExpandedParentApiEntityArgs']] = None,
                 changed_time: Optional[pulumi.Input[str]] = None,
                 connection_name: Optional[pulumi.Input[str]] = None,
                 created_time: Optional[pulumi.Input[str]] = None,
                 custom_parameter_values: Optional[pulumi.Input[Mapping[str, pulumi.Input['ParameterCustomLoginSettingValuesArgs']]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 first_expiration_time: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 keywords: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 non_secret_parameter_values: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 parameter_values: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 statuses: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectionStatusArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Connection resource.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input['ExpandedParentApiEntityArgs'] api: expanded connection provider name
        :param pulumi.Input[str] changed_time: Timestamp of last connection change.
        :param pulumi.Input[str] connection_name: The connection name.
        :param pulumi.Input[str] created_time: Timestamp of the connection creation
        :param pulumi.Input[Mapping[str, pulumi.Input['ParameterCustomLoginSettingValuesArgs']]] custom_parameter_values: Custom login setting values.
        :param pulumi.Input[str] display_name: display name
        :param pulumi.Input[str] first_expiration_time: Time in UTC when the first expiration of OAuth tokens
        :param pulumi.Input[str] id: Resource Id
        :param pulumi.Input[Sequence[pulumi.Input[str]]] keywords: List of Keywords that tag the acl
        :param pulumi.Input[str] kind: Kind of resource
        :param pulumi.Input[str] location: Resource Location
        :param pulumi.Input[str] name: Resource Name
        :param pulumi.Input[Mapping[str, Any]] non_secret_parameter_values: Tokens/Claim
        :param pulumi.Input[Mapping[str, Any]] parameter_values: Tokens/Claim
        :param pulumi.Input[Sequence[pulumi.Input['ConnectionStatusArgs']]] statuses: Status of the connection
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] type: Resource type
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if api is not None:
            pulumi.set(__self__, "api", api)
        if changed_time is not None:
            pulumi.set(__self__, "changed_time", changed_time)
        if connection_name is not None:
            pulumi.set(__self__, "connection_name", connection_name)
        if created_time is not None:
            pulumi.set(__self__, "created_time", created_time)
        if custom_parameter_values is not None:
            pulumi.set(__self__, "custom_parameter_values", custom_parameter_values)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if first_expiration_time is not None:
            pulumi.set(__self__, "first_expiration_time", first_expiration_time)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if keywords is not None:
            pulumi.set(__self__, "keywords", keywords)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if non_secret_parameter_values is not None:
            pulumi.set(__self__, "non_secret_parameter_values", non_secret_parameter_values)
        if parameter_values is not None:
            pulumi.set(__self__, "parameter_values", parameter_values)
        if statuses is not None:
            pulumi.set(__self__, "statuses", statuses)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def api(self) -> Optional[pulumi.Input['ExpandedParentApiEntityArgs']]:
        """
        expanded connection provider name
        """
        return pulumi.get(self, "api")

    @api.setter
    def api(self, value: Optional[pulumi.Input['ExpandedParentApiEntityArgs']]):
        pulumi.set(self, "api", value)

    @property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> Optional[pulumi.Input[str]]:
        """
        Timestamp of last connection change.
        """
        return pulumi.get(self, "changed_time")

    @changed_time.setter
    def changed_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "changed_time", value)

    @property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[pulumi.Input[str]]:
        """
        The connection name.
        """
        return pulumi.get(self, "connection_name")

    @connection_name.setter
    def connection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_name", value)

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[pulumi.Input[str]]:
        """
        Timestamp of the connection creation
        """
        return pulumi.get(self, "created_time")

    @created_time.setter
    def created_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_time", value)

    @property
    @pulumi.getter(name="customParameterValues")
    def custom_parameter_values(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['ParameterCustomLoginSettingValuesArgs']]]]:
        """
        Custom login setting values.
        """
        return pulumi.get(self, "custom_parameter_values")

    @custom_parameter_values.setter
    def custom_parameter_values(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['ParameterCustomLoginSettingValuesArgs']]]]):
        pulumi.set(self, "custom_parameter_values", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        display name
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="firstExpirationTime")
    def first_expiration_time(self) -> Optional[pulumi.Input[str]]:
        """
        Time in UTC when the first expiration of OAuth tokens
        """
        return pulumi.get(self, "first_expiration_time")

    @first_expiration_time.setter
    def first_expiration_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "first_expiration_time", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def keywords(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of Keywords that tag the acl
        """
        return pulumi.get(self, "keywords")

    @keywords.setter
    def keywords(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "keywords", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind of resource
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[Any]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="nonSecretParameterValues")
    def non_secret_parameter_values(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Tokens/Claim
        """
        return pulumi.get(self, "non_secret_parameter_values")

    @non_secret_parameter_values.setter
    def non_secret_parameter_values(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "non_secret_parameter_values", value)

    @property
    @pulumi.getter(name="parameterValues")
    def parameter_values(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Tokens/Claim
        """
        return pulumi.get(self, "parameter_values")

    @parameter_values.setter
    def parameter_values(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "parameter_values", value)

    @property
    @pulumi.getter
    def statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConnectionStatusArgs']]]]:
        """
        Status of the connection
        """
        return pulumi.get(self, "statuses")

    @statuses.setter
    def statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectionStatusArgs']]]]):
        pulumi.set(self, "statuses", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class Connection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api: Optional[pulumi.Input[pulumi.InputType['ExpandedParentApiEntityArgs']]] = None,
                 changed_time: Optional[pulumi.Input[str]] = None,
                 connection_name: Optional[pulumi.Input[str]] = None,
                 created_time: Optional[pulumi.Input[str]] = None,
                 custom_parameter_values: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ParameterCustomLoginSettingValuesArgs']]]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 first_expiration_time: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 keywords: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 non_secret_parameter_values: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 parameter_values: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 statuses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectionStatusArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        API Connection

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ExpandedParentApiEntityArgs']] api: expanded connection provider name
        :param pulumi.Input[str] changed_time: Timestamp of last connection change.
        :param pulumi.Input[str] connection_name: The connection name.
        :param pulumi.Input[str] created_time: Timestamp of the connection creation
        :param pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ParameterCustomLoginSettingValuesArgs']]]] custom_parameter_values: Custom login setting values.
        :param pulumi.Input[str] display_name: display name
        :param pulumi.Input[str] first_expiration_time: Time in UTC when the first expiration of OAuth tokens
        :param pulumi.Input[str] id: Resource Id
        :param pulumi.Input[Sequence[pulumi.Input[str]]] keywords: List of Keywords that tag the acl
        :param pulumi.Input[str] kind: Kind of resource
        :param pulumi.Input[str] location: Resource Location
        :param pulumi.Input[str] name: Resource Name
        :param pulumi.Input[Mapping[str, Any]] non_secret_parameter_values: Tokens/Claim
        :param pulumi.Input[Mapping[str, Any]] parameter_values: Tokens/Claim
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectionStatusArgs']]]] statuses: Status of the connection
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] type: Resource type
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        API Connection

        :param str resource_name: The name of the resource.
        :param ConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api: Optional[pulumi.Input[pulumi.InputType['ExpandedParentApiEntityArgs']]] = None,
                 changed_time: Optional[pulumi.Input[str]] = None,
                 connection_name: Optional[pulumi.Input[str]] = None,
                 created_time: Optional[pulumi.Input[str]] = None,
                 custom_parameter_values: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ParameterCustomLoginSettingValuesArgs']]]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 first_expiration_time: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 keywords: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 non_secret_parameter_values: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 parameter_values: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 statuses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectionStatusArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectionArgs.__new__(ConnectionArgs)

            __props__.__dict__["api"] = api
            __props__.__dict__["changed_time"] = changed_time
            __props__.__dict__["connection_name"] = connection_name
            __props__.__dict__["created_time"] = created_time
            __props__.__dict__["custom_parameter_values"] = custom_parameter_values
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["first_expiration_time"] = first_expiration_time
            __props__.__dict__["id"] = id
            __props__.__dict__["keywords"] = keywords
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["name"] = name
            __props__.__dict__["non_secret_parameter_values"] = non_secret_parameter_values
            __props__.__dict__["parameter_values"] = parameter_values
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["statuses"] = statuses
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tenant_id"] = tenant_id
            __props__.__dict__["type"] = type
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:web/v20150801preview:Connection"), pulumi.Alias(type_="azure-native:web:Connection"), pulumi.Alias(type_="azure-nextgen:web:Connection"), pulumi.Alias(type_="azure-native:web/v20160601:Connection"), pulumi.Alias(type_="azure-nextgen:web/v20160601:Connection")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Connection, __self__).__init__(
            'azure-native:web/v20150801preview:Connection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Connection':
        """
        Get an existing Connection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConnectionArgs.__new__(ConnectionArgs)

        __props__.__dict__["api"] = None
        __props__.__dict__["changed_time"] = None
        __props__.__dict__["created_time"] = None
        __props__.__dict__["custom_parameter_values"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["first_expiration_time"] = None
        __props__.__dict__["keywords"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["non_secret_parameter_values"] = None
        __props__.__dict__["parameter_values"] = None
        __props__.__dict__["statuses"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["tenant_id"] = None
        __props__.__dict__["type"] = None
        return Connection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def api(self) -> pulumi.Output[Optional['outputs.ExpandedParentApiEntityResponse']]:
        """
        expanded connection provider name
        """
        return pulumi.get(self, "api")

    @property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> pulumi.Output[Optional[str]]:
        """
        Timestamp of last connection change.
        """
        return pulumi.get(self, "changed_time")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[Optional[str]]:
        """
        Timestamp of the connection creation
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter(name="customParameterValues")
    def custom_parameter_values(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.ParameterCustomLoginSettingValuesResponse']]]:
        """
        Custom login setting values.
        """
        return pulumi.get(self, "custom_parameter_values")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        display name
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="firstExpirationTime")
    def first_expiration_time(self) -> pulumi.Output[Optional[str]]:
        """
        Time in UTC when the first expiration of OAuth tokens
        """
        return pulumi.get(self, "first_expiration_time")

    @property
    @pulumi.getter
    def keywords(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of Keywords that tag the acl
        """
        return pulumi.get(self, "keywords")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind of resource
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource Location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nonSecretParameterValues")
    def non_secret_parameter_values(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        Tokens/Claim
        """
        return pulumi.get(self, "non_secret_parameter_values")

    @property
    @pulumi.getter(name="parameterValues")
    def parameter_values(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        Tokens/Claim
        """
        return pulumi.get(self, "parameter_values")

    @property
    @pulumi.getter
    def statuses(self) -> pulumi.Output[Optional[Sequence['outputs.ConnectionStatusResponse']]]:
        """
        Status of the connection
        """
        return pulumi.get(self, "statuses")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

