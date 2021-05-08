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

__all__ = ['WorkerPoolArgs', 'WorkerPool']

@pulumi.input_type
class WorkerPoolArgs:
    def __init__(__self__, *,
                 projects_id: pulumi.Input[str],
                 worker_pools_id: pulumi.Input[str],
                 network_config: Optional[pulumi.Input['NetworkConfigArgs']] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 worker_config: Optional[pulumi.Input['WorkerConfigArgs']] = None):
        """
        The set of arguments for constructing a WorkerPool resource.
        :param pulumi.Input['NetworkConfigArgs'] network_config: Network configuration for the `WorkerPool`.
        :param pulumi.Input[str] region: Required. Immutable. The region where the `WorkerPool` runs. Only "us-central1" is currently supported. Note that `region` cannot be changed once the `WorkerPool` is created.
        :param pulumi.Input['WorkerConfigArgs'] worker_config: Worker configuration for the `WorkerPool`.
        """
        pulumi.set(__self__, "projects_id", projects_id)
        pulumi.set(__self__, "worker_pools_id", worker_pools_id)
        if network_config is not None:
            pulumi.set(__self__, "network_config", network_config)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if worker_config is not None:
            pulumi.set(__self__, "worker_config", worker_config)

    @property
    @pulumi.getter(name="projectsId")
    def projects_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "projects_id")

    @projects_id.setter
    def projects_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "projects_id", value)

    @property
    @pulumi.getter(name="workerPoolsId")
    def worker_pools_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "worker_pools_id")

    @worker_pools_id.setter
    def worker_pools_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "worker_pools_id", value)

    @property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> Optional[pulumi.Input['NetworkConfigArgs']]:
        """
        Network configuration for the `WorkerPool`.
        """
        return pulumi.get(self, "network_config")

    @network_config.setter
    def network_config(self, value: Optional[pulumi.Input['NetworkConfigArgs']]):
        pulumi.set(self, "network_config", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        Required. Immutable. The region where the `WorkerPool` runs. Only "us-central1" is currently supported. Note that `region` cannot be changed once the `WorkerPool` is created.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="workerConfig")
    def worker_config(self) -> Optional[pulumi.Input['WorkerConfigArgs']]:
        """
        Worker configuration for the `WorkerPool`.
        """
        return pulumi.get(self, "worker_config")

    @worker_config.setter
    def worker_config(self, value: Optional[pulumi.Input['WorkerConfigArgs']]):
        pulumi.set(self, "worker_config", value)


class WorkerPool(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 network_config: Optional[pulumi.Input[pulumi.InputType['NetworkConfigArgs']]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 worker_config: Optional[pulumi.Input[pulumi.InputType['WorkerConfigArgs']]] = None,
                 worker_pools_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a `WorkerPool` to run the builds, and returns the new worker pool.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['NetworkConfigArgs']] network_config: Network configuration for the `WorkerPool`.
        :param pulumi.Input[str] region: Required. Immutable. The region where the `WorkerPool` runs. Only "us-central1" is currently supported. Note that `region` cannot be changed once the `WorkerPool` is created.
        :param pulumi.Input[pulumi.InputType['WorkerConfigArgs']] worker_config: Worker configuration for the `WorkerPool`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkerPoolArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a `WorkerPool` to run the builds, and returns the new worker pool.

        :param str resource_name: The name of the resource.
        :param WorkerPoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkerPoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 network_config: Optional[pulumi.Input[pulumi.InputType['NetworkConfigArgs']]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 worker_config: Optional[pulumi.Input[pulumi.InputType['WorkerConfigArgs']]] = None,
                 worker_pools_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = WorkerPoolArgs.__new__(WorkerPoolArgs)

            __props__.__dict__["network_config"] = network_config
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__.__dict__["projects_id"] = projects_id
            __props__.__dict__["region"] = region
            __props__.__dict__["worker_config"] = worker_config
            if worker_pools_id is None and not opts.urn:
                raise TypeError("Missing required property 'worker_pools_id'")
            __props__.__dict__["worker_pools_id"] = worker_pools_id
            __props__.__dict__["create_time"] = None
            __props__.__dict__["delete_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["update_time"] = None
        super(WorkerPool, __self__).__init__(
            'google-native:cloudbuild/v1alpha2:WorkerPool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WorkerPool':
        """
        Get an existing WorkerPool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkerPoolArgs.__new__(WorkerPoolArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["delete_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_config"] = None
        __props__.__dict__["region"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["update_time"] = None
        __props__.__dict__["worker_config"] = None
        return WorkerPool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Time at which the request to create the `WorkerPool` was received.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> pulumi.Output[str]:
        """
        Time at which the request to delete the `WorkerPool` was received.
        """
        return pulumi.get(self, "delete_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the `WorkerPool`. Format of the name is `projects/{project_id}/workerPools/{worker_pool_id}`, where the value of {worker_pool_id} is provided in the CreateWorkerPool request.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> pulumi.Output['outputs.NetworkConfigResponse']:
        """
        Network configuration for the `WorkerPool`.
        """
        return pulumi.get(self, "network_config")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        Required. Immutable. The region where the `WorkerPool` runs. Only "us-central1" is currently supported. Note that `region` cannot be changed once the `WorkerPool` is created.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        WorkerPool state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Time at which the request to update the `WorkerPool` was received.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter(name="workerConfig")
    def worker_config(self) -> pulumi.Output['outputs.WorkerConfigResponse']:
        """
        Worker configuration for the `WorkerPool`.
        """
        return pulumi.get(self, "worker_config")

