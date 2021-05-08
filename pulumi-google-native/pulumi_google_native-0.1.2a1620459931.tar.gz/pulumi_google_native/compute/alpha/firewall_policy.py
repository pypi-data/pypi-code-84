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

__all__ = ['FirewallPolicyArgs', 'FirewallPolicy']

@pulumi.input_type
class FirewallPolicyArgs:
    def __init__(__self__, *,
                 firewall_policy: pulumi.Input[str],
                 associations: Optional[pulumi.Input[Sequence[pulumi.Input['FirewallPolicyAssociationArgs']]]] = None,
                 creation_timestamp: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 fingerprint: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 rule_tuple_count: Optional[pulumi.Input[int]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['FirewallPolicyRuleArgs']]]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 self_link_with_id: Optional[pulumi.Input[str]] = None,
                 short_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FirewallPolicy resource.
        :param pulumi.Input[Sequence[pulumi.Input['FirewallPolicyAssociationArgs']]] associations: A list of associations that belong to this firewall policy.
        :param pulumi.Input[str] creation_timestamp: [Output Only] Creation timestamp in RFC3339 text format.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when you create the resource.
        :param pulumi.Input[str] display_name: Depreacted, please use short name instead. User-provided name of the Organization firewall plicy. The name should be unique in the organization in which the firewall policy is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input[str] fingerprint: Specifies a fingerprint for this resource, which is essentially a hash of the metadata's contents and used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update metadata. You must always provide an up-to-date fingerprint hash in order to update or change metadata, otherwise the request will fail with error 412 conditionNotMet.
               
               To see the latest fingerprint, make get() request to the firewall policy.
        :param pulumi.Input[str] id: [Output Only] The unique identifier for the resource. This identifier is defined by the server.
        :param pulumi.Input[str] kind: [Output only] Type of the resource. Always compute#firewallPolicyfor firewall policies
        :param pulumi.Input[str] name: [Output Only] Name of the resource. It is a numeric ID allocated by GCP which uniquely identifies the Firewall Policy.
        :param pulumi.Input[str] parent: [Output Only] The parent of the firewall policy.
        :param pulumi.Input[str] region: [Output Only] URL of the region where the regional firewall policy resides. This field is not applicable to global firewall policies. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.
        :param pulumi.Input[int] rule_tuple_count: [Output Only] Total count of all firewall policy rule tuples. A firewall policy can not exceed a set number of tuples.
        :param pulumi.Input[Sequence[pulumi.Input['FirewallPolicyRuleArgs']]] rules: A list of rules that belong to this policy. There must always be a default rule (rule with priority 2147483647 and match "*"). If no rules are provided when creating a firewall policy, a default rule with action "allow" will be added.
        :param pulumi.Input[str] self_link: [Output Only] Server-defined URL for the resource.
        :param pulumi.Input[str] self_link_with_id: [Output Only] Server-defined URL for this resource with the resource id.
        :param pulumi.Input[str] short_name: User-provided name of the Organization firewall plicy. The name should be unique in the organization in which the firewall policy is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        pulumi.set(__self__, "firewall_policy", firewall_policy)
        if associations is not None:
            pulumi.set(__self__, "associations", associations)
        if creation_timestamp is not None:
            pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if fingerprint is not None:
            pulumi.set(__self__, "fingerprint", fingerprint)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parent is not None:
            pulumi.set(__self__, "parent", parent)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if rule_tuple_count is not None:
            pulumi.set(__self__, "rule_tuple_count", rule_tuple_count)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)
        if self_link is not None:
            pulumi.set(__self__, "self_link", self_link)
        if self_link_with_id is not None:
            pulumi.set(__self__, "self_link_with_id", self_link_with_id)
        if short_name is not None:
            pulumi.set(__self__, "short_name", short_name)

    @property
    @pulumi.getter(name="firewallPolicy")
    def firewall_policy(self) -> pulumi.Input[str]:
        return pulumi.get(self, "firewall_policy")

    @firewall_policy.setter
    def firewall_policy(self, value: pulumi.Input[str]):
        pulumi.set(self, "firewall_policy", value)

    @property
    @pulumi.getter
    def associations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FirewallPolicyAssociationArgs']]]]:
        """
        A list of associations that belong to this firewall policy.
        """
        return pulumi.get(self, "associations")

    @associations.setter
    def associations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FirewallPolicyAssociationArgs']]]]):
        pulumi.set(self, "associations", value)

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[str]]:
        """
        [Output Only] Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "creation_timestamp", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        An optional description of this resource. Provide this property when you create the resource.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Depreacted, please use short name instead. User-provided name of the Organization firewall plicy. The name should be unique in the organization in which the firewall policy is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def fingerprint(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies a fingerprint for this resource, which is essentially a hash of the metadata's contents and used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update metadata. You must always provide an up-to-date fingerprint hash in order to update or change metadata, otherwise the request will fail with error 412 conditionNotMet.

        To see the latest fingerprint, make get() request to the firewall policy.
        """
        return pulumi.get(self, "fingerprint")

    @fingerprint.setter
    def fingerprint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fingerprint", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        [Output Only] The unique identifier for the resource. This identifier is defined by the server.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        [Output only] Type of the resource. Always compute#firewallPolicyfor firewall policies
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [Output Only] Name of the resource. It is a numeric ID allocated by GCP which uniquely identifies the Firewall Policy.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[str]]:
        """
        [Output Only] The parent of the firewall policy.
        """
        return pulumi.get(self, "parent")

    @parent.setter
    def parent(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        [Output Only] URL of the region where the regional firewall policy resides. This field is not applicable to global firewall policies. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="ruleTupleCount")
    def rule_tuple_count(self) -> Optional[pulumi.Input[int]]:
        """
        [Output Only] Total count of all firewall policy rule tuples. A firewall policy can not exceed a set number of tuples.
        """
        return pulumi.get(self, "rule_tuple_count")

    @rule_tuple_count.setter
    def rule_tuple_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "rule_tuple_count", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FirewallPolicyRuleArgs']]]]:
        """
        A list of rules that belong to this policy. There must always be a default rule (rule with priority 2147483647 and match "*"). If no rules are provided when creating a firewall policy, a default rule with action "allow" will be added.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FirewallPolicyRuleArgs']]]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[str]]:
        """
        [Output Only] Server-defined URL for the resource.
        """
        return pulumi.get(self, "self_link")

    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "self_link", value)

    @property
    @pulumi.getter(name="selfLinkWithId")
    def self_link_with_id(self) -> Optional[pulumi.Input[str]]:
        """
        [Output Only] Server-defined URL for this resource with the resource id.
        """
        return pulumi.get(self, "self_link_with_id")

    @self_link_with_id.setter
    def self_link_with_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "self_link_with_id", value)

    @property
    @pulumi.getter(name="shortName")
    def short_name(self) -> Optional[pulumi.Input[str]]:
        """
        User-provided name of the Organization firewall plicy. The name should be unique in the organization in which the firewall policy is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "short_name")

    @short_name.setter
    def short_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "short_name", value)


class FirewallPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 associations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallPolicyAssociationArgs']]]]] = None,
                 creation_timestamp: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 fingerprint: Optional[pulumi.Input[str]] = None,
                 firewall_policy: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 rule_tuple_count: Optional[pulumi.Input[int]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallPolicyRuleArgs']]]]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 self_link_with_id: Optional[pulumi.Input[str]] = None,
                 short_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new policy in the specified project using the data included in the request.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallPolicyAssociationArgs']]]] associations: A list of associations that belong to this firewall policy.
        :param pulumi.Input[str] creation_timestamp: [Output Only] Creation timestamp in RFC3339 text format.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when you create the resource.
        :param pulumi.Input[str] display_name: Depreacted, please use short name instead. User-provided name of the Organization firewall plicy. The name should be unique in the organization in which the firewall policy is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input[str] fingerprint: Specifies a fingerprint for this resource, which is essentially a hash of the metadata's contents and used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update metadata. You must always provide an up-to-date fingerprint hash in order to update or change metadata, otherwise the request will fail with error 412 conditionNotMet.
               
               To see the latest fingerprint, make get() request to the firewall policy.
        :param pulumi.Input[str] id: [Output Only] The unique identifier for the resource. This identifier is defined by the server.
        :param pulumi.Input[str] kind: [Output only] Type of the resource. Always compute#firewallPolicyfor firewall policies
        :param pulumi.Input[str] name: [Output Only] Name of the resource. It is a numeric ID allocated by GCP which uniquely identifies the Firewall Policy.
        :param pulumi.Input[str] parent: [Output Only] The parent of the firewall policy.
        :param pulumi.Input[str] region: [Output Only] URL of the region where the regional firewall policy resides. This field is not applicable to global firewall policies. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.
        :param pulumi.Input[int] rule_tuple_count: [Output Only] Total count of all firewall policy rule tuples. A firewall policy can not exceed a set number of tuples.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallPolicyRuleArgs']]]] rules: A list of rules that belong to this policy. There must always be a default rule (rule with priority 2147483647 and match "*"). If no rules are provided when creating a firewall policy, a default rule with action "allow" will be added.
        :param pulumi.Input[str] self_link: [Output Only] Server-defined URL for the resource.
        :param pulumi.Input[str] self_link_with_id: [Output Only] Server-defined URL for this resource with the resource id.
        :param pulumi.Input[str] short_name: User-provided name of the Organization firewall plicy. The name should be unique in the organization in which the firewall policy is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FirewallPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new policy in the specified project using the data included in the request.

        :param str resource_name: The name of the resource.
        :param FirewallPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FirewallPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 associations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallPolicyAssociationArgs']]]]] = None,
                 creation_timestamp: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 fingerprint: Optional[pulumi.Input[str]] = None,
                 firewall_policy: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 rule_tuple_count: Optional[pulumi.Input[int]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallPolicyRuleArgs']]]]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 self_link_with_id: Optional[pulumi.Input[str]] = None,
                 short_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = FirewallPolicyArgs.__new__(FirewallPolicyArgs)

            __props__.__dict__["associations"] = associations
            __props__.__dict__["creation_timestamp"] = creation_timestamp
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["fingerprint"] = fingerprint
            if firewall_policy is None and not opts.urn:
                raise TypeError("Missing required property 'firewall_policy'")
            __props__.__dict__["firewall_policy"] = firewall_policy
            __props__.__dict__["id"] = id
            __props__.__dict__["kind"] = kind
            __props__.__dict__["name"] = name
            __props__.__dict__["parent"] = parent
            __props__.__dict__["region"] = region
            __props__.__dict__["rule_tuple_count"] = rule_tuple_count
            __props__.__dict__["rules"] = rules
            __props__.__dict__["self_link"] = self_link
            __props__.__dict__["self_link_with_id"] = self_link_with_id
            __props__.__dict__["short_name"] = short_name
        super(FirewallPolicy, __self__).__init__(
            'google-native:compute/alpha:FirewallPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FirewallPolicy':
        """
        Get an existing FirewallPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FirewallPolicyArgs.__new__(FirewallPolicyArgs)

        __props__.__dict__["associations"] = None
        __props__.__dict__["creation_timestamp"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["fingerprint"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parent"] = None
        __props__.__dict__["region"] = None
        __props__.__dict__["rule_tuple_count"] = None
        __props__.__dict__["rules"] = None
        __props__.__dict__["self_link"] = None
        __props__.__dict__["self_link_with_id"] = None
        __props__.__dict__["short_name"] = None
        return FirewallPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def associations(self) -> pulumi.Output[Sequence['outputs.FirewallPolicyAssociationResponse']]:
        """
        A list of associations that belong to this firewall policy.
        """
        return pulumi.get(self, "associations")

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[str]:
        """
        [Output Only] Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        An optional description of this resource. Provide this property when you create the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Depreacted, please use short name instead. User-provided name of the Organization firewall plicy. The name should be unique in the organization in which the firewall policy is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[str]:
        """
        Specifies a fingerprint for this resource, which is essentially a hash of the metadata's contents and used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update metadata. You must always provide an up-to-date fingerprint hash in order to update or change metadata, otherwise the request will fail with error 412 conditionNotMet.

        To see the latest fingerprint, make get() request to the firewall policy.
        """
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        [Output only] Type of the resource. Always compute#firewallPolicyfor firewall policies
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        [Output Only] Name of the resource. It is a numeric ID allocated by GCP which uniquely identifies the Firewall Policy.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parent(self) -> pulumi.Output[str]:
        """
        [Output Only] The parent of the firewall policy.
        """
        return pulumi.get(self, "parent")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        [Output Only] URL of the region where the regional firewall policy resides. This field is not applicable to global firewall policies. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="ruleTupleCount")
    def rule_tuple_count(self) -> pulumi.Output[int]:
        """
        [Output Only] Total count of all firewall policy rule tuples. A firewall policy can not exceed a set number of tuples.
        """
        return pulumi.get(self, "rule_tuple_count")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Sequence['outputs.FirewallPolicyRuleResponse']]:
        """
        A list of rules that belong to this policy. There must always be a default rule (rule with priority 2147483647 and match "*"). If no rules are provided when creating a firewall policy, a default rule with action "allow" will be added.
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        [Output Only] Server-defined URL for the resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="selfLinkWithId")
    def self_link_with_id(self) -> pulumi.Output[str]:
        """
        [Output Only] Server-defined URL for this resource with the resource id.
        """
        return pulumi.get(self, "self_link_with_id")

    @property
    @pulumi.getter(name="shortName")
    def short_name(self) -> pulumi.Output[str]:
        """
        User-provided name of the Organization firewall plicy. The name should be unique in the organization in which the firewall policy is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "short_name")

