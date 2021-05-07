# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SnapshotArgs', 'Snapshot']

@pulumi.input_type
class SnapshotArgs:
    def __init__(__self__, *,
                 db_instance_identifier: pulumi.Input[str],
                 db_snapshot_identifier: pulumi.Input[str],
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Snapshot resource.
        :param pulumi.Input[str] db_instance_identifier: The DB Instance Identifier from which to take the snapshot.
        :param pulumi.Input[str] db_snapshot_identifier: The Identifier for the snapshot.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider .
        """
        pulumi.set(__self__, "db_instance_identifier", db_instance_identifier)
        pulumi.set(__self__, "db_snapshot_identifier", db_snapshot_identifier)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter(name="dbInstanceIdentifier")
    def db_instance_identifier(self) -> pulumi.Input[str]:
        """
        The DB Instance Identifier from which to take the snapshot.
        """
        return pulumi.get(self, "db_instance_identifier")

    @db_instance_identifier.setter
    def db_instance_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "db_instance_identifier", value)

    @property
    @pulumi.getter(name="dbSnapshotIdentifier")
    def db_snapshot_identifier(self) -> pulumi.Input[str]:
        """
        The Identifier for the snapshot.
        """
        return pulumi.get(self, "db_snapshot_identifier")

    @db_snapshot_identifier.setter
    def db_snapshot_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "db_snapshot_identifier", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider .
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)


@pulumi.input_type
class _SnapshotState:
    def __init__(__self__, *,
                 allocated_storage: Optional[pulumi.Input[int]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 db_instance_identifier: Optional[pulumi.Input[str]] = None,
                 db_snapshot_arn: Optional[pulumi.Input[str]] = None,
                 db_snapshot_identifier: Optional[pulumi.Input[str]] = None,
                 encrypted: Optional[pulumi.Input[bool]] = None,
                 engine: Optional[pulumi.Input[str]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 iops: Optional[pulumi.Input[int]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 license_model: Optional[pulumi.Input[str]] = None,
                 option_group_name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 snapshot_type: Optional[pulumi.Input[str]] = None,
                 source_db_snapshot_identifier: Optional[pulumi.Input[str]] = None,
                 source_region: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 storage_type: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Snapshot resources.
        :param pulumi.Input[int] allocated_storage: Specifies the allocated storage size in gigabytes (GB).
        :param pulumi.Input[str] availability_zone: Specifies the name of the Availability Zone the DB instance was located in at the time of the DB snapshot.
        :param pulumi.Input[str] db_instance_identifier: The DB Instance Identifier from which to take the snapshot.
        :param pulumi.Input[str] db_snapshot_arn: The Amazon Resource Name (ARN) for the DB snapshot.
        :param pulumi.Input[str] db_snapshot_identifier: The Identifier for the snapshot.
        :param pulumi.Input[bool] encrypted: Specifies whether the DB snapshot is encrypted.
        :param pulumi.Input[str] engine: Specifies the name of the database engine.
        :param pulumi.Input[str] engine_version: Specifies the version of the database engine.
        :param pulumi.Input[int] iops: Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of the snapshot.
        :param pulumi.Input[str] kms_key_id: The ARN for the KMS encryption key.
        :param pulumi.Input[str] license_model: License model information for the restored DB instance.
        :param pulumi.Input[str] option_group_name: Provides the option group name for the DB snapshot.
        :param pulumi.Input[str] source_db_snapshot_identifier: The DB snapshot Arn that the DB snapshot was copied from. It only has value in case of cross customer or cross region copy.
        :param pulumi.Input[str] source_region: The region that the DB snapshot was created in or copied from.
        :param pulumi.Input[str] status: Specifies the status of this DB snapshot.
        :param pulumi.Input[str] storage_type: Specifies the storage type associated with DB snapshot.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider .
        :param pulumi.Input[str] vpc_id: Specifies the storage type associated with DB snapshot.
        """
        if allocated_storage is not None:
            pulumi.set(__self__, "allocated_storage", allocated_storage)
        if availability_zone is not None:
            pulumi.set(__self__, "availability_zone", availability_zone)
        if db_instance_identifier is not None:
            pulumi.set(__self__, "db_instance_identifier", db_instance_identifier)
        if db_snapshot_arn is not None:
            pulumi.set(__self__, "db_snapshot_arn", db_snapshot_arn)
        if db_snapshot_identifier is not None:
            pulumi.set(__self__, "db_snapshot_identifier", db_snapshot_identifier)
        if encrypted is not None:
            pulumi.set(__self__, "encrypted", encrypted)
        if engine is not None:
            pulumi.set(__self__, "engine", engine)
        if engine_version is not None:
            pulumi.set(__self__, "engine_version", engine_version)
        if iops is not None:
            pulumi.set(__self__, "iops", iops)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if license_model is not None:
            pulumi.set(__self__, "license_model", license_model)
        if option_group_name is not None:
            pulumi.set(__self__, "option_group_name", option_group_name)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if snapshot_type is not None:
            pulumi.set(__self__, "snapshot_type", snapshot_type)
        if source_db_snapshot_identifier is not None:
            pulumi.set(__self__, "source_db_snapshot_identifier", source_db_snapshot_identifier)
        if source_region is not None:
            pulumi.set(__self__, "source_region", source_region)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if storage_type is not None:
            pulumi.set(__self__, "storage_type", storage_type)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="allocatedStorage")
    def allocated_storage(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the allocated storage size in gigabytes (GB).
        """
        return pulumi.get(self, "allocated_storage")

    @allocated_storage.setter
    def allocated_storage(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "allocated_storage", value)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Availability Zone the DB instance was located in at the time of the DB snapshot.
        """
        return pulumi.get(self, "availability_zone")

    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "availability_zone", value)

    @property
    @pulumi.getter(name="dbInstanceIdentifier")
    def db_instance_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The DB Instance Identifier from which to take the snapshot.
        """
        return pulumi.get(self, "db_instance_identifier")

    @db_instance_identifier.setter
    def db_instance_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "db_instance_identifier", value)

    @property
    @pulumi.getter(name="dbSnapshotArn")
    def db_snapshot_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) for the DB snapshot.
        """
        return pulumi.get(self, "db_snapshot_arn")

    @db_snapshot_arn.setter
    def db_snapshot_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "db_snapshot_arn", value)

    @property
    @pulumi.getter(name="dbSnapshotIdentifier")
    def db_snapshot_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The Identifier for the snapshot.
        """
        return pulumi.get(self, "db_snapshot_identifier")

    @db_snapshot_identifier.setter
    def db_snapshot_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "db_snapshot_identifier", value)

    @property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether the DB snapshot is encrypted.
        """
        return pulumi.get(self, "encrypted")

    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "encrypted", value)

    @property
    @pulumi.getter
    def engine(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the database engine.
        """
        return pulumi.get(self, "engine")

    @engine.setter
    def engine(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "engine", value)

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the version of the database engine.
        """
        return pulumi.get(self, "engine_version")

    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "engine_version", value)

    @property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of the snapshot.
        """
        return pulumi.get(self, "iops")

    @iops.setter
    def iops(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "iops", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN for the KMS encryption key.
        """
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> Optional[pulumi.Input[str]]:
        """
        License model information for the restored DB instance.
        """
        return pulumi.get(self, "license_model")

    @license_model.setter
    def license_model(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "license_model", value)

    @property
    @pulumi.getter(name="optionGroupName")
    def option_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Provides the option group name for the DB snapshot.
        """
        return pulumi.get(self, "option_group_name")

    @option_group_name.setter
    def option_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "option_group_name", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="snapshotType")
    def snapshot_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "snapshot_type")

    @snapshot_type.setter
    def snapshot_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "snapshot_type", value)

    @property
    @pulumi.getter(name="sourceDbSnapshotIdentifier")
    def source_db_snapshot_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The DB snapshot Arn that the DB snapshot was copied from. It only has value in case of cross customer or cross region copy.
        """
        return pulumi.get(self, "source_db_snapshot_identifier")

    @source_db_snapshot_identifier.setter
    def source_db_snapshot_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_db_snapshot_identifier", value)

    @property
    @pulumi.getter(name="sourceRegion")
    def source_region(self) -> Optional[pulumi.Input[str]]:
        """
        The region that the DB snapshot was created in or copied from.
        """
        return pulumi.get(self, "source_region")

    @source_region.setter
    def source_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_region", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the status of this DB snapshot.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the storage type associated with DB snapshot.
        """
        return pulumi.get(self, "storage_type")

    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_type", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider .
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the storage type associated with DB snapshot.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_id", value)


class Snapshot(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 db_instance_identifier: Optional[pulumi.Input[str]] = None,
                 db_snapshot_identifier: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages an RDS database instance snapshot. For managing RDS database cluster snapshots, see the `rds.ClusterSnapshot` resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        bar = aws.rds.Instance("bar",
            allocated_storage=10,
            engine="mysql",
            engine_version="5.6.21",
            instance_class="db.t2.micro",
            name="baz",
            password="barbarbarbar",
            username="foo",
            maintenance_window="Fri:09:00-Fri:09:30",
            backup_retention_period=0,
            parameter_group_name="default.mysql5.6")
        test = aws.rds.Snapshot("test",
            db_instance_identifier=bar.id,
            db_snapshot_identifier="testsnapshot1234")
        ```

        ## Import

        `aws_db_snapshot` can be imported by using the snapshot identifier, e.g.

        ```sh
         $ pulumi import aws:rds/snapshot:Snapshot example my-snapshot
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] db_instance_identifier: The DB Instance Identifier from which to take the snapshot.
        :param pulumi.Input[str] db_snapshot_identifier: The Identifier for the snapshot.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider .
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SnapshotArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an RDS database instance snapshot. For managing RDS database cluster snapshots, see the `rds.ClusterSnapshot` resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        bar = aws.rds.Instance("bar",
            allocated_storage=10,
            engine="mysql",
            engine_version="5.6.21",
            instance_class="db.t2.micro",
            name="baz",
            password="barbarbarbar",
            username="foo",
            maintenance_window="Fri:09:00-Fri:09:30",
            backup_retention_period=0,
            parameter_group_name="default.mysql5.6")
        test = aws.rds.Snapshot("test",
            db_instance_identifier=bar.id,
            db_snapshot_identifier="testsnapshot1234")
        ```

        ## Import

        `aws_db_snapshot` can be imported by using the snapshot identifier, e.g.

        ```sh
         $ pulumi import aws:rds/snapshot:Snapshot example my-snapshot
        ```

        :param str resource_name: The name of the resource.
        :param SnapshotArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SnapshotArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 db_instance_identifier: Optional[pulumi.Input[str]] = None,
                 db_snapshot_identifier: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = SnapshotArgs.__new__(SnapshotArgs)

            if db_instance_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'db_instance_identifier'")
            __props__.__dict__["db_instance_identifier"] = db_instance_identifier
            if db_snapshot_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'db_snapshot_identifier'")
            __props__.__dict__["db_snapshot_identifier"] = db_snapshot_identifier
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tags_all"] = tags_all
            __props__.__dict__["allocated_storage"] = None
            __props__.__dict__["availability_zone"] = None
            __props__.__dict__["db_snapshot_arn"] = None
            __props__.__dict__["encrypted"] = None
            __props__.__dict__["engine"] = None
            __props__.__dict__["engine_version"] = None
            __props__.__dict__["iops"] = None
            __props__.__dict__["kms_key_id"] = None
            __props__.__dict__["license_model"] = None
            __props__.__dict__["option_group_name"] = None
            __props__.__dict__["port"] = None
            __props__.__dict__["snapshot_type"] = None
            __props__.__dict__["source_db_snapshot_identifier"] = None
            __props__.__dict__["source_region"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["storage_type"] = None
            __props__.__dict__["vpc_id"] = None
        super(Snapshot, __self__).__init__(
            'aws:rds/snapshot:Snapshot',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allocated_storage: Optional[pulumi.Input[int]] = None,
            availability_zone: Optional[pulumi.Input[str]] = None,
            db_instance_identifier: Optional[pulumi.Input[str]] = None,
            db_snapshot_arn: Optional[pulumi.Input[str]] = None,
            db_snapshot_identifier: Optional[pulumi.Input[str]] = None,
            encrypted: Optional[pulumi.Input[bool]] = None,
            engine: Optional[pulumi.Input[str]] = None,
            engine_version: Optional[pulumi.Input[str]] = None,
            iops: Optional[pulumi.Input[int]] = None,
            kms_key_id: Optional[pulumi.Input[str]] = None,
            license_model: Optional[pulumi.Input[str]] = None,
            option_group_name: Optional[pulumi.Input[str]] = None,
            port: Optional[pulumi.Input[int]] = None,
            snapshot_type: Optional[pulumi.Input[str]] = None,
            source_db_snapshot_identifier: Optional[pulumi.Input[str]] = None,
            source_region: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            storage_type: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            vpc_id: Optional[pulumi.Input[str]] = None) -> 'Snapshot':
        """
        Get an existing Snapshot resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] allocated_storage: Specifies the allocated storage size in gigabytes (GB).
        :param pulumi.Input[str] availability_zone: Specifies the name of the Availability Zone the DB instance was located in at the time of the DB snapshot.
        :param pulumi.Input[str] db_instance_identifier: The DB Instance Identifier from which to take the snapshot.
        :param pulumi.Input[str] db_snapshot_arn: The Amazon Resource Name (ARN) for the DB snapshot.
        :param pulumi.Input[str] db_snapshot_identifier: The Identifier for the snapshot.
        :param pulumi.Input[bool] encrypted: Specifies whether the DB snapshot is encrypted.
        :param pulumi.Input[str] engine: Specifies the name of the database engine.
        :param pulumi.Input[str] engine_version: Specifies the version of the database engine.
        :param pulumi.Input[int] iops: Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of the snapshot.
        :param pulumi.Input[str] kms_key_id: The ARN for the KMS encryption key.
        :param pulumi.Input[str] license_model: License model information for the restored DB instance.
        :param pulumi.Input[str] option_group_name: Provides the option group name for the DB snapshot.
        :param pulumi.Input[str] source_db_snapshot_identifier: The DB snapshot Arn that the DB snapshot was copied from. It only has value in case of cross customer or cross region copy.
        :param pulumi.Input[str] source_region: The region that the DB snapshot was created in or copied from.
        :param pulumi.Input[str] status: Specifies the status of this DB snapshot.
        :param pulumi.Input[str] storage_type: Specifies the storage type associated with DB snapshot.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider .
        :param pulumi.Input[str] vpc_id: Specifies the storage type associated with DB snapshot.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SnapshotState.__new__(_SnapshotState)

        __props__.__dict__["allocated_storage"] = allocated_storage
        __props__.__dict__["availability_zone"] = availability_zone
        __props__.__dict__["db_instance_identifier"] = db_instance_identifier
        __props__.__dict__["db_snapshot_arn"] = db_snapshot_arn
        __props__.__dict__["db_snapshot_identifier"] = db_snapshot_identifier
        __props__.__dict__["encrypted"] = encrypted
        __props__.__dict__["engine"] = engine
        __props__.__dict__["engine_version"] = engine_version
        __props__.__dict__["iops"] = iops
        __props__.__dict__["kms_key_id"] = kms_key_id
        __props__.__dict__["license_model"] = license_model
        __props__.__dict__["option_group_name"] = option_group_name
        __props__.__dict__["port"] = port
        __props__.__dict__["snapshot_type"] = snapshot_type
        __props__.__dict__["source_db_snapshot_identifier"] = source_db_snapshot_identifier
        __props__.__dict__["source_region"] = source_region
        __props__.__dict__["status"] = status
        __props__.__dict__["storage_type"] = storage_type
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["vpc_id"] = vpc_id
        return Snapshot(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allocatedStorage")
    def allocated_storage(self) -> pulumi.Output[int]:
        """
        Specifies the allocated storage size in gigabytes (GB).
        """
        return pulumi.get(self, "allocated_storage")

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Availability Zone the DB instance was located in at the time of the DB snapshot.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="dbInstanceIdentifier")
    def db_instance_identifier(self) -> pulumi.Output[str]:
        """
        The DB Instance Identifier from which to take the snapshot.
        """
        return pulumi.get(self, "db_instance_identifier")

    @property
    @pulumi.getter(name="dbSnapshotArn")
    def db_snapshot_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) for the DB snapshot.
        """
        return pulumi.get(self, "db_snapshot_arn")

    @property
    @pulumi.getter(name="dbSnapshotIdentifier")
    def db_snapshot_identifier(self) -> pulumi.Output[str]:
        """
        The Identifier for the snapshot.
        """
        return pulumi.get(self, "db_snapshot_identifier")

    @property
    @pulumi.getter
    def encrypted(self) -> pulumi.Output[bool]:
        """
        Specifies whether the DB snapshot is encrypted.
        """
        return pulumi.get(self, "encrypted")

    @property
    @pulumi.getter
    def engine(self) -> pulumi.Output[str]:
        """
        Specifies the name of the database engine.
        """
        return pulumi.get(self, "engine")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[str]:
        """
        Specifies the version of the database engine.
        """
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter
    def iops(self) -> pulumi.Output[int]:
        """
        Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of the snapshot.
        """
        return pulumi.get(self, "iops")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[str]:
        """
        The ARN for the KMS encryption key.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> pulumi.Output[str]:
        """
        License model information for the restored DB instance.
        """
        return pulumi.get(self, "license_model")

    @property
    @pulumi.getter(name="optionGroupName")
    def option_group_name(self) -> pulumi.Output[str]:
        """
        Provides the option group name for the DB snapshot.
        """
        return pulumi.get(self, "option_group_name")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[int]:
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="snapshotType")
    def snapshot_type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "snapshot_type")

    @property
    @pulumi.getter(name="sourceDbSnapshotIdentifier")
    def source_db_snapshot_identifier(self) -> pulumi.Output[str]:
        """
        The DB snapshot Arn that the DB snapshot was copied from. It only has value in case of cross customer or cross region copy.
        """
        return pulumi.get(self, "source_db_snapshot_identifier")

    @property
    @pulumi.getter(name="sourceRegion")
    def source_region(self) -> pulumi.Output[str]:
        """
        The region that the DB snapshot was created in or copied from.
        """
        return pulumi.get(self, "source_region")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Specifies the status of this DB snapshot.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> pulumi.Output[str]:
        """
        Specifies the storage type associated with DB snapshot.
        """
        return pulumi.get(self, "storage_type")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider .
        """
        return pulumi.get(self, "tags_all")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[str]:
        """
        Specifies the storage type associated with DB snapshot.
        """
        return pulumi.get(self, "vpc_id")

