# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'CostAllocationPolicyType',
    'CostAllocationResourceType',
    'RuleStatus',
]


class CostAllocationPolicyType(str, Enum):
    """
    Method of cost allocation for the rule
    """
    FIXED_PROPORTION = "FixedProportion"


class CostAllocationResourceType(str, Enum):
    """
    Type of resources contained in this cost allocation rule
    """
    DIMENSION = "Dimension"
    TAG = "Tag"


class RuleStatus(str, Enum):
    """
    Status of the rule
    """
    NOT_ACTIVE = "NotActive"
    ACTIVE = "Active"
    PROCESSING = "Processing"
