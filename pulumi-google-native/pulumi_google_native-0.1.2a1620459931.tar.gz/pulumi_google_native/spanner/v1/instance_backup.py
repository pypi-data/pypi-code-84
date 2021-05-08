# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = ['InstanceBackupArgs', 'InstanceBackup']

@pulumi.input_type
class InstanceBackupArgs:
    def __init__(__self__, *,
                 backups_id: pulumi.Input[str],
                 instances_id: pulumi.Input[str],
                 projects_id: pulumi.Input[str],
                 database: Optional[pulumi.Input[str]] = None,
                 expire_time: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 version_time: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a InstanceBackup resource.
        :param pulumi.Input[str] database: Required for the CreateBackup operation. Name of the database from which this backup was created. This needs to be in the same instance as the backup. Values are of the form `projects//instances//databases/`.
        :param pulumi.Input[str] expire_time: Required for the CreateBackup operation. The expiration time of the backup, with microseconds granularity that must be at least 6 hours and at most 366 days from the time the CreateBackup request is processed. Once the `expire_time` has passed, the backup is eligible to be automatically deleted by Cloud Spanner to free the resources used by the backup.
        :param pulumi.Input[str] name: Output only for the CreateBackup operation. Required for the UpdateBackup operation. A globally unique identifier for the backup which cannot be changed. Values are of the form `projects//instances//backups/a-z*[a-z0-9]` The final segment of the name must be between 2 and 60 characters in length. The backup is stored in the location(s) specified in the instance configuration of the instance containing the backup, identified by the prefix of the backup name of the form `projects//instances/`.
        :param pulumi.Input[str] version_time: The backup will contain an externally consistent copy of the database at the timestamp specified by `version_time`. If `version_time` is not specified, the system will set `version_time` to the `create_time` of the backup.
        """
        pulumi.set(__self__, "backups_id", backups_id)
        pulumi.set(__self__, "instances_id", instances_id)
        pulumi.set(__self__, "projects_id", projects_id)
        if database is not None:
            pulumi.set(__self__, "database", database)
        if expire_time is not None:
            pulumi.set(__self__, "expire_time", expire_time)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if version_time is not None:
            pulumi.set(__self__, "version_time", version_time)

    @property
    @pulumi.getter(name="backupsId")
    def backups_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "backups_id")

    @backups_id.setter
    def backups_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "backups_id", value)

    @property
    @pulumi.getter(name="instancesId")
    def instances_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "instances_id")

    @instances_id.setter
    def instances_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "instances_id", value)

    @property
    @pulumi.getter(name="projectsId")
    def projects_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "projects_id")

    @projects_id.setter
    def projects_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "projects_id", value)

    @property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[str]]:
        """
        Required for the CreateBackup operation. Name of the database from which this backup was created. This needs to be in the same instance as the backup. Values are of the form `projects//instances//databases/`.
        """
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[pulumi.Input[str]]:
        """
        Required for the CreateBackup operation. The expiration time of the backup, with microseconds granularity that must be at least 6 hours and at most 366 days from the time the CreateBackup request is processed. Once the `expire_time` has passed, the backup is eligible to be automatically deleted by Cloud Spanner to free the resources used by the backup.
        """
        return pulumi.get(self, "expire_time")

    @expire_time.setter
    def expire_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expire_time", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Output only for the CreateBackup operation. Required for the UpdateBackup operation. A globally unique identifier for the backup which cannot be changed. Values are of the form `projects//instances//backups/a-z*[a-z0-9]` The final segment of the name must be between 2 and 60 characters in length. The backup is stored in the location(s) specified in the instance configuration of the instance containing the backup, identified by the prefix of the backup name of the form `projects//instances/`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="versionTime")
    def version_time(self) -> Optional[pulumi.Input[str]]:
        """
        The backup will contain an externally consistent copy of the database at the timestamp specified by `version_time`. If `version_time` is not specified, the system will set `version_time` to the `create_time` of the backup.
        """
        return pulumi.get(self, "version_time")

    @version_time.setter
    def version_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version_time", value)


class InstanceBackup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backups_id: Optional[pulumi.Input[str]] = None,
                 database: Optional[pulumi.Input[str]] = None,
                 expire_time: Optional[pulumi.Input[str]] = None,
                 instances_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 version_time: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Starts creating a new Cloud Spanner Backup. The returned backup long-running operation will have a name of the format `projects//instances//backups//operations/` and can be used to track creation of the backup. The metadata field type is CreateBackupMetadata. The response field type is Backup, if successful. Cancelling the returned operation will stop the creation and delete the backup. There can be only one pending backup creation per database. Backup creation of different databases can run concurrently.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database: Required for the CreateBackup operation. Name of the database from which this backup was created. This needs to be in the same instance as the backup. Values are of the form `projects//instances//databases/`.
        :param pulumi.Input[str] expire_time: Required for the CreateBackup operation. The expiration time of the backup, with microseconds granularity that must be at least 6 hours and at most 366 days from the time the CreateBackup request is processed. Once the `expire_time` has passed, the backup is eligible to be automatically deleted by Cloud Spanner to free the resources used by the backup.
        :param pulumi.Input[str] name: Output only for the CreateBackup operation. Required for the UpdateBackup operation. A globally unique identifier for the backup which cannot be changed. Values are of the form `projects//instances//backups/a-z*[a-z0-9]` The final segment of the name must be between 2 and 60 characters in length. The backup is stored in the location(s) specified in the instance configuration of the instance containing the backup, identified by the prefix of the backup name of the form `projects//instances/`.
        :param pulumi.Input[str] version_time: The backup will contain an externally consistent copy of the database at the timestamp specified by `version_time`. If `version_time` is not specified, the system will set `version_time` to the `create_time` of the backup.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InstanceBackupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Starts creating a new Cloud Spanner Backup. The returned backup long-running operation will have a name of the format `projects//instances//backups//operations/` and can be used to track creation of the backup. The metadata field type is CreateBackupMetadata. The response field type is Backup, if successful. Cancelling the returned operation will stop the creation and delete the backup. There can be only one pending backup creation per database. Backup creation of different databases can run concurrently.

        :param str resource_name: The name of the resource.
        :param InstanceBackupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceBackupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backups_id: Optional[pulumi.Input[str]] = None,
                 database: Optional[pulumi.Input[str]] = None,
                 expire_time: Optional[pulumi.Input[str]] = None,
                 instances_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 version_time: Optional[pulumi.Input[str]] = None,
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
            __props__ = InstanceBackupArgs.__new__(InstanceBackupArgs)

            if backups_id is None and not opts.urn:
                raise TypeError("Missing required property 'backups_id'")
            __props__.__dict__["backups_id"] = backups_id
            __props__.__dict__["database"] = database
            __props__.__dict__["expire_time"] = expire_time
            if instances_id is None and not opts.urn:
                raise TypeError("Missing required property 'instances_id'")
            __props__.__dict__["instances_id"] = instances_id
            __props__.__dict__["name"] = name
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__.__dict__["projects_id"] = projects_id
            __props__.__dict__["version_time"] = version_time
            __props__.__dict__["create_time"] = None
            __props__.__dict__["encryption_info"] = None
            __props__.__dict__["referencing_databases"] = None
            __props__.__dict__["size_bytes"] = None
            __props__.__dict__["state"] = None
        super(InstanceBackup, __self__).__init__(
            'google-native:spanner/v1:InstanceBackup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'InstanceBackup':
        """
        Get an existing InstanceBackup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InstanceBackupArgs.__new__(InstanceBackupArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["database"] = None
        __props__.__dict__["encryption_info"] = None
        __props__.__dict__["expire_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["referencing_databases"] = None
        __props__.__dict__["size_bytes"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["version_time"] = None
        return InstanceBackup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time the CreateBackup request is received. If the request does not specify `version_time`, the `version_time` of the backup will be equivalent to the `create_time`.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def database(self) -> pulumi.Output[str]:
        """
        Required for the CreateBackup operation. Name of the database from which this backup was created. This needs to be in the same instance as the backup. Values are of the form `projects//instances//databases/`.
        """
        return pulumi.get(self, "database")

    @property
    @pulumi.getter(name="encryptionInfo")
    def encryption_info(self) -> pulumi.Output['outputs.EncryptionInfoResponse']:
        """
        The encryption information for the backup.
        """
        return pulumi.get(self, "encryption_info")

    @property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> pulumi.Output[str]:
        """
        Required for the CreateBackup operation. The expiration time of the backup, with microseconds granularity that must be at least 6 hours and at most 366 days from the time the CreateBackup request is processed. Once the `expire_time` has passed, the backup is eligible to be automatically deleted by Cloud Spanner to free the resources used by the backup.
        """
        return pulumi.get(self, "expire_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Output only for the CreateBackup operation. Required for the UpdateBackup operation. A globally unique identifier for the backup which cannot be changed. Values are of the form `projects//instances//backups/a-z*[a-z0-9]` The final segment of the name must be between 2 and 60 characters in length. The backup is stored in the location(s) specified in the instance configuration of the instance containing the backup, identified by the prefix of the backup name of the form `projects//instances/`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="referencingDatabases")
    def referencing_databases(self) -> pulumi.Output[Sequence[str]]:
        """
        The names of the restored databases that reference the backup. The database names are of the form `projects//instances//databases/`. Referencing databases may exist in different instances. The existence of any referencing database prevents the backup from being deleted. When a restored database from the backup enters the `READY` state, the reference to the backup is removed.
        """
        return pulumi.get(self, "referencing_databases")

    @property
    @pulumi.getter(name="sizeBytes")
    def size_bytes(self) -> pulumi.Output[str]:
        """
        Size of the backup in bytes.
        """
        return pulumi.get(self, "size_bytes")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of the backup.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="versionTime")
    def version_time(self) -> pulumi.Output[str]:
        """
        The backup will contain an externally consistent copy of the database at the timestamp specified by `version_time`. If `version_time` is not specified, the system will set `version_time` to the `create_time` of the backup.
        """
        return pulumi.get(self, "version_time")

