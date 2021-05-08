# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['FileShareArgs', 'FileShare']

@pulumi.input_type
class FileShareArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 share_name: Optional[pulumi.Input[str]] = None,
                 share_quota: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a FileShare resource.
        :param pulumi.Input[str] account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: A name-value pair to associate with the share as metadata.
        :param pulumi.Input[str] share_name: The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
        :param pulumi.Input[int] share_quota: The maximum size of the share, in gigabytes. Must be greater than 0, and less than or equal to 5TB (5120).
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if share_name is not None:
            pulumi.set(__self__, "share_name", share_name)
        if share_quota is not None:
            pulumi.set(__self__, "share_quota", share_quota)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the user's subscription. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A name-value pair to associate with the share as metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter(name="shareName")
    def share_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
        """
        return pulumi.get(self, "share_name")

    @share_name.setter
    def share_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "share_name", value)

    @property
    @pulumi.getter(name="shareQuota")
    def share_quota(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum size of the share, in gigabytes. Must be greater than 0, and less than or equal to 5TB (5120).
        """
        return pulumi.get(self, "share_quota")

    @share_quota.setter
    def share_quota(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "share_quota", value)


class FileShare(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 share_name: Optional[pulumi.Input[str]] = None,
                 share_quota: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Properties of the file share, including Id, resource name, resource type, Etag.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: A name-value pair to associate with the share as metadata.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[str] share_name: The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
        :param pulumi.Input[int] share_quota: The maximum size of the share, in gigabytes. Must be greater than 0, and less than or equal to 5TB (5120).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FileShareArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Properties of the file share, including Id, resource name, resource type, Etag.

        :param str resource_name: The name of the resource.
        :param FileShareArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FileShareArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 share_name: Optional[pulumi.Input[str]] = None,
                 share_quota: Optional[pulumi.Input[int]] = None,
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
            __props__ = FileShareArgs.__new__(FileShareArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["metadata"] = metadata
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["share_name"] = share_name
            __props__.__dict__["share_quota"] = share_quota
            __props__.__dict__["etag"] = None
            __props__.__dict__["last_modified_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:storage/v20190401:FileShare"), pulumi.Alias(type_="azure-native:storage:FileShare"), pulumi.Alias(type_="azure-nextgen:storage:FileShare"), pulumi.Alias(type_="azure-native:storage/v20190601:FileShare"), pulumi.Alias(type_="azure-nextgen:storage/v20190601:FileShare"), pulumi.Alias(type_="azure-native:storage/v20200801preview:FileShare"), pulumi.Alias(type_="azure-nextgen:storage/v20200801preview:FileShare"), pulumi.Alias(type_="azure-native:storage/v20210101:FileShare"), pulumi.Alias(type_="azure-nextgen:storage/v20210101:FileShare"), pulumi.Alias(type_="azure-native:storage/v20210201:FileShare"), pulumi.Alias(type_="azure-nextgen:storage/v20210201:FileShare")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(FileShare, __self__).__init__(
            'azure-native:storage/v20190401:FileShare',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FileShare':
        """
        Get an existing FileShare resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FileShareArgs.__new__(FileShareArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["last_modified_time"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["share_quota"] = None
        __props__.__dict__["type"] = None
        return FileShare(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        Resource Etag.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[str]:
        """
        Returns the date and time the share was last modified.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A name-value pair to associate with the share as metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="shareQuota")
    def share_quota(self) -> pulumi.Output[Optional[int]]:
        """
        The maximum size of the share, in gigabytes. Must be greater than 0, and less than or equal to 5TB (5120).
        """
        return pulumi.get(self, "share_quota")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

