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

__all__ = ['ChangeArgs', 'Change']

@pulumi.input_type
class ChangeArgs:
    def __init__(__self__, *,
                 change_id: pulumi.Input[str],
                 managed_zone: pulumi.Input[str],
                 project: pulumi.Input[str],
                 additions: Optional[pulumi.Input[Sequence[pulumi.Input['ResourceRecordSetArgs']]]] = None,
                 deletions: Optional[pulumi.Input[Sequence[pulumi.Input['ResourceRecordSetArgs']]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 is_serving: Optional[pulumi.Input[bool]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Change resource.
        :param pulumi.Input[Sequence[pulumi.Input['ResourceRecordSetArgs']]] additions: Which ResourceRecordSets to add?
        :param pulumi.Input[Sequence[pulumi.Input['ResourceRecordSetArgs']]] deletions: Which ResourceRecordSets to remove? Must match existing data exactly.
        :param pulumi.Input[str] id: Unique identifier for the resource; defined by the server (output only).
        :param pulumi.Input[bool] is_serving: If the DNS queries for the zone will be served.
        :param pulumi.Input[str] start_time: The time that this operation was started by the server (output only). This is in RFC3339 text format.
        :param pulumi.Input[str] status: Status of the operation (output only). A status of "done" means that the request to update the authoritative servers has been sent, but the servers might not be updated yet.
        """
        pulumi.set(__self__, "change_id", change_id)
        pulumi.set(__self__, "managed_zone", managed_zone)
        pulumi.set(__self__, "project", project)
        if additions is not None:
            pulumi.set(__self__, "additions", additions)
        if deletions is not None:
            pulumi.set(__self__, "deletions", deletions)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if is_serving is not None:
            pulumi.set(__self__, "is_serving", is_serving)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if start_time is not None:
            pulumi.set(__self__, "start_time", start_time)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="changeId")
    def change_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "change_id")

    @change_id.setter
    def change_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "change_id", value)

    @property
    @pulumi.getter(name="managedZone")
    def managed_zone(self) -> pulumi.Input[str]:
        return pulumi.get(self, "managed_zone")

    @managed_zone.setter
    def managed_zone(self, value: pulumi.Input[str]):
        pulumi.set(self, "managed_zone", value)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def additions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ResourceRecordSetArgs']]]]:
        """
        Which ResourceRecordSets to add?
        """
        return pulumi.get(self, "additions")

    @additions.setter
    def additions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ResourceRecordSetArgs']]]]):
        pulumi.set(self, "additions", value)

    @property
    @pulumi.getter
    def deletions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ResourceRecordSetArgs']]]]:
        """
        Which ResourceRecordSets to remove? Must match existing data exactly.
        """
        return pulumi.get(self, "deletions")

    @deletions.setter
    def deletions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ResourceRecordSetArgs']]]]):
        pulumi.set(self, "deletions", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier for the resource; defined by the server (output only).
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="isServing")
    def is_serving(self) -> Optional[pulumi.Input[bool]]:
        """
        If the DNS queries for the zone will be served.
        """
        return pulumi.get(self, "is_serving")

    @is_serving.setter
    def is_serving(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_serving", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[str]]:
        """
        The time that this operation was started by the server (output only). This is in RFC3339 text format.
        """
        return pulumi.get(self, "start_time")

    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_time", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Status of the operation (output only). A status of "done" means that the request to update the authoritative servers has been sent, but the servers might not be updated yet.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class Change(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceRecordSetArgs']]]]] = None,
                 change_id: Optional[pulumi.Input[str]] = None,
                 deletions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceRecordSetArgs']]]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 is_serving: Optional[pulumi.Input[bool]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 managed_zone: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Atomically updates the ResourceRecordSet collection.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceRecordSetArgs']]]] additions: Which ResourceRecordSets to add?
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceRecordSetArgs']]]] deletions: Which ResourceRecordSets to remove? Must match existing data exactly.
        :param pulumi.Input[str] id: Unique identifier for the resource; defined by the server (output only).
        :param pulumi.Input[bool] is_serving: If the DNS queries for the zone will be served.
        :param pulumi.Input[str] start_time: The time that this operation was started by the server (output only). This is in RFC3339 text format.
        :param pulumi.Input[str] status: Status of the operation (output only). A status of "done" means that the request to update the authoritative servers has been sent, but the servers might not be updated yet.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ChangeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Atomically updates the ResourceRecordSet collection.

        :param str resource_name: The name of the resource.
        :param ChangeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ChangeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceRecordSetArgs']]]]] = None,
                 change_id: Optional[pulumi.Input[str]] = None,
                 deletions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceRecordSetArgs']]]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 is_serving: Optional[pulumi.Input[bool]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 managed_zone: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
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
            __props__ = ChangeArgs.__new__(ChangeArgs)

            __props__.__dict__["additions"] = additions
            if change_id is None and not opts.urn:
                raise TypeError("Missing required property 'change_id'")
            __props__.__dict__["change_id"] = change_id
            __props__.__dict__["deletions"] = deletions
            __props__.__dict__["id"] = id
            __props__.__dict__["is_serving"] = is_serving
            __props__.__dict__["kind"] = kind
            if managed_zone is None and not opts.urn:
                raise TypeError("Missing required property 'managed_zone'")
            __props__.__dict__["managed_zone"] = managed_zone
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            __props__.__dict__["start_time"] = start_time
            __props__.__dict__["status"] = status
        super(Change, __self__).__init__(
            'google-native:dns/v1beta2:Change',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Change':
        """
        Get an existing Change resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ChangeArgs.__new__(ChangeArgs)

        __props__.__dict__["additions"] = None
        __props__.__dict__["deletions"] = None
        __props__.__dict__["is_serving"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["start_time"] = None
        __props__.__dict__["status"] = None
        return Change(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def additions(self) -> pulumi.Output[Sequence['outputs.ResourceRecordSetResponse']]:
        """
        Which ResourceRecordSets to add?
        """
        return pulumi.get(self, "additions")

    @property
    @pulumi.getter
    def deletions(self) -> pulumi.Output[Sequence['outputs.ResourceRecordSetResponse']]:
        """
        Which ResourceRecordSets to remove? Must match existing data exactly.
        """
        return pulumi.get(self, "deletions")

    @property
    @pulumi.getter(name="isServing")
    def is_serving(self) -> pulumi.Output[bool]:
        """
        If the DNS queries for the zone will be served.
        """
        return pulumi.get(self, "is_serving")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[str]:
        """
        The time that this operation was started by the server (output only). This is in RFC3339 text format.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Status of the operation (output only). A status of "done" means that the request to update the authoritative servers has been sent, but the servers might not be updated yet.
        """
        return pulumi.get(self, "status")

