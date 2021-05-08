# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AlertRuleKind',
    'CaseSeverity',
    'DataConnectorKind',
    'IncidentClassification',
    'IncidentClassificationReason',
    'IncidentSeverity',
    'IncidentStatus',
]


class AlertRuleKind(str, Enum):
    """
    The alert rule kind
    """
    SCHEDULED = "Scheduled"
    MICROSOFT_SECURITY_INCIDENT_CREATION = "MicrosoftSecurityIncidentCreation"
    FUSION = "Fusion"


class CaseSeverity(str, Enum):
    """
    The severity of the incident
    """
    CRITICAL = "Critical"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"
    INFORMATIONAL = "Informational"


class DataConnectorKind(str, Enum):
    """
    The data connector kind
    """
    AZURE_ACTIVE_DIRECTORY = "AzureActiveDirectory"
    AZURE_SECURITY_CENTER = "AzureSecurityCenter"
    MICROSOFT_CLOUD_APP_SECURITY = "MicrosoftCloudAppSecurity"
    THREAT_INTELLIGENCE = "ThreatIntelligence"
    OFFICE365 = "Office365"
    AMAZON_WEB_SERVICES_CLOUD_TRAIL = "AmazonWebServicesCloudTrail"
    AZURE_ADVANCED_THREAT_PROTECTION = "AzureAdvancedThreatProtection"
    MICROSOFT_DEFENDER_ADVANCED_THREAT_PROTECTION = "MicrosoftDefenderAdvancedThreatProtection"


class IncidentClassification(str, Enum):
    """
    The reason the incident was closed
    """
    UNDETERMINED = "Undetermined"
    TRUE_POSITIVE = "TruePositive"
    BENIGN_POSITIVE = "BenignPositive"
    FALSE_POSITIVE = "FalsePositive"


class IncidentClassificationReason(str, Enum):
    """
    The classification reason the incident was closed with
    """
    SUSPICIOUS_ACTIVITY = "SuspiciousActivity"
    SUSPICIOUS_BUT_EXPECTED = "SuspiciousButExpected"
    INCORRECT_ALERT_LOGIC = "IncorrectAlertLogic"
    INACCURATE_DATA = "InaccurateData"


class IncidentSeverity(str, Enum):
    """
    The severity of the incident
    """
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"
    INFORMATIONAL = "Informational"


class IncidentStatus(str, Enum):
    """
    The status of the incident
    """
    NEW = "New"
    ACTIVE = "Active"
    CLOSED = "Closed"
