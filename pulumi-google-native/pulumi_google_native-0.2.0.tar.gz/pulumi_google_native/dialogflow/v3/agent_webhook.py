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

__all__ = ['AgentWebhookArgs', 'AgentWebhook']

@pulumi.input_type
class AgentWebhookArgs:
    def __init__(__self__, *,
                 agents_id: pulumi.Input[str],
                 locations_id: pulumi.Input[str],
                 projects_id: pulumi.Input[str],
                 webhooks_id: pulumi.Input[str],
                 disabled: Optional[pulumi.Input[bool]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 generic_web_service: Optional[pulumi.Input['GoogleCloudDialogflowCxV3WebhookGenericWebServiceArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 timeout: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AgentWebhook resource.
        :param pulumi.Input[bool] disabled: Indicates whether the webhook is disabled.
        :param pulumi.Input[str] display_name: Required. The human-readable name of the webhook, unique within the agent.
        :param pulumi.Input['GoogleCloudDialogflowCxV3WebhookGenericWebServiceArgs'] generic_web_service: Configuration for a generic web service.
        :param pulumi.Input[str] name: The unique identifier of the webhook. Required for the Webhooks.UpdateWebhook method. Webhooks.CreateWebhook populates the name automatically. Format: `projects//locations//agents//webhooks/`.
        :param pulumi.Input[str] timeout: Webhook execution timeout. Execution is considered failed if Dialogflow doesn't receive a response from webhook at the end of the timeout period. Defaults to 5 seconds, maximum allowed timeout is 30 seconds.
        """
        pulumi.set(__self__, "agents_id", agents_id)
        pulumi.set(__self__, "locations_id", locations_id)
        pulumi.set(__self__, "projects_id", projects_id)
        pulumi.set(__self__, "webhooks_id", webhooks_id)
        if disabled is not None:
            pulumi.set(__self__, "disabled", disabled)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if generic_web_service is not None:
            pulumi.set(__self__, "generic_web_service", generic_web_service)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if timeout is not None:
            pulumi.set(__self__, "timeout", timeout)

    @property
    @pulumi.getter(name="agentsId")
    def agents_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "agents_id")

    @agents_id.setter
    def agents_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "agents_id", value)

    @property
    @pulumi.getter(name="locationsId")
    def locations_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "locations_id")

    @locations_id.setter
    def locations_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "locations_id", value)

    @property
    @pulumi.getter(name="projectsId")
    def projects_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "projects_id")

    @projects_id.setter
    def projects_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "projects_id", value)

    @property
    @pulumi.getter(name="webhooksId")
    def webhooks_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "webhooks_id")

    @webhooks_id.setter
    def webhooks_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "webhooks_id", value)

    @property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the webhook is disabled.
        """
        return pulumi.get(self, "disabled")

    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disabled", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Required. The human-readable name of the webhook, unique within the agent.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="genericWebService")
    def generic_web_service(self) -> Optional[pulumi.Input['GoogleCloudDialogflowCxV3WebhookGenericWebServiceArgs']]:
        """
        Configuration for a generic web service.
        """
        return pulumi.get(self, "generic_web_service")

    @generic_web_service.setter
    def generic_web_service(self, value: Optional[pulumi.Input['GoogleCloudDialogflowCxV3WebhookGenericWebServiceArgs']]):
        pulumi.set(self, "generic_web_service", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The unique identifier of the webhook. Required for the Webhooks.UpdateWebhook method. Webhooks.CreateWebhook populates the name automatically. Format: `projects//locations//agents//webhooks/`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[str]]:
        """
        Webhook execution timeout. Execution is considered failed if Dialogflow doesn't receive a response from webhook at the end of the timeout period. Defaults to 5 seconds, maximum allowed timeout is 30 seconds.
        """
        return pulumi.get(self, "timeout")

    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "timeout", value)


class AgentWebhook(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agents_id: Optional[pulumi.Input[str]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 generic_web_service: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3WebhookGenericWebServiceArgs']]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 timeout: Optional[pulumi.Input[str]] = None,
                 webhooks_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a webhook in the specified agent.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] disabled: Indicates whether the webhook is disabled.
        :param pulumi.Input[str] display_name: Required. The human-readable name of the webhook, unique within the agent.
        :param pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3WebhookGenericWebServiceArgs']] generic_web_service: Configuration for a generic web service.
        :param pulumi.Input[str] name: The unique identifier of the webhook. Required for the Webhooks.UpdateWebhook method. Webhooks.CreateWebhook populates the name automatically. Format: `projects//locations//agents//webhooks/`.
        :param pulumi.Input[str] timeout: Webhook execution timeout. Execution is considered failed if Dialogflow doesn't receive a response from webhook at the end of the timeout period. Defaults to 5 seconds, maximum allowed timeout is 30 seconds.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AgentWebhookArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a webhook in the specified agent.

        :param str resource_name: The name of the resource.
        :param AgentWebhookArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AgentWebhookArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agents_id: Optional[pulumi.Input[str]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 generic_web_service: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3WebhookGenericWebServiceArgs']]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 timeout: Optional[pulumi.Input[str]] = None,
                 webhooks_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = AgentWebhookArgs.__new__(AgentWebhookArgs)

            if agents_id is None and not opts.urn:
                raise TypeError("Missing required property 'agents_id'")
            __props__.__dict__["agents_id"] = agents_id
            __props__.__dict__["disabled"] = disabled
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["generic_web_service"] = generic_web_service
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__.__dict__["locations_id"] = locations_id
            __props__.__dict__["name"] = name
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__.__dict__["projects_id"] = projects_id
            __props__.__dict__["timeout"] = timeout
            if webhooks_id is None and not opts.urn:
                raise TypeError("Missing required property 'webhooks_id'")
            __props__.__dict__["webhooks_id"] = webhooks_id
        super(AgentWebhook, __self__).__init__(
            'google-native:dialogflow/v3:AgentWebhook',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AgentWebhook':
        """
        Get an existing AgentWebhook resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AgentWebhookArgs.__new__(AgentWebhookArgs)

        __props__.__dict__["disabled"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["generic_web_service"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["timeout"] = None
        return AgentWebhook(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[bool]:
        """
        Indicates whether the webhook is disabled.
        """
        return pulumi.get(self, "disabled")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Required. The human-readable name of the webhook, unique within the agent.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="genericWebService")
    def generic_web_service(self) -> pulumi.Output['outputs.GoogleCloudDialogflowCxV3WebhookGenericWebServiceResponse']:
        """
        Configuration for a generic web service.
        """
        return pulumi.get(self, "generic_web_service")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The unique identifier of the webhook. Required for the Webhooks.UpdateWebhook method. Webhooks.CreateWebhook populates the name automatically. Format: `projects//locations//agents//webhooks/`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def timeout(self) -> pulumi.Output[str]:
        """
        Webhook execution timeout. Execution is considered failed if Dialogflow doesn't receive a response from webhook at the end of the timeout period. Defaults to 5 seconds, maximum allowed timeout is 30 seconds.
        """
        return pulumi.get(self, "timeout")

