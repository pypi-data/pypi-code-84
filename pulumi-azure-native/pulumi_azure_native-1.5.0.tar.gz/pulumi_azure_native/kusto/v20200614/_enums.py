# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AzureSkuName',
    'AzureSkuTier',
    'ClusterPrincipalRole',
    'DataConnectionKind',
    'DatabasePrincipalRole',
    'DefaultPrincipalsModificationKind',
    'IdentityType',
    'Kind',
    'PrincipalType',
]


class AzureSkuName(str, Enum):
    """
    SKU name.
    """
    STANDARD_DS13_V2_1_T_B_PS = "Standard_DS13_v2+1TB_PS"
    STANDARD_DS13_V2_2_T_B_PS = "Standard_DS13_v2+2TB_PS"
    STANDARD_DS14_V2_3_T_B_PS = "Standard_DS14_v2+3TB_PS"
    STANDARD_DS14_V2_4_T_B_PS = "Standard_DS14_v2+4TB_PS"
    STANDARD_D13_V2 = "Standard_D13_v2"
    STANDARD_D14_V2 = "Standard_D14_v2"
    STANDARD_L8S = "Standard_L8s"
    STANDARD_L16S = "Standard_L16s"
    STANDARD_D11_V2 = "Standard_D11_v2"
    STANDARD_D12_V2 = "Standard_D12_v2"
    STANDARD_L4S = "Standard_L4s"
    DEV_NO_SL_A_STANDARD_D11_V2 = "Dev(No SLA)_Standard_D11_v2"
    STANDARD_E2A_V4 = "Standard_E2a_v4"
    STANDARD_E4A_V4 = "Standard_E4a_v4"
    STANDARD_E8A_V4 = "Standard_E8a_v4"
    STANDARD_E16A_V4 = "Standard_E16a_v4"
    STANDARD_E8AS_V4_1_T_B_PS = "Standard_E8as_v4+1TB_PS"
    STANDARD_E8AS_V4_2_T_B_PS = "Standard_E8as_v4+2TB_PS"
    STANDARD_E16AS_V4_3_T_B_PS = "Standard_E16as_v4+3TB_PS"
    STANDARD_E16AS_V4_4_T_B_PS = "Standard_E16as_v4+4TB_PS"
    DEV_NO_SL_A_STANDARD_E2A_V4 = "Dev(No SLA)_Standard_E2a_v4"


class AzureSkuTier(str, Enum):
    """
    SKU tier.
    """
    BASIC = "Basic"
    STANDARD = "Standard"


class ClusterPrincipalRole(str, Enum):
    """
    Cluster principal role.
    """
    ALL_DATABASES_ADMIN = "AllDatabasesAdmin"
    ALL_DATABASES_VIEWER = "AllDatabasesViewer"


class DataConnectionKind(str, Enum):
    """
    Kind of the endpoint for the data connection
    """
    EVENT_HUB = "EventHub"
    EVENT_GRID = "EventGrid"
    IOT_HUB = "IotHub"


class DatabasePrincipalRole(str, Enum):
    """
    Database principal role.
    """
    ADMIN = "Admin"
    INGESTOR = "Ingestor"
    MONITOR = "Monitor"
    USER = "User"
    UNRESTRICTED_VIEWERS = "UnrestrictedViewers"
    VIEWER = "Viewer"


class DefaultPrincipalsModificationKind(str, Enum):
    """
    The default principals modification kind
    """
    UNION = "Union"
    REPLACE = "Replace"
    NONE = "None"


class IdentityType(str, Enum):
    """
    The identity type.
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"


class Kind(str, Enum):
    """
    Kind of the database
    """
    READ_WRITE = "ReadWrite"
    READ_ONLY_FOLLOWING = "ReadOnlyFollowing"


class PrincipalType(str, Enum):
    """
    Principal type.
    """
    APP = "App"
    GROUP = "Group"
    USER = "User"
