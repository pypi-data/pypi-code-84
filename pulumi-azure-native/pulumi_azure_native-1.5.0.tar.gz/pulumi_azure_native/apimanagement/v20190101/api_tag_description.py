# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['ApiTagDescriptionArgs', 'ApiTagDescription']

@pulumi.input_type
class ApiTagDescriptionArgs:
    def __init__(__self__, *,
                 api_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 external_docs_description: Optional[pulumi.Input[str]] = None,
                 external_docs_url: Optional[pulumi.Input[str]] = None,
                 tag_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ApiTagDescription resource.
        :param pulumi.Input[str] api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] description: Description of the Tag.
        :param pulumi.Input[str] external_docs_description: Description of the external resources describing the tag.
        :param pulumi.Input[str] external_docs_url: Absolute URL of external resources describing the tag.
        :param pulumi.Input[str] tag_id: Tag identifier. Must be unique in the current API Management service instance.
        """
        pulumi.set(__self__, "api_id", api_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if external_docs_description is not None:
            pulumi.set(__self__, "external_docs_description", external_docs_description)
        if external_docs_url is not None:
            pulumi.set(__self__, "external_docs_url", external_docs_url)
        if tag_id is not None:
            pulumi.set(__self__, "tag_id", tag_id)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[str]:
        """
        API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
        """
        return pulumi.get(self, "api_id")

    @api_id.setter
    def api_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_id", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The name of the API Management service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the Tag.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="externalDocsDescription")
    def external_docs_description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the external resources describing the tag.
        """
        return pulumi.get(self, "external_docs_description")

    @external_docs_description.setter
    def external_docs_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_docs_description", value)

    @property
    @pulumi.getter(name="externalDocsUrl")
    def external_docs_url(self) -> Optional[pulumi.Input[str]]:
        """
        Absolute URL of external resources describing the tag.
        """
        return pulumi.get(self, "external_docs_url")

    @external_docs_url.setter
    def external_docs_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_docs_url", value)

    @property
    @pulumi.getter(name="tagId")
    def tag_id(self) -> Optional[pulumi.Input[str]]:
        """
        Tag identifier. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "tag_id")

    @tag_id.setter
    def tag_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tag_id", value)


class ApiTagDescription(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 external_docs_description: Optional[pulumi.Input[str]] = None,
                 external_docs_url: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 tag_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Contract details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
        :param pulumi.Input[str] description: Description of the Tag.
        :param pulumi.Input[str] external_docs_description: Description of the external resources describing the tag.
        :param pulumi.Input[str] external_docs_url: Absolute URL of external resources describing the tag.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] tag_id: Tag identifier. Must be unique in the current API Management service instance.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApiTagDescriptionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Contract details.

        :param str resource_name: The name of the resource.
        :param ApiTagDescriptionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApiTagDescriptionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 external_docs_description: Optional[pulumi.Input[str]] = None,
                 external_docs_url: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 tag_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = ApiTagDescriptionArgs.__new__(ApiTagDescriptionArgs)

            if api_id is None and not opts.urn:
                raise TypeError("Missing required property 'api_id'")
            __props__.__dict__["api_id"] = api_id
            __props__.__dict__["description"] = description
            __props__.__dict__["external_docs_description"] = external_docs_description
            __props__.__dict__["external_docs_url"] = external_docs_url
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["tag_id"] = tag_id
            __props__.__dict__["display_name"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:apimanagement/v20190101:ApiTagDescription"), pulumi.Alias(type_="azure-native:apimanagement:ApiTagDescription"), pulumi.Alias(type_="azure-nextgen:apimanagement:ApiTagDescription"), pulumi.Alias(type_="azure-native:apimanagement/v20170301:ApiTagDescription"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20170301:ApiTagDescription"), pulumi.Alias(type_="azure-native:apimanagement/v20180101:ApiTagDescription"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20180101:ApiTagDescription"), pulumi.Alias(type_="azure-native:apimanagement/v20180601preview:ApiTagDescription"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20180601preview:ApiTagDescription"), pulumi.Alias(type_="azure-native:apimanagement/v20191201:ApiTagDescription"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20191201:ApiTagDescription"), pulumi.Alias(type_="azure-native:apimanagement/v20191201preview:ApiTagDescription"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20191201preview:ApiTagDescription"), pulumi.Alias(type_="azure-native:apimanagement/v20200601preview:ApiTagDescription"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20200601preview:ApiTagDescription"), pulumi.Alias(type_="azure-native:apimanagement/v20201201:ApiTagDescription"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20201201:ApiTagDescription"), pulumi.Alias(type_="azure-native:apimanagement/v20210101preview:ApiTagDescription"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20210101preview:ApiTagDescription")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ApiTagDescription, __self__).__init__(
            'azure-native:apimanagement/v20190101:ApiTagDescription',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ApiTagDescription':
        """
        Get an existing ApiTagDescription resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApiTagDescriptionArgs.__new__(ApiTagDescriptionArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["external_docs_description"] = None
        __props__.__dict__["external_docs_url"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        return ApiTagDescription(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the Tag.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        Tag name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="externalDocsDescription")
    def external_docs_description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the external resources describing the tag.
        """
        return pulumi.get(self, "external_docs_description")

    @property
    @pulumi.getter(name="externalDocsUrl")
    def external_docs_url(self) -> pulumi.Output[Optional[str]]:
        """
        Absolute URL of external resources describing the tag.
        """
        return pulumi.get(self, "external_docs_url")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type for API Management resource.
        """
        return pulumi.get(self, "type")

