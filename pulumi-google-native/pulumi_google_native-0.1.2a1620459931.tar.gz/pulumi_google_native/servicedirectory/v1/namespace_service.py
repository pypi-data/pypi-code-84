# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = ['NamespaceServiceArgs', 'NamespaceService']

@pulumi.input_type
class NamespaceServiceArgs:
    def __init__(__self__, *,
                 locations_id: pulumi.Input[str],
                 namespaces_id: pulumi.Input[str],
                 projects_id: pulumi.Input[str],
                 services_id: pulumi.Input[str],
                 annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a NamespaceService resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] annotations: Optional. Annotations for the service. This data can be consumed by service clients. Restrictions: * The entire annotations dictionary may contain up to 2000 characters, spread accoss all key-value pairs. Annotations that go beyond this limit are rejected * Valid annotation keys have two segments: an optional prefix and name, separated by a slash (/). The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (.), not longer than 253 characters in total, followed by a slash (/). Annotations that fails to meet these requirements are rejected * The `(*.)google.com/` and `(*.)googleapis.com/` prefixes are reserved for system annotations managed by Service Directory. If the user tries to write to these keyspaces, those entries are silently ignored by the system Note: This field is equivalent to the `metadata` field in the v1beta1 API. They have the same syntax and read/write to the same location in Service Directory.
        :param pulumi.Input[str] name: Immutable. The resource name for the service in the format `projects/*/locations/*/namespaces/*/services/*`.
        """
        pulumi.set(__self__, "locations_id", locations_id)
        pulumi.set(__self__, "namespaces_id", namespaces_id)
        pulumi.set(__self__, "projects_id", projects_id)
        pulumi.set(__self__, "services_id", services_id)
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="locationsId")
    def locations_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "locations_id")

    @locations_id.setter
    def locations_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "locations_id", value)

    @property
    @pulumi.getter(name="namespacesId")
    def namespaces_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "namespaces_id")

    @namespaces_id.setter
    def namespaces_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespaces_id", value)

    @property
    @pulumi.getter(name="projectsId")
    def projects_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "projects_id")

    @projects_id.setter
    def projects_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "projects_id", value)

    @property
    @pulumi.getter(name="servicesId")
    def services_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "services_id")

    @services_id.setter
    def services_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "services_id", value)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Optional. Annotations for the service. This data can be consumed by service clients. Restrictions: * The entire annotations dictionary may contain up to 2000 characters, spread accoss all key-value pairs. Annotations that go beyond this limit are rejected * Valid annotation keys have two segments: an optional prefix and name, separated by a slash (/). The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (.), not longer than 253 characters in total, followed by a slash (/). Annotations that fails to meet these requirements are rejected * The `(*.)google.com/` and `(*.)googleapis.com/` prefixes are reserved for system annotations managed by Service Directory. If the user tries to write to these keyspaces, those entries are silently ignored by the system Note: This field is equivalent to the `metadata` field in the v1beta1 API. They have the same syntax and read/write to the same location in Service Directory.
        """
        return pulumi.get(self, "annotations")

    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "annotations", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Immutable. The resource name for the service in the format `projects/*/locations/*/namespaces/*/services/*`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class NamespaceService(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespaces_id: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 services_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a service, and returns the new service.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] annotations: Optional. Annotations for the service. This data can be consumed by service clients. Restrictions: * The entire annotations dictionary may contain up to 2000 characters, spread accoss all key-value pairs. Annotations that go beyond this limit are rejected * Valid annotation keys have two segments: an optional prefix and name, separated by a slash (/). The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (.), not longer than 253 characters in total, followed by a slash (/). Annotations that fails to meet these requirements are rejected * The `(*.)google.com/` and `(*.)googleapis.com/` prefixes are reserved for system annotations managed by Service Directory. If the user tries to write to these keyspaces, those entries are silently ignored by the system Note: This field is equivalent to the `metadata` field in the v1beta1 API. They have the same syntax and read/write to the same location in Service Directory.
        :param pulumi.Input[str] name: Immutable. The resource name for the service in the format `projects/*/locations/*/namespaces/*/services/*`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NamespaceServiceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a service, and returns the new service.

        :param str resource_name: The name of the resource.
        :param NamespaceServiceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NamespaceServiceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespaces_id: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 services_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = NamespaceServiceArgs.__new__(NamespaceServiceArgs)

            __props__.__dict__["annotations"] = annotations
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__.__dict__["locations_id"] = locations_id
            __props__.__dict__["name"] = name
            if namespaces_id is None and not opts.urn:
                raise TypeError("Missing required property 'namespaces_id'")
            __props__.__dict__["namespaces_id"] = namespaces_id
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__.__dict__["projects_id"] = projects_id
            if services_id is None and not opts.urn:
                raise TypeError("Missing required property 'services_id'")
            __props__.__dict__["services_id"] = services_id
            __props__.__dict__["endpoints"] = None
        super(NamespaceService, __self__).__init__(
            'google-native:servicedirectory/v1:NamespaceService',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NamespaceService':
        """
        Get an existing NamespaceService resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NamespaceServiceArgs.__new__(NamespaceServiceArgs)

        __props__.__dict__["annotations"] = None
        __props__.__dict__["endpoints"] = None
        __props__.__dict__["name"] = None
        return NamespaceService(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Optional. Annotations for the service. This data can be consumed by service clients. Restrictions: * The entire annotations dictionary may contain up to 2000 characters, spread accoss all key-value pairs. Annotations that go beyond this limit are rejected * Valid annotation keys have two segments: an optional prefix and name, separated by a slash (/). The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (.), not longer than 253 characters in total, followed by a slash (/). Annotations that fails to meet these requirements are rejected * The `(*.)google.com/` and `(*.)googleapis.com/` prefixes are reserved for system annotations managed by Service Directory. If the user tries to write to these keyspaces, those entries are silently ignored by the system Note: This field is equivalent to the `metadata` field in the v1beta1 API. They have the same syntax and read/write to the same location in Service Directory.
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter
    def endpoints(self) -> pulumi.Output[Sequence['outputs.EndpointResponse']]:
        """
        Endpoints associated with this service. Returned on LookupService.ResolveService. Control plane clients should use RegistrationService.ListEndpoints.
        """
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Immutable. The resource name for the service in the format `projects/*/locations/*/namespaces/*/services/*`.
        """
        return pulumi.get(self, "name")

