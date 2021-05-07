# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['TapePoolArgs', 'TapePool']

@pulumi.input_type
class TapePoolArgs:
    def __init__(__self__, *,
                 pool_name: pulumi.Input[str],
                 storage_class: pulumi.Input[str],
                 retention_lock_time_in_days: Optional[pulumi.Input[int]] = None,
                 retention_lock_type: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a TapePool resource.
        :param pulumi.Input[str] pool_name: The name of the new custom tape pool.
        :param pulumi.Input[str] storage_class: The storage class that is associated with the new custom pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class that corresponds to the pool. Possible values are `DEEP_ARCHIVE` or `GLACIER`.
        :param pulumi.Input[int] retention_lock_time_in_days: Tape retention lock time is set in days. Tape retention lock can be enabled for up to 100 years (36,500 days). Default value is 0.
        :param pulumi.Input[str] retention_lock_type: Tape retention lock can be configured in two modes. When configured in governance mode, AWS accounts with specific IAM permissions are authorized to remove the tape retention lock from archived virtual tapes. When configured in compliance mode, the tape retention lock cannot be removed by any user, including the root AWS account. Possible values are `COMPLIANCE`, `GOVERNANCE`, and `NONE`. Default value is `NONE`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider .
        """
        pulumi.set(__self__, "pool_name", pool_name)
        pulumi.set(__self__, "storage_class", storage_class)
        if retention_lock_time_in_days is not None:
            pulumi.set(__self__, "retention_lock_time_in_days", retention_lock_time_in_days)
        if retention_lock_type is not None:
            pulumi.set(__self__, "retention_lock_type", retention_lock_type)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter(name="poolName")
    def pool_name(self) -> pulumi.Input[str]:
        """
        The name of the new custom tape pool.
        """
        return pulumi.get(self, "pool_name")

    @pool_name.setter
    def pool_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "pool_name", value)

    @property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> pulumi.Input[str]:
        """
        The storage class that is associated with the new custom pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class that corresponds to the pool. Possible values are `DEEP_ARCHIVE` or `GLACIER`.
        """
        return pulumi.get(self, "storage_class")

    @storage_class.setter
    def storage_class(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_class", value)

    @property
    @pulumi.getter(name="retentionLockTimeInDays")
    def retention_lock_time_in_days(self) -> Optional[pulumi.Input[int]]:
        """
        Tape retention lock time is set in days. Tape retention lock can be enabled for up to 100 years (36,500 days). Default value is 0.
        """
        return pulumi.get(self, "retention_lock_time_in_days")

    @retention_lock_time_in_days.setter
    def retention_lock_time_in_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "retention_lock_time_in_days", value)

    @property
    @pulumi.getter(name="retentionLockType")
    def retention_lock_type(self) -> Optional[pulumi.Input[str]]:
        """
        Tape retention lock can be configured in two modes. When configured in governance mode, AWS accounts with specific IAM permissions are authorized to remove the tape retention lock from archived virtual tapes. When configured in compliance mode, the tape retention lock cannot be removed by any user, including the root AWS account. Possible values are `COMPLIANCE`, `GOVERNANCE`, and `NONE`. Default value is `NONE`.
        """
        return pulumi.get(self, "retention_lock_type")

    @retention_lock_type.setter
    def retention_lock_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "retention_lock_type", value)

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
class _TapePoolState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 retention_lock_time_in_days: Optional[pulumi.Input[int]] = None,
                 retention_lock_type: Optional[pulumi.Input[str]] = None,
                 storage_class: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering TapePool resources.
        :param pulumi.Input[str] arn: Volume Amazon Resource Name (ARN), e.g. `aws_storagegateway_tape_pool.example arn:aws:storagegateway:us-east-1:123456789012:tapepool/pool-12345678`.
        :param pulumi.Input[str] pool_name: The name of the new custom tape pool.
        :param pulumi.Input[int] retention_lock_time_in_days: Tape retention lock time is set in days. Tape retention lock can be enabled for up to 100 years (36,500 days). Default value is 0.
        :param pulumi.Input[str] retention_lock_type: Tape retention lock can be configured in two modes. When configured in governance mode, AWS accounts with specific IAM permissions are authorized to remove the tape retention lock from archived virtual tapes. When configured in compliance mode, the tape retention lock cannot be removed by any user, including the root AWS account. Possible values are `COMPLIANCE`, `GOVERNANCE`, and `NONE`. Default value is `NONE`.
        :param pulumi.Input[str] storage_class: The storage class that is associated with the new custom pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class that corresponds to the pool. Possible values are `DEEP_ARCHIVE` or `GLACIER`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider .
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if pool_name is not None:
            pulumi.set(__self__, "pool_name", pool_name)
        if retention_lock_time_in_days is not None:
            pulumi.set(__self__, "retention_lock_time_in_days", retention_lock_time_in_days)
        if retention_lock_type is not None:
            pulumi.set(__self__, "retention_lock_type", retention_lock_type)
        if storage_class is not None:
            pulumi.set(__self__, "storage_class", storage_class)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        Volume Amazon Resource Name (ARN), e.g. `aws_storagegateway_tape_pool.example arn:aws:storagegateway:us-east-1:123456789012:tapepool/pool-12345678`.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="poolName")
    def pool_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the new custom tape pool.
        """
        return pulumi.get(self, "pool_name")

    @pool_name.setter
    def pool_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pool_name", value)

    @property
    @pulumi.getter(name="retentionLockTimeInDays")
    def retention_lock_time_in_days(self) -> Optional[pulumi.Input[int]]:
        """
        Tape retention lock time is set in days. Tape retention lock can be enabled for up to 100 years (36,500 days). Default value is 0.
        """
        return pulumi.get(self, "retention_lock_time_in_days")

    @retention_lock_time_in_days.setter
    def retention_lock_time_in_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "retention_lock_time_in_days", value)

    @property
    @pulumi.getter(name="retentionLockType")
    def retention_lock_type(self) -> Optional[pulumi.Input[str]]:
        """
        Tape retention lock can be configured in two modes. When configured in governance mode, AWS accounts with specific IAM permissions are authorized to remove the tape retention lock from archived virtual tapes. When configured in compliance mode, the tape retention lock cannot be removed by any user, including the root AWS account. Possible values are `COMPLIANCE`, `GOVERNANCE`, and `NONE`. Default value is `NONE`.
        """
        return pulumi.get(self, "retention_lock_type")

    @retention_lock_type.setter
    def retention_lock_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "retention_lock_type", value)

    @property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[pulumi.Input[str]]:
        """
        The storage class that is associated with the new custom pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class that corresponds to the pool. Possible values are `DEEP_ARCHIVE` or `GLACIER`.
        """
        return pulumi.get(self, "storage_class")

    @storage_class.setter
    def storage_class(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_class", value)

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


class TapePool(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 retention_lock_time_in_days: Optional[pulumi.Input[int]] = None,
                 retention_lock_type: Optional[pulumi.Input[str]] = None,
                 storage_class: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages an AWS Storage Gateway Tape Pool.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.storagegateway.TapePool("example",
            pool_name="example",
            storage_class="GLACIER")
        ```

        ## Import

        `aws_storagegateway_tape_pool` can be imported by using the volume Amazon Resource Name (ARN), e.g.

        ```sh
         $ pulumi import aws:storagegateway/tapePool:TapePool example arn:aws:storagegateway:us-east-1:123456789012:tapepool/pool-12345678
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] pool_name: The name of the new custom tape pool.
        :param pulumi.Input[int] retention_lock_time_in_days: Tape retention lock time is set in days. Tape retention lock can be enabled for up to 100 years (36,500 days). Default value is 0.
        :param pulumi.Input[str] retention_lock_type: Tape retention lock can be configured in two modes. When configured in governance mode, AWS accounts with specific IAM permissions are authorized to remove the tape retention lock from archived virtual tapes. When configured in compliance mode, the tape retention lock cannot be removed by any user, including the root AWS account. Possible values are `COMPLIANCE`, `GOVERNANCE`, and `NONE`. Default value is `NONE`.
        :param pulumi.Input[str] storage_class: The storage class that is associated with the new custom pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class that corresponds to the pool. Possible values are `DEEP_ARCHIVE` or `GLACIER`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider .
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TapePoolArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an AWS Storage Gateway Tape Pool.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.storagegateway.TapePool("example",
            pool_name="example",
            storage_class="GLACIER")
        ```

        ## Import

        `aws_storagegateway_tape_pool` can be imported by using the volume Amazon Resource Name (ARN), e.g.

        ```sh
         $ pulumi import aws:storagegateway/tapePool:TapePool example arn:aws:storagegateway:us-east-1:123456789012:tapepool/pool-12345678
        ```

        :param str resource_name: The name of the resource.
        :param TapePoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TapePoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 retention_lock_time_in_days: Optional[pulumi.Input[int]] = None,
                 retention_lock_type: Optional[pulumi.Input[str]] = None,
                 storage_class: Optional[pulumi.Input[str]] = None,
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
            __props__ = TapePoolArgs.__new__(TapePoolArgs)

            if pool_name is None and not opts.urn:
                raise TypeError("Missing required property 'pool_name'")
            __props__.__dict__["pool_name"] = pool_name
            __props__.__dict__["retention_lock_time_in_days"] = retention_lock_time_in_days
            __props__.__dict__["retention_lock_type"] = retention_lock_type
            if storage_class is None and not opts.urn:
                raise TypeError("Missing required property 'storage_class'")
            __props__.__dict__["storage_class"] = storage_class
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tags_all"] = tags_all
            __props__.__dict__["arn"] = None
        super(TapePool, __self__).__init__(
            'aws:storagegateway/tapePool:TapePool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            pool_name: Optional[pulumi.Input[str]] = None,
            retention_lock_time_in_days: Optional[pulumi.Input[int]] = None,
            retention_lock_type: Optional[pulumi.Input[str]] = None,
            storage_class: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'TapePool':
        """
        Get an existing TapePool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Volume Amazon Resource Name (ARN), e.g. `aws_storagegateway_tape_pool.example arn:aws:storagegateway:us-east-1:123456789012:tapepool/pool-12345678`.
        :param pulumi.Input[str] pool_name: The name of the new custom tape pool.
        :param pulumi.Input[int] retention_lock_time_in_days: Tape retention lock time is set in days. Tape retention lock can be enabled for up to 100 years (36,500 days). Default value is 0.
        :param pulumi.Input[str] retention_lock_type: Tape retention lock can be configured in two modes. When configured in governance mode, AWS accounts with specific IAM permissions are authorized to remove the tape retention lock from archived virtual tapes. When configured in compliance mode, the tape retention lock cannot be removed by any user, including the root AWS account. Possible values are `COMPLIANCE`, `GOVERNANCE`, and `NONE`. Default value is `NONE`.
        :param pulumi.Input[str] storage_class: The storage class that is associated with the new custom pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class that corresponds to the pool. Possible values are `DEEP_ARCHIVE` or `GLACIER`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider .
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TapePoolState.__new__(_TapePoolState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["pool_name"] = pool_name
        __props__.__dict__["retention_lock_time_in_days"] = retention_lock_time_in_days
        __props__.__dict__["retention_lock_type"] = retention_lock_type
        __props__.__dict__["storage_class"] = storage_class
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        return TapePool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Volume Amazon Resource Name (ARN), e.g. `aws_storagegateway_tape_pool.example arn:aws:storagegateway:us-east-1:123456789012:tapepool/pool-12345678`.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="poolName")
    def pool_name(self) -> pulumi.Output[str]:
        """
        The name of the new custom tape pool.
        """
        return pulumi.get(self, "pool_name")

    @property
    @pulumi.getter(name="retentionLockTimeInDays")
    def retention_lock_time_in_days(self) -> pulumi.Output[Optional[int]]:
        """
        Tape retention lock time is set in days. Tape retention lock can be enabled for up to 100 years (36,500 days). Default value is 0.
        """
        return pulumi.get(self, "retention_lock_time_in_days")

    @property
    @pulumi.getter(name="retentionLockType")
    def retention_lock_type(self) -> pulumi.Output[Optional[str]]:
        """
        Tape retention lock can be configured in two modes. When configured in governance mode, AWS accounts with specific IAM permissions are authorized to remove the tape retention lock from archived virtual tapes. When configured in compliance mode, the tape retention lock cannot be removed by any user, including the root AWS account. Possible values are `COMPLIANCE`, `GOVERNANCE`, and `NONE`. Default value is `NONE`.
        """
        return pulumi.get(self, "retention_lock_type")

    @property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> pulumi.Output[str]:
        """
        The storage class that is associated with the new custom pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class that corresponds to the pool. Possible values are `DEEP_ARCHIVE` or `GLACIER`.
        """
        return pulumi.get(self, "storage_class")

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

