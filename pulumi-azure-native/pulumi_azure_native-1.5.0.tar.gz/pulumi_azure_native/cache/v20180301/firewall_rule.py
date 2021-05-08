# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['FirewallRuleArgs', 'FirewallRule']

@pulumi.input_type
class FirewallRuleArgs:
    def __init__(__self__, *,
                 cache_name: pulumi.Input[str],
                 end_ip: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 start_ip: pulumi.Input[str],
                 rule_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FirewallRule resource.
        :param pulumi.Input[str] cache_name: The name of the Redis cache.
        :param pulumi.Input[str] end_ip: highest IP address included in the range
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] start_ip: lowest IP address included in the range
        :param pulumi.Input[str] rule_name: The name of the firewall rule.
        """
        pulumi.set(__self__, "cache_name", cache_name)
        pulumi.set(__self__, "end_ip", end_ip)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "start_ip", start_ip)
        if rule_name is not None:
            pulumi.set(__self__, "rule_name", rule_name)

    @property
    @pulumi.getter(name="cacheName")
    def cache_name(self) -> pulumi.Input[str]:
        """
        The name of the Redis cache.
        """
        return pulumi.get(self, "cache_name")

    @cache_name.setter
    def cache_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cache_name", value)

    @property
    @pulumi.getter(name="endIP")
    def end_ip(self) -> pulumi.Input[str]:
        """
        highest IP address included in the range
        """
        return pulumi.get(self, "end_ip")

    @end_ip.setter
    def end_ip(self, value: pulumi.Input[str]):
        pulumi.set(self, "end_ip", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="startIP")
    def start_ip(self) -> pulumi.Input[str]:
        """
        lowest IP address included in the range
        """
        return pulumi.get(self, "start_ip")

    @start_ip.setter
    def start_ip(self, value: pulumi.Input[str]):
        pulumi.set(self, "start_ip", value)

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the firewall rule.
        """
        return pulumi.get(self, "rule_name")

    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rule_name", value)


class FirewallRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cache_name: Optional[pulumi.Input[str]] = None,
                 end_ip: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 start_ip: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A firewall rule on a redis cache has a name, and describes a contiguous range of IP addresses permitted to connect

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cache_name: The name of the Redis cache.
        :param pulumi.Input[str] end_ip: highest IP address included in the range
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] rule_name: The name of the firewall rule.
        :param pulumi.Input[str] start_ip: lowest IP address included in the range
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FirewallRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A firewall rule on a redis cache has a name, and describes a contiguous range of IP addresses permitted to connect

        :param str resource_name: The name of the resource.
        :param FirewallRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FirewallRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cache_name: Optional[pulumi.Input[str]] = None,
                 end_ip: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 start_ip: Optional[pulumi.Input[str]] = None,
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
            __props__ = FirewallRuleArgs.__new__(FirewallRuleArgs)

            if cache_name is None and not opts.urn:
                raise TypeError("Missing required property 'cache_name'")
            __props__.__dict__["cache_name"] = cache_name
            if end_ip is None and not opts.urn:
                raise TypeError("Missing required property 'end_ip'")
            __props__.__dict__["end_ip"] = end_ip
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["rule_name"] = rule_name
            if start_ip is None and not opts.urn:
                raise TypeError("Missing required property 'start_ip'")
            __props__.__dict__["start_ip"] = start_ip
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:cache/v20180301:FirewallRule"), pulumi.Alias(type_="azure-native:cache:FirewallRule"), pulumi.Alias(type_="azure-nextgen:cache:FirewallRule"), pulumi.Alias(type_="azure-native:cache/v20160401:FirewallRule"), pulumi.Alias(type_="azure-nextgen:cache/v20160401:FirewallRule"), pulumi.Alias(type_="azure-native:cache/v20170201:FirewallRule"), pulumi.Alias(type_="azure-nextgen:cache/v20170201:FirewallRule"), pulumi.Alias(type_="azure-native:cache/v20171001:FirewallRule"), pulumi.Alias(type_="azure-nextgen:cache/v20171001:FirewallRule"), pulumi.Alias(type_="azure-native:cache/v20190701:FirewallRule"), pulumi.Alias(type_="azure-nextgen:cache/v20190701:FirewallRule"), pulumi.Alias(type_="azure-native:cache/v20200601:FirewallRule"), pulumi.Alias(type_="azure-nextgen:cache/v20200601:FirewallRule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(FirewallRule, __self__).__init__(
            'azure-native:cache/v20180301:FirewallRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FirewallRule':
        """
        Get an existing FirewallRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FirewallRuleArgs.__new__(FirewallRuleArgs)

        __props__.__dict__["end_ip"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["start_ip"] = None
        __props__.__dict__["type"] = None
        return FirewallRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="endIP")
    def end_ip(self) -> pulumi.Output[str]:
        """
        highest IP address included in the range
        """
        return pulumi.get(self, "end_ip")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="startIP")
    def start_ip(self) -> pulumi.Output[str]:
        """
        lowest IP address included in the range
        """
        return pulumi.get(self, "start_ip")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

