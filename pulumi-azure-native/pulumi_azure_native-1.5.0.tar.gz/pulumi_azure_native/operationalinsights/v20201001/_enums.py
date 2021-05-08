# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'BillingType',
    'ClusterSkuNameEnum',
    'IdentityType',
    'PublicNetworkAccessType',
    'WorkspaceEntityStatus',
    'WorkspaceSkuNameEnum',
]


class BillingType(str, Enum):
    """
    Configures whether billing will be only on the cluster or each workspace will be billed by its proportional use. This does not change the overall billing, only how it will be distributed. Default value is 'Cluster'
    """
    CLUSTER = "Cluster"
    WORKSPACES = "Workspaces"


class ClusterSkuNameEnum(str, Enum):
    """
    The name of the SKU.
    """
    CAPACITY_RESERVATION = "CapacityReservation"


class IdentityType(str, Enum):
    """
    Type of managed service identity.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    NONE = "None"


class PublicNetworkAccessType(str, Enum):
    """
    The network access type for accessing Log Analytics query.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class WorkspaceEntityStatus(str, Enum):
    """
    The provisioning state of the workspace.
    """
    CREATING = "Creating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    DELETING = "Deleting"
    PROVISIONING_ACCOUNT = "ProvisioningAccount"
    UPDATING = "Updating"


class WorkspaceSkuNameEnum(str, Enum):
    """
    The name of the SKU.
    """
    FREE = "Free"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    PER_NODE = "PerNode"
    PER_GB2018 = "PerGB2018"
    STANDALONE = "Standalone"
    CAPACITY_RESERVATION = "CapacityReservation"
    LA_CLUSTER = "LACluster"
