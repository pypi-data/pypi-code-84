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

__all__ = ['OrganizationReplayArgs', 'OrganizationReplay']

@pulumi.input_type
class OrganizationReplayArgs:
    def __init__(__self__, *,
                 locations_id: pulumi.Input[str],
                 organizations_id: pulumi.Input[str],
                 replays_id: pulumi.Input[str],
                 config: Optional[pulumi.Input['GoogleCloudPolicysimulatorV1beta1ReplayConfigArgs']] = None):
        """
        The set of arguments for constructing a OrganizationReplay resource.
        :param pulumi.Input['GoogleCloudPolicysimulatorV1beta1ReplayConfigArgs'] config: Required. The configuration used for the `Replay`.
        """
        pulumi.set(__self__, "locations_id", locations_id)
        pulumi.set(__self__, "organizations_id", organizations_id)
        pulumi.set(__self__, "replays_id", replays_id)
        if config is not None:
            pulumi.set(__self__, "config", config)

    @property
    @pulumi.getter(name="locationsId")
    def locations_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "locations_id")

    @locations_id.setter
    def locations_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "locations_id", value)

    @property
    @pulumi.getter(name="organizationsId")
    def organizations_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "organizations_id")

    @organizations_id.setter
    def organizations_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "organizations_id", value)

    @property
    @pulumi.getter(name="replaysId")
    def replays_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "replays_id")

    @replays_id.setter
    def replays_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "replays_id", value)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input['GoogleCloudPolicysimulatorV1beta1ReplayConfigArgs']]:
        """
        Required. The configuration used for the `Replay`.
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input['GoogleCloudPolicysimulatorV1beta1ReplayConfigArgs']]):
        pulumi.set(self, "config", value)


class OrganizationReplay(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudPolicysimulatorV1beta1ReplayConfigArgs']]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 organizations_id: Optional[pulumi.Input[str]] = None,
                 replays_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates and starts a Replay using the given ReplayConfig.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['GoogleCloudPolicysimulatorV1beta1ReplayConfigArgs']] config: Required. The configuration used for the `Replay`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OrganizationReplayArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates and starts a Replay using the given ReplayConfig.

        :param str resource_name: The name of the resource.
        :param OrganizationReplayArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OrganizationReplayArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudPolicysimulatorV1beta1ReplayConfigArgs']]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 organizations_id: Optional[pulumi.Input[str]] = None,
                 replays_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = OrganizationReplayArgs.__new__(OrganizationReplayArgs)

            __props__.__dict__["config"] = config
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__.__dict__["locations_id"] = locations_id
            if organizations_id is None and not opts.urn:
                raise TypeError("Missing required property 'organizations_id'")
            __props__.__dict__["organizations_id"] = organizations_id
            if replays_id is None and not opts.urn:
                raise TypeError("Missing required property 'replays_id'")
            __props__.__dict__["replays_id"] = replays_id
            __props__.__dict__["name"] = None
            __props__.__dict__["results_summary"] = None
            __props__.__dict__["state"] = None
        super(OrganizationReplay, __self__).__init__(
            'google-native:policysimulator/v1beta1:OrganizationReplay',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OrganizationReplay':
        """
        Get an existing OrganizationReplay resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OrganizationReplayArgs.__new__(OrganizationReplayArgs)

        __props__.__dict__["config"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["results_summary"] = None
        __props__.__dict__["state"] = None
        return OrganizationReplay(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def config(self) -> pulumi.Output['outputs.GoogleCloudPolicysimulatorV1beta1ReplayConfigResponse']:
        """
        Required. The configuration used for the `Replay`.
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the `Replay`, which has the following format: `{projects|folders|organizations}/{resource-id}/locations/global/replays/{replay-id}`, where `{resource-id}` is the ID of the project, folder, or organization that owns the Replay. Example: `projects/my-example-project/locations/global/replays/506a5f7f-38ce-4d7d-8e03-479ce1833c36`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resultsSummary")
    def results_summary(self) -> pulumi.Output['outputs.GoogleCloudPolicysimulatorV1beta1ReplayResultsSummaryResponse']:
        """
        Summary statistics about the replayed log entries.
        """
        return pulumi.get(self, "results_summary")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of the `Replay`.
        """
        return pulumi.get(self, "state")

