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

__all__ = ['GroupArgs', 'Group']

@pulumi.input_type
class GroupArgs:
    def __init__(__self__, *,
                 groups_id: pulumi.Input[str],
                 additional_group_keys: Optional[pulumi.Input[Sequence[pulumi.Input['EntityKeyArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 dynamic_group_metadata: Optional[pulumi.Input['DynamicGroupMetadataArgs']] = None,
                 group_key: Optional[pulumi.Input['EntityKeyArgs']] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 parent: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Group resource.
        :param pulumi.Input[Sequence[pulumi.Input['EntityKeyArgs']]] additional_group_keys: Additional entity key aliases for a Group.
        :param pulumi.Input[str] description: An extended description to help users determine the purpose of a `Group`. Must not be longer than 4,096 characters.
        :param pulumi.Input[str] display_name: The display name of the `Group`.
        :param pulumi.Input['DynamicGroupMetadataArgs'] dynamic_group_metadata: Optional. Dynamic group metadata like queries and status.
        :param pulumi.Input['EntityKeyArgs'] group_key: Required. Immutable. The `EntityKey` of the `Group`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Required. One or more label entries that apply to the Group. Currently supported labels contain a key with an empty value. Google Groups are the default type of group and have a label with a key of `cloudidentity.googleapis.com/groups.discussion_forum` and an empty value. Existing Google Groups can have an additional label with a key of `cloudidentity.googleapis.com/groups.security` and an empty value added to them. **This is an immutable change and the security label cannot be removed once added.** Dynamic groups have a label with a key of `cloudidentity.googleapis.com/groups.dynamic`. Identity-mapped groups for Cloud Search have a label with a key of `system/groups/external` and an empty value. Examples: {"cloudidentity.googleapis.com/groups.discussion_forum": ""} or {"system/groups/external": ""}.
        :param pulumi.Input[str] parent: Required. Immutable. The resource name of the entity under which this `Group` resides in the Cloud Identity resource hierarchy. Must be of the form `identitysources/{identity_source_id}` for external- identity-mapped groups or `customers/{customer_id}` for Google Groups.
        """
        pulumi.set(__self__, "groups_id", groups_id)
        if additional_group_keys is not None:
            pulumi.set(__self__, "additional_group_keys", additional_group_keys)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if dynamic_group_metadata is not None:
            pulumi.set(__self__, "dynamic_group_metadata", dynamic_group_metadata)
        if group_key is not None:
            pulumi.set(__self__, "group_key", group_key)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if parent is not None:
            pulumi.set(__self__, "parent", parent)

    @property
    @pulumi.getter(name="groupsId")
    def groups_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "groups_id")

    @groups_id.setter
    def groups_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "groups_id", value)

    @property
    @pulumi.getter(name="additionalGroupKeys")
    def additional_group_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EntityKeyArgs']]]]:
        """
        Additional entity key aliases for a Group.
        """
        return pulumi.get(self, "additional_group_keys")

    @additional_group_keys.setter
    def additional_group_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EntityKeyArgs']]]]):
        pulumi.set(self, "additional_group_keys", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        An extended description to help users determine the purpose of a `Group`. Must not be longer than 4,096 characters.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the `Group`.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="dynamicGroupMetadata")
    def dynamic_group_metadata(self) -> Optional[pulumi.Input['DynamicGroupMetadataArgs']]:
        """
        Optional. Dynamic group metadata like queries and status.
        """
        return pulumi.get(self, "dynamic_group_metadata")

    @dynamic_group_metadata.setter
    def dynamic_group_metadata(self, value: Optional[pulumi.Input['DynamicGroupMetadataArgs']]):
        pulumi.set(self, "dynamic_group_metadata", value)

    @property
    @pulumi.getter(name="groupKey")
    def group_key(self) -> Optional[pulumi.Input['EntityKeyArgs']]:
        """
        Required. Immutable. The `EntityKey` of the `Group`.
        """
        return pulumi.get(self, "group_key")

    @group_key.setter
    def group_key(self, value: Optional[pulumi.Input['EntityKeyArgs']]):
        pulumi.set(self, "group_key", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Required. One or more label entries that apply to the Group. Currently supported labels contain a key with an empty value. Google Groups are the default type of group and have a label with a key of `cloudidentity.googleapis.com/groups.discussion_forum` and an empty value. Existing Google Groups can have an additional label with a key of `cloudidentity.googleapis.com/groups.security` and an empty value added to them. **This is an immutable change and the security label cannot be removed once added.** Dynamic groups have a label with a key of `cloudidentity.googleapis.com/groups.dynamic`. Identity-mapped groups for Cloud Search have a label with a key of `system/groups/external` and an empty value. Examples: {"cloudidentity.googleapis.com/groups.discussion_forum": ""} or {"system/groups/external": ""}.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[str]]:
        """
        Required. Immutable. The resource name of the entity under which this `Group` resides in the Cloud Identity resource hierarchy. Must be of the form `identitysources/{identity_source_id}` for external- identity-mapped groups or `customers/{customer_id}` for Google Groups.
        """
        return pulumi.get(self, "parent")

    @parent.setter
    def parent(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent", value)


class Group(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_group_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EntityKeyArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 dynamic_group_metadata: Optional[pulumi.Input[pulumi.InputType['DynamicGroupMetadataArgs']]] = None,
                 group_key: Optional[pulumi.Input[pulumi.InputType['EntityKeyArgs']]] = None,
                 groups_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a `Group`.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EntityKeyArgs']]]] additional_group_keys: Additional entity key aliases for a Group.
        :param pulumi.Input[str] description: An extended description to help users determine the purpose of a `Group`. Must not be longer than 4,096 characters.
        :param pulumi.Input[str] display_name: The display name of the `Group`.
        :param pulumi.Input[pulumi.InputType['DynamicGroupMetadataArgs']] dynamic_group_metadata: Optional. Dynamic group metadata like queries and status.
        :param pulumi.Input[pulumi.InputType['EntityKeyArgs']] group_key: Required. Immutable. The `EntityKey` of the `Group`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Required. One or more label entries that apply to the Group. Currently supported labels contain a key with an empty value. Google Groups are the default type of group and have a label with a key of `cloudidentity.googleapis.com/groups.discussion_forum` and an empty value. Existing Google Groups can have an additional label with a key of `cloudidentity.googleapis.com/groups.security` and an empty value added to them. **This is an immutable change and the security label cannot be removed once added.** Dynamic groups have a label with a key of `cloudidentity.googleapis.com/groups.dynamic`. Identity-mapped groups for Cloud Search have a label with a key of `system/groups/external` and an empty value. Examples: {"cloudidentity.googleapis.com/groups.discussion_forum": ""} or {"system/groups/external": ""}.
        :param pulumi.Input[str] parent: Required. Immutable. The resource name of the entity under which this `Group` resides in the Cloud Identity resource hierarchy. Must be of the form `identitysources/{identity_source_id}` for external- identity-mapped groups or `customers/{customer_id}` for Google Groups.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a `Group`.

        :param str resource_name: The name of the resource.
        :param GroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_group_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EntityKeyArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 dynamic_group_metadata: Optional[pulumi.Input[pulumi.InputType['DynamicGroupMetadataArgs']]] = None,
                 group_key: Optional[pulumi.Input[pulumi.InputType['EntityKeyArgs']]] = None,
                 groups_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
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
            __props__ = GroupArgs.__new__(GroupArgs)

            __props__.__dict__["additional_group_keys"] = additional_group_keys
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["dynamic_group_metadata"] = dynamic_group_metadata
            __props__.__dict__["group_key"] = group_key
            if groups_id is None and not opts.urn:
                raise TypeError("Missing required property 'groups_id'")
            __props__.__dict__["groups_id"] = groups_id
            __props__.__dict__["labels"] = labels
            __props__.__dict__["parent"] = parent
            __props__.__dict__["create_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["update_time"] = None
        super(Group, __self__).__init__(
            'google-native:cloudidentity/v1beta1:Group',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Group':
        """
        Get an existing Group resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GroupArgs.__new__(GroupArgs)

        __props__.__dict__["additional_group_keys"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["dynamic_group_metadata"] = None
        __props__.__dict__["group_key"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parent"] = None
        __props__.__dict__["update_time"] = None
        return Group(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalGroupKeys")
    def additional_group_keys(self) -> pulumi.Output[Sequence['outputs.EntityKeyResponse']]:
        """
        Additional entity key aliases for a Group.
        """
        return pulumi.get(self, "additional_group_keys")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time when the `Group` was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        An extended description to help users determine the purpose of a `Group`. Must not be longer than 4,096 characters.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The display name of the `Group`.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="dynamicGroupMetadata")
    def dynamic_group_metadata(self) -> pulumi.Output['outputs.DynamicGroupMetadataResponse']:
        """
        Optional. Dynamic group metadata like queries and status.
        """
        return pulumi.get(self, "dynamic_group_metadata")

    @property
    @pulumi.getter(name="groupKey")
    def group_key(self) -> pulumi.Output['outputs.EntityKeyResponse']:
        """
        Required. Immutable. The `EntityKey` of the `Group`.
        """
        return pulumi.get(self, "group_key")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Required. One or more label entries that apply to the Group. Currently supported labels contain a key with an empty value. Google Groups are the default type of group and have a label with a key of `cloudidentity.googleapis.com/groups.discussion_forum` and an empty value. Existing Google Groups can have an additional label with a key of `cloudidentity.googleapis.com/groups.security` and an empty value added to them. **This is an immutable change and the security label cannot be removed once added.** Dynamic groups have a label with a key of `cloudidentity.googleapis.com/groups.dynamic`. Identity-mapped groups for Cloud Search have a label with a key of `system/groups/external` and an empty value. Examples: {"cloudidentity.googleapis.com/groups.discussion_forum": ""} or {"system/groups/external": ""}.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The [resource name](https://cloud.google.com/apis/design/resource_names) of the `Group`. Shall be of the form `groups/{group_id}`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parent(self) -> pulumi.Output[str]:
        """
        Required. Immutable. The resource name of the entity under which this `Group` resides in the Cloud Identity resource hierarchy. Must be of the form `identitysources/{identity_source_id}` for external- identity-mapped groups or `customers/{customer_id}` for Google Groups.
        """
        return pulumi.get(self, "parent")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The time when the `Group` was last updated.
        """
        return pulumi.get(self, "update_time")

