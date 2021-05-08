# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'BackupStorageRedundancy',
    'BackupType',
    'CompositePathSortOrder',
    'ConflictResolutionMode',
    'ConnectorOffer',
    'CreateMode',
    'DataType',
    'DatabaseAccountKind',
    'DatabaseAccountOfferType',
    'DefaultConsistencyLevel',
    'IndexKind',
    'IndexingMode',
    'PartitionKind',
    'ResourceIdentityType',
    'RestoreMode',
    'RoleDefinitionType',
    'ServerVersion',
    'SpatialType',
    'TriggerOperation',
    'TriggerType',
]


class BackupStorageRedundancy(str, Enum):
    """
    Enum to indicate type of backup residency
    """
    GEO = "Geo"
    LOCAL = "Local"
    ZONE = "Zone"


class BackupType(str, Enum):
    """
    Describes the mode of backups.
    """
    PERIODIC = "Periodic"
    CONTINUOUS = "Continuous"


class CompositePathSortOrder(str, Enum):
    """
    Sort order for composite paths.
    """
    ASCENDING = "Ascending"
    DESCENDING = "Descending"


class ConflictResolutionMode(str, Enum):
    """
    Indicates the conflict resolution mode.
    """
    LAST_WRITER_WINS = "LastWriterWins"
    CUSTOM = "Custom"


class ConnectorOffer(str, Enum):
    """
    The cassandra connector offer type for the Cosmos DB database C* account.
    """
    SMALL = "Small"


class CreateMode(str, Enum):
    """
    Enum to indicate the mode of account creation.
    """
    DEFAULT = "Default"
    RESTORE = "Restore"


class DataType(str, Enum):
    """
    The datatype for which the indexing behavior is applied to.
    """
    STRING = "String"
    NUMBER = "Number"
    POINT = "Point"
    POLYGON = "Polygon"
    LINE_STRING = "LineString"
    MULTI_POLYGON = "MultiPolygon"


class DatabaseAccountKind(str, Enum):
    """
    Indicates the type of database account. This can only be set at database account creation.
    """
    GLOBAL_DOCUMENT_DB = "GlobalDocumentDB"
    MONGO_DB = "MongoDB"
    PARSE = "Parse"


class DatabaseAccountOfferType(str, Enum):
    """
    The offer type for the database
    """
    STANDARD = "Standard"


class DefaultConsistencyLevel(str, Enum):
    """
    The default consistency level and configuration settings of the Cosmos DB account.
    """
    EVENTUAL = "Eventual"
    SESSION = "Session"
    BOUNDED_STALENESS = "BoundedStaleness"
    STRONG = "Strong"
    CONSISTENT_PREFIX = "ConsistentPrefix"


class IndexKind(str, Enum):
    """
    Indicates the type of index.
    """
    HASH = "Hash"
    RANGE = "Range"
    SPATIAL = "Spatial"


class IndexingMode(str, Enum):
    """
    Indicates the indexing mode.
    """
    CONSISTENT = "Consistent"
    LAZY = "Lazy"
    NONE = "None"


class PartitionKind(str, Enum):
    """
    Indicates the kind of algorithm used for partitioning
    """
    HASH = "Hash"
    RANGE = "Range"


class ResourceIdentityType(str, Enum):
    """
    The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"
    NONE = "None"


class RestoreMode(str, Enum):
    """
    Describes the mode of the restore.
    """
    POINT_IN_TIME = "PointInTime"


class RoleDefinitionType(str, Enum):
    """
    Indicates whether the Role Definition was built-in or user created.
    """
    BUILT_IN_ROLE = "BuiltInRole"
    CUSTOM_ROLE = "CustomRole"


class ServerVersion(str, Enum):
    """
    Describes the ServerVersion of an a MongoDB account.
    """
    SERVER_VERSION_3_2 = "3.2"
    SERVER_VERSION_3_6 = "3.6"


class SpatialType(str, Enum):
    """
    Indicates the spatial type of index.
    """
    POINT = "Point"
    LINE_STRING = "LineString"
    POLYGON = "Polygon"
    MULTI_POLYGON = "MultiPolygon"


class TriggerOperation(str, Enum):
    """
    The operation the trigger is associated with
    """
    ALL = "All"
    CREATE = "Create"
    UPDATE = "Update"
    DELETE = "Delete"
    REPLACE = "Replace"


class TriggerType(str, Enum):
    """
    Type of the Trigger
    """
    PRE = "Pre"
    POST = "Post"
