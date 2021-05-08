# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['FolderBucketArgs', 'FolderBucket']

@pulumi.input_type
class FolderBucketArgs:
    def __init__(__self__, *,
                 buckets_id: pulumi.Input[str],
                 folders_id: pulumi.Input[str],
                 locations_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 locked: Optional[pulumi.Input[bool]] = None,
                 restricted_fields: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 retention_days: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a FolderBucket resource.
        :param pulumi.Input[str] description: Describes this bucket.
        :param pulumi.Input[bool] locked: Whether the bucket has been locked. The retention period on a locked bucket may not be changed. Locked buckets may only be deleted if they are empty.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] restricted_fields: Log entry field paths that are denied access in this bucket. The following fields and their children are eligible: textPayload, jsonPayload, protoPayload, httpRequest, labels, sourceLocation. Restricting a repeated field will restrict all values. Adding a parent will block all child fields e.g. foo.bar will block foo.bar.baz.
        :param pulumi.Input[int] retention_days: Logs will be retained by default for this amount of time, after which they will automatically be deleted. The minimum retention period is 1 day. If this value is set to zero at bucket creation time, the default time of 30 days will be used.
        """
        pulumi.set(__self__, "buckets_id", buckets_id)
        pulumi.set(__self__, "folders_id", folders_id)
        pulumi.set(__self__, "locations_id", locations_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if locked is not None:
            pulumi.set(__self__, "locked", locked)
        if restricted_fields is not None:
            pulumi.set(__self__, "restricted_fields", restricted_fields)
        if retention_days is not None:
            pulumi.set(__self__, "retention_days", retention_days)

    @property
    @pulumi.getter(name="bucketsId")
    def buckets_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "buckets_id")

    @buckets_id.setter
    def buckets_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "buckets_id", value)

    @property
    @pulumi.getter(name="foldersId")
    def folders_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "folders_id")

    @folders_id.setter
    def folders_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "folders_id", value)

    @property
    @pulumi.getter(name="locationsId")
    def locations_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "locations_id")

    @locations_id.setter
    def locations_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "locations_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Describes this bucket.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def locked(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the bucket has been locked. The retention period on a locked bucket may not be changed. Locked buckets may only be deleted if they are empty.
        """
        return pulumi.get(self, "locked")

    @locked.setter
    def locked(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "locked", value)

    @property
    @pulumi.getter(name="restrictedFields")
    def restricted_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Log entry field paths that are denied access in this bucket. The following fields and their children are eligible: textPayload, jsonPayload, protoPayload, httpRequest, labels, sourceLocation. Restricting a repeated field will restrict all values. Adding a parent will block all child fields e.g. foo.bar will block foo.bar.baz.
        """
        return pulumi.get(self, "restricted_fields")

    @restricted_fields.setter
    def restricted_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "restricted_fields", value)

    @property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[pulumi.Input[int]]:
        """
        Logs will be retained by default for this amount of time, after which they will automatically be deleted. The minimum retention period is 1 day. If this value is set to zero at bucket creation time, the default time of 30 days will be used.
        """
        return pulumi.get(self, "retention_days")

    @retention_days.setter
    def retention_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "retention_days", value)


class FolderBucket(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 buckets_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 folders_id: Optional[pulumi.Input[str]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 locked: Optional[pulumi.Input[bool]] = None,
                 restricted_fields: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 retention_days: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Creates a bucket that can be used to store log entries. Once a bucket has been created, the region cannot be changed.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Describes this bucket.
        :param pulumi.Input[bool] locked: Whether the bucket has been locked. The retention period on a locked bucket may not be changed. Locked buckets may only be deleted if they are empty.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] restricted_fields: Log entry field paths that are denied access in this bucket. The following fields and their children are eligible: textPayload, jsonPayload, protoPayload, httpRequest, labels, sourceLocation. Restricting a repeated field will restrict all values. Adding a parent will block all child fields e.g. foo.bar will block foo.bar.baz.
        :param pulumi.Input[int] retention_days: Logs will be retained by default for this amount of time, after which they will automatically be deleted. The minimum retention period is 1 day. If this value is set to zero at bucket creation time, the default time of 30 days will be used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FolderBucketArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a bucket that can be used to store log entries. Once a bucket has been created, the region cannot be changed.

        :param str resource_name: The name of the resource.
        :param FolderBucketArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FolderBucketArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 buckets_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 folders_id: Optional[pulumi.Input[str]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 locked: Optional[pulumi.Input[bool]] = None,
                 restricted_fields: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 retention_days: Optional[pulumi.Input[int]] = None,
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
            __props__ = FolderBucketArgs.__new__(FolderBucketArgs)

            if buckets_id is None and not opts.urn:
                raise TypeError("Missing required property 'buckets_id'")
            __props__.__dict__["buckets_id"] = buckets_id
            __props__.__dict__["description"] = description
            if folders_id is None and not opts.urn:
                raise TypeError("Missing required property 'folders_id'")
            __props__.__dict__["folders_id"] = folders_id
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__.__dict__["locations_id"] = locations_id
            __props__.__dict__["locked"] = locked
            __props__.__dict__["restricted_fields"] = restricted_fields
            __props__.__dict__["retention_days"] = retention_days
            __props__.__dict__["create_time"] = None
            __props__.__dict__["lifecycle_state"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["update_time"] = None
        super(FolderBucket, __self__).__init__(
            'google-native:logging/v2:FolderBucket',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FolderBucket':
        """
        Get an existing FolderBucket resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FolderBucketArgs.__new__(FolderBucketArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["lifecycle_state"] = None
        __props__.__dict__["locked"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["restricted_fields"] = None
        __props__.__dict__["retention_days"] = None
        __props__.__dict__["update_time"] = None
        return FolderBucket(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The creation timestamp of the bucket. This is not set for any of the default buckets.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Describes this bucket.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lifecycleState")
    def lifecycle_state(self) -> pulumi.Output[str]:
        """
        The bucket lifecycle state.
        """
        return pulumi.get(self, "lifecycle_state")

    @property
    @pulumi.getter
    def locked(self) -> pulumi.Output[bool]:
        """
        Whether the bucket has been locked. The retention period on a locked bucket may not be changed. Locked buckets may only be deleted if they are empty.
        """
        return pulumi.get(self, "locked")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the bucket. For example: "projects/my-project-id/locations/my-location/buckets/my-bucket-id" The supported locations are: global, us-central1, us-east1, us-west1, asia-east1, europe-west1.For the location of global it is unspecified where logs are actually stored. Once a bucket has been created, the location can not be changed.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="restrictedFields")
    def restricted_fields(self) -> pulumi.Output[Sequence[str]]:
        """
        Log entry field paths that are denied access in this bucket. The following fields and their children are eligible: textPayload, jsonPayload, protoPayload, httpRequest, labels, sourceLocation. Restricting a repeated field will restrict all values. Adding a parent will block all child fields e.g. foo.bar will block foo.bar.baz.
        """
        return pulumi.get(self, "restricted_fields")

    @property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> pulumi.Output[int]:
        """
        Logs will be retained by default for this amount of time, after which they will automatically be deleted. The minimum retention period is 1 day. If this value is set to zero at bucket creation time, the default time of 30 days will be used.
        """
        return pulumi.get(self, "retention_days")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The last update timestamp of the bucket.
        """
        return pulumi.get(self, "update_time")

