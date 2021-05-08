# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['OrganizationInstanceAttachmentArgs', 'OrganizationInstanceAttachment']

@pulumi.input_type
class OrganizationInstanceAttachmentArgs:
    def __init__(__self__, *,
                 attachments_id: pulumi.Input[str],
                 instances_id: pulumi.Input[str],
                 organizations_id: pulumi.Input[str],
                 environment: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a OrganizationInstanceAttachment resource.
        :param pulumi.Input[str] environment: ID of the attached environment.
        """
        pulumi.set(__self__, "attachments_id", attachments_id)
        pulumi.set(__self__, "instances_id", instances_id)
        pulumi.set(__self__, "organizations_id", organizations_id)
        if environment is not None:
            pulumi.set(__self__, "environment", environment)

    @property
    @pulumi.getter(name="attachmentsId")
    def attachments_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "attachments_id")

    @attachments_id.setter
    def attachments_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "attachments_id", value)

    @property
    @pulumi.getter(name="instancesId")
    def instances_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "instances_id")

    @instances_id.setter
    def instances_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "instances_id", value)

    @property
    @pulumi.getter(name="organizationsId")
    def organizations_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "organizations_id")

    @organizations_id.setter
    def organizations_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "organizations_id", value)

    @property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the attached environment.
        """
        return pulumi.get(self, "environment")

    @environment.setter
    def environment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "environment", value)


class OrganizationInstanceAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attachments_id: Optional[pulumi.Input[str]] = None,
                 environment: Optional[pulumi.Input[str]] = None,
                 instances_id: Optional[pulumi.Input[str]] = None,
                 organizations_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new attachment of an environment to an instance. **Note:** Not supported for Apigee hybrid.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] environment: ID of the attached environment.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OrganizationInstanceAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new attachment of an environment to an instance. **Note:** Not supported for Apigee hybrid.

        :param str resource_name: The name of the resource.
        :param OrganizationInstanceAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OrganizationInstanceAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attachments_id: Optional[pulumi.Input[str]] = None,
                 environment: Optional[pulumi.Input[str]] = None,
                 instances_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = OrganizationInstanceAttachmentArgs.__new__(OrganizationInstanceAttachmentArgs)

            if attachments_id is None and not opts.urn:
                raise TypeError("Missing required property 'attachments_id'")
            __props__.__dict__["attachments_id"] = attachments_id
            __props__.__dict__["environment"] = environment
            if instances_id is None and not opts.urn:
                raise TypeError("Missing required property 'instances_id'")
            __props__.__dict__["instances_id"] = instances_id
            if organizations_id is None and not opts.urn:
                raise TypeError("Missing required property 'organizations_id'")
            __props__.__dict__["organizations_id"] = organizations_id
            __props__.__dict__["created_at"] = None
            __props__.__dict__["name"] = None
        super(OrganizationInstanceAttachment, __self__).__init__(
            'google-native:apigee/v1:OrganizationInstanceAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OrganizationInstanceAttachment':
        """
        Get an existing OrganizationInstanceAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OrganizationInstanceAttachmentArgs.__new__(OrganizationInstanceAttachmentArgs)

        __props__.__dict__["created_at"] = None
        __props__.__dict__["environment"] = None
        __props__.__dict__["name"] = None
        return OrganizationInstanceAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Time the attachment was created in milliseconds since epoch.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def environment(self) -> pulumi.Output[str]:
        """
        ID of the attached environment.
        """
        return pulumi.get(self, "environment")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        ID of the attachment.
        """
        return pulumi.get(self, "name")

