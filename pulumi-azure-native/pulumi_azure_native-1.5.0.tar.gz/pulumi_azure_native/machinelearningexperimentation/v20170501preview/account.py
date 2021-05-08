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

__all__ = ['AccountArgs', 'Account']

@pulumi.input_type
class AccountArgs:
    def __init__(__self__, *,
                 key_vault_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 storage_account: pulumi.Input['StorageAccountPropertiesArgs'],
                 vso_account_id: pulumi.Input[str],
                 account_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 seats: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Account resource.
        :param pulumi.Input[str] key_vault_id: The fully qualified arm id of the user key vault.
        :param pulumi.Input[str] resource_group_name: The name of the resource group to which the machine learning team account belongs.
        :param pulumi.Input['StorageAccountPropertiesArgs'] storage_account: The properties of the storage account for the machine learning team account.
        :param pulumi.Input[str] vso_account_id: The fully qualified arm id of the vso account to be used for this team account.
        :param pulumi.Input[str] account_name: The name of the machine learning team account.
        :param pulumi.Input[str] description: The description of this workspace.
        :param pulumi.Input[str] friendly_name: The friendly name for this workspace. This will be the workspace name in the arm id when the workspace object gets created
        :param pulumi.Input[str] location: The location of the resource. This cannot be changed after the resource is created.
        :param pulumi.Input[str] seats: The no of users/seats who can access this team account. This property defines the charge on the team account.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags of the resource.
        """
        pulumi.set(__self__, "key_vault_id", key_vault_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "storage_account", storage_account)
        pulumi.set(__self__, "vso_account_id", vso_account_id)
        if account_name is not None:
            pulumi.set(__self__, "account_name", account_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if friendly_name is not None:
            pulumi.set(__self__, "friendly_name", friendly_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if seats is not None:
            pulumi.set(__self__, "seats", seats)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="keyVaultId")
    def key_vault_id(self) -> pulumi.Input[str]:
        """
        The fully qualified arm id of the user key vault.
        """
        return pulumi.get(self, "key_vault_id")

    @key_vault_id.setter
    def key_vault_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_vault_id", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group to which the machine learning team account belongs.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> pulumi.Input['StorageAccountPropertiesArgs']:
        """
        The properties of the storage account for the machine learning team account.
        """
        return pulumi.get(self, "storage_account")

    @storage_account.setter
    def storage_account(self, value: pulumi.Input['StorageAccountPropertiesArgs']):
        pulumi.set(self, "storage_account", value)

    @property
    @pulumi.getter(name="vsoAccountId")
    def vso_account_id(self) -> pulumi.Input[str]:
        """
        The fully qualified arm id of the vso account to be used for this team account.
        """
        return pulumi.get(self, "vso_account_id")

    @vso_account_id.setter
    def vso_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vso_account_id", value)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the machine learning team account.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of this workspace.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[str]]:
        """
        The friendly name for this workspace. This will be the workspace name in the arm id when the workspace object gets created
        """
        return pulumi.get(self, "friendly_name")

    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "friendly_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the resource. This cannot be changed after the resource is created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def seats(self) -> Optional[pulumi.Input[str]]:
        """
        The no of users/seats who can access this team account. This property defines the charge on the team account.
        """
        return pulumi.get(self, "seats")

    @seats.setter
    def seats(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "seats", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Account(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 key_vault_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 seats: Optional[pulumi.Input[str]] = None,
                 storage_account: Optional[pulumi.Input[pulumi.InputType['StorageAccountPropertiesArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vso_account_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An object that represents a machine learning team account.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the machine learning team account.
        :param pulumi.Input[str] description: The description of this workspace.
        :param pulumi.Input[str] friendly_name: The friendly name for this workspace. This will be the workspace name in the arm id when the workspace object gets created
        :param pulumi.Input[str] key_vault_id: The fully qualified arm id of the user key vault.
        :param pulumi.Input[str] location: The location of the resource. This cannot be changed after the resource is created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group to which the machine learning team account belongs.
        :param pulumi.Input[str] seats: The no of users/seats who can access this team account. This property defines the charge on the team account.
        :param pulumi.Input[pulumi.InputType['StorageAccountPropertiesArgs']] storage_account: The properties of the storage account for the machine learning team account.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags of the resource.
        :param pulumi.Input[str] vso_account_id: The fully qualified arm id of the vso account to be used for this team account.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An object that represents a machine learning team account.

        :param str resource_name: The name of the resource.
        :param AccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 key_vault_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 seats: Optional[pulumi.Input[str]] = None,
                 storage_account: Optional[pulumi.Input[pulumi.InputType['StorageAccountPropertiesArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vso_account_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = AccountArgs.__new__(AccountArgs)

            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["description"] = description
            __props__.__dict__["friendly_name"] = friendly_name
            if key_vault_id is None and not opts.urn:
                raise TypeError("Missing required property 'key_vault_id'")
            __props__.__dict__["key_vault_id"] = key_vault_id
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["seats"] = seats
            if storage_account is None and not opts.urn:
                raise TypeError("Missing required property 'storage_account'")
            __props__.__dict__["storage_account"] = storage_account
            __props__.__dict__["tags"] = tags
            if vso_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'vso_account_id'")
            __props__.__dict__["vso_account_id"] = vso_account_id
            __props__.__dict__["account_id"] = None
            __props__.__dict__["creation_date"] = None
            __props__.__dict__["discovery_uri"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:machinelearningexperimentation/v20170501preview:Account"), pulumi.Alias(type_="azure-native:machinelearningexperimentation:Account"), pulumi.Alias(type_="azure-nextgen:machinelearningexperimentation:Account")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Account, __self__).__init__(
            'azure-native:machinelearningexperimentation/v20170501preview:Account',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Account':
        """
        Get an existing Account resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AccountArgs.__new__(AccountArgs)

        __props__.__dict__["account_id"] = None
        __props__.__dict__["creation_date"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["discovery_uri"] = None
        __props__.__dict__["friendly_name"] = None
        __props__.__dict__["key_vault_id"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["seats"] = None
        __props__.__dict__["storage_account"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["vso_account_id"] = None
        return Account(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        The immutable id associated with this team account.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[str]:
        """
        The creation date of the machine learning team account in ISO8601 format.
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of this workspace.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="discoveryUri")
    def discovery_uri(self) -> pulumi.Output[str]:
        """
        The uri for this machine learning team account.
        """
        return pulumi.get(self, "discovery_uri")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[Optional[str]]:
        """
        The friendly name for this workspace. This will be the workspace name in the arm id when the workspace object gets created
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter(name="keyVaultId")
    def key_vault_id(self) -> pulumi.Output[str]:
        """
        The fully qualified arm id of the user key vault.
        """
        return pulumi.get(self, "key_vault_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location of the resource. This cannot be changed after the resource is created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The current deployment state of team account resource. The provisioningState is to indicate states for resource provisioning.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def seats(self) -> pulumi.Output[Optional[str]]:
        """
        The no of users/seats who can access this team account. This property defines the charge on the team account.
        """
        return pulumi.get(self, "seats")

    @property
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> pulumi.Output['outputs.StorageAccountPropertiesResponse']:
        """
        The properties of the storage account for the machine learning team account.
        """
        return pulumi.get(self, "storage_account")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vsoAccountId")
    def vso_account_id(self) -> pulumi.Output[str]:
        """
        The fully qualified arm id of the vso account to be used for this team account.
        """
        return pulumi.get(self, "vso_account_id")

