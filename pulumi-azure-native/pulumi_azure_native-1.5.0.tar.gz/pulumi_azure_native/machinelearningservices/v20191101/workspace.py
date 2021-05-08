# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['WorkspaceArgs', 'Workspace']

@pulumi.input_type
class WorkspaceArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 application_insights: Optional[pulumi.Input[str]] = None,
                 container_registry: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 discovery_url: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['IdentityArgs']] = None,
                 key_vault: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input['SkuArgs']] = None,
                 storage_account: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Workspace resource.
        :param pulumi.Input[str] resource_group_name: Name of the resource group in which workspace is located.
        :param pulumi.Input[str] application_insights: ARM id of the application insights associated with this workspace. This cannot be changed once the workspace has been created
        :param pulumi.Input[str] container_registry: ARM id of the container registry associated with this workspace. This cannot be changed once the workspace has been created
        :param pulumi.Input[str] description: The description of this workspace.
        :param pulumi.Input[str] discovery_url: Url for the discovery service to identify regional endpoints for machine learning experimentation services
        :param pulumi.Input[str] friendly_name: The friendly name for this workspace. This name in mutable
        :param pulumi.Input['IdentityArgs'] identity: The identity of the resource.
        :param pulumi.Input[str] key_vault: ARM id of the key vault associated with this workspace. This cannot be changed once the workspace has been created
        :param pulumi.Input[str] location: Specifies the location of the resource.
        :param pulumi.Input['SkuArgs'] sku: The sku of the workspace.
        :param pulumi.Input[str] storage_account: ARM id of the storage account associated with this workspace. This cannot be changed once the workspace has been created
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Contains resource tags defined as key/value pairs.
        :param pulumi.Input[str] workspace_name: Name of Azure Machine Learning workspace.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if application_insights is not None:
            pulumi.set(__self__, "application_insights", application_insights)
        if container_registry is not None:
            pulumi.set(__self__, "container_registry", container_registry)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if discovery_url is not None:
            pulumi.set(__self__, "discovery_url", discovery_url)
        if friendly_name is not None:
            pulumi.set(__self__, "friendly_name", friendly_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if key_vault is not None:
            pulumi.set(__self__, "key_vault", key_vault)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if storage_account is not None:
            pulumi.set(__self__, "storage_account", storage_account)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if workspace_name is not None:
            pulumi.set(__self__, "workspace_name", workspace_name)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group in which workspace is located.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="applicationInsights")
    def application_insights(self) -> Optional[pulumi.Input[str]]:
        """
        ARM id of the application insights associated with this workspace. This cannot be changed once the workspace has been created
        """
        return pulumi.get(self, "application_insights")

    @application_insights.setter
    def application_insights(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_insights", value)

    @property
    @pulumi.getter(name="containerRegistry")
    def container_registry(self) -> Optional[pulumi.Input[str]]:
        """
        ARM id of the container registry associated with this workspace. This cannot be changed once the workspace has been created
        """
        return pulumi.get(self, "container_registry")

    @container_registry.setter
    def container_registry(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "container_registry", value)

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
    @pulumi.getter(name="discoveryUrl")
    def discovery_url(self) -> Optional[pulumi.Input[str]]:
        """
        Url for the discovery service to identify regional endpoints for machine learning experimentation services
        """
        return pulumi.get(self, "discovery_url")

    @discovery_url.setter
    def discovery_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "discovery_url", value)

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[str]]:
        """
        The friendly name for this workspace. This name in mutable
        """
        return pulumi.get(self, "friendly_name")

    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "friendly_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['IdentityArgs']]:
        """
        The identity of the resource.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['IdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="keyVault")
    def key_vault(self) -> Optional[pulumi.Input[str]]:
        """
        ARM id of the key vault associated with this workspace. This cannot be changed once the workspace has been created
        """
        return pulumi.get(self, "key_vault")

    @key_vault.setter
    def key_vault(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_vault", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the location of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['SkuArgs']]:
        """
        The sku of the workspace.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['SkuArgs']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> Optional[pulumi.Input[str]]:
        """
        ARM id of the storage account associated with this workspace. This cannot be changed once the workspace has been created
        """
        return pulumi.get(self, "storage_account")

    @storage_account.setter
    def storage_account(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_account", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Contains resource tags defined as key/value pairs.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of Azure Machine Learning workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workspace_name", value)


class Workspace(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_insights: Optional[pulumi.Input[str]] = None,
                 container_registry: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 discovery_url: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 key_vault: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 storage_account: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An object that represents a machine learning workspace.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_insights: ARM id of the application insights associated with this workspace. This cannot be changed once the workspace has been created
        :param pulumi.Input[str] container_registry: ARM id of the container registry associated with this workspace. This cannot be changed once the workspace has been created
        :param pulumi.Input[str] description: The description of this workspace.
        :param pulumi.Input[str] discovery_url: Url for the discovery service to identify regional endpoints for machine learning experimentation services
        :param pulumi.Input[str] friendly_name: The friendly name for this workspace. This name in mutable
        :param pulumi.Input[pulumi.InputType['IdentityArgs']] identity: The identity of the resource.
        :param pulumi.Input[str] key_vault: ARM id of the key vault associated with this workspace. This cannot be changed once the workspace has been created
        :param pulumi.Input[str] location: Specifies the location of the resource.
        :param pulumi.Input[str] resource_group_name: Name of the resource group in which workspace is located.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: The sku of the workspace.
        :param pulumi.Input[str] storage_account: ARM id of the storage account associated with this workspace. This cannot be changed once the workspace has been created
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Contains resource tags defined as key/value pairs.
        :param pulumi.Input[str] workspace_name: Name of Azure Machine Learning workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkspaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An object that represents a machine learning workspace.

        :param str resource_name: The name of the resource.
        :param WorkspaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_insights: Optional[pulumi.Input[str]] = None,
                 container_registry: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 discovery_url: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 key_vault: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 storage_account: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = WorkspaceArgs.__new__(WorkspaceArgs)

            __props__.__dict__["application_insights"] = application_insights
            __props__.__dict__["container_registry"] = container_registry
            __props__.__dict__["description"] = description
            __props__.__dict__["discovery_url"] = discovery_url
            __props__.__dict__["friendly_name"] = friendly_name
            __props__.__dict__["identity"] = identity
            __props__.__dict__["key_vault"] = key_vault
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["storage_account"] = storage_account
            __props__.__dict__["tags"] = tags
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["workspace_id"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20191101:Workspace"), pulumi.Alias(type_="azure-native:machinelearningservices:Workspace"), pulumi.Alias(type_="azure-nextgen:machinelearningservices:Workspace"), pulumi.Alias(type_="azure-native:machinelearningservices/v20180301preview:Workspace"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20180301preview:Workspace"), pulumi.Alias(type_="azure-native:machinelearningservices/v20181119:Workspace"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20181119:Workspace"), pulumi.Alias(type_="azure-native:machinelearningservices/v20190501:Workspace"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20190501:Workspace"), pulumi.Alias(type_="azure-native:machinelearningservices/v20190601:Workspace"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20190601:Workspace"), pulumi.Alias(type_="azure-native:machinelearningservices/v20200101:Workspace"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20200101:Workspace"), pulumi.Alias(type_="azure-native:machinelearningservices/v20200218preview:Workspace"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20200218preview:Workspace"), pulumi.Alias(type_="azure-native:machinelearningservices/v20200301:Workspace"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20200301:Workspace"), pulumi.Alias(type_="azure-native:machinelearningservices/v20200401:Workspace"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20200401:Workspace"), pulumi.Alias(type_="azure-native:machinelearningservices/v20200501preview:Workspace"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20200501preview:Workspace"), pulumi.Alias(type_="azure-native:machinelearningservices/v20200515preview:Workspace"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20200515preview:Workspace"), pulumi.Alias(type_="azure-native:machinelearningservices/v20200601:Workspace"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20200601:Workspace"), pulumi.Alias(type_="azure-native:machinelearningservices/v20200801:Workspace"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20200801:Workspace"), pulumi.Alias(type_="azure-native:machinelearningservices/v20200901preview:Workspace"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20200901preview:Workspace"), pulumi.Alias(type_="azure-native:machinelearningservices/v20210101:Workspace"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20210101:Workspace"), pulumi.Alias(type_="azure-native:machinelearningservices/v20210401:Workspace"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20210401:Workspace")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Workspace, __self__).__init__(
            'azure-native:machinelearningservices/v20191101:Workspace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Workspace':
        """
        Get an existing Workspace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkspaceArgs.__new__(WorkspaceArgs)

        __props__.__dict__["application_insights"] = None
        __props__.__dict__["container_registry"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["discovery_url"] = None
        __props__.__dict__["friendly_name"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["key_vault"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["storage_account"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["workspace_id"] = None
        return Workspace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationInsights")
    def application_insights(self) -> pulumi.Output[Optional[str]]:
        """
        ARM id of the application insights associated with this workspace. This cannot be changed once the workspace has been created
        """
        return pulumi.get(self, "application_insights")

    @property
    @pulumi.getter(name="containerRegistry")
    def container_registry(self) -> pulumi.Output[Optional[str]]:
        """
        ARM id of the container registry associated with this workspace. This cannot be changed once the workspace has been created
        """
        return pulumi.get(self, "container_registry")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        The creation time of the machine learning workspace in ISO8601 format.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of this workspace.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="discoveryUrl")
    def discovery_url(self) -> pulumi.Output[Optional[str]]:
        """
        Url for the discovery service to identify regional endpoints for machine learning experimentation services
        """
        return pulumi.get(self, "discovery_url")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[Optional[str]]:
        """
        The friendly name for this workspace. This name in mutable
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityResponse']]:
        """
        The identity of the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="keyVault")
    def key_vault(self) -> pulumi.Output[Optional[str]]:
        """
        ARM id of the key vault associated with this workspace. This cannot be changed once the workspace has been created
        """
        return pulumi.get(self, "key_vault")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The current deployment state of workspace resource. The provisioningState is to indicate states for resource provisioning.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        The sku of the workspace.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> pulumi.Output[Optional[str]]:
        """
        ARM id of the storage account associated with this workspace. This cannot be changed once the workspace has been created
        """
        return pulumi.get(self, "storage_account")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Contains resource tags defined as key/value pairs.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Specifies the type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Output[str]:
        """
        The immutable id associated with this workspace.
        """
        return pulumi.get(self, "workspace_id")

