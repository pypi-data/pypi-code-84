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

__all__ = ['ResponsePolicyArgs', 'ResponsePolicy']

@pulumi.input_type
class ResponsePolicyArgs:
    def __init__(__self__, *,
                 project: pulumi.Input[str],
                 response_policy: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 gke_clusters: Optional[pulumi.Input[Sequence[pulumi.Input['ResponsePolicyGKEClusterArgs']]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 networks: Optional[pulumi.Input[Sequence[pulumi.Input['ResponsePolicyNetworkArgs']]]] = None,
                 response_policy_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ResponsePolicy resource.
        :param pulumi.Input[str] description: User-provided description for this Response Policy.
        :param pulumi.Input[Sequence[pulumi.Input['ResponsePolicyGKEClusterArgs']]] gke_clusters: The list of Google Kubernetes Engine clusters to which this response policy is applied.
        :param pulumi.Input[str] id: Unique identifier for the resource; defined by the server (output only).
        :param pulumi.Input[Sequence[pulumi.Input['ResponsePolicyNetworkArgs']]] networks: List of network names specifying networks to which this policy is applied.
        :param pulumi.Input[str] response_policy_name: User assigned name for this Response Policy.
        """
        pulumi.set(__self__, "project", project)
        pulumi.set(__self__, "response_policy", response_policy)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if gke_clusters is not None:
            pulumi.set(__self__, "gke_clusters", gke_clusters)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if networks is not None:
            pulumi.set(__self__, "networks", networks)
        if response_policy_name is not None:
            pulumi.set(__self__, "response_policy_name", response_policy_name)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="responsePolicy")
    def response_policy(self) -> pulumi.Input[str]:
        return pulumi.get(self, "response_policy")

    @response_policy.setter
    def response_policy(self, value: pulumi.Input[str]):
        pulumi.set(self, "response_policy", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        User-provided description for this Response Policy.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="gkeClusters")
    def gke_clusters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ResponsePolicyGKEClusterArgs']]]]:
        """
        The list of Google Kubernetes Engine clusters to which this response policy is applied.
        """
        return pulumi.get(self, "gke_clusters")

    @gke_clusters.setter
    def gke_clusters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ResponsePolicyGKEClusterArgs']]]]):
        pulumi.set(self, "gke_clusters", value)

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
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def networks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ResponsePolicyNetworkArgs']]]]:
        """
        List of network names specifying networks to which this policy is applied.
        """
        return pulumi.get(self, "networks")

    @networks.setter
    def networks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ResponsePolicyNetworkArgs']]]]):
        pulumi.set(self, "networks", value)

    @property
    @pulumi.getter(name="responsePolicyName")
    def response_policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        User assigned name for this Response Policy.
        """
        return pulumi.get(self, "response_policy_name")

    @response_policy_name.setter
    def response_policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "response_policy_name", value)


class ResponsePolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 gke_clusters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResponsePolicyGKEClusterArgs']]]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 networks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResponsePolicyNetworkArgs']]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 response_policy: Optional[pulumi.Input[str]] = None,
                 response_policy_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new Response Policy

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: User-provided description for this Response Policy.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResponsePolicyGKEClusterArgs']]]] gke_clusters: The list of Google Kubernetes Engine clusters to which this response policy is applied.
        :param pulumi.Input[str] id: Unique identifier for the resource; defined by the server (output only).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResponsePolicyNetworkArgs']]]] networks: List of network names specifying networks to which this policy is applied.
        :param pulumi.Input[str] response_policy_name: User assigned name for this Response Policy.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ResponsePolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new Response Policy

        :param str resource_name: The name of the resource.
        :param ResponsePolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ResponsePolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 gke_clusters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResponsePolicyGKEClusterArgs']]]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 networks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResponsePolicyNetworkArgs']]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 response_policy: Optional[pulumi.Input[str]] = None,
                 response_policy_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = ResponsePolicyArgs.__new__(ResponsePolicyArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["gke_clusters"] = gke_clusters
            __props__.__dict__["id"] = id
            __props__.__dict__["kind"] = kind
            __props__.__dict__["networks"] = networks
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            if response_policy is None and not opts.urn:
                raise TypeError("Missing required property 'response_policy'")
            __props__.__dict__["response_policy"] = response_policy
            __props__.__dict__["response_policy_name"] = response_policy_name
        super(ResponsePolicy, __self__).__init__(
            'google-native:dns/v1beta2:ResponsePolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ResponsePolicy':
        """
        Get an existing ResponsePolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ResponsePolicyArgs.__new__(ResponsePolicyArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["gke_clusters"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["networks"] = None
        __props__.__dict__["response_policy_name"] = None
        return ResponsePolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        User-provided description for this Response Policy.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="gkeClusters")
    def gke_clusters(self) -> pulumi.Output[Sequence['outputs.ResponsePolicyGKEClusterResponse']]:
        """
        The list of Google Kubernetes Engine clusters to which this response policy is applied.
        """
        return pulumi.get(self, "gke_clusters")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def networks(self) -> pulumi.Output[Sequence['outputs.ResponsePolicyNetworkResponse']]:
        """
        List of network names specifying networks to which this policy is applied.
        """
        return pulumi.get(self, "networks")

    @property
    @pulumi.getter(name="responsePolicyName")
    def response_policy_name(self) -> pulumi.Output[str]:
        """
        User assigned name for this Response Policy.
        """
        return pulumi.get(self, "response_policy_name")

