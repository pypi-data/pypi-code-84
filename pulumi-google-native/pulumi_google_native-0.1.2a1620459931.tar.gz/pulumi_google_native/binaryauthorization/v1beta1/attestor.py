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

__all__ = ['AttestorArgs', 'Attestor']

@pulumi.input_type
class AttestorArgs:
    def __init__(__self__, *,
                 attestors_id: pulumi.Input[str],
                 projects_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 user_owned_drydock_note: Optional[pulumi.Input['UserOwnedDrydockNoteArgs']] = None):
        """
        The set of arguments for constructing a Attestor resource.
        :param pulumi.Input[str] description: Optional. A descriptive comment. This field may be updated. The field may be displayed in chooser dialogs.
        :param pulumi.Input[str] name: Required. The resource name, in the format: `projects/*/attestors/*`. This field may not be updated.
        :param pulumi.Input['UserOwnedDrydockNoteArgs'] user_owned_drydock_note: A Drydock ATTESTATION_AUTHORITY Note, created by the user.
        """
        pulumi.set(__self__, "attestors_id", attestors_id)
        pulumi.set(__self__, "projects_id", projects_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if user_owned_drydock_note is not None:
            pulumi.set(__self__, "user_owned_drydock_note", user_owned_drydock_note)

    @property
    @pulumi.getter(name="attestorsId")
    def attestors_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "attestors_id")

    @attestors_id.setter
    def attestors_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "attestors_id", value)

    @property
    @pulumi.getter(name="projectsId")
    def projects_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "projects_id")

    @projects_id.setter
    def projects_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "projects_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. A descriptive comment. This field may be updated. The field may be displayed in chooser dialogs.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Required. The resource name, in the format: `projects/*/attestors/*`. This field may not be updated.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="userOwnedDrydockNote")
    def user_owned_drydock_note(self) -> Optional[pulumi.Input['UserOwnedDrydockNoteArgs']]:
        """
        A Drydock ATTESTATION_AUTHORITY Note, created by the user.
        """
        return pulumi.get(self, "user_owned_drydock_note")

    @user_owned_drydock_note.setter
    def user_owned_drydock_note(self, value: Optional[pulumi.Input['UserOwnedDrydockNoteArgs']]):
        pulumi.set(self, "user_owned_drydock_note", value)


class Attestor(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attestors_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 user_owned_drydock_note: Optional[pulumi.Input[pulumi.InputType['UserOwnedDrydockNoteArgs']]] = None,
                 __props__=None):
        """
        Creates an attestor, and returns a copy of the new attestor. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed, ALREADY_EXISTS if the attestor already exists.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Optional. A descriptive comment. This field may be updated. The field may be displayed in chooser dialogs.
        :param pulumi.Input[str] name: Required. The resource name, in the format: `projects/*/attestors/*`. This field may not be updated.
        :param pulumi.Input[pulumi.InputType['UserOwnedDrydockNoteArgs']] user_owned_drydock_note: A Drydock ATTESTATION_AUTHORITY Note, created by the user.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AttestorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates an attestor, and returns a copy of the new attestor. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed, ALREADY_EXISTS if the attestor already exists.

        :param str resource_name: The name of the resource.
        :param AttestorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AttestorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attestors_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 user_owned_drydock_note: Optional[pulumi.Input[pulumi.InputType['UserOwnedDrydockNoteArgs']]] = None,
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
            __props__ = AttestorArgs.__new__(AttestorArgs)

            if attestors_id is None and not opts.urn:
                raise TypeError("Missing required property 'attestors_id'")
            __props__.__dict__["attestors_id"] = attestors_id
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__.__dict__["projects_id"] = projects_id
            __props__.__dict__["user_owned_drydock_note"] = user_owned_drydock_note
            __props__.__dict__["update_time"] = None
        super(Attestor, __self__).__init__(
            'google-native:binaryauthorization/v1beta1:Attestor',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Attestor':
        """
        Get an existing Attestor resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AttestorArgs.__new__(AttestorArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["update_time"] = None
        __props__.__dict__["user_owned_drydock_note"] = None
        return Attestor(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Optional. A descriptive comment. This field may be updated. The field may be displayed in chooser dialogs.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Required. The resource name, in the format: `projects/*/attestors/*`. This field may not be updated.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Time when the attestor was last updated.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter(name="userOwnedDrydockNote")
    def user_owned_drydock_note(self) -> pulumi.Output['outputs.UserOwnedDrydockNoteResponse']:
        """
        A Drydock ATTESTATION_AUTHORITY Note, created by the user.
        """
        return pulumi.get(self, "user_owned_drydock_note")

