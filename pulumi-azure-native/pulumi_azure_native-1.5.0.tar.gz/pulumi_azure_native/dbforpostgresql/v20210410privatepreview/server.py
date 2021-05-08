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

__all__ = ['ServerArgs', 'Server']

@pulumi.input_type
class ServerArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 administrator_login: Optional[pulumi.Input[str]] = None,
                 administrator_login_password: Optional[pulumi.Input[str]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 create_mode: Optional[pulumi.Input[Union[str, 'CreateMode']]] = None,
                 delegated_subnet_arguments: Optional[pulumi.Input['ServerPropertiesDelegatedSubnetArgumentsArgs']] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 ha_enabled: Optional[pulumi.Input['HAEnabledEnum']] = None,
                 identity: Optional[pulumi.Input['IdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 maintenance_window: Optional[pulumi.Input['MaintenanceWindowArgs']] = None,
                 point_in_time_utc: Optional[pulumi.Input[str]] = None,
                 private_dns_zone_arguments: Optional[pulumi.Input['ServerPropertiesPrivateDnsZoneArgumentsArgs']] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input['SkuArgs']] = None,
                 source_resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_server_name: Optional[pulumi.Input[str]] = None,
                 source_subscription_id: Optional[pulumi.Input[str]] = None,
                 storage_profile: Optional[pulumi.Input['StorageProfileArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[Union[str, 'ServerVersion']]] = None):
        """
        The set of arguments for constructing a Server resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] administrator_login: The administrator's login name of a server. Can only be specified when the server is being created (and is required for creation).
        :param pulumi.Input[str] administrator_login_password: The administrator login password (required for server creation).
        :param pulumi.Input[str] availability_zone: availability Zone information of the server.
        :param pulumi.Input[Union[str, 'CreateMode']] create_mode: The mode to create a new PostgreSQL server.
        :param pulumi.Input[str] display_name: The display name of a server.
        :param pulumi.Input['HAEnabledEnum'] ha_enabled: stand by count value can be either enabled or disabled
        :param pulumi.Input['IdentityArgs'] identity: The Azure Active Directory identity of the server.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['MaintenanceWindowArgs'] maintenance_window: Maintenance window of a server.
        :param pulumi.Input[str] point_in_time_utc: Restore point creation time (ISO8601 format), specifying the time to restore from.
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input['SkuArgs'] sku: The SKU (pricing tier) of the server.
        :param pulumi.Input[str] source_resource_group_name: The resource group name of source PostgreSQL server name to restore from.
        :param pulumi.Input[str] source_server_name: The source PostgreSQL server name to restore from.
        :param pulumi.Input[str] source_subscription_id: The subscription id of source PostgreSQL server name to restore from.
        :param pulumi.Input['StorageProfileArgs'] storage_profile: Storage profile of a server.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Union[str, 'ServerVersion']] version: PostgreSQL Server version.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if administrator_login is not None:
            pulumi.set(__self__, "administrator_login", administrator_login)
        if administrator_login_password is not None:
            pulumi.set(__self__, "administrator_login_password", administrator_login_password)
        if availability_zone is not None:
            pulumi.set(__self__, "availability_zone", availability_zone)
        if create_mode is not None:
            pulumi.set(__self__, "create_mode", create_mode)
        if delegated_subnet_arguments is not None:
            pulumi.set(__self__, "delegated_subnet_arguments", delegated_subnet_arguments)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if ha_enabled is not None:
            pulumi.set(__self__, "ha_enabled", ha_enabled)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if maintenance_window is not None:
            pulumi.set(__self__, "maintenance_window", maintenance_window)
        if point_in_time_utc is not None:
            pulumi.set(__self__, "point_in_time_utc", point_in_time_utc)
        if private_dns_zone_arguments is not None:
            pulumi.set(__self__, "private_dns_zone_arguments", private_dns_zone_arguments)
        if server_name is not None:
            pulumi.set(__self__, "server_name", server_name)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if source_resource_group_name is not None:
            pulumi.set(__self__, "source_resource_group_name", source_resource_group_name)
        if source_server_name is not None:
            pulumi.set(__self__, "source_server_name", source_server_name)
        if source_subscription_id is not None:
            pulumi.set(__self__, "source_subscription_id", source_subscription_id)
        if storage_profile is not None:
            pulumi.set(__self__, "storage_profile", storage_profile)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> Optional[pulumi.Input[str]]:
        """
        The administrator's login name of a server. Can only be specified when the server is being created (and is required for creation).
        """
        return pulumi.get(self, "administrator_login")

    @administrator_login.setter
    def administrator_login(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "administrator_login", value)

    @property
    @pulumi.getter(name="administratorLoginPassword")
    def administrator_login_password(self) -> Optional[pulumi.Input[str]]:
        """
        The administrator login password (required for server creation).
        """
        return pulumi.get(self, "administrator_login_password")

    @administrator_login_password.setter
    def administrator_login_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "administrator_login_password", value)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[str]]:
        """
        availability Zone information of the server.
        """
        return pulumi.get(self, "availability_zone")

    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "availability_zone", value)

    @property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[pulumi.Input[Union[str, 'CreateMode']]]:
        """
        The mode to create a new PostgreSQL server.
        """
        return pulumi.get(self, "create_mode")

    @create_mode.setter
    def create_mode(self, value: Optional[pulumi.Input[Union[str, 'CreateMode']]]):
        pulumi.set(self, "create_mode", value)

    @property
    @pulumi.getter(name="delegatedSubnetArguments")
    def delegated_subnet_arguments(self) -> Optional[pulumi.Input['ServerPropertiesDelegatedSubnetArgumentsArgs']]:
        return pulumi.get(self, "delegated_subnet_arguments")

    @delegated_subnet_arguments.setter
    def delegated_subnet_arguments(self, value: Optional[pulumi.Input['ServerPropertiesDelegatedSubnetArgumentsArgs']]):
        pulumi.set(self, "delegated_subnet_arguments", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of a server.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="haEnabled")
    def ha_enabled(self) -> Optional[pulumi.Input['HAEnabledEnum']]:
        """
        stand by count value can be either enabled or disabled
        """
        return pulumi.get(self, "ha_enabled")

    @ha_enabled.setter
    def ha_enabled(self, value: Optional[pulumi.Input['HAEnabledEnum']]):
        pulumi.set(self, "ha_enabled", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['IdentityArgs']]:
        """
        The Azure Active Directory identity of the server.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['IdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[pulumi.Input['MaintenanceWindowArgs']]:
        """
        Maintenance window of a server.
        """
        return pulumi.get(self, "maintenance_window")

    @maintenance_window.setter
    def maintenance_window(self, value: Optional[pulumi.Input['MaintenanceWindowArgs']]):
        pulumi.set(self, "maintenance_window", value)

    @property
    @pulumi.getter(name="pointInTimeUTC")
    def point_in_time_utc(self) -> Optional[pulumi.Input[str]]:
        """
        Restore point creation time (ISO8601 format), specifying the time to restore from.
        """
        return pulumi.get(self, "point_in_time_utc")

    @point_in_time_utc.setter
    def point_in_time_utc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "point_in_time_utc", value)

    @property
    @pulumi.getter(name="privateDnsZoneArguments")
    def private_dns_zone_arguments(self) -> Optional[pulumi.Input['ServerPropertiesPrivateDnsZoneArgumentsArgs']]:
        return pulumi.get(self, "private_dns_zone_arguments")

    @private_dns_zone_arguments.setter
    def private_dns_zone_arguments(self, value: Optional[pulumi.Input['ServerPropertiesPrivateDnsZoneArgumentsArgs']]):
        pulumi.set(self, "private_dns_zone_arguments", value)

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the server.
        """
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['SkuArgs']]:
        """
        The SKU (pricing tier) of the server.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['SkuArgs']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="sourceResourceGroupName")
    def source_resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource group name of source PostgreSQL server name to restore from.
        """
        return pulumi.get(self, "source_resource_group_name")

    @source_resource_group_name.setter
    def source_resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_resource_group_name", value)

    @property
    @pulumi.getter(name="sourceServerName")
    def source_server_name(self) -> Optional[pulumi.Input[str]]:
        """
        The source PostgreSQL server name to restore from.
        """
        return pulumi.get(self, "source_server_name")

    @source_server_name.setter
    def source_server_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_server_name", value)

    @property
    @pulumi.getter(name="sourceSubscriptionId")
    def source_subscription_id(self) -> Optional[pulumi.Input[str]]:
        """
        The subscription id of source PostgreSQL server name to restore from.
        """
        return pulumi.get(self, "source_subscription_id")

    @source_subscription_id.setter
    def source_subscription_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_subscription_id", value)

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input['StorageProfileArgs']]:
        """
        Storage profile of a server.
        """
        return pulumi.get(self, "storage_profile")

    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input['StorageProfileArgs']]):
        pulumi.set(self, "storage_profile", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[Union[str, 'ServerVersion']]]:
        """
        PostgreSQL Server version.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[Union[str, 'ServerVersion']]]):
        pulumi.set(self, "version", value)


class Server(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 administrator_login: Optional[pulumi.Input[str]] = None,
                 administrator_login_password: Optional[pulumi.Input[str]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 create_mode: Optional[pulumi.Input[Union[str, 'CreateMode']]] = None,
                 delegated_subnet_arguments: Optional[pulumi.Input[pulumi.InputType['ServerPropertiesDelegatedSubnetArgumentsArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 ha_enabled: Optional[pulumi.Input['HAEnabledEnum']] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 maintenance_window: Optional[pulumi.Input[pulumi.InputType['MaintenanceWindowArgs']]] = None,
                 point_in_time_utc: Optional[pulumi.Input[str]] = None,
                 private_dns_zone_arguments: Optional[pulumi.Input[pulumi.InputType['ServerPropertiesPrivateDnsZoneArgumentsArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 source_resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_server_name: Optional[pulumi.Input[str]] = None,
                 source_subscription_id: Optional[pulumi.Input[str]] = None,
                 storage_profile: Optional[pulumi.Input[pulumi.InputType['StorageProfileArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[Union[str, 'ServerVersion']]] = None,
                 __props__=None):
        """
        Represents a server.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] administrator_login: The administrator's login name of a server. Can only be specified when the server is being created (and is required for creation).
        :param pulumi.Input[str] administrator_login_password: The administrator login password (required for server creation).
        :param pulumi.Input[str] availability_zone: availability Zone information of the server.
        :param pulumi.Input[Union[str, 'CreateMode']] create_mode: The mode to create a new PostgreSQL server.
        :param pulumi.Input[str] display_name: The display name of a server.
        :param pulumi.Input['HAEnabledEnum'] ha_enabled: stand by count value can be either enabled or disabled
        :param pulumi.Input[pulumi.InputType['IdentityArgs']] identity: The Azure Active Directory identity of the server.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[pulumi.InputType['MaintenanceWindowArgs']] maintenance_window: Maintenance window of a server.
        :param pulumi.Input[str] point_in_time_utc: Restore point creation time (ISO8601 format), specifying the time to restore from.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: The SKU (pricing tier) of the server.
        :param pulumi.Input[str] source_resource_group_name: The resource group name of source PostgreSQL server name to restore from.
        :param pulumi.Input[str] source_server_name: The source PostgreSQL server name to restore from.
        :param pulumi.Input[str] source_subscription_id: The subscription id of source PostgreSQL server name to restore from.
        :param pulumi.Input[pulumi.InputType['StorageProfileArgs']] storage_profile: Storage profile of a server.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Union[str, 'ServerVersion']] version: PostgreSQL Server version.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a server.

        :param str resource_name: The name of the resource.
        :param ServerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 administrator_login: Optional[pulumi.Input[str]] = None,
                 administrator_login_password: Optional[pulumi.Input[str]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 create_mode: Optional[pulumi.Input[Union[str, 'CreateMode']]] = None,
                 delegated_subnet_arguments: Optional[pulumi.Input[pulumi.InputType['ServerPropertiesDelegatedSubnetArgumentsArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 ha_enabled: Optional[pulumi.Input['HAEnabledEnum']] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 maintenance_window: Optional[pulumi.Input[pulumi.InputType['MaintenanceWindowArgs']]] = None,
                 point_in_time_utc: Optional[pulumi.Input[str]] = None,
                 private_dns_zone_arguments: Optional[pulumi.Input[pulumi.InputType['ServerPropertiesPrivateDnsZoneArgumentsArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 source_resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_server_name: Optional[pulumi.Input[str]] = None,
                 source_subscription_id: Optional[pulumi.Input[str]] = None,
                 storage_profile: Optional[pulumi.Input[pulumi.InputType['StorageProfileArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[Union[str, 'ServerVersion']]] = None,
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
            __props__ = ServerArgs.__new__(ServerArgs)

            __props__.__dict__["administrator_login"] = administrator_login
            __props__.__dict__["administrator_login_password"] = administrator_login_password
            __props__.__dict__["availability_zone"] = availability_zone
            __props__.__dict__["create_mode"] = create_mode
            __props__.__dict__["delegated_subnet_arguments"] = delegated_subnet_arguments
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["ha_enabled"] = ha_enabled
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["maintenance_window"] = maintenance_window
            __props__.__dict__["point_in_time_utc"] = point_in_time_utc
            __props__.__dict__["private_dns_zone_arguments"] = private_dns_zone_arguments
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["server_name"] = server_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["source_resource_group_name"] = source_resource_group_name
            __props__.__dict__["source_server_name"] = source_server_name
            __props__.__dict__["source_subscription_id"] = source_subscription_id
            __props__.__dict__["storage_profile"] = storage_profile
            __props__.__dict__["tags"] = tags
            __props__.__dict__["version"] = version
            __props__.__dict__["byok_enforcement"] = None
            __props__.__dict__["fully_qualified_domain_name"] = None
            __props__.__dict__["ha_state"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["public_network_access"] = None
            __props__.__dict__["standby_availability_zone"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:dbforpostgresql/v20210410privatepreview:Server"), pulumi.Alias(type_="azure-native:dbforpostgresql/v20200214preview:Server"), pulumi.Alias(type_="azure-nextgen:dbforpostgresql/v20200214preview:Server"), pulumi.Alias(type_="azure-native:dbforpostgresql/v20200214privatepreview:Server"), pulumi.Alias(type_="azure-nextgen:dbforpostgresql/v20200214privatepreview:Server")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Server, __self__).__init__(
            'azure-native:dbforpostgresql/v20210410privatepreview:Server',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Server':
        """
        Get an existing Server resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServerArgs.__new__(ServerArgs)

        __props__.__dict__["administrator_login"] = None
        __props__.__dict__["availability_zone"] = None
        __props__.__dict__["byok_enforcement"] = None
        __props__.__dict__["delegated_subnet_arguments"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["fully_qualified_domain_name"] = None
        __props__.__dict__["ha_enabled"] = None
        __props__.__dict__["ha_state"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["maintenance_window"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["point_in_time_utc"] = None
        __props__.__dict__["private_dns_zone_arguments"] = None
        __props__.__dict__["public_network_access"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["source_resource_group_name"] = None
        __props__.__dict__["source_server_name"] = None
        __props__.__dict__["source_subscription_id"] = None
        __props__.__dict__["standby_availability_zone"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["storage_profile"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["version"] = None
        return Server(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> pulumi.Output[Optional[str]]:
        """
        The administrator's login name of a server. Can only be specified when the server is being created (and is required for creation).
        """
        return pulumi.get(self, "administrator_login")

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[Optional[str]]:
        """
        availability Zone information of the server.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="byokEnforcement")
    def byok_enforcement(self) -> pulumi.Output[str]:
        """
        Status showing whether the data encryption is enabled with customer-managed keys.
        """
        return pulumi.get(self, "byok_enforcement")

    @property
    @pulumi.getter(name="delegatedSubnetArguments")
    def delegated_subnet_arguments(self) -> pulumi.Output[Optional['outputs.ServerPropertiesResponseDelegatedSubnetArguments']]:
        return pulumi.get(self, "delegated_subnet_arguments")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The display name of a server.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="fullyQualifiedDomainName")
    def fully_qualified_domain_name(self) -> pulumi.Output[str]:
        """
        The fully qualified domain name of a server.
        """
        return pulumi.get(self, "fully_qualified_domain_name")

    @property
    @pulumi.getter(name="haEnabled")
    def ha_enabled(self) -> pulumi.Output[Optional[str]]:
        """
        stand by count value can be either enabled or disabled
        """
        return pulumi.get(self, "ha_enabled")

    @property
    @pulumi.getter(name="haState")
    def ha_state(self) -> pulumi.Output[str]:
        """
        A state of a HA server that is visible to user.
        """
        return pulumi.get(self, "ha_state")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityResponse']]:
        """
        The Azure Active Directory identity of the server.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> pulumi.Output[Optional['outputs.MaintenanceWindowResponse']]:
        """
        Maintenance window of a server.
        """
        return pulumi.get(self, "maintenance_window")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pointInTimeUTC")
    def point_in_time_utc(self) -> pulumi.Output[Optional[str]]:
        """
        Restore point creation time (ISO8601 format), specifying the time to restore from.
        """
        return pulumi.get(self, "point_in_time_utc")

    @property
    @pulumi.getter(name="privateDnsZoneArguments")
    def private_dns_zone_arguments(self) -> pulumi.Output[Optional['outputs.ServerPropertiesResponsePrivateDnsZoneArguments']]:
        return pulumi.get(self, "private_dns_zone_arguments")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[str]:
        """
        public network access is enabled or not
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        The SKU (pricing tier) of the server.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="sourceResourceGroupName")
    def source_resource_group_name(self) -> pulumi.Output[Optional[str]]:
        """
        The resource group name of source PostgreSQL server name to restore from.
        """
        return pulumi.get(self, "source_resource_group_name")

    @property
    @pulumi.getter(name="sourceServerName")
    def source_server_name(self) -> pulumi.Output[Optional[str]]:
        """
        The source PostgreSQL server name to restore from.
        """
        return pulumi.get(self, "source_server_name")

    @property
    @pulumi.getter(name="sourceSubscriptionId")
    def source_subscription_id(self) -> pulumi.Output[Optional[str]]:
        """
        The subscription id of source PostgreSQL server name to restore from.
        """
        return pulumi.get(self, "source_subscription_id")

    @property
    @pulumi.getter(name="standbyAvailabilityZone")
    def standby_availability_zone(self) -> pulumi.Output[str]:
        """
        availability Zone information of the server.
        """
        return pulumi.get(self, "standby_availability_zone")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        A state of a server that is visible to user.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> pulumi.Output[Optional['outputs.StorageProfileResponse']]:
        """
        Storage profile of a server.
        """
        return pulumi.get(self, "storage_profile")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[str]]:
        """
        PostgreSQL Server version.
        """
        return pulumi.get(self, "version")

