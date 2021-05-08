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

__all__ = ['OrganizationEnvironmentTraceConfigOverrideArgs', 'OrganizationEnvironmentTraceConfigOverride']

@pulumi.input_type
class OrganizationEnvironmentTraceConfigOverrideArgs:
    def __init__(__self__, *,
                 environments_id: pulumi.Input[str],
                 organizations_id: pulumi.Input[str],
                 overrides_id: pulumi.Input[str],
                 api_proxy: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sampling_config: Optional[pulumi.Input['GoogleCloudApigeeV1TraceSamplingConfigArgs']] = None):
        """
        The set of arguments for constructing a OrganizationEnvironmentTraceConfigOverride resource.
        :param pulumi.Input[str] api_proxy: ID of the API proxy that will have its trace configuration overridden.
        :param pulumi.Input[str] name: ID of the trace configuration override specified as a system-generated UUID.
        :param pulumi.Input['GoogleCloudApigeeV1TraceSamplingConfigArgs'] sampling_config: Trace configuration to override.
        """
        pulumi.set(__self__, "environments_id", environments_id)
        pulumi.set(__self__, "organizations_id", organizations_id)
        pulumi.set(__self__, "overrides_id", overrides_id)
        if api_proxy is not None:
            pulumi.set(__self__, "api_proxy", api_proxy)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if sampling_config is not None:
            pulumi.set(__self__, "sampling_config", sampling_config)

    @property
    @pulumi.getter(name="environmentsId")
    def environments_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "environments_id")

    @environments_id.setter
    def environments_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "environments_id", value)

    @property
    @pulumi.getter(name="organizationsId")
    def organizations_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "organizations_id")

    @organizations_id.setter
    def organizations_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "organizations_id", value)

    @property
    @pulumi.getter(name="overridesId")
    def overrides_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "overrides_id")

    @overrides_id.setter
    def overrides_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "overrides_id", value)

    @property
    @pulumi.getter(name="apiProxy")
    def api_proxy(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the API proxy that will have its trace configuration overridden.
        """
        return pulumi.get(self, "api_proxy")

    @api_proxy.setter
    def api_proxy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_proxy", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the trace configuration override specified as a system-generated UUID.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="samplingConfig")
    def sampling_config(self) -> Optional[pulumi.Input['GoogleCloudApigeeV1TraceSamplingConfigArgs']]:
        """
        Trace configuration to override.
        """
        return pulumi.get(self, "sampling_config")

    @sampling_config.setter
    def sampling_config(self, value: Optional[pulumi.Input['GoogleCloudApigeeV1TraceSamplingConfigArgs']]):
        pulumi.set(self, "sampling_config", value)


class OrganizationEnvironmentTraceConfigOverride(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_proxy: Optional[pulumi.Input[str]] = None,
                 environments_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organizations_id: Optional[pulumi.Input[str]] = None,
                 overrides_id: Optional[pulumi.Input[str]] = None,
                 sampling_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1TraceSamplingConfigArgs']]] = None,
                 __props__=None):
        """
        Creates a trace configuration override. The response contains a system-generated UUID, that can be used to view, update, or delete the configuration override. Use the List API to view the existing trace configuration overrides.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_proxy: ID of the API proxy that will have its trace configuration overridden.
        :param pulumi.Input[str] name: ID of the trace configuration override specified as a system-generated UUID.
        :param pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1TraceSamplingConfigArgs']] sampling_config: Trace configuration to override.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OrganizationEnvironmentTraceConfigOverrideArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a trace configuration override. The response contains a system-generated UUID, that can be used to view, update, or delete the configuration override. Use the List API to view the existing trace configuration overrides.

        :param str resource_name: The name of the resource.
        :param OrganizationEnvironmentTraceConfigOverrideArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OrganizationEnvironmentTraceConfigOverrideArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_proxy: Optional[pulumi.Input[str]] = None,
                 environments_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organizations_id: Optional[pulumi.Input[str]] = None,
                 overrides_id: Optional[pulumi.Input[str]] = None,
                 sampling_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudApigeeV1TraceSamplingConfigArgs']]] = None,
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
            __props__ = OrganizationEnvironmentTraceConfigOverrideArgs.__new__(OrganizationEnvironmentTraceConfigOverrideArgs)

            __props__.__dict__["api_proxy"] = api_proxy
            if environments_id is None and not opts.urn:
                raise TypeError("Missing required property 'environments_id'")
            __props__.__dict__["environments_id"] = environments_id
            __props__.__dict__["name"] = name
            if organizations_id is None and not opts.urn:
                raise TypeError("Missing required property 'organizations_id'")
            __props__.__dict__["organizations_id"] = organizations_id
            if overrides_id is None and not opts.urn:
                raise TypeError("Missing required property 'overrides_id'")
            __props__.__dict__["overrides_id"] = overrides_id
            __props__.__dict__["sampling_config"] = sampling_config
        super(OrganizationEnvironmentTraceConfigOverride, __self__).__init__(
            'google-native:apigee/v1:OrganizationEnvironmentTraceConfigOverride',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OrganizationEnvironmentTraceConfigOverride':
        """
        Get an existing OrganizationEnvironmentTraceConfigOverride resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OrganizationEnvironmentTraceConfigOverrideArgs.__new__(OrganizationEnvironmentTraceConfigOverrideArgs)

        __props__.__dict__["api_proxy"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["sampling_config"] = None
        return OrganizationEnvironmentTraceConfigOverride(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiProxy")
    def api_proxy(self) -> pulumi.Output[str]:
        """
        ID of the API proxy that will have its trace configuration overridden.
        """
        return pulumi.get(self, "api_proxy")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        ID of the trace configuration override specified as a system-generated UUID.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="samplingConfig")
    def sampling_config(self) -> pulumi.Output['outputs.GoogleCloudApigeeV1TraceSamplingConfigResponse']:
        """
        Trace configuration to override.
        """
        return pulumi.get(self, "sampling_config")

