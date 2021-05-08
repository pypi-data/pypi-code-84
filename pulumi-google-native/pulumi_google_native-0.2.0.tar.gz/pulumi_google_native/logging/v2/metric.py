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

__all__ = ['MetricArgs', 'Metric']

@pulumi.input_type
class MetricArgs:
    def __init__(__self__, *,
                 metrics_id: pulumi.Input[str],
                 projects_id: pulumi.Input[str],
                 bucket_options: Optional[pulumi.Input['BucketOptionsArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 label_extractors: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 metric_descriptor: Optional[pulumi.Input['MetricDescriptorArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 value_extractor: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Metric resource.
        :param pulumi.Input['BucketOptionsArgs'] bucket_options: Optional. The bucket_options are required when the logs-based metric is using a DISTRIBUTION value type and it describes the bucket boundaries used to create a histogram of the extracted values.
        :param pulumi.Input[str] description: Optional. A description of this metric, which is used in documentation. The maximum length of the description is 8000 characters.
        :param pulumi.Input[str] filter: Required. An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced_filters) which is used to match log entries. Example: "resource.type=gae_app AND severity>=ERROR" The maximum length of the filter is 20000 characters.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] label_extractors: Optional. A map from a label key string to an extractor expression which is used to extract data from a log entry field and assign as the label value. Each label key specified in the LabelDescriptor must have an associated extractor expression in this map. The syntax of the extractor expression is the same as for the value_extractor field.The extracted value is converted to the type defined in the label descriptor. If the either the extraction or the type conversion fails, the label will have a default value. The default value for a string label is an empty string, for an integer label its 0, and for a boolean label its false.Note that there are upper bounds on the maximum number of labels and the number of active time series that are allowed in a project.
        :param pulumi.Input['MetricDescriptorArgs'] metric_descriptor: Optional. The metric descriptor associated with the logs-based metric. If unspecified, it uses a default metric descriptor with a DELTA metric kind, INT64 value type, with no labels and a unit of "1". Such a metric counts the number of log entries matching the filter expression.The name, type, and description fields in the metric_descriptor are output only, and is constructed using the name and description field in the LogMetric.To create a logs-based metric that records a distribution of log values, a DELTA metric kind with a DISTRIBUTION value type must be used along with a value_extractor expression in the LogMetric.Each label in the metric descriptor must have a matching label name as the key and an extractor expression as the value in the label_extractors map.The metric_kind and value_type fields in the metric_descriptor cannot be updated once initially configured. New labels can be added in the metric_descriptor, but existing labels cannot be modified except for their description.
        :param pulumi.Input[str] name: Required. The client-assigned metric identifier. Examples: "error_count", "nginx/requests".Metric identifiers are limited to 100 characters and can include only the following characters: A-Z, a-z, 0-9, and the special characters _-.,+!*',()%/. The forward-slash character (/) denotes a hierarchy of name pieces, and it cannot be the first character of the name.The metric identifier in this field must not be URL-encoded (https://en.wikipedia.org/wiki/Percent-encoding). However, when the metric identifier appears as the [METRIC_ID] part of a metric_name API parameter, then the metric identifier must be URL-encoded. Example: "projects/my-project/metrics/nginx%2Frequests".
        :param pulumi.Input[str] value_extractor: Optional. A value_extractor is required when using a distribution logs-based metric to extract the values to record from a log entry. Two functions are supported for value extraction: EXTRACT(field) or REGEXP_EXTRACT(field, regex). The argument are: 1. field: The name of the log entry field from which the value is to be extracted. 2. regex: A regular expression using the Google RE2 syntax (https://github.com/google/re2/wiki/Syntax) with a single capture group to extract data from the specified log entry field. The value of the field is converted to a string before applying the regex. It is an error to specify a regex that does not include exactly one capture group.The result of the extraction must be convertible to a double type, as the distribution always records double values. If either the extraction or the conversion to double fails, then those values are not recorded in the distribution.Example: REGEXP_EXTRACT(jsonPayload.request, ".*quantity=(\d+).*")
        """
        pulumi.set(__self__, "metrics_id", metrics_id)
        pulumi.set(__self__, "projects_id", projects_id)
        if bucket_options is not None:
            pulumi.set(__self__, "bucket_options", bucket_options)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if filter is not None:
            pulumi.set(__self__, "filter", filter)
        if label_extractors is not None:
            pulumi.set(__self__, "label_extractors", label_extractors)
        if metric_descriptor is not None:
            pulumi.set(__self__, "metric_descriptor", metric_descriptor)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if value_extractor is not None:
            pulumi.set(__self__, "value_extractor", value_extractor)

    @property
    @pulumi.getter(name="metricsId")
    def metrics_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "metrics_id")

    @metrics_id.setter
    def metrics_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "metrics_id", value)

    @property
    @pulumi.getter(name="projectsId")
    def projects_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "projects_id")

    @projects_id.setter
    def projects_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "projects_id", value)

    @property
    @pulumi.getter(name="bucketOptions")
    def bucket_options(self) -> Optional[pulumi.Input['BucketOptionsArgs']]:
        """
        Optional. The bucket_options are required when the logs-based metric is using a DISTRIBUTION value type and it describes the bucket boundaries used to create a histogram of the extracted values.
        """
        return pulumi.get(self, "bucket_options")

    @bucket_options.setter
    def bucket_options(self, value: Optional[pulumi.Input['BucketOptionsArgs']]):
        pulumi.set(self, "bucket_options", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. A description of this metric, which is used in documentation. The maximum length of the description is 8000 characters.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[str]]:
        """
        Required. An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced_filters) which is used to match log entries. Example: "resource.type=gae_app AND severity>=ERROR" The maximum length of the filter is 20000 characters.
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filter", value)

    @property
    @pulumi.getter(name="labelExtractors")
    def label_extractors(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Optional. A map from a label key string to an extractor expression which is used to extract data from a log entry field and assign as the label value. Each label key specified in the LabelDescriptor must have an associated extractor expression in this map. The syntax of the extractor expression is the same as for the value_extractor field.The extracted value is converted to the type defined in the label descriptor. If the either the extraction or the type conversion fails, the label will have a default value. The default value for a string label is an empty string, for an integer label its 0, and for a boolean label its false.Note that there are upper bounds on the maximum number of labels and the number of active time series that are allowed in a project.
        """
        return pulumi.get(self, "label_extractors")

    @label_extractors.setter
    def label_extractors(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "label_extractors", value)

    @property
    @pulumi.getter(name="metricDescriptor")
    def metric_descriptor(self) -> Optional[pulumi.Input['MetricDescriptorArgs']]:
        """
        Optional. The metric descriptor associated with the logs-based metric. If unspecified, it uses a default metric descriptor with a DELTA metric kind, INT64 value type, with no labels and a unit of "1". Such a metric counts the number of log entries matching the filter expression.The name, type, and description fields in the metric_descriptor are output only, and is constructed using the name and description field in the LogMetric.To create a logs-based metric that records a distribution of log values, a DELTA metric kind with a DISTRIBUTION value type must be used along with a value_extractor expression in the LogMetric.Each label in the metric descriptor must have a matching label name as the key and an extractor expression as the value in the label_extractors map.The metric_kind and value_type fields in the metric_descriptor cannot be updated once initially configured. New labels can be added in the metric_descriptor, but existing labels cannot be modified except for their description.
        """
        return pulumi.get(self, "metric_descriptor")

    @metric_descriptor.setter
    def metric_descriptor(self, value: Optional[pulumi.Input['MetricDescriptorArgs']]):
        pulumi.set(self, "metric_descriptor", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Required. The client-assigned metric identifier. Examples: "error_count", "nginx/requests".Metric identifiers are limited to 100 characters and can include only the following characters: A-Z, a-z, 0-9, and the special characters _-.,+!*',()%/. The forward-slash character (/) denotes a hierarchy of name pieces, and it cannot be the first character of the name.The metric identifier in this field must not be URL-encoded (https://en.wikipedia.org/wiki/Percent-encoding). However, when the metric identifier appears as the [METRIC_ID] part of a metric_name API parameter, then the metric identifier must be URL-encoded. Example: "projects/my-project/metrics/nginx%2Frequests".
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="valueExtractor")
    def value_extractor(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. A value_extractor is required when using a distribution logs-based metric to extract the values to record from a log entry. Two functions are supported for value extraction: EXTRACT(field) or REGEXP_EXTRACT(field, regex). The argument are: 1. field: The name of the log entry field from which the value is to be extracted. 2. regex: A regular expression using the Google RE2 syntax (https://github.com/google/re2/wiki/Syntax) with a single capture group to extract data from the specified log entry field. The value of the field is converted to a string before applying the regex. It is an error to specify a regex that does not include exactly one capture group.The result of the extraction must be convertible to a double type, as the distribution always records double values. If either the extraction or the conversion to double fails, then those values are not recorded in the distribution.Example: REGEXP_EXTRACT(jsonPayload.request, ".*quantity=(\d+).*")
        """
        return pulumi.get(self, "value_extractor")

    @value_extractor.setter
    def value_extractor(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value_extractor", value)


class Metric(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket_options: Optional[pulumi.Input[pulumi.InputType['BucketOptionsArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 label_extractors: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 metric_descriptor: Optional[pulumi.Input[pulumi.InputType['MetricDescriptorArgs']]] = None,
                 metrics_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 value_extractor: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a logs-based metric.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['BucketOptionsArgs']] bucket_options: Optional. The bucket_options are required when the logs-based metric is using a DISTRIBUTION value type and it describes the bucket boundaries used to create a histogram of the extracted values.
        :param pulumi.Input[str] description: Optional. A description of this metric, which is used in documentation. The maximum length of the description is 8000 characters.
        :param pulumi.Input[str] filter: Required. An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced_filters) which is used to match log entries. Example: "resource.type=gae_app AND severity>=ERROR" The maximum length of the filter is 20000 characters.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] label_extractors: Optional. A map from a label key string to an extractor expression which is used to extract data from a log entry field and assign as the label value. Each label key specified in the LabelDescriptor must have an associated extractor expression in this map. The syntax of the extractor expression is the same as for the value_extractor field.The extracted value is converted to the type defined in the label descriptor. If the either the extraction or the type conversion fails, the label will have a default value. The default value for a string label is an empty string, for an integer label its 0, and for a boolean label its false.Note that there are upper bounds on the maximum number of labels and the number of active time series that are allowed in a project.
        :param pulumi.Input[pulumi.InputType['MetricDescriptorArgs']] metric_descriptor: Optional. The metric descriptor associated with the logs-based metric. If unspecified, it uses a default metric descriptor with a DELTA metric kind, INT64 value type, with no labels and a unit of "1". Such a metric counts the number of log entries matching the filter expression.The name, type, and description fields in the metric_descriptor are output only, and is constructed using the name and description field in the LogMetric.To create a logs-based metric that records a distribution of log values, a DELTA metric kind with a DISTRIBUTION value type must be used along with a value_extractor expression in the LogMetric.Each label in the metric descriptor must have a matching label name as the key and an extractor expression as the value in the label_extractors map.The metric_kind and value_type fields in the metric_descriptor cannot be updated once initially configured. New labels can be added in the metric_descriptor, but existing labels cannot be modified except for their description.
        :param pulumi.Input[str] name: Required. The client-assigned metric identifier. Examples: "error_count", "nginx/requests".Metric identifiers are limited to 100 characters and can include only the following characters: A-Z, a-z, 0-9, and the special characters _-.,+!*',()%/. The forward-slash character (/) denotes a hierarchy of name pieces, and it cannot be the first character of the name.The metric identifier in this field must not be URL-encoded (https://en.wikipedia.org/wiki/Percent-encoding). However, when the metric identifier appears as the [METRIC_ID] part of a metric_name API parameter, then the metric identifier must be URL-encoded. Example: "projects/my-project/metrics/nginx%2Frequests".
        :param pulumi.Input[str] value_extractor: Optional. A value_extractor is required when using a distribution logs-based metric to extract the values to record from a log entry. Two functions are supported for value extraction: EXTRACT(field) or REGEXP_EXTRACT(field, regex). The argument are: 1. field: The name of the log entry field from which the value is to be extracted. 2. regex: A regular expression using the Google RE2 syntax (https://github.com/google/re2/wiki/Syntax) with a single capture group to extract data from the specified log entry field. The value of the field is converted to a string before applying the regex. It is an error to specify a regex that does not include exactly one capture group.The result of the extraction must be convertible to a double type, as the distribution always records double values. If either the extraction or the conversion to double fails, then those values are not recorded in the distribution.Example: REGEXP_EXTRACT(jsonPayload.request, ".*quantity=(\d+).*")
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MetricArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a logs-based metric.

        :param str resource_name: The name of the resource.
        :param MetricArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MetricArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket_options: Optional[pulumi.Input[pulumi.InputType['BucketOptionsArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 label_extractors: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 metric_descriptor: Optional[pulumi.Input[pulumi.InputType['MetricDescriptorArgs']]] = None,
                 metrics_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 value_extractor: Optional[pulumi.Input[str]] = None,
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
            __props__ = MetricArgs.__new__(MetricArgs)

            __props__.__dict__["bucket_options"] = bucket_options
            __props__.__dict__["description"] = description
            __props__.__dict__["filter"] = filter
            __props__.__dict__["label_extractors"] = label_extractors
            __props__.__dict__["metric_descriptor"] = metric_descriptor
            if metrics_id is None and not opts.urn:
                raise TypeError("Missing required property 'metrics_id'")
            __props__.__dict__["metrics_id"] = metrics_id
            __props__.__dict__["name"] = name
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__.__dict__["projects_id"] = projects_id
            __props__.__dict__["value_extractor"] = value_extractor
            __props__.__dict__["create_time"] = None
            __props__.__dict__["update_time"] = None
        super(Metric, __self__).__init__(
            'google-native:logging/v2:Metric',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Metric':
        """
        Get an existing Metric resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MetricArgs.__new__(MetricArgs)

        __props__.__dict__["bucket_options"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["filter"] = None
        __props__.__dict__["label_extractors"] = None
        __props__.__dict__["metric_descriptor"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["update_time"] = None
        __props__.__dict__["value_extractor"] = None
        return Metric(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bucketOptions")
    def bucket_options(self) -> pulumi.Output['outputs.BucketOptionsResponse']:
        """
        Optional. The bucket_options are required when the logs-based metric is using a DISTRIBUTION value type and it describes the bucket boundaries used to create a histogram of the extracted values.
        """
        return pulumi.get(self, "bucket_options")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The creation timestamp of the metric.This field may not be present for older metrics.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Optional. A description of this metric, which is used in documentation. The maximum length of the description is 8000 characters.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def filter(self) -> pulumi.Output[str]:
        """
        Required. An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced_filters) which is used to match log entries. Example: "resource.type=gae_app AND severity>=ERROR" The maximum length of the filter is 20000 characters.
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter(name="labelExtractors")
    def label_extractors(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Optional. A map from a label key string to an extractor expression which is used to extract data from a log entry field and assign as the label value. Each label key specified in the LabelDescriptor must have an associated extractor expression in this map. The syntax of the extractor expression is the same as for the value_extractor field.The extracted value is converted to the type defined in the label descriptor. If the either the extraction or the type conversion fails, the label will have a default value. The default value for a string label is an empty string, for an integer label its 0, and for a boolean label its false.Note that there are upper bounds on the maximum number of labels and the number of active time series that are allowed in a project.
        """
        return pulumi.get(self, "label_extractors")

    @property
    @pulumi.getter(name="metricDescriptor")
    def metric_descriptor(self) -> pulumi.Output['outputs.MetricDescriptorResponse']:
        """
        Optional. The metric descriptor associated with the logs-based metric. If unspecified, it uses a default metric descriptor with a DELTA metric kind, INT64 value type, with no labels and a unit of "1". Such a metric counts the number of log entries matching the filter expression.The name, type, and description fields in the metric_descriptor are output only, and is constructed using the name and description field in the LogMetric.To create a logs-based metric that records a distribution of log values, a DELTA metric kind with a DISTRIBUTION value type must be used along with a value_extractor expression in the LogMetric.Each label in the metric descriptor must have a matching label name as the key and an extractor expression as the value in the label_extractors map.The metric_kind and value_type fields in the metric_descriptor cannot be updated once initially configured. New labels can be added in the metric_descriptor, but existing labels cannot be modified except for their description.
        """
        return pulumi.get(self, "metric_descriptor")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Required. The client-assigned metric identifier. Examples: "error_count", "nginx/requests".Metric identifiers are limited to 100 characters and can include only the following characters: A-Z, a-z, 0-9, and the special characters _-.,+!*',()%/. The forward-slash character (/) denotes a hierarchy of name pieces, and it cannot be the first character of the name.The metric identifier in this field must not be URL-encoded (https://en.wikipedia.org/wiki/Percent-encoding). However, when the metric identifier appears as the [METRIC_ID] part of a metric_name API parameter, then the metric identifier must be URL-encoded. Example: "projects/my-project/metrics/nginx%2Frequests".
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The last update timestamp of the metric.This field may not be present for older metrics.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter(name="valueExtractor")
    def value_extractor(self) -> pulumi.Output[str]:
        """
        Optional. A value_extractor is required when using a distribution logs-based metric to extract the values to record from a log entry. Two functions are supported for value extraction: EXTRACT(field) or REGEXP_EXTRACT(field, regex). The argument are: 1. field: The name of the log entry field from which the value is to be extracted. 2. regex: A regular expression using the Google RE2 syntax (https://github.com/google/re2/wiki/Syntax) with a single capture group to extract data from the specified log entry field. The value of the field is converted to a string before applying the regex. It is an error to specify a regex that does not include exactly one capture group.The result of the extraction must be convertible to a double type, as the distribution always records double values. If either the extraction or the conversion to double fails, then those values are not recorded in the distribution.Example: REGEXP_EXTRACT(jsonPayload.request, ".*quantity=(\d+).*")
        """
        return pulumi.get(self, "value_extractor")

