# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ReplicationSubnetGroupArgs', 'ReplicationSubnetGroup']

@pulumi.input_type
class ReplicationSubnetGroupArgs:
    def __init__(__self__, *,
                 replication_subnet_group_description: pulumi.Input[str],
                 replication_subnet_group_id: pulumi.Input[str],
                 subnet_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ReplicationSubnetGroup resource.
        :param pulumi.Input[str] replication_subnet_group_description: The description for the subnet group.
        :param pulumi.Input[str] replication_subnet_group_id: The name for the replication subnet group. This value is stored as a lowercase string.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: A list of the EC2 subnet IDs for the subnet group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider .
        """
        pulumi.set(__self__, "replication_subnet_group_description", replication_subnet_group_description)
        pulumi.set(__self__, "replication_subnet_group_id", replication_subnet_group_id)
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter(name="replicationSubnetGroupDescription")
    def replication_subnet_group_description(self) -> pulumi.Input[str]:
        """
        The description for the subnet group.
        """
        return pulumi.get(self, "replication_subnet_group_description")

    @replication_subnet_group_description.setter
    def replication_subnet_group_description(self, value: pulumi.Input[str]):
        pulumi.set(self, "replication_subnet_group_description", value)

    @property
    @pulumi.getter(name="replicationSubnetGroupId")
    def replication_subnet_group_id(self) -> pulumi.Input[str]:
        """
        The name for the replication subnet group. This value is stored as a lowercase string.
        """
        return pulumi.get(self, "replication_subnet_group_id")

    @replication_subnet_group_id.setter
    def replication_subnet_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "replication_subnet_group_id", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of the EC2 subnet IDs for the subnet group.
        """
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "subnet_ids", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
class _ReplicationSubnetGroupState:
    def __init__(__self__, *,
                 replication_subnet_group_arn: Optional[pulumi.Input[str]] = None,
                 replication_subnet_group_description: Optional[pulumi.Input[str]] = None,
                 replication_subnet_group_id: Optional[pulumi.Input[str]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ReplicationSubnetGroup resources.
        :param pulumi.Input[str] replication_subnet_group_description: The description for the subnet group.
        :param pulumi.Input[str] replication_subnet_group_id: The name for the replication subnet group. This value is stored as a lowercase string.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: A list of the EC2 subnet IDs for the subnet group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider .
        :param pulumi.Input[str] vpc_id: The ID of the VPC the subnet group is in.
        """
        if replication_subnet_group_arn is not None:
            pulumi.set(__self__, "replication_subnet_group_arn", replication_subnet_group_arn)
        if replication_subnet_group_description is not None:
            pulumi.set(__self__, "replication_subnet_group_description", replication_subnet_group_description)
        if replication_subnet_group_id is not None:
            pulumi.set(__self__, "replication_subnet_group_id", replication_subnet_group_id)
        if subnet_ids is not None:
            pulumi.set(__self__, "subnet_ids", subnet_ids)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="replicationSubnetGroupArn")
    def replication_subnet_group_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "replication_subnet_group_arn")

    @replication_subnet_group_arn.setter
    def replication_subnet_group_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "replication_subnet_group_arn", value)

    @property
    @pulumi.getter(name="replicationSubnetGroupDescription")
    def replication_subnet_group_description(self) -> Optional[pulumi.Input[str]]:
        """
        The description for the subnet group.
        """
        return pulumi.get(self, "replication_subnet_group_description")

    @replication_subnet_group_description.setter
    def replication_subnet_group_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "replication_subnet_group_description", value)

    @property
    @pulumi.getter(name="replicationSubnetGroupId")
    def replication_subnet_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The name for the replication subnet group. This value is stored as a lowercase string.
        """
        return pulumi.get(self, "replication_subnet_group_id")

    @replication_subnet_group_id.setter
    def replication_subnet_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "replication_subnet_group_id", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of the EC2 subnet IDs for the subnet group.
        """
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "subnet_ids", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
        The ID of the VPC the subnet group is in.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_id", value)


class ReplicationSubnetGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 replication_subnet_group_description: Optional[pulumi.Input[str]] = None,
                 replication_subnet_group_id: Optional[pulumi.Input[str]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides a DMS (Data Migration Service) replication subnet group resource. DMS replication subnet groups can be created, updated, deleted, and imported.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        # Create a new replication subnet group
        test = aws.dms.ReplicationSubnetGroup("test",
            replication_subnet_group_description="Test replication subnet group",
            replication_subnet_group_id="test-dms-replication-subnet-group-tf",
            subnet_ids=["subnet-12345678"],
            tags={
                "Name": "test",
            })
        ```

        ## Import

        Replication subnet groups can be imported using the `replication_subnet_group_id`, e.g.

        ```sh
         $ pulumi import aws:dms/replicationSubnetGroup:ReplicationSubnetGroup test test-dms-replication-subnet-group-tf
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] replication_subnet_group_description: The description for the subnet group.
        :param pulumi.Input[str] replication_subnet_group_id: The name for the replication subnet group. This value is stored as a lowercase string.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: A list of the EC2 subnet IDs for the subnet group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider .
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ReplicationSubnetGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a DMS (Data Migration Service) replication subnet group resource. DMS replication subnet groups can be created, updated, deleted, and imported.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        # Create a new replication subnet group
        test = aws.dms.ReplicationSubnetGroup("test",
            replication_subnet_group_description="Test replication subnet group",
            replication_subnet_group_id="test-dms-replication-subnet-group-tf",
            subnet_ids=["subnet-12345678"],
            tags={
                "Name": "test",
            })
        ```

        ## Import

        Replication subnet groups can be imported using the `replication_subnet_group_id`, e.g.

        ```sh
         $ pulumi import aws:dms/replicationSubnetGroup:ReplicationSubnetGroup test test-dms-replication-subnet-group-tf
        ```

        :param str resource_name: The name of the resource.
        :param ReplicationSubnetGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ReplicationSubnetGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 replication_subnet_group_description: Optional[pulumi.Input[str]] = None,
                 replication_subnet_group_id: Optional[pulumi.Input[str]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
            __props__ = ReplicationSubnetGroupArgs.__new__(ReplicationSubnetGroupArgs)

            if replication_subnet_group_description is None and not opts.urn:
                raise TypeError("Missing required property 'replication_subnet_group_description'")
            __props__.__dict__["replication_subnet_group_description"] = replication_subnet_group_description
            if replication_subnet_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'replication_subnet_group_id'")
            __props__.__dict__["replication_subnet_group_id"] = replication_subnet_group_id
            if subnet_ids is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_ids'")
            __props__.__dict__["subnet_ids"] = subnet_ids
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tags_all"] = tags_all
            __props__.__dict__["replication_subnet_group_arn"] = None
            __props__.__dict__["vpc_id"] = None
        super(ReplicationSubnetGroup, __self__).__init__(
            'aws:dms/replicationSubnetGroup:ReplicationSubnetGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            replication_subnet_group_arn: Optional[pulumi.Input[str]] = None,
            replication_subnet_group_description: Optional[pulumi.Input[str]] = None,
            replication_subnet_group_id: Optional[pulumi.Input[str]] = None,
            subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            vpc_id: Optional[pulumi.Input[str]] = None) -> 'ReplicationSubnetGroup':
        """
        Get an existing ReplicationSubnetGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] replication_subnet_group_description: The description for the subnet group.
        :param pulumi.Input[str] replication_subnet_group_id: The name for the replication subnet group. This value is stored as a lowercase string.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: A list of the EC2 subnet IDs for the subnet group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider .
        :param pulumi.Input[str] vpc_id: The ID of the VPC the subnet group is in.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ReplicationSubnetGroupState.__new__(_ReplicationSubnetGroupState)

        __props__.__dict__["replication_subnet_group_arn"] = replication_subnet_group_arn
        __props__.__dict__["replication_subnet_group_description"] = replication_subnet_group_description
        __props__.__dict__["replication_subnet_group_id"] = replication_subnet_group_id
        __props__.__dict__["subnet_ids"] = subnet_ids
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["vpc_id"] = vpc_id
        return ReplicationSubnetGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="replicationSubnetGroupArn")
    def replication_subnet_group_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "replication_subnet_group_arn")

    @property
    @pulumi.getter(name="replicationSubnetGroupDescription")
    def replication_subnet_group_description(self) -> pulumi.Output[str]:
        """
        The description for the subnet group.
        """
        return pulumi.get(self, "replication_subnet_group_description")

    @property
    @pulumi.getter(name="replicationSubnetGroupId")
    def replication_subnet_group_id(self) -> pulumi.Output[str]:
        """
        The name for the replication subnet group. This value is stored as a lowercase string.
        """
        return pulumi.get(self, "replication_subnet_group_id")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of the EC2 subnet IDs for the subnet group.
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
        The ID of the VPC the subnet group is in.
        """
        return pulumi.get(self, "vpc_id")

