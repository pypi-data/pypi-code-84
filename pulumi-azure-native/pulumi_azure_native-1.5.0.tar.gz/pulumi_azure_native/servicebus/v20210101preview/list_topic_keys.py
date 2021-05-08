# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'ListTopicKeysResult',
    'AwaitableListTopicKeysResult',
    'list_topic_keys',
]

@pulumi.output_type
class ListTopicKeysResult:
    """
    Namespace/ServiceBus Connection String
    """
    def __init__(__self__, alias_primary_connection_string=None, alias_secondary_connection_string=None, key_name=None, primary_connection_string=None, primary_key=None, secondary_connection_string=None, secondary_key=None):
        if alias_primary_connection_string and not isinstance(alias_primary_connection_string, str):
            raise TypeError("Expected argument 'alias_primary_connection_string' to be a str")
        pulumi.set(__self__, "alias_primary_connection_string", alias_primary_connection_string)
        if alias_secondary_connection_string and not isinstance(alias_secondary_connection_string, str):
            raise TypeError("Expected argument 'alias_secondary_connection_string' to be a str")
        pulumi.set(__self__, "alias_secondary_connection_string", alias_secondary_connection_string)
        if key_name and not isinstance(key_name, str):
            raise TypeError("Expected argument 'key_name' to be a str")
        pulumi.set(__self__, "key_name", key_name)
        if primary_connection_string and not isinstance(primary_connection_string, str):
            raise TypeError("Expected argument 'primary_connection_string' to be a str")
        pulumi.set(__self__, "primary_connection_string", primary_connection_string)
        if primary_key and not isinstance(primary_key, str):
            raise TypeError("Expected argument 'primary_key' to be a str")
        pulumi.set(__self__, "primary_key", primary_key)
        if secondary_connection_string and not isinstance(secondary_connection_string, str):
            raise TypeError("Expected argument 'secondary_connection_string' to be a str")
        pulumi.set(__self__, "secondary_connection_string", secondary_connection_string)
        if secondary_key and not isinstance(secondary_key, str):
            raise TypeError("Expected argument 'secondary_key' to be a str")
        pulumi.set(__self__, "secondary_key", secondary_key)

    @property
    @pulumi.getter(name="aliasPrimaryConnectionString")
    def alias_primary_connection_string(self) -> str:
        """
        Primary connection string of the alias if GEO DR is enabled
        """
        return pulumi.get(self, "alias_primary_connection_string")

    @property
    @pulumi.getter(name="aliasSecondaryConnectionString")
    def alias_secondary_connection_string(self) -> str:
        """
        Secondary  connection string of the alias if GEO DR is enabled
        """
        return pulumi.get(self, "alias_secondary_connection_string")

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> str:
        """
        A string that describes the authorization rule.
        """
        return pulumi.get(self, "key_name")

    @property
    @pulumi.getter(name="primaryConnectionString")
    def primary_connection_string(self) -> str:
        """
        Primary connection string of the created namespace authorization rule.
        """
        return pulumi.get(self, "primary_connection_string")

    @property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> str:
        """
        A base64-encoded 256-bit primary key for signing and validating the SAS token.
        """
        return pulumi.get(self, "primary_key")

    @property
    @pulumi.getter(name="secondaryConnectionString")
    def secondary_connection_string(self) -> str:
        """
        Secondary connection string of the created namespace authorization rule.
        """
        return pulumi.get(self, "secondary_connection_string")

    @property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> str:
        """
        A base64-encoded 256-bit primary key for signing and validating the SAS token.
        """
        return pulumi.get(self, "secondary_key")


class AwaitableListTopicKeysResult(ListTopicKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListTopicKeysResult(
            alias_primary_connection_string=self.alias_primary_connection_string,
            alias_secondary_connection_string=self.alias_secondary_connection_string,
            key_name=self.key_name,
            primary_connection_string=self.primary_connection_string,
            primary_key=self.primary_key,
            secondary_connection_string=self.secondary_connection_string,
            secondary_key=self.secondary_key)


def list_topic_keys(authorization_rule_name: Optional[str] = None,
                    namespace_name: Optional[str] = None,
                    resource_group_name: Optional[str] = None,
                    topic_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListTopicKeysResult:
    """
    Namespace/ServiceBus Connection String


    :param str authorization_rule_name: The authorization rule name.
    :param str namespace_name: The namespace name
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    :param str topic_name: The topic name.
    """
    __args__ = dict()
    __args__['authorizationRuleName'] = authorization_rule_name
    __args__['namespaceName'] = namespace_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['topicName'] = topic_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:servicebus/v20210101preview:listTopicKeys', __args__, opts=opts, typ=ListTopicKeysResult).value

    return AwaitableListTopicKeysResult(
        alias_primary_connection_string=__ret__.alias_primary_connection_string,
        alias_secondary_connection_string=__ret__.alias_secondary_connection_string,
        key_name=__ret__.key_name,
        primary_connection_string=__ret__.primary_connection_string,
        primary_key=__ret__.primary_key,
        secondary_connection_string=__ret__.secondary_connection_string,
        secondary_key=__ret__.secondary_key)
