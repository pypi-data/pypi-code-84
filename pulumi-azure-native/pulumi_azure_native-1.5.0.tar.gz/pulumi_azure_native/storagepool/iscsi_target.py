# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['IscsiTargetArgs', 'IscsiTarget']

@pulumi.input_type
class IscsiTargetArgs:
    def __init__(__self__, *,
                 disk_pool_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 tpgs: pulumi.Input[Sequence[pulumi.Input['TargetPortalGroupCreateArgs']]],
                 iscsi_target_name: Optional[pulumi.Input[str]] = None,
                 target_iqn: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IscsiTarget resource.
        :param pulumi.Input[str] disk_pool_name: The name of the Disk pool.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input['TargetPortalGroupCreateArgs']]] tpgs: List of iSCSI target portal groups. Can have 1 portal group at most.
        :param pulumi.Input[str] iscsi_target_name: The name of the iSCSI target.
        :param pulumi.Input[str] target_iqn: iSCSI target IQN (iSCSI Qualified Name); example: "iqn.2005-03.org.iscsi:server".
        """
        pulumi.set(__self__, "disk_pool_name", disk_pool_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "tpgs", tpgs)
        if iscsi_target_name is not None:
            pulumi.set(__self__, "iscsi_target_name", iscsi_target_name)
        if target_iqn is not None:
            pulumi.set(__self__, "target_iqn", target_iqn)

    @property
    @pulumi.getter(name="diskPoolName")
    def disk_pool_name(self) -> pulumi.Input[str]:
        """
        The name of the Disk pool.
        """
        return pulumi.get(self, "disk_pool_name")

    @disk_pool_name.setter
    def disk_pool_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "disk_pool_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def tpgs(self) -> pulumi.Input[Sequence[pulumi.Input['TargetPortalGroupCreateArgs']]]:
        """
        List of iSCSI target portal groups. Can have 1 portal group at most.
        """
        return pulumi.get(self, "tpgs")

    @tpgs.setter
    def tpgs(self, value: pulumi.Input[Sequence[pulumi.Input['TargetPortalGroupCreateArgs']]]):
        pulumi.set(self, "tpgs", value)

    @property
    @pulumi.getter(name="iscsiTargetName")
    def iscsi_target_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the iSCSI target.
        """
        return pulumi.get(self, "iscsi_target_name")

    @iscsi_target_name.setter
    def iscsi_target_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "iscsi_target_name", value)

    @property
    @pulumi.getter(name="targetIqn")
    def target_iqn(self) -> Optional[pulumi.Input[str]]:
        """
        iSCSI target IQN (iSCSI Qualified Name); example: "iqn.2005-03.org.iscsi:server".
        """
        return pulumi.get(self, "target_iqn")

    @target_iqn.setter
    def target_iqn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_iqn", value)


class IscsiTarget(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disk_pool_name: Optional[pulumi.Input[str]] = None,
                 iscsi_target_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 target_iqn: Optional[pulumi.Input[str]] = None,
                 tpgs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TargetPortalGroupCreateArgs']]]]] = None,
                 __props__=None):
        """
        Response for iSCSI target requests.
        API Version: 2020-03-15-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] disk_pool_name: The name of the Disk pool.
        :param pulumi.Input[str] iscsi_target_name: The name of the iSCSI target.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] target_iqn: iSCSI target IQN (iSCSI Qualified Name); example: "iqn.2005-03.org.iscsi:server".
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TargetPortalGroupCreateArgs']]]] tpgs: List of iSCSI target portal groups. Can have 1 portal group at most.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IscsiTargetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Response for iSCSI target requests.
        API Version: 2020-03-15-preview.

        :param str resource_name: The name of the resource.
        :param IscsiTargetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IscsiTargetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disk_pool_name: Optional[pulumi.Input[str]] = None,
                 iscsi_target_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 target_iqn: Optional[pulumi.Input[str]] = None,
                 tpgs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TargetPortalGroupCreateArgs']]]]] = None,
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
            __props__ = IscsiTargetArgs.__new__(IscsiTargetArgs)

            if disk_pool_name is None and not opts.urn:
                raise TypeError("Missing required property 'disk_pool_name'")
            __props__.__dict__["disk_pool_name"] = disk_pool_name
            __props__.__dict__["iscsi_target_name"] = iscsi_target_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["target_iqn"] = target_iqn
            if tpgs is None and not opts.urn:
                raise TypeError("Missing required property 'tpgs'")
            __props__.__dict__["tpgs"] = tpgs
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:storagepool:IscsiTarget"), pulumi.Alias(type_="azure-native:storagepool/v20200315preview:IscsiTarget"), pulumi.Alias(type_="azure-nextgen:storagepool/v20200315preview:IscsiTarget"), pulumi.Alias(type_="azure-native:storagepool/v20210401preview:IscsiTarget"), pulumi.Alias(type_="azure-nextgen:storagepool/v20210401preview:IscsiTarget")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(IscsiTarget, __self__).__init__(
            'azure-native:storagepool:IscsiTarget',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IscsiTarget':
        """
        Get an existing IscsiTarget resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IscsiTargetArgs.__new__(IscsiTargetArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["target_iqn"] = None
        __props__.__dict__["tpgs"] = None
        __props__.__dict__["type"] = None
        return IscsiTarget(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        State of the operation on the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Operational status of the iSCSI target.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="targetIqn")
    def target_iqn(self) -> pulumi.Output[str]:
        """
        iSCSI target IQN (iSCSI Qualified Name); example: "iqn.2005-03.org.iscsi:server".
        """
        return pulumi.get(self, "target_iqn")

    @property
    @pulumi.getter
    def tpgs(self) -> pulumi.Output[Sequence['outputs.TargetPortalGroupResponse']]:
        """
        List of iSCSI target portal groups. Can have 1 portal group at most.
        """
        return pulumi.get(self, "tpgs")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
        """
        return pulumi.get(self, "type")

