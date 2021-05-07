# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['PolicyArgs', 'Policy']

@pulumi.input_type
class PolicyArgs:
    def __init__(__self__, *,
                 autoscaling_group_name: pulumi.Input[str],
                 adjustment_type: Optional[pulumi.Input[str]] = None,
                 cooldown: Optional[pulumi.Input[int]] = None,
                 estimated_instance_warmup: Optional[pulumi.Input[int]] = None,
                 metric_aggregation_type: Optional[pulumi.Input[str]] = None,
                 min_adjustment_magnitude: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None,
                 scaling_adjustment: Optional[pulumi.Input[int]] = None,
                 step_adjustments: Optional[pulumi.Input[Sequence[pulumi.Input['PolicyStepAdjustmentArgs']]]] = None,
                 target_tracking_configuration: Optional[pulumi.Input['PolicyTargetTrackingConfigurationArgs']] = None):
        """
        The set of arguments for constructing a Policy resource.
        :param pulumi.Input[str] autoscaling_group_name: The name of the autoscaling group.
        :param pulumi.Input[str] adjustment_type: Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
        :param pulumi.Input[int] cooldown: The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.
        :param pulumi.Input[int] estimated_instance_warmup: The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group's specified cooldown period.
        :param pulumi.Input[str] metric_aggregation_type: The aggregation type for the policy's metrics. Valid values are "Minimum", "Maximum", and "Average". Without a value, AWS will treat the aggregation type as "Average".
        :param pulumi.Input[int] min_adjustment_magnitude: Minimum value to scale by when `adjustment_type` is set to `PercentChangeInCapacity`.
        :param pulumi.Input[str] name: The name of the dimension.
        :param pulumi.Input[str] policy_type: The policy type, either "SimpleScaling", "StepScaling" or "TargetTrackingScaling". If this value isn't provided, AWS will default to "SimpleScaling."
        :param pulumi.Input[int] scaling_adjustment: The number of members by which to
               scale, when the adjustment bounds are breached. A positive value scales
               up. A negative value scales down.
        :param pulumi.Input[Sequence[pulumi.Input['PolicyStepAdjustmentArgs']]] step_adjustments: A set of adjustments that manage
               group scaling. These have the following structure:
        :param pulumi.Input['PolicyTargetTrackingConfigurationArgs'] target_tracking_configuration: A target tracking policy. These have the following structure:
        """
        pulumi.set(__self__, "autoscaling_group_name", autoscaling_group_name)
        if adjustment_type is not None:
            pulumi.set(__self__, "adjustment_type", adjustment_type)
        if cooldown is not None:
            pulumi.set(__self__, "cooldown", cooldown)
        if estimated_instance_warmup is not None:
            pulumi.set(__self__, "estimated_instance_warmup", estimated_instance_warmup)
        if metric_aggregation_type is not None:
            pulumi.set(__self__, "metric_aggregation_type", metric_aggregation_type)
        if min_adjustment_magnitude is not None:
            pulumi.set(__self__, "min_adjustment_magnitude", min_adjustment_magnitude)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if policy_type is not None:
            pulumi.set(__self__, "policy_type", policy_type)
        if scaling_adjustment is not None:
            pulumi.set(__self__, "scaling_adjustment", scaling_adjustment)
        if step_adjustments is not None:
            pulumi.set(__self__, "step_adjustments", step_adjustments)
        if target_tracking_configuration is not None:
            pulumi.set(__self__, "target_tracking_configuration", target_tracking_configuration)

    @property
    @pulumi.getter(name="autoscalingGroupName")
    def autoscaling_group_name(self) -> pulumi.Input[str]:
        """
        The name of the autoscaling group.
        """
        return pulumi.get(self, "autoscaling_group_name")

    @autoscaling_group_name.setter
    def autoscaling_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "autoscaling_group_name", value)

    @property
    @pulumi.getter(name="adjustmentType")
    def adjustment_type(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
        """
        return pulumi.get(self, "adjustment_type")

    @adjustment_type.setter
    def adjustment_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "adjustment_type", value)

    @property
    @pulumi.getter
    def cooldown(self) -> Optional[pulumi.Input[int]]:
        """
        The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.
        """
        return pulumi.get(self, "cooldown")

    @cooldown.setter
    def cooldown(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cooldown", value)

    @property
    @pulumi.getter(name="estimatedInstanceWarmup")
    def estimated_instance_warmup(self) -> Optional[pulumi.Input[int]]:
        """
        The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group's specified cooldown period.
        """
        return pulumi.get(self, "estimated_instance_warmup")

    @estimated_instance_warmup.setter
    def estimated_instance_warmup(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "estimated_instance_warmup", value)

    @property
    @pulumi.getter(name="metricAggregationType")
    def metric_aggregation_type(self) -> Optional[pulumi.Input[str]]:
        """
        The aggregation type for the policy's metrics. Valid values are "Minimum", "Maximum", and "Average". Without a value, AWS will treat the aggregation type as "Average".
        """
        return pulumi.get(self, "metric_aggregation_type")

    @metric_aggregation_type.setter
    def metric_aggregation_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_aggregation_type", value)

    @property
    @pulumi.getter(name="minAdjustmentMagnitude")
    def min_adjustment_magnitude(self) -> Optional[pulumi.Input[int]]:
        """
        Minimum value to scale by when `adjustment_type` is set to `PercentChangeInCapacity`.
        """
        return pulumi.get(self, "min_adjustment_magnitude")

    @min_adjustment_magnitude.setter
    def min_adjustment_magnitude(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_adjustment_magnitude", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the dimension.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[pulumi.Input[str]]:
        """
        The policy type, either "SimpleScaling", "StepScaling" or "TargetTrackingScaling". If this value isn't provided, AWS will default to "SimpleScaling."
        """
        return pulumi.get(self, "policy_type")

    @policy_type.setter
    def policy_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_type", value)

    @property
    @pulumi.getter(name="scalingAdjustment")
    def scaling_adjustment(self) -> Optional[pulumi.Input[int]]:
        """
        The number of members by which to
        scale, when the adjustment bounds are breached. A positive value scales
        up. A negative value scales down.
        """
        return pulumi.get(self, "scaling_adjustment")

    @scaling_adjustment.setter
    def scaling_adjustment(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "scaling_adjustment", value)

    @property
    @pulumi.getter(name="stepAdjustments")
    def step_adjustments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PolicyStepAdjustmentArgs']]]]:
        """
        A set of adjustments that manage
        group scaling. These have the following structure:
        """
        return pulumi.get(self, "step_adjustments")

    @step_adjustments.setter
    def step_adjustments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PolicyStepAdjustmentArgs']]]]):
        pulumi.set(self, "step_adjustments", value)

    @property
    @pulumi.getter(name="targetTrackingConfiguration")
    def target_tracking_configuration(self) -> Optional[pulumi.Input['PolicyTargetTrackingConfigurationArgs']]:
        """
        A target tracking policy. These have the following structure:
        """
        return pulumi.get(self, "target_tracking_configuration")

    @target_tracking_configuration.setter
    def target_tracking_configuration(self, value: Optional[pulumi.Input['PolicyTargetTrackingConfigurationArgs']]):
        pulumi.set(self, "target_tracking_configuration", value)


@pulumi.input_type
class _PolicyState:
    def __init__(__self__, *,
                 adjustment_type: Optional[pulumi.Input[str]] = None,
                 arn: Optional[pulumi.Input[str]] = None,
                 autoscaling_group_name: Optional[pulumi.Input[str]] = None,
                 cooldown: Optional[pulumi.Input[int]] = None,
                 estimated_instance_warmup: Optional[pulumi.Input[int]] = None,
                 metric_aggregation_type: Optional[pulumi.Input[str]] = None,
                 min_adjustment_magnitude: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None,
                 scaling_adjustment: Optional[pulumi.Input[int]] = None,
                 step_adjustments: Optional[pulumi.Input[Sequence[pulumi.Input['PolicyStepAdjustmentArgs']]]] = None,
                 target_tracking_configuration: Optional[pulumi.Input['PolicyTargetTrackingConfigurationArgs']] = None):
        """
        Input properties used for looking up and filtering Policy resources.
        :param pulumi.Input[str] adjustment_type: Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
        :param pulumi.Input[str] arn: The ARN assigned by AWS to the scaling policy.
        :param pulumi.Input[str] autoscaling_group_name: The name of the autoscaling group.
        :param pulumi.Input[int] cooldown: The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.
        :param pulumi.Input[int] estimated_instance_warmup: The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group's specified cooldown period.
        :param pulumi.Input[str] metric_aggregation_type: The aggregation type for the policy's metrics. Valid values are "Minimum", "Maximum", and "Average". Without a value, AWS will treat the aggregation type as "Average".
        :param pulumi.Input[int] min_adjustment_magnitude: Minimum value to scale by when `adjustment_type` is set to `PercentChangeInCapacity`.
        :param pulumi.Input[str] name: The name of the dimension.
        :param pulumi.Input[str] policy_type: The policy type, either "SimpleScaling", "StepScaling" or "TargetTrackingScaling". If this value isn't provided, AWS will default to "SimpleScaling."
        :param pulumi.Input[int] scaling_adjustment: The number of members by which to
               scale, when the adjustment bounds are breached. A positive value scales
               up. A negative value scales down.
        :param pulumi.Input[Sequence[pulumi.Input['PolicyStepAdjustmentArgs']]] step_adjustments: A set of adjustments that manage
               group scaling. These have the following structure:
        :param pulumi.Input['PolicyTargetTrackingConfigurationArgs'] target_tracking_configuration: A target tracking policy. These have the following structure:
        """
        if adjustment_type is not None:
            pulumi.set(__self__, "adjustment_type", adjustment_type)
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if autoscaling_group_name is not None:
            pulumi.set(__self__, "autoscaling_group_name", autoscaling_group_name)
        if cooldown is not None:
            pulumi.set(__self__, "cooldown", cooldown)
        if estimated_instance_warmup is not None:
            pulumi.set(__self__, "estimated_instance_warmup", estimated_instance_warmup)
        if metric_aggregation_type is not None:
            pulumi.set(__self__, "metric_aggregation_type", metric_aggregation_type)
        if min_adjustment_magnitude is not None:
            pulumi.set(__self__, "min_adjustment_magnitude", min_adjustment_magnitude)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if policy_type is not None:
            pulumi.set(__self__, "policy_type", policy_type)
        if scaling_adjustment is not None:
            pulumi.set(__self__, "scaling_adjustment", scaling_adjustment)
        if step_adjustments is not None:
            pulumi.set(__self__, "step_adjustments", step_adjustments)
        if target_tracking_configuration is not None:
            pulumi.set(__self__, "target_tracking_configuration", target_tracking_configuration)

    @property
    @pulumi.getter(name="adjustmentType")
    def adjustment_type(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
        """
        return pulumi.get(self, "adjustment_type")

    @adjustment_type.setter
    def adjustment_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "adjustment_type", value)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN assigned by AWS to the scaling policy.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="autoscalingGroupName")
    def autoscaling_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the autoscaling group.
        """
        return pulumi.get(self, "autoscaling_group_name")

    @autoscaling_group_name.setter
    def autoscaling_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "autoscaling_group_name", value)

    @property
    @pulumi.getter
    def cooldown(self) -> Optional[pulumi.Input[int]]:
        """
        The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.
        """
        return pulumi.get(self, "cooldown")

    @cooldown.setter
    def cooldown(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cooldown", value)

    @property
    @pulumi.getter(name="estimatedInstanceWarmup")
    def estimated_instance_warmup(self) -> Optional[pulumi.Input[int]]:
        """
        The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group's specified cooldown period.
        """
        return pulumi.get(self, "estimated_instance_warmup")

    @estimated_instance_warmup.setter
    def estimated_instance_warmup(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "estimated_instance_warmup", value)

    @property
    @pulumi.getter(name="metricAggregationType")
    def metric_aggregation_type(self) -> Optional[pulumi.Input[str]]:
        """
        The aggregation type for the policy's metrics. Valid values are "Minimum", "Maximum", and "Average". Without a value, AWS will treat the aggregation type as "Average".
        """
        return pulumi.get(self, "metric_aggregation_type")

    @metric_aggregation_type.setter
    def metric_aggregation_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_aggregation_type", value)

    @property
    @pulumi.getter(name="minAdjustmentMagnitude")
    def min_adjustment_magnitude(self) -> Optional[pulumi.Input[int]]:
        """
        Minimum value to scale by when `adjustment_type` is set to `PercentChangeInCapacity`.
        """
        return pulumi.get(self, "min_adjustment_magnitude")

    @min_adjustment_magnitude.setter
    def min_adjustment_magnitude(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_adjustment_magnitude", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the dimension.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[pulumi.Input[str]]:
        """
        The policy type, either "SimpleScaling", "StepScaling" or "TargetTrackingScaling". If this value isn't provided, AWS will default to "SimpleScaling."
        """
        return pulumi.get(self, "policy_type")

    @policy_type.setter
    def policy_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_type", value)

    @property
    @pulumi.getter(name="scalingAdjustment")
    def scaling_adjustment(self) -> Optional[pulumi.Input[int]]:
        """
        The number of members by which to
        scale, when the adjustment bounds are breached. A positive value scales
        up. A negative value scales down.
        """
        return pulumi.get(self, "scaling_adjustment")

    @scaling_adjustment.setter
    def scaling_adjustment(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "scaling_adjustment", value)

    @property
    @pulumi.getter(name="stepAdjustments")
    def step_adjustments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PolicyStepAdjustmentArgs']]]]:
        """
        A set of adjustments that manage
        group scaling. These have the following structure:
        """
        return pulumi.get(self, "step_adjustments")

    @step_adjustments.setter
    def step_adjustments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PolicyStepAdjustmentArgs']]]]):
        pulumi.set(self, "step_adjustments", value)

    @property
    @pulumi.getter(name="targetTrackingConfiguration")
    def target_tracking_configuration(self) -> Optional[pulumi.Input['PolicyTargetTrackingConfigurationArgs']]:
        """
        A target tracking policy. These have the following structure:
        """
        return pulumi.get(self, "target_tracking_configuration")

    @target_tracking_configuration.setter
    def target_tracking_configuration(self, value: Optional[pulumi.Input['PolicyTargetTrackingConfigurationArgs']]):
        pulumi.set(self, "target_tracking_configuration", value)


class Policy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 adjustment_type: Optional[pulumi.Input[str]] = None,
                 autoscaling_group_name: Optional[pulumi.Input[str]] = None,
                 cooldown: Optional[pulumi.Input[int]] = None,
                 estimated_instance_warmup: Optional[pulumi.Input[int]] = None,
                 metric_aggregation_type: Optional[pulumi.Input[str]] = None,
                 min_adjustment_magnitude: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None,
                 scaling_adjustment: Optional[pulumi.Input[int]] = None,
                 step_adjustments: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicyStepAdjustmentArgs']]]]] = None,
                 target_tracking_configuration: Optional[pulumi.Input[pulumi.InputType['PolicyTargetTrackingConfigurationArgs']]] = None,
                 __props__=None):
        """
        Provides an AutoScaling Scaling Policy resource.

        > **NOTE:** You may want to omit `desired_capacity` attribute from attached `autoscaling.Group`
        when using autoscaling policies. It's good practice to pick either
        [manual](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-manual-scaling.html)
        or [dynamic](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-scale-based-on-demand.html)
        (policy-based) scaling.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        bar = aws.autoscaling.Group("bar",
            availability_zones=["us-east-1a"],
            max_size=5,
            min_size=2,
            health_check_grace_period=300,
            health_check_type="ELB",
            force_delete=True,
            launch_configuration=aws_launch_configuration["foo"]["name"])
        bat = aws.autoscaling.Policy("bat",
            scaling_adjustment=4,
            adjustment_type="ChangeInCapacity",
            cooldown=300,
            autoscaling_group_name=bar.name)
        ```

        ## Import

        AutoScaling scaling policy can be imported using the role autoscaling_group_name and name separated by `/`.

        ```sh
         $ pulumi import aws:autoscaling/policy:Policy test-policy asg-name/policy-name
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] adjustment_type: Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
        :param pulumi.Input[str] autoscaling_group_name: The name of the autoscaling group.
        :param pulumi.Input[int] cooldown: The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.
        :param pulumi.Input[int] estimated_instance_warmup: The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group's specified cooldown period.
        :param pulumi.Input[str] metric_aggregation_type: The aggregation type for the policy's metrics. Valid values are "Minimum", "Maximum", and "Average". Without a value, AWS will treat the aggregation type as "Average".
        :param pulumi.Input[int] min_adjustment_magnitude: Minimum value to scale by when `adjustment_type` is set to `PercentChangeInCapacity`.
        :param pulumi.Input[str] name: The name of the dimension.
        :param pulumi.Input[str] policy_type: The policy type, either "SimpleScaling", "StepScaling" or "TargetTrackingScaling". If this value isn't provided, AWS will default to "SimpleScaling."
        :param pulumi.Input[int] scaling_adjustment: The number of members by which to
               scale, when the adjustment bounds are breached. A positive value scales
               up. A negative value scales down.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicyStepAdjustmentArgs']]]] step_adjustments: A set of adjustments that manage
               group scaling. These have the following structure:
        :param pulumi.Input[pulumi.InputType['PolicyTargetTrackingConfigurationArgs']] target_tracking_configuration: A target tracking policy. These have the following structure:
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an AutoScaling Scaling Policy resource.

        > **NOTE:** You may want to omit `desired_capacity` attribute from attached `autoscaling.Group`
        when using autoscaling policies. It's good practice to pick either
        [manual](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-manual-scaling.html)
        or [dynamic](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-scale-based-on-demand.html)
        (policy-based) scaling.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        bar = aws.autoscaling.Group("bar",
            availability_zones=["us-east-1a"],
            max_size=5,
            min_size=2,
            health_check_grace_period=300,
            health_check_type="ELB",
            force_delete=True,
            launch_configuration=aws_launch_configuration["foo"]["name"])
        bat = aws.autoscaling.Policy("bat",
            scaling_adjustment=4,
            adjustment_type="ChangeInCapacity",
            cooldown=300,
            autoscaling_group_name=bar.name)
        ```

        ## Import

        AutoScaling scaling policy can be imported using the role autoscaling_group_name and name separated by `/`.

        ```sh
         $ pulumi import aws:autoscaling/policy:Policy test-policy asg-name/policy-name
        ```

        :param str resource_name: The name of the resource.
        :param PolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 adjustment_type: Optional[pulumi.Input[str]] = None,
                 autoscaling_group_name: Optional[pulumi.Input[str]] = None,
                 cooldown: Optional[pulumi.Input[int]] = None,
                 estimated_instance_warmup: Optional[pulumi.Input[int]] = None,
                 metric_aggregation_type: Optional[pulumi.Input[str]] = None,
                 min_adjustment_magnitude: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None,
                 scaling_adjustment: Optional[pulumi.Input[int]] = None,
                 step_adjustments: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicyStepAdjustmentArgs']]]]] = None,
                 target_tracking_configuration: Optional[pulumi.Input[pulumi.InputType['PolicyTargetTrackingConfigurationArgs']]] = None,
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
            __props__ = PolicyArgs.__new__(PolicyArgs)

            __props__.__dict__["adjustment_type"] = adjustment_type
            if autoscaling_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'autoscaling_group_name'")
            __props__.__dict__["autoscaling_group_name"] = autoscaling_group_name
            __props__.__dict__["cooldown"] = cooldown
            __props__.__dict__["estimated_instance_warmup"] = estimated_instance_warmup
            __props__.__dict__["metric_aggregation_type"] = metric_aggregation_type
            __props__.__dict__["min_adjustment_magnitude"] = min_adjustment_magnitude
            __props__.__dict__["name"] = name
            __props__.__dict__["policy_type"] = policy_type
            __props__.__dict__["scaling_adjustment"] = scaling_adjustment
            __props__.__dict__["step_adjustments"] = step_adjustments
            __props__.__dict__["target_tracking_configuration"] = target_tracking_configuration
            __props__.__dict__["arn"] = None
        super(Policy, __self__).__init__(
            'aws:autoscaling/policy:Policy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            adjustment_type: Optional[pulumi.Input[str]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            autoscaling_group_name: Optional[pulumi.Input[str]] = None,
            cooldown: Optional[pulumi.Input[int]] = None,
            estimated_instance_warmup: Optional[pulumi.Input[int]] = None,
            metric_aggregation_type: Optional[pulumi.Input[str]] = None,
            min_adjustment_magnitude: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            policy_type: Optional[pulumi.Input[str]] = None,
            scaling_adjustment: Optional[pulumi.Input[int]] = None,
            step_adjustments: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicyStepAdjustmentArgs']]]]] = None,
            target_tracking_configuration: Optional[pulumi.Input[pulumi.InputType['PolicyTargetTrackingConfigurationArgs']]] = None) -> 'Policy':
        """
        Get an existing Policy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] adjustment_type: Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
        :param pulumi.Input[str] arn: The ARN assigned by AWS to the scaling policy.
        :param pulumi.Input[str] autoscaling_group_name: The name of the autoscaling group.
        :param pulumi.Input[int] cooldown: The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.
        :param pulumi.Input[int] estimated_instance_warmup: The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group's specified cooldown period.
        :param pulumi.Input[str] metric_aggregation_type: The aggregation type for the policy's metrics. Valid values are "Minimum", "Maximum", and "Average". Without a value, AWS will treat the aggregation type as "Average".
        :param pulumi.Input[int] min_adjustment_magnitude: Minimum value to scale by when `adjustment_type` is set to `PercentChangeInCapacity`.
        :param pulumi.Input[str] name: The name of the dimension.
        :param pulumi.Input[str] policy_type: The policy type, either "SimpleScaling", "StepScaling" or "TargetTrackingScaling". If this value isn't provided, AWS will default to "SimpleScaling."
        :param pulumi.Input[int] scaling_adjustment: The number of members by which to
               scale, when the adjustment bounds are breached. A positive value scales
               up. A negative value scales down.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicyStepAdjustmentArgs']]]] step_adjustments: A set of adjustments that manage
               group scaling. These have the following structure:
        :param pulumi.Input[pulumi.InputType['PolicyTargetTrackingConfigurationArgs']] target_tracking_configuration: A target tracking policy. These have the following structure:
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PolicyState.__new__(_PolicyState)

        __props__.__dict__["adjustment_type"] = adjustment_type
        __props__.__dict__["arn"] = arn
        __props__.__dict__["autoscaling_group_name"] = autoscaling_group_name
        __props__.__dict__["cooldown"] = cooldown
        __props__.__dict__["estimated_instance_warmup"] = estimated_instance_warmup
        __props__.__dict__["metric_aggregation_type"] = metric_aggregation_type
        __props__.__dict__["min_adjustment_magnitude"] = min_adjustment_magnitude
        __props__.__dict__["name"] = name
        __props__.__dict__["policy_type"] = policy_type
        __props__.__dict__["scaling_adjustment"] = scaling_adjustment
        __props__.__dict__["step_adjustments"] = step_adjustments
        __props__.__dict__["target_tracking_configuration"] = target_tracking_configuration
        return Policy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="adjustmentType")
    def adjustment_type(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
        """
        return pulumi.get(self, "adjustment_type")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN assigned by AWS to the scaling policy.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="autoscalingGroupName")
    def autoscaling_group_name(self) -> pulumi.Output[str]:
        """
        The name of the autoscaling group.
        """
        return pulumi.get(self, "autoscaling_group_name")

    @property
    @pulumi.getter
    def cooldown(self) -> pulumi.Output[Optional[int]]:
        """
        The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.
        """
        return pulumi.get(self, "cooldown")

    @property
    @pulumi.getter(name="estimatedInstanceWarmup")
    def estimated_instance_warmup(self) -> pulumi.Output[Optional[int]]:
        """
        The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group's specified cooldown period.
        """
        return pulumi.get(self, "estimated_instance_warmup")

    @property
    @pulumi.getter(name="metricAggregationType")
    def metric_aggregation_type(self) -> pulumi.Output[str]:
        """
        The aggregation type for the policy's metrics. Valid values are "Minimum", "Maximum", and "Average". Without a value, AWS will treat the aggregation type as "Average".
        """
        return pulumi.get(self, "metric_aggregation_type")

    @property
    @pulumi.getter(name="minAdjustmentMagnitude")
    def min_adjustment_magnitude(self) -> pulumi.Output[Optional[int]]:
        """
        Minimum value to scale by when `adjustment_type` is set to `PercentChangeInCapacity`.
        """
        return pulumi.get(self, "min_adjustment_magnitude")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the dimension.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Output[Optional[str]]:
        """
        The policy type, either "SimpleScaling", "StepScaling" or "TargetTrackingScaling". If this value isn't provided, AWS will default to "SimpleScaling."
        """
        return pulumi.get(self, "policy_type")

    @property
    @pulumi.getter(name="scalingAdjustment")
    def scaling_adjustment(self) -> pulumi.Output[Optional[int]]:
        """
        The number of members by which to
        scale, when the adjustment bounds are breached. A positive value scales
        up. A negative value scales down.
        """
        return pulumi.get(self, "scaling_adjustment")

    @property
    @pulumi.getter(name="stepAdjustments")
    def step_adjustments(self) -> pulumi.Output[Optional[Sequence['outputs.PolicyStepAdjustment']]]:
        """
        A set of adjustments that manage
        group scaling. These have the following structure:
        """
        return pulumi.get(self, "step_adjustments")

    @property
    @pulumi.getter(name="targetTrackingConfiguration")
    def target_tracking_configuration(self) -> pulumi.Output[Optional['outputs.PolicyTargetTrackingConfiguration']]:
        """
        A target tracking policy. These have the following structure:
        """
        return pulumi.get(self, "target_tracking_configuration")

