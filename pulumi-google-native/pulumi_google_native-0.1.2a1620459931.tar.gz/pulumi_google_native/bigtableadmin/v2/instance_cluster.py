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

__all__ = ['InstanceClusterArgs', 'InstanceCluster']

@pulumi.input_type
class InstanceClusterArgs:
    def __init__(__self__, *,
                 clusters_id: pulumi.Input[str],
                 instances_id: pulumi.Input[str],
                 projects_id: pulumi.Input[str],
                 default_storage_type: Optional[pulumi.Input[str]] = None,
                 encryption_config: Optional[pulumi.Input['EncryptionConfigArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 serve_nodes: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a InstanceCluster resource.
        :param pulumi.Input[str] default_storage_type: Immutable. The type of storage used by this cluster to serve its parent instance's tables, unless explicitly overridden.
        :param pulumi.Input['EncryptionConfigArgs'] encryption_config: Immutable. The encryption configuration for CMEK-protected clusters.
        :param pulumi.Input[str] location: Immutable. The location where this cluster's nodes and storage reside. For best performance, clients should be located as close as possible to this cluster. Currently only zones are supported, so values should be of the form `projects/{project}/locations/{zone}`.
        :param pulumi.Input[str] name: The unique name of the cluster. Values are of the form `projects/{project}/instances/{instance}/clusters/a-z*`.
        :param pulumi.Input[int] serve_nodes: Required. The number of nodes allocated to this cluster. More nodes enable higher throughput and more consistent performance.
        """
        pulumi.set(__self__, "clusters_id", clusters_id)
        pulumi.set(__self__, "instances_id", instances_id)
        pulumi.set(__self__, "projects_id", projects_id)
        if default_storage_type is not None:
            pulumi.set(__self__, "default_storage_type", default_storage_type)
        if encryption_config is not None:
            pulumi.set(__self__, "encryption_config", encryption_config)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if serve_nodes is not None:
            pulumi.set(__self__, "serve_nodes", serve_nodes)

    @property
    @pulumi.getter(name="clustersId")
    def clusters_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "clusters_id")

    @clusters_id.setter
    def clusters_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "clusters_id", value)

    @property
    @pulumi.getter(name="instancesId")
    def instances_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "instances_id")

    @instances_id.setter
    def instances_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "instances_id", value)

    @property
    @pulumi.getter(name="projectsId")
    def projects_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "projects_id")

    @projects_id.setter
    def projects_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "projects_id", value)

    @property
    @pulumi.getter(name="defaultStorageType")
    def default_storage_type(self) -> Optional[pulumi.Input[str]]:
        """
        Immutable. The type of storage used by this cluster to serve its parent instance's tables, unless explicitly overridden.
        """
        return pulumi.get(self, "default_storage_type")

    @default_storage_type.setter
    def default_storage_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_storage_type", value)

    @property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> Optional[pulumi.Input['EncryptionConfigArgs']]:
        """
        Immutable. The encryption configuration for CMEK-protected clusters.
        """
        return pulumi.get(self, "encryption_config")

    @encryption_config.setter
    def encryption_config(self, value: Optional[pulumi.Input['EncryptionConfigArgs']]):
        pulumi.set(self, "encryption_config", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Immutable. The location where this cluster's nodes and storage reside. For best performance, clients should be located as close as possible to this cluster. Currently only zones are supported, so values should be of the form `projects/{project}/locations/{zone}`.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The unique name of the cluster. Values are of the form `projects/{project}/instances/{instance}/clusters/a-z*`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="serveNodes")
    def serve_nodes(self) -> Optional[pulumi.Input[int]]:
        """
        Required. The number of nodes allocated to this cluster. More nodes enable higher throughput and more consistent performance.
        """
        return pulumi.get(self, "serve_nodes")

    @serve_nodes.setter
    def serve_nodes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "serve_nodes", value)


class InstanceCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 clusters_id: Optional[pulumi.Input[str]] = None,
                 default_storage_type: Optional[pulumi.Input[str]] = None,
                 encryption_config: Optional[pulumi.Input[pulumi.InputType['EncryptionConfigArgs']]] = None,
                 instances_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 serve_nodes: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Creates a cluster within an instance.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_storage_type: Immutable. The type of storage used by this cluster to serve its parent instance's tables, unless explicitly overridden.
        :param pulumi.Input[pulumi.InputType['EncryptionConfigArgs']] encryption_config: Immutable. The encryption configuration for CMEK-protected clusters.
        :param pulumi.Input[str] location: Immutable. The location where this cluster's nodes and storage reside. For best performance, clients should be located as close as possible to this cluster. Currently only zones are supported, so values should be of the form `projects/{project}/locations/{zone}`.
        :param pulumi.Input[str] name: The unique name of the cluster. Values are of the form `projects/{project}/instances/{instance}/clusters/a-z*`.
        :param pulumi.Input[int] serve_nodes: Required. The number of nodes allocated to this cluster. More nodes enable higher throughput and more consistent performance.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InstanceClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a cluster within an instance.

        :param str resource_name: The name of the resource.
        :param InstanceClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 clusters_id: Optional[pulumi.Input[str]] = None,
                 default_storage_type: Optional[pulumi.Input[str]] = None,
                 encryption_config: Optional[pulumi.Input[pulumi.InputType['EncryptionConfigArgs']]] = None,
                 instances_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 serve_nodes: Optional[pulumi.Input[int]] = None,
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
            __props__ = InstanceClusterArgs.__new__(InstanceClusterArgs)

            if clusters_id is None and not opts.urn:
                raise TypeError("Missing required property 'clusters_id'")
            __props__.__dict__["clusters_id"] = clusters_id
            __props__.__dict__["default_storage_type"] = default_storage_type
            __props__.__dict__["encryption_config"] = encryption_config
            if instances_id is None and not opts.urn:
                raise TypeError("Missing required property 'instances_id'")
            __props__.__dict__["instances_id"] = instances_id
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__.__dict__["projects_id"] = projects_id
            __props__.__dict__["serve_nodes"] = serve_nodes
            __props__.__dict__["state"] = None
        super(InstanceCluster, __self__).__init__(
            'google-native:bigtableadmin/v2:InstanceCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'InstanceCluster':
        """
        Get an existing InstanceCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InstanceClusterArgs.__new__(InstanceClusterArgs)

        __props__.__dict__["default_storage_type"] = None
        __props__.__dict__["encryption_config"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["serve_nodes"] = None
        __props__.__dict__["state"] = None
        return InstanceCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="defaultStorageType")
    def default_storage_type(self) -> pulumi.Output[str]:
        """
        Immutable. The type of storage used by this cluster to serve its parent instance's tables, unless explicitly overridden.
        """
        return pulumi.get(self, "default_storage_type")

    @property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> pulumi.Output['outputs.EncryptionConfigResponse']:
        """
        Immutable. The encryption configuration for CMEK-protected clusters.
        """
        return pulumi.get(self, "encryption_config")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Immutable. The location where this cluster's nodes and storage reside. For best performance, clients should be located as close as possible to this cluster. Currently only zones are supported, so values should be of the form `projects/{project}/locations/{zone}`.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The unique name of the cluster. Values are of the form `projects/{project}/instances/{instance}/clusters/a-z*`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="serveNodes")
    def serve_nodes(self) -> pulumi.Output[int]:
        """
        Required. The number of nodes allocated to this cluster. More nodes enable higher throughput and more consistent performance.
        """
        return pulumi.get(self, "serve_nodes")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of the cluster.
        """
        return pulumi.get(self, "state")

