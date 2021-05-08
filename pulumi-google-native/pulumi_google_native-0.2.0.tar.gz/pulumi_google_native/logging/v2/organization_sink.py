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

__all__ = ['OrganizationSinkArgs', 'OrganizationSink']

@pulumi.input_type
class OrganizationSinkArgs:
    def __init__(__self__, *,
                 organizations_id: pulumi.Input[str],
                 sinks_id: pulumi.Input[str],
                 bigquery_options: Optional[pulumi.Input['BigQueryOptionsArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination: Optional[pulumi.Input[str]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 exclusions: Optional[pulumi.Input[Sequence[pulumi.Input['LogExclusionArgs']]]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 include_children: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 unique_writer_identity: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a OrganizationSink resource.
        :param pulumi.Input['BigQueryOptionsArgs'] bigquery_options: Optional. Options that affect sinks exporting data to BigQuery.
        :param pulumi.Input[str] description: Optional. A description of this sink. The maximum length of the description is 8000 characters.
        :param pulumi.Input[str] destination: Required. The export destination: "storage.googleapis.com/[GCS_BUCKET]" "bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]" "pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]" The sink's writer_identity, set when the sink is created, must have permission to write to the destination or else the log entries are not exported. For more information, see Exporting Logs with Sinks (https://cloud.google.com/logging/docs/api/tasks/exporting-logs).
        :param pulumi.Input[bool] disabled: Optional. If set to True, then this sink is disabled and it does not export any log entries.
        :param pulumi.Input[Sequence[pulumi.Input['LogExclusionArgs']]] exclusions: Optional. Log entries that match any of the exclusion filters will not be exported. If a log entry is matched by both filter and one of exclusion_filters it will not be exported.
        :param pulumi.Input[str] filter: Optional. An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced-queries). The only exported log entries are those that are in the resource owning the sink and that match the filter. For example: logName="projects/[PROJECT_ID]/logs/[LOG_ID]" AND severity>=ERROR 
        :param pulumi.Input[bool] include_children: Optional. This field applies only to sinks owned by organizations and folders. If the field is false, the default, only the logs owned by the sink's parent resource are available for export. If the field is true, then logs from all the projects, folders, and billing accounts contained in the sink's parent resource are also available for export. Whether a particular log entry from the children is exported depends on the sink's filter expression. For example, if this field is true, then the filter resource.type=gce_instance would export all Compute Engine VM instance log entries from all projects in the sink's parent. To only export entries from certain child projects, filter on the project part of the log name: logName:("projects/test-project1/" OR "projects/test-project2/") AND resource.type=gce_instance 
        :param pulumi.Input[str] name: Required. The client-assigned sink identifier, unique within the project. Example: "my-syslog-errors-to-pubsub". Sink identifiers are limited to 100 characters and can include only the following characters: upper and lower-case alphanumeric characters, underscores, hyphens, and periods. First character has to be alphanumeric.
        """
        pulumi.set(__self__, "organizations_id", organizations_id)
        pulumi.set(__self__, "sinks_id", sinks_id)
        if bigquery_options is not None:
            pulumi.set(__self__, "bigquery_options", bigquery_options)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if destination is not None:
            pulumi.set(__self__, "destination", destination)
        if disabled is not None:
            pulumi.set(__self__, "disabled", disabled)
        if exclusions is not None:
            pulumi.set(__self__, "exclusions", exclusions)
        if filter is not None:
            pulumi.set(__self__, "filter", filter)
        if include_children is not None:
            pulumi.set(__self__, "include_children", include_children)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if unique_writer_identity is not None:
            pulumi.set(__self__, "unique_writer_identity", unique_writer_identity)

    @property
    @pulumi.getter(name="organizationsId")
    def organizations_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "organizations_id")

    @organizations_id.setter
    def organizations_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "organizations_id", value)

    @property
    @pulumi.getter(name="sinksId")
    def sinks_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "sinks_id")

    @sinks_id.setter
    def sinks_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "sinks_id", value)

    @property
    @pulumi.getter(name="bigqueryOptions")
    def bigquery_options(self) -> Optional[pulumi.Input['BigQueryOptionsArgs']]:
        """
        Optional. Options that affect sinks exporting data to BigQuery.
        """
        return pulumi.get(self, "bigquery_options")

    @bigquery_options.setter
    def bigquery_options(self, value: Optional[pulumi.Input['BigQueryOptionsArgs']]):
        pulumi.set(self, "bigquery_options", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. A description of this sink. The maximum length of the description is 8000 characters.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[str]]:
        """
        Required. The export destination: "storage.googleapis.com/[GCS_BUCKET]" "bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]" "pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]" The sink's writer_identity, set when the sink is created, must have permission to write to the destination or else the log entries are not exported. For more information, see Exporting Logs with Sinks (https://cloud.google.com/logging/docs/api/tasks/exporting-logs).
        """
        return pulumi.get(self, "destination")

    @destination.setter
    def destination(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination", value)

    @property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Optional. If set to True, then this sink is disabled and it does not export any log entries.
        """
        return pulumi.get(self, "disabled")

    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disabled", value)

    @property
    @pulumi.getter
    def exclusions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LogExclusionArgs']]]]:
        """
        Optional. Log entries that match any of the exclusion filters will not be exported. If a log entry is matched by both filter and one of exclusion_filters it will not be exported.
        """
        return pulumi.get(self, "exclusions")

    @exclusions.setter
    def exclusions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LogExclusionArgs']]]]):
        pulumi.set(self, "exclusions", value)

    @property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced-queries). The only exported log entries are those that are in the resource owning the sink and that match the filter. For example: logName="projects/[PROJECT_ID]/logs/[LOG_ID]" AND severity>=ERROR 
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filter", value)

    @property
    @pulumi.getter(name="includeChildren")
    def include_children(self) -> Optional[pulumi.Input[bool]]:
        """
        Optional. This field applies only to sinks owned by organizations and folders. If the field is false, the default, only the logs owned by the sink's parent resource are available for export. If the field is true, then logs from all the projects, folders, and billing accounts contained in the sink's parent resource are also available for export. Whether a particular log entry from the children is exported depends on the sink's filter expression. For example, if this field is true, then the filter resource.type=gce_instance would export all Compute Engine VM instance log entries from all projects in the sink's parent. To only export entries from certain child projects, filter on the project part of the log name: logName:("projects/test-project1/" OR "projects/test-project2/") AND resource.type=gce_instance 
        """
        return pulumi.get(self, "include_children")

    @include_children.setter
    def include_children(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_children", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Required. The client-assigned sink identifier, unique within the project. Example: "my-syslog-errors-to-pubsub". Sink identifiers are limited to 100 characters and can include only the following characters: upper and lower-case alphanumeric characters, underscores, hyphens, and periods. First character has to be alphanumeric.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="uniqueWriterIdentity")
    def unique_writer_identity(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "unique_writer_identity")

    @unique_writer_identity.setter
    def unique_writer_identity(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "unique_writer_identity", value)


class OrganizationSink(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bigquery_options: Optional[pulumi.Input[pulumi.InputType['BigQueryOptionsArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination: Optional[pulumi.Input[str]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 exclusions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LogExclusionArgs']]]]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 include_children: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organizations_id: Optional[pulumi.Input[str]] = None,
                 sinks_id: Optional[pulumi.Input[str]] = None,
                 unique_writer_identity: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a sink that exports specified log entries to a destination. The export of newly-ingested log entries begins immediately, unless the sink's writer_identity is not permitted to write to the destination. A sink can export log entries only from the resource owning the sink.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['BigQueryOptionsArgs']] bigquery_options: Optional. Options that affect sinks exporting data to BigQuery.
        :param pulumi.Input[str] description: Optional. A description of this sink. The maximum length of the description is 8000 characters.
        :param pulumi.Input[str] destination: Required. The export destination: "storage.googleapis.com/[GCS_BUCKET]" "bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]" "pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]" The sink's writer_identity, set when the sink is created, must have permission to write to the destination or else the log entries are not exported. For more information, see Exporting Logs with Sinks (https://cloud.google.com/logging/docs/api/tasks/exporting-logs).
        :param pulumi.Input[bool] disabled: Optional. If set to True, then this sink is disabled and it does not export any log entries.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LogExclusionArgs']]]] exclusions: Optional. Log entries that match any of the exclusion filters will not be exported. If a log entry is matched by both filter and one of exclusion_filters it will not be exported.
        :param pulumi.Input[str] filter: Optional. An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced-queries). The only exported log entries are those that are in the resource owning the sink and that match the filter. For example: logName="projects/[PROJECT_ID]/logs/[LOG_ID]" AND severity>=ERROR 
        :param pulumi.Input[bool] include_children: Optional. This field applies only to sinks owned by organizations and folders. If the field is false, the default, only the logs owned by the sink's parent resource are available for export. If the field is true, then logs from all the projects, folders, and billing accounts contained in the sink's parent resource are also available for export. Whether a particular log entry from the children is exported depends on the sink's filter expression. For example, if this field is true, then the filter resource.type=gce_instance would export all Compute Engine VM instance log entries from all projects in the sink's parent. To only export entries from certain child projects, filter on the project part of the log name: logName:("projects/test-project1/" OR "projects/test-project2/") AND resource.type=gce_instance 
        :param pulumi.Input[str] name: Required. The client-assigned sink identifier, unique within the project. Example: "my-syslog-errors-to-pubsub". Sink identifiers are limited to 100 characters and can include only the following characters: upper and lower-case alphanumeric characters, underscores, hyphens, and periods. First character has to be alphanumeric.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OrganizationSinkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a sink that exports specified log entries to a destination. The export of newly-ingested log entries begins immediately, unless the sink's writer_identity is not permitted to write to the destination. A sink can export log entries only from the resource owning the sink.

        :param str resource_name: The name of the resource.
        :param OrganizationSinkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OrganizationSinkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bigquery_options: Optional[pulumi.Input[pulumi.InputType['BigQueryOptionsArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination: Optional[pulumi.Input[str]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 exclusions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LogExclusionArgs']]]]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 include_children: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organizations_id: Optional[pulumi.Input[str]] = None,
                 sinks_id: Optional[pulumi.Input[str]] = None,
                 unique_writer_identity: Optional[pulumi.Input[str]] = None,
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
            __props__ = OrganizationSinkArgs.__new__(OrganizationSinkArgs)

            __props__.__dict__["bigquery_options"] = bigquery_options
            __props__.__dict__["description"] = description
            __props__.__dict__["destination"] = destination
            __props__.__dict__["disabled"] = disabled
            __props__.__dict__["exclusions"] = exclusions
            __props__.__dict__["filter"] = filter
            __props__.__dict__["include_children"] = include_children
            __props__.__dict__["name"] = name
            if organizations_id is None and not opts.urn:
                raise TypeError("Missing required property 'organizations_id'")
            __props__.__dict__["organizations_id"] = organizations_id
            if sinks_id is None and not opts.urn:
                raise TypeError("Missing required property 'sinks_id'")
            __props__.__dict__["sinks_id"] = sinks_id
            __props__.__dict__["unique_writer_identity"] = unique_writer_identity
            __props__.__dict__["create_time"] = None
            __props__.__dict__["update_time"] = None
            __props__.__dict__["writer_identity"] = None
        super(OrganizationSink, __self__).__init__(
            'google-native:logging/v2:OrganizationSink',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OrganizationSink':
        """
        Get an existing OrganizationSink resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OrganizationSinkArgs.__new__(OrganizationSinkArgs)

        __props__.__dict__["bigquery_options"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["destination"] = None
        __props__.__dict__["disabled"] = None
        __props__.__dict__["exclusions"] = None
        __props__.__dict__["filter"] = None
        __props__.__dict__["include_children"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["update_time"] = None
        __props__.__dict__["writer_identity"] = None
        return OrganizationSink(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bigqueryOptions")
    def bigquery_options(self) -> pulumi.Output['outputs.BigQueryOptionsResponse']:
        """
        Optional. Options that affect sinks exporting data to BigQuery.
        """
        return pulumi.get(self, "bigquery_options")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The creation timestamp of the sink.This field may not be present for older sinks.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Optional. A description of this sink. The maximum length of the description is 8000 characters.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def destination(self) -> pulumi.Output[str]:
        """
        Required. The export destination: "storage.googleapis.com/[GCS_BUCKET]" "bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]" "pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]" The sink's writer_identity, set when the sink is created, must have permission to write to the destination or else the log entries are not exported. For more information, see Exporting Logs with Sinks (https://cloud.google.com/logging/docs/api/tasks/exporting-logs).
        """
        return pulumi.get(self, "destination")

    @property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[bool]:
        """
        Optional. If set to True, then this sink is disabled and it does not export any log entries.
        """
        return pulumi.get(self, "disabled")

    @property
    @pulumi.getter
    def exclusions(self) -> pulumi.Output[Sequence['outputs.LogExclusionResponse']]:
        """
        Optional. Log entries that match any of the exclusion filters will not be exported. If a log entry is matched by both filter and one of exclusion_filters it will not be exported.
        """
        return pulumi.get(self, "exclusions")

    @property
    @pulumi.getter
    def filter(self) -> pulumi.Output[str]:
        """
        Optional. An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced-queries). The only exported log entries are those that are in the resource owning the sink and that match the filter. For example: logName="projects/[PROJECT_ID]/logs/[LOG_ID]" AND severity>=ERROR 
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter(name="includeChildren")
    def include_children(self) -> pulumi.Output[bool]:
        """
        Optional. This field applies only to sinks owned by organizations and folders. If the field is false, the default, only the logs owned by the sink's parent resource are available for export. If the field is true, then logs from all the projects, folders, and billing accounts contained in the sink's parent resource are also available for export. Whether a particular log entry from the children is exported depends on the sink's filter expression. For example, if this field is true, then the filter resource.type=gce_instance would export all Compute Engine VM instance log entries from all projects in the sink's parent. To only export entries from certain child projects, filter on the project part of the log name: logName:("projects/test-project1/" OR "projects/test-project2/") AND resource.type=gce_instance 
        """
        return pulumi.get(self, "include_children")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Required. The client-assigned sink identifier, unique within the project. Example: "my-syslog-errors-to-pubsub". Sink identifiers are limited to 100 characters and can include only the following characters: upper and lower-case alphanumeric characters, underscores, hyphens, and periods. First character has to be alphanumeric.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The last update timestamp of the sink.This field may not be present for older sinks.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter(name="writerIdentity")
    def writer_identity(self) -> pulumi.Output[str]:
        """
        An IAM identity—a service account or group—under which Logging writes the exported log entries to the sink's destination. This field is set by sinks.create and sinks.update based on the value of unique_writer_identity in those methods.Until you grant this identity write-access to the destination, log entry exports from this sink will fail. For more information, see Granting Access for a Resource (https://cloud.google.com/iam/docs/granting-roles-to-service-accounts#granting_access_to_a_service_account_for_a_resource). Consult the destination service's documentation to determine the appropriate IAM roles to assign to the identity.
        """
        return pulumi.get(self, "writer_identity")

