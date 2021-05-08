# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['DatasetConsentStoreAttributeDefinitionArgs', 'DatasetConsentStoreAttributeDefinition']

@pulumi.input_type
class DatasetConsentStoreAttributeDefinitionArgs:
    def __init__(__self__, *,
                 attribute_definitions_id: pulumi.Input[str],
                 consent_stores_id: pulumi.Input[str],
                 datasets_id: pulumi.Input[str],
                 locations_id: pulumi.Input[str],
                 projects_id: pulumi.Input[str],
                 allowed_values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 consent_default_values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 data_mapping_default_value: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DatasetConsentStoreAttributeDefinition resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_values: Required. Possible values for the attribute. The number of allowed values must not exceed 100. An empty list is invalid. The list can only be expanded after creation.
        :param pulumi.Input[str] category: Required. The category of the attribute. The value of this field cannot be changed after creation.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] consent_default_values: Optional. Default values of the attribute in Consents. If no default values are specified, it defaults to an empty value.
        :param pulumi.Input[str] data_mapping_default_value: Optional. Default value of the attribute in User data mappings. If no default value is specified, it defaults to an empty value. This field is only applicable to attributes of the category `RESOURCE`.
        :param pulumi.Input[str] description: Optional. A description of the attribute.
        :param pulumi.Input[str] name: Resource name of the Attribute definition, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/attributeDefinitions/{attribute_definition_id}`. Cannot be changed after creation.
        """
        pulumi.set(__self__, "attribute_definitions_id", attribute_definitions_id)
        pulumi.set(__self__, "consent_stores_id", consent_stores_id)
        pulumi.set(__self__, "datasets_id", datasets_id)
        pulumi.set(__self__, "locations_id", locations_id)
        pulumi.set(__self__, "projects_id", projects_id)
        if allowed_values is not None:
            pulumi.set(__self__, "allowed_values", allowed_values)
        if category is not None:
            pulumi.set(__self__, "category", category)
        if consent_default_values is not None:
            pulumi.set(__self__, "consent_default_values", consent_default_values)
        if data_mapping_default_value is not None:
            pulumi.set(__self__, "data_mapping_default_value", data_mapping_default_value)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="attributeDefinitionsId")
    def attribute_definitions_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "attribute_definitions_id")

    @attribute_definitions_id.setter
    def attribute_definitions_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "attribute_definitions_id", value)

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
    @pulumi.getter(name="allowedValues")
    def allowed_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Required. Possible values for the attribute. The number of allowed values must not exceed 100. An empty list is invalid. The list can only be expanded after creation.
        """
        return pulumi.get(self, "allowed_values")

    @allowed_values.setter
    def allowed_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowed_values", value)

    @property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[str]]:
        """
        Required. The category of the attribute. The value of this field cannot be changed after creation.
        """
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter(name="consentDefaultValues")
    def consent_default_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Optional. Default values of the attribute in Consents. If no default values are specified, it defaults to an empty value.
        """
        return pulumi.get(self, "consent_default_values")

    @consent_default_values.setter
    def consent_default_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "consent_default_values", value)

    @property
    @pulumi.getter(name="dataMappingDefaultValue")
    def data_mapping_default_value(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Default value of the attribute in User data mappings. If no default value is specified, it defaults to an empty value. This field is only applicable to attributes of the category `RESOURCE`.
        """
        return pulumi.get(self, "data_mapping_default_value")

    @data_mapping_default_value.setter
    def data_mapping_default_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_mapping_default_value", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. A description of the attribute.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Resource name of the Attribute definition, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/attributeDefinitions/{attribute_definition_id}`. Cannot be changed after creation.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class DatasetConsentStoreAttributeDefinition(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allowed_values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 attribute_definitions_id: Optional[pulumi.Input[str]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 consent_default_values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 consent_stores_id: Optional[pulumi.Input[str]] = None,
                 data_mapping_default_value: Optional[pulumi.Input[str]] = None,
                 datasets_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new Attribute definition in the parent consent store.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_values: Required. Possible values for the attribute. The number of allowed values must not exceed 100. An empty list is invalid. The list can only be expanded after creation.
        :param pulumi.Input[str] category: Required. The category of the attribute. The value of this field cannot be changed after creation.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] consent_default_values: Optional. Default values of the attribute in Consents. If no default values are specified, it defaults to an empty value.
        :param pulumi.Input[str] data_mapping_default_value: Optional. Default value of the attribute in User data mappings. If no default value is specified, it defaults to an empty value. This field is only applicable to attributes of the category `RESOURCE`.
        :param pulumi.Input[str] description: Optional. A description of the attribute.
        :param pulumi.Input[str] name: Resource name of the Attribute definition, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/attributeDefinitions/{attribute_definition_id}`. Cannot be changed after creation.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DatasetConsentStoreAttributeDefinitionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new Attribute definition in the parent consent store.

        :param str resource_name: The name of the resource.
        :param DatasetConsentStoreAttributeDefinitionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatasetConsentStoreAttributeDefinitionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allowed_values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 attribute_definitions_id: Optional[pulumi.Input[str]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 consent_default_values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 consent_stores_id: Optional[pulumi.Input[str]] = None,
                 data_mapping_default_value: Optional[pulumi.Input[str]] = None,
                 datasets_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = DatasetConsentStoreAttributeDefinitionArgs.__new__(DatasetConsentStoreAttributeDefinitionArgs)

            __props__.__dict__["allowed_values"] = allowed_values
            if attribute_definitions_id is None and not opts.urn:
                raise TypeError("Missing required property 'attribute_definitions_id'")
            __props__.__dict__["attribute_definitions_id"] = attribute_definitions_id
            __props__.__dict__["category"] = category
            __props__.__dict__["consent_default_values"] = consent_default_values
            if consent_stores_id is None and not opts.urn:
                raise TypeError("Missing required property 'consent_stores_id'")
            __props__.__dict__["consent_stores_id"] = consent_stores_id
            __props__.__dict__["data_mapping_default_value"] = data_mapping_default_value
            if datasets_id is None and not opts.urn:
                raise TypeError("Missing required property 'datasets_id'")
            __props__.__dict__["datasets_id"] = datasets_id
            __props__.__dict__["description"] = description
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__.__dict__["locations_id"] = locations_id
            __props__.__dict__["name"] = name
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__.__dict__["projects_id"] = projects_id
        super(DatasetConsentStoreAttributeDefinition, __self__).__init__(
            'google-native:healthcare/v1beta1:DatasetConsentStoreAttributeDefinition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DatasetConsentStoreAttributeDefinition':
        """
        Get an existing DatasetConsentStoreAttributeDefinition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DatasetConsentStoreAttributeDefinitionArgs.__new__(DatasetConsentStoreAttributeDefinitionArgs)

        __props__.__dict__["allowed_values"] = None
        __props__.__dict__["category"] = None
        __props__.__dict__["consent_default_values"] = None
        __props__.__dict__["data_mapping_default_value"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        return DatasetConsentStoreAttributeDefinition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowedValues")
    def allowed_values(self) -> pulumi.Output[Sequence[str]]:
        """
        Required. Possible values for the attribute. The number of allowed values must not exceed 100. An empty list is invalid. The list can only be expanded after creation.
        """
        return pulumi.get(self, "allowed_values")

    @property
    @pulumi.getter
    def category(self) -> pulumi.Output[str]:
        """
        Required. The category of the attribute. The value of this field cannot be changed after creation.
        """
        return pulumi.get(self, "category")

    @property
    @pulumi.getter(name="consentDefaultValues")
    def consent_default_values(self) -> pulumi.Output[Sequence[str]]:
        """
        Optional. Default values of the attribute in Consents. If no default values are specified, it defaults to an empty value.
        """
        return pulumi.get(self, "consent_default_values")

    @property
    @pulumi.getter(name="dataMappingDefaultValue")
    def data_mapping_default_value(self) -> pulumi.Output[str]:
        """
        Optional. Default value of the attribute in User data mappings. If no default value is specified, it defaults to an empty value. This field is only applicable to attributes of the category `RESOURCE`.
        """
        return pulumi.get(self, "data_mapping_default_value")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Optional. A description of the attribute.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name of the Attribute definition, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/attributeDefinitions/{attribute_definition_id}`. Cannot be changed after creation.
        """
        return pulumi.get(self, "name")

