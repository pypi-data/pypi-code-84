# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'LifecyclePolicyPolicyDetails',
    'LifecyclePolicyPolicyDetailsSchedule',
    'LifecyclePolicyPolicyDetailsScheduleCreateRule',
    'LifecyclePolicyPolicyDetailsScheduleRetainRule',
]

@pulumi.output_type
class LifecyclePolicyPolicyDetails(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "resourceTypes":
            suggest = "resource_types"
        elif key == "targetTags":
            suggest = "target_tags"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LifecyclePolicyPolicyDetails. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LifecyclePolicyPolicyDetails.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LifecyclePolicyPolicyDetails.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 resource_types: Sequence[str],
                 schedules: Sequence['outputs.LifecyclePolicyPolicyDetailsSchedule'],
                 target_tags: Mapping[str, str]):
        """
        :param Sequence[str] resource_types: A list of resource types that should be targeted by the lifecycle policy. `VOLUME` is currently the only allowed value.
        :param Sequence['LifecyclePolicyPolicyDetailsScheduleArgs'] schedules: See the `schedule` configuration block.
        :param Mapping[str, str] target_tags: A map of tag keys and their values. Any resources that match the `resource_types` and are tagged with _any_ of these tags will be targeted.
        """
        pulumi.set(__self__, "resource_types", resource_types)
        pulumi.set(__self__, "schedules", schedules)
        pulumi.set(__self__, "target_tags", target_tags)

    @property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Sequence[str]:
        """
        A list of resource types that should be targeted by the lifecycle policy. `VOLUME` is currently the only allowed value.
        """
        return pulumi.get(self, "resource_types")

    @property
    @pulumi.getter
    def schedules(self) -> Sequence['outputs.LifecyclePolicyPolicyDetailsSchedule']:
        """
        See the `schedule` configuration block.
        """
        return pulumi.get(self, "schedules")

    @property
    @pulumi.getter(name="targetTags")
    def target_tags(self) -> Mapping[str, str]:
        """
        A map of tag keys and their values. Any resources that match the `resource_types` and are tagged with _any_ of these tags will be targeted.
        """
        return pulumi.get(self, "target_tags")


@pulumi.output_type
class LifecyclePolicyPolicyDetailsSchedule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createRule":
            suggest = "create_rule"
        elif key == "retainRule":
            suggest = "retain_rule"
        elif key == "copyTags":
            suggest = "copy_tags"
        elif key == "tagsToAdd":
            suggest = "tags_to_add"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LifecyclePolicyPolicyDetailsSchedule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LifecyclePolicyPolicyDetailsSchedule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LifecyclePolicyPolicyDetailsSchedule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 create_rule: 'outputs.LifecyclePolicyPolicyDetailsScheduleCreateRule',
                 name: str,
                 retain_rule: 'outputs.LifecyclePolicyPolicyDetailsScheduleRetainRule',
                 copy_tags: Optional[bool] = None,
                 tags_to_add: Optional[Mapping[str, str]] = None):
        """
        :param 'LifecyclePolicyPolicyDetailsScheduleCreateRuleArgs' create_rule: See the `create_rule` block. Max of 1 per schedule.
        :param str name: A name for the schedule.
        :param 'LifecyclePolicyPolicyDetailsScheduleRetainRuleArgs' retain_rule: See the `retain_rule` block. Max of 1 per schedule.
        :param bool copy_tags: Copy all user-defined tags on a source volume to snapshots of the volume created by this policy.
        :param Mapping[str, str] tags_to_add: A map of tag keys and their values. DLM lifecycle policies will already tag the snapshot with the tags on the volume. This configuration adds extra tags on top of these.
        """
        pulumi.set(__self__, "create_rule", create_rule)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "retain_rule", retain_rule)
        if copy_tags is not None:
            pulumi.set(__self__, "copy_tags", copy_tags)
        if tags_to_add is not None:
            pulumi.set(__self__, "tags_to_add", tags_to_add)

    @property
    @pulumi.getter(name="createRule")
    def create_rule(self) -> 'outputs.LifecyclePolicyPolicyDetailsScheduleCreateRule':
        """
        See the `create_rule` block. Max of 1 per schedule.
        """
        return pulumi.get(self, "create_rule")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        A name for the schedule.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="retainRule")
    def retain_rule(self) -> 'outputs.LifecyclePolicyPolicyDetailsScheduleRetainRule':
        """
        See the `retain_rule` block. Max of 1 per schedule.
        """
        return pulumi.get(self, "retain_rule")

    @property
    @pulumi.getter(name="copyTags")
    def copy_tags(self) -> Optional[bool]:
        """
        Copy all user-defined tags on a source volume to snapshots of the volume created by this policy.
        """
        return pulumi.get(self, "copy_tags")

    @property
    @pulumi.getter(name="tagsToAdd")
    def tags_to_add(self) -> Optional[Mapping[str, str]]:
        """
        A map of tag keys and their values. DLM lifecycle policies will already tag the snapshot with the tags on the volume. This configuration adds extra tags on top of these.
        """
        return pulumi.get(self, "tags_to_add")


@pulumi.output_type
class LifecyclePolicyPolicyDetailsScheduleCreateRule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "intervalUnit":
            suggest = "interval_unit"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LifecyclePolicyPolicyDetailsScheduleCreateRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LifecyclePolicyPolicyDetailsScheduleCreateRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LifecyclePolicyPolicyDetailsScheduleCreateRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 interval: int,
                 interval_unit: Optional[str] = None,
                 times: Optional[str] = None):
        """
        :param int interval: How often this lifecycle policy should be evaluated. `1`, `2`,`3`,`4`,`6`,`8`,`12` or `24` are valid values.
        :param str interval_unit: The unit for how often the lifecycle policy should be evaluated. `HOURS` is currently the only allowed value and also the default value.
        :param str times: A list of times in 24 hour clock format that sets when the lifecycle policy should be evaluated. Max of 1.
        """
        pulumi.set(__self__, "interval", interval)
        if interval_unit is not None:
            pulumi.set(__self__, "interval_unit", interval_unit)
        if times is not None:
            pulumi.set(__self__, "times", times)

    @property
    @pulumi.getter
    def interval(self) -> int:
        """
        How often this lifecycle policy should be evaluated. `1`, `2`,`3`,`4`,`6`,`8`,`12` or `24` are valid values.
        """
        return pulumi.get(self, "interval")

    @property
    @pulumi.getter(name="intervalUnit")
    def interval_unit(self) -> Optional[str]:
        """
        The unit for how often the lifecycle policy should be evaluated. `HOURS` is currently the only allowed value and also the default value.
        """
        return pulumi.get(self, "interval_unit")

    @property
    @pulumi.getter
    def times(self) -> Optional[str]:
        """
        A list of times in 24 hour clock format that sets when the lifecycle policy should be evaluated. Max of 1.
        """
        return pulumi.get(self, "times")


@pulumi.output_type
class LifecyclePolicyPolicyDetailsScheduleRetainRule(dict):
    def __init__(__self__, *,
                 count: int):
        """
        :param int count: How many snapshots to keep. Must be an integer between 1 and 1000.
        """
        pulumi.set(__self__, "count", count)

    @property
    @pulumi.getter
    def count(self) -> int:
        """
        How many snapshots to keep. Must be an integer between 1 and 1000.
        """
        return pulumi.get(self, "count")


