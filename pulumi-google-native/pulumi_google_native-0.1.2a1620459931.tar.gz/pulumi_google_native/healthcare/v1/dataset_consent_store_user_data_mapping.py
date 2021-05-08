# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['DatasetConsentStoreUserDataMappingArgs', 'DatasetConsentStoreUserDataMapping']

@pulumi.input_type
class DatasetConsentStoreUserDataMappingArgs:
    def __init__(__self__, *,
                 consent_stores_id: pulumi.Input[str],
                 datasets_id: pulumi.Input[str],
                 locations_id: pulumi.Input[str],
                 projects_id: pulumi.Input[str],
                 user_data_mappings_id: pulumi.Input[str],
                 data_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_attributes: Optional[pulumi.Input[Sequence[pulumi.Input['AttributeArgs']]]] = None,
                 user_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DatasetConsentStoreUserDataMapping resource.
        :param pulumi.Input[str] data_id: Required. A unique identifier for the mapped resource.
        :param pulumi.Input[str] name: Resource name of the User data mapping, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/userDataMappings/{user_data_mapping_id}`.
        :param pulumi.Input[Sequence[pulumi.Input['AttributeArgs']]] resource_attributes: Attributes of the resource. Only explicitly set attributes are displayed here. Attribute definitions with defaults set implicitly apply to these User data mappings. Attributes listed here must be single valued, that is, exactly one value is specified for the field "values" in each Attribute.
        :param pulumi.Input[str] user_id: Required. User's UUID provided by the client.
        """
        pulumi.set(__self__, "consent_stores_id", consent_stores_id)
        pulumi.set(__self__, "datasets_id", datasets_id)
        pulumi.set(__self__, "locations_id", locations_id)
        pulumi.set(__self__, "projects_id", projects_id)
        pulumi.set(__self__, "user_data_mappings_id", user_data_mappings_id)
        if data_id is not None:
            pulumi.set(__self__, "data_id", data_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_attributes is not None:
            pulumi.set(__self__, "resource_attributes", resource_attributes)
        if user_id is not None:
            pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter(name="consentStoresId")
    def consent_stores_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "consent_stores_id")

    @consent_stores_id.setter
    def consent_stores_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "consent_stores_id", value)

    @property
    @pulumi.getter(name="datasetsId")
    def datasets_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "datasets_id")

    @datasets_id.setter
    def datasets_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "datasets_id", value)

    @property
    @pulumi.getter(name="locationsId")
    def locations_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "locations_id")

    @locations_id.setter
    def locations_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "locations_id", value)

    @property
    @pulumi.getter(name="projectsId")
    def projects_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "projects_id")

    @projects_id.setter
    def projects_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "projects_id", value)

    @property
    @pulumi.getter(name="userDataMappingsId")
    def user_data_mappings_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "user_data_mappings_id")

    @user_data_mappings_id.setter
    def user_data_mappings_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_data_mappings_id", value)

    @property
    @pulumi.getter(name="dataId")
    def data_id(self) -> Optional[pulumi.Input[str]]:
        """
        Required. A unique identifier for the mapped resource.
        """
        return pulumi.get(self, "data_id")

    @data_id.setter
    def data_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Resource name of the User data mapping, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/userDataMappings/{user_data_mapping_id}`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceAttributes")
    def resource_attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AttributeArgs']]]]:
        """
        Attributes of the resource. Only explicitly set attributes are displayed here. Attribute definitions with defaults set implicitly apply to these User data mappings. Attributes listed here must be single valued, that is, exactly one value is specified for the field "values" in each Attribute.
        """
        return pulumi.get(self, "resource_attributes")

    @resource_attributes.setter
    def resource_attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AttributeArgs']]]]):
        pulumi.set(self, "resource_attributes", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[str]]:
        """
        Required. User's UUID provided by the client.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_id", value)


class DatasetConsentStoreUserDataMapping(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 consent_stores_id: Optional[pulumi.Input[str]] = None,
                 data_id: Optional[pulumi.Input[str]] = None,
                 datasets_id: Optional[pulumi.Input[str]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 resource_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AttributeArgs']]]]] = None,
                 user_data_mappings_id: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new User data mapping in the parent consent store.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] data_id: Required. A unique identifier for the mapped resource.
        :param pulumi.Input[str] name: Resource name of the User data mapping, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/userDataMappings/{user_data_mapping_id}`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AttributeArgs']]]] resource_attributes: Attributes of the resource. Only explicitly set attributes are displayed here. Attribute definitions with defaults set implicitly apply to these User data mappings. Attributes listed here must be single valued, that is, exactly one value is specified for the field "values" in each Attribute.
        :param pulumi.Input[str] user_id: Required. User's UUID provided by the client.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DatasetConsentStoreUserDataMappingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new User data mapping in the parent consent store.

        :param str resource_name: The name of the resource.
        :param DatasetConsentStoreUserDataMappingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatasetConsentStoreUserDataMappingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 consent_stores_id: Optional[pulumi.Input[str]] = None,
                 data_id: Optional[pulumi.Input[str]] = None,
                 datasets_id: Optional[pulumi.Input[str]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 resource_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AttributeArgs']]]]] = None,
                 user_data_mappings_id: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = DatasetConsentStoreUserDataMappingArgs.__new__(DatasetConsentStoreUserDataMappingArgs)

            if consent_stores_id is None and not opts.urn:
                raise TypeError("Missing required property 'consent_stores_id'")
            __props__.__dict__["consent_stores_id"] = consent_stores_id
            __props__.__dict__["data_id"] = data_id
            if datasets_id is None and not opts.urn:
                raise TypeError("Missing required property 'datasets_id'")
            __props__.__dict__["datasets_id"] = datasets_id
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__.__dict__["locations_id"] = locations_id
            __props__.__dict__["name"] = name
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__.__dict__["projects_id"] = projects_id
            __props__.__dict__["resource_attributes"] = resource_attributes
            if user_data_mappings_id is None and not opts.urn:
                raise TypeError("Missing required property 'user_data_mappings_id'")
            __props__.__dict__["user_data_mappings_id"] = user_data_mappings_id
            __props__.__dict__["user_id"] = user_id
            __props__.__dict__["archive_time"] = None
            __props__.__dict__["archived"] = None
        super(DatasetConsentStoreUserDataMapping, __self__).__init__(
            'google-native:healthcare/v1:DatasetConsentStoreUserDataMapping',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DatasetConsentStoreUserDataMapping':
        """
        Get an existing DatasetConsentStoreUserDataMapping resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DatasetConsentStoreUserDataMappingArgs.__new__(DatasetConsentStoreUserDataMappingArgs)

        __props__.__dict__["archive_time"] = None
        __props__.__dict__["archived"] = None
        __props__.__dict__["data_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["resource_attributes"] = None
        __props__.__dict__["user_id"] = None
        return DatasetConsentStoreUserDataMapping(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="archiveTime")
    def archive_time(self) -> pulumi.Output[str]:
        """
        Indicates the time when this mapping was archived.
        """
        return pulumi.get(self, "archive_time")

    @property
    @pulumi.getter
    def archived(self) -> pulumi.Output[bool]:
        """
        Indicates whether this mapping is archived.
        """
        return pulumi.get(self, "archived")

    @property
    @pulumi.getter(name="dataId")
    def data_id(self) -> pulumi.Output[str]:
        """
        Required. A unique identifier for the mapped resource.
        """
        return pulumi.get(self, "data_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name of the User data mapping, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/userDataMappings/{user_data_mapping_id}`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceAttributes")
    def resource_attributes(self) -> pulumi.Output[Sequence['outputs.AttributeResponse']]:
        """
        Attributes of the resource. Only explicitly set attributes are displayed here. Attribute definitions with defaults set implicitly apply to these User data mappings. Attributes listed here must be single valued, that is, exactly one value is specified for the field "values" in each Attribute.
        """
        return pulumi.get(self, "resource_attributes")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[str]:
        """
        Required. User's UUID provided by the client.
        """
        return pulumi.get(self, "user_id")

