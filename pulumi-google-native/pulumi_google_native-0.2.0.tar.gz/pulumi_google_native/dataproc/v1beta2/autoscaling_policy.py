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

__all__ = ['AutoscalingPolicyArgs', 'AutoscalingPolicy']

@pulumi.input_type
class AutoscalingPolicyArgs:
    def __init__(__self__, *,
                 autoscaling_policies_id: pulumi.Input[str],
                 locations_id: pulumi.Input[str],
                 projects_id: pulumi.Input[str],
                 basic_algorithm: Optional[pulumi.Input['BasicAutoscalingAlgorithmArgs']] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 secondary_worker_config: Optional[pulumi.Input['InstanceGroupAutoscalingPolicyConfigArgs']] = None,
                 worker_config: Optional[pulumi.Input['InstanceGroupAutoscalingPolicyConfigArgs']] = None):
        """
        The set of arguments for constructing a AutoscalingPolicy resource.
        :param pulumi.Input[str] id: Required. The policy id.The id must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). Cannot begin or end with underscore or hyphen. Must consist of between 3 and 50 characters.
        :param pulumi.Input['InstanceGroupAutoscalingPolicyConfigArgs'] secondary_worker_config: Optional. Describes how the autoscaler will operate for secondary workers.
        :param pulumi.Input['InstanceGroupAutoscalingPolicyConfigArgs'] worker_config: Required. Describes how the autoscaler will operate for primary workers.
        """
        pulumi.set(__self__, "autoscaling_policies_id", autoscaling_policies_id)
        pulumi.set(__self__, "locations_id", locations_id)
        pulumi.set(__self__, "projects_id", projects_id)
        if basic_algorithm is not None:
            pulumi.set(__self__, "basic_algorithm", basic_algorithm)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if secondary_worker_config is not None:
            pulumi.set(__self__, "secondary_worker_config", secondary_worker_config)
        if worker_config is not None:
            pulumi.set(__self__, "worker_config", worker_config)

    @property
    @pulumi.getter(name="autoscalingPoliciesId")
    def autoscaling_policies_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "autoscaling_policies_id")

    @autoscaling_policies_id.setter
    def autoscaling_policies_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "autoscaling_policies_id", value)

    @property
    @pulumi.getter(name="locationsId")
    def locations_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "locations_id")

    @locations_id.setter
    def locations_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "locations_id", value)

    @property
    @pulumi.getter(name="projectsId")
    def projects_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "projects_id")

    @projects_id.setter
    def projects_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "projects_id", value)

    @property
    @pulumi.getter(name="basicAlgorithm")
    def basic_algorithm(self) -> Optional[pulumi.Input['BasicAutoscalingAlgorithmArgs']]:
        return pulumi.get(self, "basic_algorithm")

    @basic_algorithm.setter
    def basic_algorithm(self, value: Optional[pulumi.Input['BasicAutoscalingAlgorithmArgs']]):
        pulumi.set(self, "basic_algorithm", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Required. The policy id.The id must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). Cannot begin or end with underscore or hyphen. Must consist of between 3 and 50 characters.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="secondaryWorkerConfig")
    def secondary_worker_config(self) -> Optional[pulumi.Input['InstanceGroupAutoscalingPolicyConfigArgs']]:
        """
        Optional. Describes how the autoscaler will operate for secondary workers.
        """
        return pulumi.get(self, "secondary_worker_config")

    @secondary_worker_config.setter
    def secondary_worker_config(self, value: Optional[pulumi.Input['InstanceGroupAutoscalingPolicyConfigArgs']]):
        pulumi.set(self, "secondary_worker_config", value)

    @property
    @pulumi.getter(name="workerConfig")
    def worker_config(self) -> Optional[pulumi.Input['InstanceGroupAutoscalingPolicyConfigArgs']]:
        """
        Required. Describes how the autoscaler will operate for primary workers.
        """
        return pulumi.get(self, "worker_config")

    @worker_config.setter
    def worker_config(self, value: Optional[pulumi.Input['InstanceGroupAutoscalingPolicyConfigArgs']]):
        pulumi.set(self, "worker_config", value)


class AutoscalingPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 autoscaling_policies_id: Optional[pulumi.Input[str]] = None,
                 basic_algorithm: Optional[pulumi.Input[pulumi.InputType['BasicAutoscalingAlgorithmArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 secondary_worker_config: Optional[pulumi.Input[pulumi.InputType['InstanceGroupAutoscalingPolicyConfigArgs']]] = None,
                 worker_config: Optional[pulumi.Input[pulumi.InputType['InstanceGroupAutoscalingPolicyConfigArgs']]] = None,
                 __props__=None):
        """
        Creates new autoscaling policy.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] id: Required. The policy id.The id must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). Cannot begin or end with underscore or hyphen. Must consist of between 3 and 50 characters.
        :param pulumi.Input[pulumi.InputType['InstanceGroupAutoscalingPolicyConfigArgs']] secondary_worker_config: Optional. Describes how the autoscaler will operate for secondary workers.
        :param pulumi.Input[pulumi.InputType['InstanceGroupAutoscalingPolicyConfigArgs']] worker_config: Required. Describes how the autoscaler will operate for primary workers.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AutoscalingPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates new autoscaling policy.

        :param str resource_name: The name of the resource.
        :param AutoscalingPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AutoscalingPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 autoscaling_policies_id: Optional[pulumi.Input[str]] = None,
                 basic_algorithm: Optional[pulumi.Input[pulumi.InputType['BasicAutoscalingAlgorithmArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 secondary_worker_config: Optional[pulumi.Input[pulumi.InputType['InstanceGroupAutoscalingPolicyConfigArgs']]] = None,
                 worker_config: Optional[pulumi.Input[pulumi.InputType['InstanceGroupAutoscalingPolicyConfigArgs']]] = None,
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
            __props__ = AutoscalingPolicyArgs.__new__(AutoscalingPolicyArgs)

            if autoscaling_policies_id is None and not opts.urn:
                raise TypeError("Missing required property 'autoscaling_policies_id'")
            __props__.__dict__["autoscaling_policies_id"] = autoscaling_policies_id
            __props__.__dict__["basic_algorithm"] = basic_algorithm
            __props__.__dict__["id"] = id
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__.__dict__["locations_id"] = locations_id
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__.__dict__["projects_id"] = projects_id
            __props__.__dict__["secondary_worker_config"] = secondary_worker_config
            __props__.__dict__["worker_config"] = worker_config
            __props__.__dict__["name"] = None
        super(AutoscalingPolicy, __self__).__init__(
            'google-native:dataproc/v1beta2:AutoscalingPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AutoscalingPolicy':
        """
        Get an existing AutoscalingPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AutoscalingPolicyArgs.__new__(AutoscalingPolicyArgs)

        __props__.__dict__["basic_algorithm"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["secondary_worker_config"] = None
        __props__.__dict__["worker_config"] = None
        return AutoscalingPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="basicAlgorithm")
    def basic_algorithm(self) -> pulumi.Output['outputs.BasicAutoscalingAlgorithmResponse']:
        return pulumi.get(self, "basic_algorithm")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The "resource name" of the autoscaling policy, as described in https://cloud.google.com/apis/design/resource_names. For projects.regions.autoscalingPolicies, the resource name of the policy has the following format: projects/{project_id}/regions/{region}/autoscalingPolicies/{policy_id} For projects.locations.autoscalingPolicies, the resource name of the policy has the following format: projects/{project_id}/locations/{location}/autoscalingPolicies/{policy_id}
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="secondaryWorkerConfig")
    def secondary_worker_config(self) -> pulumi.Output['outputs.InstanceGroupAutoscalingPolicyConfigResponse']:
        """
        Optional. Describes how the autoscaler will operate for secondary workers.
        """
        return pulumi.get(self, "secondary_worker_config")

    @property
    @pulumi.getter(name="workerConfig")
    def worker_config(self) -> pulumi.Output['outputs.InstanceGroupAutoscalingPolicyConfigResponse']:
        """
        Required. Describes how the autoscaler will operate for primary workers.
        """
        return pulumi.get(self, "worker_config")

