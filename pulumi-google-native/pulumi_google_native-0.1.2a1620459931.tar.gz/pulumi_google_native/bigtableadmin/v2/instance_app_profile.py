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

__all__ = ['InstanceAppProfileArgs', 'InstanceAppProfile']

@pulumi.input_type
class InstanceAppProfileArgs:
    def __init__(__self__, *,
                 app_profiles_id: pulumi.Input[str],
                 instances_id: pulumi.Input[str],
                 projects_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 multi_cluster_routing_use_any: Optional[pulumi.Input['MultiClusterRoutingUseAnyArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 single_cluster_routing: Optional[pulumi.Input['SingleClusterRoutingArgs']] = None):
        """
        The set of arguments for constructing a InstanceAppProfile resource.
        :param pulumi.Input[str] description: Long form description of the use case for this AppProfile.
        :param pulumi.Input[str] etag: Strongly validated etag for optimistic concurrency control. Preserve the value returned from `GetAppProfile` when calling `UpdateAppProfile` to fail the request if there has been a modification in the mean time. The `update_mask` of the request need not include `etag` for this protection to apply. See [Wikipedia](https://en.wikipedia.org/wiki/HTTP_ETag) and [RFC 7232](https://tools.ietf.org/html/rfc7232#section-2.3) for more details.
        :param pulumi.Input['MultiClusterRoutingUseAnyArgs'] multi_cluster_routing_use_any: Use a multi-cluster routing policy.
        :param pulumi.Input[str] name: The unique name of the app profile. Values are of the form `projects/{project}/instances/{instance}/appProfiles/_a-zA-Z0-9*`.
        :param pulumi.Input['SingleClusterRoutingArgs'] single_cluster_routing: Use a single-cluster routing policy.
        """
        pulumi.set(__self__, "app_profiles_id", app_profiles_id)
        pulumi.set(__self__, "instances_id", instances_id)
        pulumi.set(__self__, "projects_id", projects_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if multi_cluster_routing_use_any is not None:
            pulumi.set(__self__, "multi_cluster_routing_use_any", multi_cluster_routing_use_any)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if single_cluster_routing is not None:
            pulumi.set(__self__, "single_cluster_routing", single_cluster_routing)

    @property
    @pulumi.getter(name="appProfilesId")
    def app_profiles_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "app_profiles_id")

    @app_profiles_id.setter
    def app_profiles_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "app_profiles_id", value)

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
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Long form description of the use case for this AppProfile.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        Strongly validated etag for optimistic concurrency control. Preserve the value returned from `GetAppProfile` when calling `UpdateAppProfile` to fail the request if there has been a modification in the mean time. The `update_mask` of the request need not include `etag` for this protection to apply. See [Wikipedia](https://en.wikipedia.org/wiki/HTTP_ETag) and [RFC 7232](https://tools.ietf.org/html/rfc7232#section-2.3) for more details.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter(name="multiClusterRoutingUseAny")
    def multi_cluster_routing_use_any(self) -> Optional[pulumi.Input['MultiClusterRoutingUseAnyArgs']]:
        """
        Use a multi-cluster routing policy.
        """
        return pulumi.get(self, "multi_cluster_routing_use_any")

    @multi_cluster_routing_use_any.setter
    def multi_cluster_routing_use_any(self, value: Optional[pulumi.Input['MultiClusterRoutingUseAnyArgs']]):
        pulumi.set(self, "multi_cluster_routing_use_any", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The unique name of the app profile. Values are of the form `projects/{project}/instances/{instance}/appProfiles/_a-zA-Z0-9*`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="singleClusterRouting")
    def single_cluster_routing(self) -> Optional[pulumi.Input['SingleClusterRoutingArgs']]:
        """
        Use a single-cluster routing policy.
        """
        return pulumi.get(self, "single_cluster_routing")

    @single_cluster_routing.setter
    def single_cluster_routing(self, value: Optional[pulumi.Input['SingleClusterRoutingArgs']]):
        pulumi.set(self, "single_cluster_routing", value)


class InstanceAppProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_profiles_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 instances_id: Optional[pulumi.Input[str]] = None,
                 multi_cluster_routing_use_any: Optional[pulumi.Input[pulumi.InputType['MultiClusterRoutingUseAnyArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 single_cluster_routing: Optional[pulumi.Input[pulumi.InputType['SingleClusterRoutingArgs']]] = None,
                 __props__=None):
        """
        Creates an app profile within an instance.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Long form description of the use case for this AppProfile.
        :param pulumi.Input[str] etag: Strongly validated etag for optimistic concurrency control. Preserve the value returned from `GetAppProfile` when calling `UpdateAppProfile` to fail the request if there has been a modification in the mean time. The `update_mask` of the request need not include `etag` for this protection to apply. See [Wikipedia](https://en.wikipedia.org/wiki/HTTP_ETag) and [RFC 7232](https://tools.ietf.org/html/rfc7232#section-2.3) for more details.
        :param pulumi.Input[pulumi.InputType['MultiClusterRoutingUseAnyArgs']] multi_cluster_routing_use_any: Use a multi-cluster routing policy.
        :param pulumi.Input[str] name: The unique name of the app profile. Values are of the form `projects/{project}/instances/{instance}/appProfiles/_a-zA-Z0-9*`.
        :param pulumi.Input[pulumi.InputType['SingleClusterRoutingArgs']] single_cluster_routing: Use a single-cluster routing policy.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InstanceAppProfileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates an app profile within an instance.

        :param str resource_name: The name of the resource.
        :param InstanceAppProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceAppProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_profiles_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 instances_id: Optional[pulumi.Input[str]] = None,
                 multi_cluster_routing_use_any: Optional[pulumi.Input[pulumi.InputType['MultiClusterRoutingUseAnyArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 single_cluster_routing: Optional[pulumi.Input[pulumi.InputType['SingleClusterRoutingArgs']]] = None,
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
            __props__ = InstanceAppProfileArgs.__new__(InstanceAppProfileArgs)

            if app_profiles_id is None and not opts.urn:
                raise TypeError("Missing required property 'app_profiles_id'")
            __props__.__dict__["app_profiles_id"] = app_profiles_id
            __props__.__dict__["description"] = description
            __props__.__dict__["etag"] = etag
            if instances_id is None and not opts.urn:
                raise TypeError("Missing required property 'instances_id'")
            __props__.__dict__["instances_id"] = instances_id
            __props__.__dict__["multi_cluster_routing_use_any"] = multi_cluster_routing_use_any
            __props__.__dict__["name"] = name
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__.__dict__["projects_id"] = projects_id
            __props__.__dict__["single_cluster_routing"] = single_cluster_routing
        super(InstanceAppProfile, __self__).__init__(
            'google-native:bigtableadmin/v2:InstanceAppProfile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'InstanceAppProfile':
        """
        Get an existing InstanceAppProfile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InstanceAppProfileArgs.__new__(InstanceAppProfileArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["multi_cluster_routing_use_any"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["single_cluster_routing"] = None
        return InstanceAppProfile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Long form description of the use case for this AppProfile.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        Strongly validated etag for optimistic concurrency control. Preserve the value returned from `GetAppProfile` when calling `UpdateAppProfile` to fail the request if there has been a modification in the mean time. The `update_mask` of the request need not include `etag` for this protection to apply. See [Wikipedia](https://en.wikipedia.org/wiki/HTTP_ETag) and [RFC 7232](https://tools.ietf.org/html/rfc7232#section-2.3) for more details.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="multiClusterRoutingUseAny")
    def multi_cluster_routing_use_any(self) -> pulumi.Output['outputs.MultiClusterRoutingUseAnyResponse']:
        """
        Use a multi-cluster routing policy.
        """
        return pulumi.get(self, "multi_cluster_routing_use_any")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The unique name of the app profile. Values are of the form `projects/{project}/instances/{instance}/appProfiles/_a-zA-Z0-9*`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="singleClusterRouting")
    def single_cluster_routing(self) -> pulumi.Output['outputs.SingleClusterRoutingResponse']:
        """
        Use a single-cluster routing policy.
        """
        return pulumi.get(self, "single_cluster_routing")

