# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'EnableHelmOperator',
    'OperatorScope',
    'OperatorType',
]


class EnableHelmOperator(str, Enum):
    """
    Option to enable Helm Operator for this git configuration.
    """
    TRUE = "true"
    FALSE = "false"


class OperatorScope(str, Enum):
    """
    Scope at which the operator will be installed.
    """
    CLUSTER = "cluster"
    NAMESPACE = "namespace"


class OperatorType(str, Enum):
    """
    Type of the operator
    """
    FLUX = "Flux"
