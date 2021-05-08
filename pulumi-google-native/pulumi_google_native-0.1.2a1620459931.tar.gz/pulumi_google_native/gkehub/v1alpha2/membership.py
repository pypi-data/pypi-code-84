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

__all__ = ['MembershipArgs', 'Membership']

@pulumi.input_type
class MembershipArgs:
    def __init__(__self__, *,
                 locations_id: pulumi.Input[str],
                 memberships_id: pulumi.Input[str],
                 projects_id: pulumi.Input[str],
                 authority: Optional[pulumi.Input['AuthorityArgs']] = None,
                 endpoint: Optional[pulumi.Input['MembershipEndpointArgs']] = None,
                 external_id: Optional[pulumi.Input[str]] = None,
                 infrastructure_type: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Membership resource.
        :param pulumi.Input['AuthorityArgs'] authority: Optional. How to identify workloads from this Membership. See the documentation on Workload Identity for more details: https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity
        :param pulumi.Input['MembershipEndpointArgs'] endpoint: Optional. Endpoint information to reach this member.
        :param pulumi.Input[str] external_id: Optional. An externally-generated and managed ID for this Membership. This ID may be modified after creation, but this is not recommended. For GKE clusters, external_id is managed by the Hub API and updates will be ignored. The ID must match the regex: `a-zA-Z0-9*` If this Membership represents a Kubernetes cluster, this value should be set to the UID of the `kube-system` namespace object.
        :param pulumi.Input[str] infrastructure_type: Optional. The infrastructure type this Membership is running on.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. GCP labels for this membership.
        """
        pulumi.set(__self__, "locations_id", locations_id)
        pulumi.set(__self__, "memberships_id", memberships_id)
        pulumi.set(__self__, "projects_id", projects_id)
        if authority is not None:
            pulumi.set(__self__, "authority", authority)
        if endpoint is not None:
            pulumi.set(__self__, "endpoint", endpoint)
        if external_id is not None:
            pulumi.set(__self__, "external_id", external_id)
        if infrastructure_type is not None:
            pulumi.set(__self__, "infrastructure_type", infrastructure_type)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)

    @property
    @pulumi.getter(name="locationsId")
    def locations_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "locations_id")

    @locations_id.setter
    def locations_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "locations_id", value)

    @property
    @pulumi.getter(name="membershipsId")
    def memberships_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "memberships_id")

    @memberships_id.setter
    def memberships_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "memberships_id", value)

    @property
    @pulumi.getter(name="projectsId")
    def projects_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "projects_id")

    @projects_id.setter
    def projects_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "projects_id", value)

    @property
    @pulumi.getter
    def authority(self) -> Optional[pulumi.Input['AuthorityArgs']]:
        """
        Optional. How to identify workloads from this Membership. See the documentation on Workload Identity for more details: https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity
        """
        return pulumi.get(self, "authority")

    @authority.setter
    def authority(self, value: Optional[pulumi.Input['AuthorityArgs']]):
        pulumi.set(self, "authority", value)

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input['MembershipEndpointArgs']]:
        """
        Optional. Endpoint information to reach this member.
        """
        return pulumi.get(self, "endpoint")

    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input['MembershipEndpointArgs']]):
        pulumi.set(self, "endpoint", value)

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. An externally-generated and managed ID for this Membership. This ID may be modified after creation, but this is not recommended. For GKE clusters, external_id is managed by the Hub API and updates will be ignored. The ID must match the regex: `a-zA-Z0-9*` If this Membership represents a Kubernetes cluster, this value should be set to the UID of the `kube-system` namespace object.
        """
        return pulumi.get(self, "external_id")

    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_id", value)

    @property
    @pulumi.getter(name="infrastructureType")
    def infrastructure_type(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. The infrastructure type this Membership is running on.
        """
        return pulumi.get(self, "infrastructure_type")

    @infrastructure_type.setter
    def infrastructure_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "infrastructure_type", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Optional. GCP labels for this membership.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)


class Membership(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authority: Optional[pulumi.Input[pulumi.InputType['AuthorityArgs']]] = None,
                 endpoint: Optional[pulumi.Input[pulumi.InputType['MembershipEndpointArgs']]] = None,
                 external_id: Optional[pulumi.Input[str]] = None,
                 infrastructure_type: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 memberships_id: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Adds a new Membership.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AuthorityArgs']] authority: Optional. How to identify workloads from this Membership. See the documentation on Workload Identity for more details: https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity
        :param pulumi.Input[pulumi.InputType['MembershipEndpointArgs']] endpoint: Optional. Endpoint information to reach this member.
        :param pulumi.Input[str] external_id: Optional. An externally-generated and managed ID for this Membership. This ID may be modified after creation, but this is not recommended. For GKE clusters, external_id is managed by the Hub API and updates will be ignored. The ID must match the regex: `a-zA-Z0-9*` If this Membership represents a Kubernetes cluster, this value should be set to the UID of the `kube-system` namespace object.
        :param pulumi.Input[str] infrastructure_type: Optional. The infrastructure type this Membership is running on.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. GCP labels for this membership.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MembershipArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Adds a new Membership.

        :param str resource_name: The name of the resource.
        :param MembershipArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MembershipArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authority: Optional[pulumi.Input[pulumi.InputType['AuthorityArgs']]] = None,
                 endpoint: Optional[pulumi.Input[pulumi.InputType['MembershipEndpointArgs']]] = None,
                 external_id: Optional[pulumi.Input[str]] = None,
                 infrastructure_type: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 memberships_id: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = MembershipArgs.__new__(MembershipArgs)

            __props__.__dict__["authority"] = authority
            __props__.__dict__["endpoint"] = endpoint
            __props__.__dict__["external_id"] = external_id
            __props__.__dict__["infrastructure_type"] = infrastructure_type
            __props__.__dict__["labels"] = labels
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__.__dict__["locations_id"] = locations_id
            if memberships_id is None and not opts.urn:
                raise TypeError("Missing required property 'memberships_id'")
            __props__.__dict__["memberships_id"] = memberships_id
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__.__dict__["projects_id"] = projects_id
            __props__.__dict__["create_time"] = None
            __props__.__dict__["delete_time"] = None
            __props__.__dict__["description"] = None
            __props__.__dict__["last_connection_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["unique_id"] = None
            __props__.__dict__["update_time"] = None
        super(Membership, __self__).__init__(
            'google-native:gkehub/v1alpha2:Membership',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Membership':
        """
        Get an existing Membership resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MembershipArgs.__new__(MembershipArgs)

        __props__.__dict__["authority"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["delete_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["endpoint"] = None
        __props__.__dict__["external_id"] = None
        __props__.__dict__["infrastructure_type"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["last_connection_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["unique_id"] = None
        __props__.__dict__["update_time"] = None
        return Membership(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def authority(self) -> pulumi.Output['outputs.AuthorityResponse']:
        """
        Optional. How to identify workloads from this Membership. See the documentation on Workload Identity for more details: https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity
        """
        return pulumi.get(self, "authority")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        When the Membership was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> pulumi.Output[str]:
        """
        When the Membership was deleted.
        """
        return pulumi.get(self, "delete_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Description of this membership, limited to 63 characters. Must match the regex: `a-zA-Z0-9*` This field is present for legacy purposes.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output['outputs.MembershipEndpointResponse']:
        """
        Optional. Endpoint information to reach this member.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> pulumi.Output[str]:
        """
        Optional. An externally-generated and managed ID for this Membership. This ID may be modified after creation, but this is not recommended. For GKE clusters, external_id is managed by the Hub API and updates will be ignored. The ID must match the regex: `a-zA-Z0-9*` If this Membership represents a Kubernetes cluster, this value should be set to the UID of the `kube-system` namespace object.
        """
        return pulumi.get(self, "external_id")

    @property
    @pulumi.getter(name="infrastructureType")
    def infrastructure_type(self) -> pulumi.Output[str]:
        """
        Optional. The infrastructure type this Membership is running on.
        """
        return pulumi.get(self, "infrastructure_type")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Optional. GCP labels for this membership.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="lastConnectionTime")
    def last_connection_time(self) -> pulumi.Output[str]:
        """
        For clusters using Connect, the timestamp of the most recent connection established with Google Cloud. This time is updated every several minutes, not continuously. For clusters that do not use GKE Connect, or that have never connected successfully, this field will be unset.
        """
        return pulumi.get(self, "last_connection_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The full, unique name of this Membership resource in the format `projects/*/locations/*/memberships/{membership_id}`, set during creation. `membership_id` must be a valid RFC 1123 compliant DNS label: 1. At most 63 characters in length 2. It must consist of lower case alphanumeric characters or `-` 3. It must start and end with an alphanumeric character Which can be expressed as the regex: `[a-z0-9]([-a-z0-9]*[a-z0-9])?`, with a maximum length of 63 characters.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output['outputs.MembershipStateResponse']:
        """
        State of the Membership resource.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> pulumi.Output[str]:
        """
        Google-generated UUID for this resource. This is unique across all Membership resources. If a Membership resource is deleted and another resource with the same name is created, it gets a different unique_id.
        """
        return pulumi.get(self, "unique_id")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        When the Membership was last updated.
        """
        return pulumi.get(self, "update_time")

