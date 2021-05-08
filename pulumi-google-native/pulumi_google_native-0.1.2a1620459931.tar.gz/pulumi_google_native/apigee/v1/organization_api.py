# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = ['OrganizationApiArgs', 'OrganizationApi']

@pulumi.input_type
class OrganizationApiArgs:
    def __init__(__self__, *,
                 apis_id: pulumi.Input[str],
                 organizations_id: pulumi.Input[str],
                 content_type: Optional[pulumi.Input[str]] = None,
                 data: Optional[pulumi.Input[str]] = None,
                 extensions: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]] = None):
        """
        The set of arguments for constructing a OrganizationApi resource.
        :param pulumi.Input[str] content_type: The HTTP Content-Type header value specifying the content type of the body.
        :param pulumi.Input[str] data: The HTTP request/response body as raw binary.
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]] extensions: Application specific response metadata. Must be set in the first response for streaming APIs.
        """
        pulumi.set(__self__, "apis_id", apis_id)
        pulumi.set(__self__, "organizations_id", organizations_id)
        if content_type is not None:
            pulumi.set(__self__, "content_type", content_type)
        if data is not None:
            pulumi.set(__self__, "data", data)
        if extensions is not None:
            pulumi.set(__self__, "extensions", extensions)

    @property
    @pulumi.getter(name="apisId")
    def apis_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "apis_id")

    @apis_id.setter
    def apis_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "apis_id", value)

    @property
    @pulumi.getter(name="organizationsId")
    def organizations_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "organizations_id")

    @organizations_id.setter
    def organizations_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "organizations_id", value)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[str]]:
        """
        The HTTP Content-Type header value specifying the content type of the body.
        """
        return pulumi.get(self, "content_type")

    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_type", value)

    @property
    @pulumi.getter
    def data(self) -> Optional[pulumi.Input[str]]:
        """
        The HTTP request/response body as raw binary.
        """
        return pulumi.get(self, "data")

    @data.setter
    def data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data", value)

    @property
    @pulumi.getter
    def extensions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]]:
        """
        Application specific response metadata. Must be set in the first response for streaming APIs.
        """
        return pulumi.get(self, "extensions")

    @extensions.setter
    def extensions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]]):
        pulumi.set(self, "extensions", value)


class OrganizationApi(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 apis_id: Optional[pulumi.Input[str]] = None,
                 content_type: Optional[pulumi.Input[str]] = None,
                 data: Optional[pulumi.Input[str]] = None,
                 extensions: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]] = None,
                 organizations_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates an API proxy. The API proxy created will not be accessible at runtime until it is deployed to an environment. Create a new API proxy by setting the `name` query parameter to the name of the API proxy. Import an API proxy configuration bundle stored in zip format on your local machine to your organization by doing the following: * Set the `name` query parameter to the name of the API proxy. * Set the `action` query parameter to `import`. * Set the `Content-Type` header to `multipart/form-data`. * Pass as a file the name of API proxy configuration bundle stored in zip format on your local machine using the `file` form field. **Note**: To validate the API proxy configuration bundle only without importing it, set the `action` query parameter to `validate`. When importing an API proxy configuration bundle, if the API proxy does not exist, it will be created. If the API proxy exists, then a new revision is created. Invalid API proxy configurations are rejected, and a list of validation errors is returned to the client.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] content_type: The HTTP Content-Type header value specifying the content type of the body.
        :param pulumi.Input[str] data: The HTTP request/response body as raw binary.
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]] extensions: Application specific response metadata. Must be set in the first response for streaming APIs.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OrganizationApiArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates an API proxy. The API proxy created will not be accessible at runtime until it is deployed to an environment. Create a new API proxy by setting the `name` query parameter to the name of the API proxy. Import an API proxy configuration bundle stored in zip format on your local machine to your organization by doing the following: * Set the `name` query parameter to the name of the API proxy. * Set the `action` query parameter to `import`. * Set the `Content-Type` header to `multipart/form-data`. * Pass as a file the name of API proxy configuration bundle stored in zip format on your local machine using the `file` form field. **Note**: To validate the API proxy configuration bundle only without importing it, set the `action` query parameter to `validate`. When importing an API proxy configuration bundle, if the API proxy does not exist, it will be created. If the API proxy exists, then a new revision is created. Invalid API proxy configurations are rejected, and a list of validation errors is returned to the client.

        :param str resource_name: The name of the resource.
        :param OrganizationApiArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OrganizationApiArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 apis_id: Optional[pulumi.Input[str]] = None,
                 content_type: Optional[pulumi.Input[str]] = None,
                 data: Optional[pulumi.Input[str]] = None,
                 extensions: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]] = None,
                 organizations_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = OrganizationApiArgs.__new__(OrganizationApiArgs)

            if apis_id is None and not opts.urn:
                raise TypeError("Missing required property 'apis_id'")
            __props__.__dict__["apis_id"] = apis_id
            __props__.__dict__["content_type"] = content_type
            __props__.__dict__["data"] = data
            __props__.__dict__["extensions"] = extensions
            if organizations_id is None and not opts.urn:
                raise TypeError("Missing required property 'organizations_id'")
            __props__.__dict__["organizations_id"] = organizations_id
            __props__.__dict__["latest_revision_id"] = None
            __props__.__dict__["meta_data"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["revision"] = None
        super(OrganizationApi, __self__).__init__(
            'google-native:apigee/v1:OrganizationApi',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OrganizationApi':
        """
        Get an existing OrganizationApi resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OrganizationApiArgs.__new__(OrganizationApiArgs)

        __props__.__dict__["latest_revision_id"] = None
        __props__.__dict__["meta_data"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["revision"] = None
        return OrganizationApi(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="latestRevisionId")
    def latest_revision_id(self) -> pulumi.Output[str]:
        """
        The id of the most recently created revision for this api proxy.
        """
        return pulumi.get(self, "latest_revision_id")

    @property
    @pulumi.getter(name="metaData")
    def meta_data(self) -> pulumi.Output['outputs.GoogleCloudApigeeV1EntityMetadataResponse']:
        """
        Metadata describing the API proxy.
        """
        return pulumi.get(self, "meta_data")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the API proxy.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def revision(self) -> pulumi.Output[Sequence[str]]:
        """
        List of revisons defined for the API proxy.
        """
        return pulumi.get(self, "revision")

