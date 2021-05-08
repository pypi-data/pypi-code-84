# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ManagementAssociationArgs', 'ManagementAssociation']

@pulumi.input_type
class ManagementAssociationArgs:
    def __init__(__self__, *,
                 provider_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 resource_name: pulumi.Input[str],
                 resource_type: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 management_association_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['ManagementAssociationPropertiesArgs']] = None):
        """
        The set of arguments for constructing a ManagementAssociation resource.
        :param pulumi.Input[str] provider_name: Provider name for the parent resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group to get. The name is case insensitive.
        :param pulumi.Input[str] resource_name: Parent resource name.
        :param pulumi.Input[str] resource_type: Resource type for the parent resource
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] management_association_name: User ManagementAssociation Name.
        :param pulumi.Input['ManagementAssociationPropertiesArgs'] properties: Properties for ManagementAssociation object supported by the OperationsManagement resource provider.
        """
        pulumi.set(__self__, "provider_name", provider_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "resource_name", resource_name)
        pulumi.set(__self__, "resource_type", resource_type)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if management_association_name is not None:
            pulumi.set(__self__, "management_association_name", management_association_name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> pulumi.Input[str]:
        """
        Provider name for the parent resource.
        """
        return pulumi.get(self, "provider_name")

    @provider_name.setter
    def provider_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "provider_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group to get. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[str]:
        """
        Parent resource name.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[str]:
        """
        Resource type for the parent resource
        """
        return pulumi.get(self, "resource_type")

    @resource_type.setter
    def resource_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_type", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="managementAssociationName")
    def management_association_name(self) -> Optional[pulumi.Input[str]]:
        """
        User ManagementAssociation Name.
        """
        return pulumi.get(self, "management_association_name")

    @management_association_name.setter
    def management_association_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "management_association_name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['ManagementAssociationPropertiesArgs']]:
        """
        Properties for ManagementAssociation object supported by the OperationsManagement resource provider.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['ManagementAssociationPropertiesArgs']]):
        pulumi.set(self, "properties", value)


class ManagementAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 management_association_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['ManagementAssociationPropertiesArgs']]] = None,
                 provider_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The container for solution.
        API Version: 2015-11-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] management_association_name: User ManagementAssociation Name.
        :param pulumi.Input[pulumi.InputType['ManagementAssociationPropertiesArgs']] properties: Properties for ManagementAssociation object supported by the OperationsManagement resource provider.
        :param pulumi.Input[str] provider_name: Provider name for the parent resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group to get. The name is case insensitive.
        :param pulumi.Input[str] resource_name_: Parent resource name.
        :param pulumi.Input[str] resource_type: Resource type for the parent resource
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ManagementAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The container for solution.
        API Version: 2015-11-01-preview.

        :param str resource_name: The name of the resource.
        :param ManagementAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagementAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 management_association_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['ManagementAssociationPropertiesArgs']]] = None,
                 provider_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
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
            __props__ = ManagementAssociationArgs.__new__(ManagementAssociationArgs)

            __props__.__dict__["location"] = location
            __props__.__dict__["management_association_name"] = management_association_name
            __props__.__dict__["properties"] = properties
            if provider_name is None and not opts.urn:
                raise TypeError("Missing required property 'provider_name'")
            __props__.__dict__["provider_name"] = provider_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if resource_name_ is None and not opts.urn:
                raise TypeError("Missing required property 'resource_name_'")
            __props__.__dict__["resource_name"] = resource_name_
            if resource_type is None and not opts.urn:
                raise TypeError("Missing required property 'resource_type'")
            __props__.__dict__["resource_type"] = resource_type
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:operationsmanagement:ManagementAssociation"), pulumi.Alias(type_="azure-native:operationsmanagement/v20151101preview:ManagementAssociation"), pulumi.Alias(type_="azure-nextgen:operationsmanagement/v20151101preview:ManagementAssociation")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ManagementAssociation, __self__).__init__(
            'azure-native:operationsmanagement:ManagementAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ManagementAssociation':
        """
        Get an existing ManagementAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ManagementAssociationArgs.__new__(ManagementAssociationArgs)

        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["type"] = None
        return ManagementAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.ManagementAssociationPropertiesResponse']:
        """
        Properties for ManagementAssociation object supported by the OperationsManagement resource provider.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

