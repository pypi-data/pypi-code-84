# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = ['ManagedInstanceKeyArgs', 'ManagedInstanceKey']

@pulumi.input_type
class ManagedInstanceKeyArgs:
    def __init__(__self__, *,
                 managed_instance_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 server_key_type: pulumi.Input[Union[str, 'ServerKeyType']],
                 key_name: Optional[pulumi.Input[str]] = None,
                 uri: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ManagedInstanceKey resource.
        :param pulumi.Input[str] managed_instance_name: The name of the managed instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[Union[str, 'ServerKeyType']] server_key_type: The key type like 'ServiceManaged', 'AzureKeyVault'.
        :param pulumi.Input[str] key_name: The name of the managed instance key to be operated on (updated or created).
        :param pulumi.Input[str] uri: The URI of the key. If the ServerKeyType is AzureKeyVault, then the URI is required.
        """
        pulumi.set(__self__, "managed_instance_name", managed_instance_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "server_key_type", server_key_type)
        if key_name is not None:
            pulumi.set(__self__, "key_name", key_name)
        if uri is not None:
            pulumi.set(__self__, "uri", uri)

    @property
    @pulumi.getter(name="managedInstanceName")
    def managed_instance_name(self) -> pulumi.Input[str]:
        """
        The name of the managed instance.
        """
        return pulumi.get(self, "managed_instance_name")

    @managed_instance_name.setter
    def managed_instance_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "managed_instance_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serverKeyType")
    def server_key_type(self) -> pulumi.Input[Union[str, 'ServerKeyType']]:
        """
        The key type like 'ServiceManaged', 'AzureKeyVault'.
        """
        return pulumi.get(self, "server_key_type")

    @server_key_type.setter
    def server_key_type(self, value: pulumi.Input[Union[str, 'ServerKeyType']]):
        pulumi.set(self, "server_key_type", value)

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the managed instance key to be operated on (updated or created).
        """
        return pulumi.get(self, "key_name")

    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_name", value)

    @property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[str]]:
        """
        The URI of the key. If the ServerKeyType is AzureKeyVault, then the URI is required.
        """
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uri", value)


class ManagedInstanceKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key_name: Optional[pulumi.Input[str]] = None,
                 managed_instance_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_key_type: Optional[pulumi.Input[Union[str, 'ServerKeyType']]] = None,
                 uri: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A managed instance key.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key_name: The name of the managed instance key to be operated on (updated or created).
        :param pulumi.Input[str] managed_instance_name: The name of the managed instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[Union[str, 'ServerKeyType']] server_key_type: The key type like 'ServiceManaged', 'AzureKeyVault'.
        :param pulumi.Input[str] uri: The URI of the key. If the ServerKeyType is AzureKeyVault, then the URI is required.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ManagedInstanceKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A managed instance key.

        :param str resource_name: The name of the resource.
        :param ManagedInstanceKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagedInstanceKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key_name: Optional[pulumi.Input[str]] = None,
                 managed_instance_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_key_type: Optional[pulumi.Input[Union[str, 'ServerKeyType']]] = None,
                 uri: Optional[pulumi.Input[str]] = None,
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
            __props__ = ManagedInstanceKeyArgs.__new__(ManagedInstanceKeyArgs)

            __props__.__dict__["key_name"] = key_name
            if managed_instance_name is None and not opts.urn:
                raise TypeError("Missing required property 'managed_instance_name'")
            __props__.__dict__["managed_instance_name"] = managed_instance_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if server_key_type is None and not opts.urn:
                raise TypeError("Missing required property 'server_key_type'")
            __props__.__dict__["server_key_type"] = server_key_type
            __props__.__dict__["uri"] = uri
            __props__.__dict__["creation_date"] = None
            __props__.__dict__["kind"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["thumbprint"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:sql/v20200801preview:ManagedInstanceKey"), pulumi.Alias(type_="azure-native:sql:ManagedInstanceKey"), pulumi.Alias(type_="azure-nextgen:sql:ManagedInstanceKey"), pulumi.Alias(type_="azure-native:sql/v20171001preview:ManagedInstanceKey"), pulumi.Alias(type_="azure-nextgen:sql/v20171001preview:ManagedInstanceKey"), pulumi.Alias(type_="azure-native:sql/v20200202preview:ManagedInstanceKey"), pulumi.Alias(type_="azure-nextgen:sql/v20200202preview:ManagedInstanceKey"), pulumi.Alias(type_="azure-native:sql/v20201101preview:ManagedInstanceKey"), pulumi.Alias(type_="azure-nextgen:sql/v20201101preview:ManagedInstanceKey")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ManagedInstanceKey, __self__).__init__(
            'azure-native:sql/v20200801preview:ManagedInstanceKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ManagedInstanceKey':
        """
        Get an existing ManagedInstanceKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ManagedInstanceKeyArgs.__new__(ManagedInstanceKeyArgs)

        __props__.__dict__["creation_date"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["thumbprint"] = None
        __props__.__dict__["type"] = None
        return ManagedInstanceKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[str]:
        """
        The key creation date.
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Kind of encryption protector. This is metadata used for the Azure portal experience.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def thumbprint(self) -> pulumi.Output[str]:
        """
        Thumbprint of the key.
        """
        return pulumi.get(self, "thumbprint")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

