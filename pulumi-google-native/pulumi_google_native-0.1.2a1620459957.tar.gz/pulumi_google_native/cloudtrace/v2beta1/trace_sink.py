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

__all__ = ['TraceSinkArgs', 'TraceSink']

@pulumi.input_type
class TraceSinkArgs:
    def __init__(__self__, *,
                 projects_id: pulumi.Input[str],
                 trace_sinks_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 output_config: Optional[pulumi.Input['OutputConfigArgs']] = None):
        """
        The set of arguments for constructing a TraceSink resource.
        :param pulumi.Input[str] name: Required. The canonical sink resource name, unique within the project. Must be of the form: project/[PROJECT_NUMBER]/traceSinks/[SINK_ID]. E.g.: `"projects/12345/traceSinks/my-project-trace-sink"`. Sink identifiers are limited to 256 characters and can include only the following characters: upper and lower-case alphanumeric characters, underscores, hyphens, and periods.
        :param pulumi.Input['OutputConfigArgs'] output_config: Required. The export destination.
        """
        pulumi.set(__self__, "projects_id", projects_id)
        pulumi.set(__self__, "trace_sinks_id", trace_sinks_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if output_config is not None:
            pulumi.set(__self__, "output_config", output_config)

    @property
    @pulumi.getter(name="projectsId")
    def projects_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "projects_id")

    @projects_id.setter
    def projects_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "projects_id", value)

    @property
    @pulumi.getter(name="traceSinksId")
    def trace_sinks_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "trace_sinks_id")

    @trace_sinks_id.setter
    def trace_sinks_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "trace_sinks_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Required. The canonical sink resource name, unique within the project. Must be of the form: project/[PROJECT_NUMBER]/traceSinks/[SINK_ID]. E.g.: `"projects/12345/traceSinks/my-project-trace-sink"`. Sink identifiers are limited to 256 characters and can include only the following characters: upper and lower-case alphanumeric characters, underscores, hyphens, and periods.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="outputConfig")
    def output_config(self) -> Optional[pulumi.Input['OutputConfigArgs']]:
        """
        Required. The export destination.
        """
        return pulumi.get(self, "output_config")

    @output_config.setter
    def output_config(self, value: Optional[pulumi.Input['OutputConfigArgs']]):
        pulumi.set(self, "output_config", value)


class TraceSink(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 output_config: Optional[pulumi.Input[pulumi.InputType['OutputConfigArgs']]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 trace_sinks_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a sink that exports trace spans to a destination. The export of newly-ingested traces begins immediately, unless the sink's `writer_identity` is not permitted to write to the destination. A sink can export traces only from the resource owning the sink (the 'parent').

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Required. The canonical sink resource name, unique within the project. Must be of the form: project/[PROJECT_NUMBER]/traceSinks/[SINK_ID]. E.g.: `"projects/12345/traceSinks/my-project-trace-sink"`. Sink identifiers are limited to 256 characters and can include only the following characters: upper and lower-case alphanumeric characters, underscores, hyphens, and periods.
        :param pulumi.Input[pulumi.InputType['OutputConfigArgs']] output_config: Required. The export destination.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TraceSinkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a sink that exports trace spans to a destination. The export of newly-ingested traces begins immediately, unless the sink's `writer_identity` is not permitted to write to the destination. A sink can export traces only from the resource owning the sink (the 'parent').

        :param str resource_name: The name of the resource.
        :param TraceSinkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TraceSinkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 output_config: Optional[pulumi.Input[pulumi.InputType['OutputConfigArgs']]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 trace_sinks_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = TraceSinkArgs.__new__(TraceSinkArgs)

            __props__.__dict__["name"] = name
            __props__.__dict__["output_config"] = output_config
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__.__dict__["projects_id"] = projects_id
            if trace_sinks_id is None and not opts.urn:
                raise TypeError("Missing required property 'trace_sinks_id'")
            __props__.__dict__["trace_sinks_id"] = trace_sinks_id
            __props__.__dict__["writer_identity"] = None
        super(TraceSink, __self__).__init__(
            'google-native:cloudtrace/v2beta1:TraceSink',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TraceSink':
        """
        Get an existing TraceSink resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TraceSinkArgs.__new__(TraceSinkArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["output_config"] = None
        __props__.__dict__["writer_identity"] = None
        return TraceSink(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Required. The canonical sink resource name, unique within the project. Must be of the form: project/[PROJECT_NUMBER]/traceSinks/[SINK_ID]. E.g.: `"projects/12345/traceSinks/my-project-trace-sink"`. Sink identifiers are limited to 256 characters and can include only the following characters: upper and lower-case alphanumeric characters, underscores, hyphens, and periods.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="outputConfig")
    def output_config(self) -> pulumi.Output['outputs.OutputConfigResponse']:
        """
        Required. The export destination.
        """
        return pulumi.get(self, "output_config")

    @property
    @pulumi.getter(name="writerIdentity")
    def writer_identity(self) -> pulumi.Output[str]:
        """
        A service account name for exporting the data. This field is set by sinks.create and sinks.update. The service account will need to be granted write access to the destination specified in the output configuration, see [Granting access for a resource](/iam/docs/granting-roles-to-service-accounts#granting_access_to_a_service_account_for_a_resource). To create tables and write data this account will need the dataEditor role. Read more about roles in the [BigQuery documentation](https://cloud.google.com/bigquery/docs/access-control). E.g.: "service-00000001@00000002.iam.gserviceaccount.com"
        """
        return pulumi.get(self, "writer_identity")

