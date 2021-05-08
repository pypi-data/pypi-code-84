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

__all__ = ['ConversationProfileArgs', 'ConversationProfile']

@pulumi.input_type
class ConversationProfileArgs:
    def __init__(__self__, *,
                 conversation_profiles_id: pulumi.Input[str],
                 locations_id: pulumi.Input[str],
                 projects_id: pulumi.Input[str],
                 automated_agent_config: Optional[pulumi.Input['GoogleCloudDialogflowV2AutomatedAgentConfigArgs']] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 human_agent_assistant_config: Optional[pulumi.Input['GoogleCloudDialogflowV2HumanAgentAssistantConfigArgs']] = None,
                 human_agent_handoff_config: Optional[pulumi.Input['GoogleCloudDialogflowV2HumanAgentHandoffConfigArgs']] = None,
                 language_code: Optional[pulumi.Input[str]] = None,
                 logging_config: Optional[pulumi.Input['GoogleCloudDialogflowV2LoggingConfigArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 new_message_event_notification_config: Optional[pulumi.Input['GoogleCloudDialogflowV2NotificationConfigArgs']] = None,
                 notification_config: Optional[pulumi.Input['GoogleCloudDialogflowV2NotificationConfigArgs']] = None,
                 stt_config: Optional[pulumi.Input['GoogleCloudDialogflowV2SpeechToTextConfigArgs']] = None):
        """
        The set of arguments for constructing a ConversationProfile resource.
        :param pulumi.Input['GoogleCloudDialogflowV2AutomatedAgentConfigArgs'] automated_agent_config: Configuration for an automated agent to use with this profile.
        :param pulumi.Input[str] display_name: Required. Human readable name for this profile. Max length 1024 bytes.
        :param pulumi.Input['GoogleCloudDialogflowV2HumanAgentAssistantConfigArgs'] human_agent_assistant_config: Configuration for agent assistance to use with this profile.
        :param pulumi.Input['GoogleCloudDialogflowV2HumanAgentHandoffConfigArgs'] human_agent_handoff_config: Configuration for connecting to a live agent. Currently, this feature is not general available, please contact Google to get access.
        :param pulumi.Input[str] language_code: Language which represents the conversationProfile. If unspecified, the default language code en-us applies. Users need to create a ConversationProfile for each language they want to support.
        :param pulumi.Input['GoogleCloudDialogflowV2LoggingConfigArgs'] logging_config: Configuration for logging conversation lifecycle events.
        :param pulumi.Input[str] name: The unique identifier of this conversation profile. Format: `projects//locations//conversationProfiles/`.
        :param pulumi.Input['GoogleCloudDialogflowV2NotificationConfigArgs'] new_message_event_notification_config: Configuration for publishing new message events. Event will be sent in format of ConversationEvent
        :param pulumi.Input['GoogleCloudDialogflowV2NotificationConfigArgs'] notification_config: Configuration for publishing conversation lifecycle events.
        :param pulumi.Input['GoogleCloudDialogflowV2SpeechToTextConfigArgs'] stt_config: Settings for speech transcription.
        """
        pulumi.set(__self__, "conversation_profiles_id", conversation_profiles_id)
        pulumi.set(__self__, "locations_id", locations_id)
        pulumi.set(__self__, "projects_id", projects_id)
        if automated_agent_config is not None:
            pulumi.set(__self__, "automated_agent_config", automated_agent_config)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if human_agent_assistant_config is not None:
            pulumi.set(__self__, "human_agent_assistant_config", human_agent_assistant_config)
        if human_agent_handoff_config is not None:
            pulumi.set(__self__, "human_agent_handoff_config", human_agent_handoff_config)
        if language_code is not None:
            pulumi.set(__self__, "language_code", language_code)
        if logging_config is not None:
            pulumi.set(__self__, "logging_config", logging_config)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if new_message_event_notification_config is not None:
            pulumi.set(__self__, "new_message_event_notification_config", new_message_event_notification_config)
        if notification_config is not None:
            pulumi.set(__self__, "notification_config", notification_config)
        if stt_config is not None:
            pulumi.set(__self__, "stt_config", stt_config)

    @property
    @pulumi.getter(name="conversationProfilesId")
    def conversation_profiles_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "conversation_profiles_id")

    @conversation_profiles_id.setter
    def conversation_profiles_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "conversation_profiles_id", value)

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
    @pulumi.getter(name="automatedAgentConfig")
    def automated_agent_config(self) -> Optional[pulumi.Input['GoogleCloudDialogflowV2AutomatedAgentConfigArgs']]:
        """
        Configuration for an automated agent to use with this profile.
        """
        return pulumi.get(self, "automated_agent_config")

    @automated_agent_config.setter
    def automated_agent_config(self, value: Optional[pulumi.Input['GoogleCloudDialogflowV2AutomatedAgentConfigArgs']]):
        pulumi.set(self, "automated_agent_config", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Required. Human readable name for this profile. Max length 1024 bytes.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="humanAgentAssistantConfig")
    def human_agent_assistant_config(self) -> Optional[pulumi.Input['GoogleCloudDialogflowV2HumanAgentAssistantConfigArgs']]:
        """
        Configuration for agent assistance to use with this profile.
        """
        return pulumi.get(self, "human_agent_assistant_config")

    @human_agent_assistant_config.setter
    def human_agent_assistant_config(self, value: Optional[pulumi.Input['GoogleCloudDialogflowV2HumanAgentAssistantConfigArgs']]):
        pulumi.set(self, "human_agent_assistant_config", value)

    @property
    @pulumi.getter(name="humanAgentHandoffConfig")
    def human_agent_handoff_config(self) -> Optional[pulumi.Input['GoogleCloudDialogflowV2HumanAgentHandoffConfigArgs']]:
        """
        Configuration for connecting to a live agent. Currently, this feature is not general available, please contact Google to get access.
        """
        return pulumi.get(self, "human_agent_handoff_config")

    @human_agent_handoff_config.setter
    def human_agent_handoff_config(self, value: Optional[pulumi.Input['GoogleCloudDialogflowV2HumanAgentHandoffConfigArgs']]):
        pulumi.set(self, "human_agent_handoff_config", value)

    @property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[str]]:
        """
        Language which represents the conversationProfile. If unspecified, the default language code en-us applies. Users need to create a ConversationProfile for each language they want to support.
        """
        return pulumi.get(self, "language_code")

    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "language_code", value)

    @property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[pulumi.Input['GoogleCloudDialogflowV2LoggingConfigArgs']]:
        """
        Configuration for logging conversation lifecycle events.
        """
        return pulumi.get(self, "logging_config")

    @logging_config.setter
    def logging_config(self, value: Optional[pulumi.Input['GoogleCloudDialogflowV2LoggingConfigArgs']]):
        pulumi.set(self, "logging_config", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The unique identifier of this conversation profile. Format: `projects//locations//conversationProfiles/`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="newMessageEventNotificationConfig")
    def new_message_event_notification_config(self) -> Optional[pulumi.Input['GoogleCloudDialogflowV2NotificationConfigArgs']]:
        """
        Configuration for publishing new message events. Event will be sent in format of ConversationEvent
        """
        return pulumi.get(self, "new_message_event_notification_config")

    @new_message_event_notification_config.setter
    def new_message_event_notification_config(self, value: Optional[pulumi.Input['GoogleCloudDialogflowV2NotificationConfigArgs']]):
        pulumi.set(self, "new_message_event_notification_config", value)

    @property
    @pulumi.getter(name="notificationConfig")
    def notification_config(self) -> Optional[pulumi.Input['GoogleCloudDialogflowV2NotificationConfigArgs']]:
        """
        Configuration for publishing conversation lifecycle events.
        """
        return pulumi.get(self, "notification_config")

    @notification_config.setter
    def notification_config(self, value: Optional[pulumi.Input['GoogleCloudDialogflowV2NotificationConfigArgs']]):
        pulumi.set(self, "notification_config", value)

    @property
    @pulumi.getter(name="sttConfig")
    def stt_config(self) -> Optional[pulumi.Input['GoogleCloudDialogflowV2SpeechToTextConfigArgs']]:
        """
        Settings for speech transcription.
        """
        return pulumi.get(self, "stt_config")

    @stt_config.setter
    def stt_config(self, value: Optional[pulumi.Input['GoogleCloudDialogflowV2SpeechToTextConfigArgs']]):
        pulumi.set(self, "stt_config", value)


class ConversationProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automated_agent_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2AutomatedAgentConfigArgs']]] = None,
                 conversation_profiles_id: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 human_agent_assistant_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2HumanAgentAssistantConfigArgs']]] = None,
                 human_agent_handoff_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2HumanAgentHandoffConfigArgs']]] = None,
                 language_code: Optional[pulumi.Input[str]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 logging_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2LoggingConfigArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 new_message_event_notification_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2NotificationConfigArgs']]] = None,
                 notification_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2NotificationConfigArgs']]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 stt_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2SpeechToTextConfigArgs']]] = None,
                 __props__=None):
        """
        Creates a conversation profile in the specified project. ConversationProfile.CreateTime and ConversationProfile.UpdateTime aren't populated in the response. You can retrieve them via GetConversationProfile API.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2AutomatedAgentConfigArgs']] automated_agent_config: Configuration for an automated agent to use with this profile.
        :param pulumi.Input[str] display_name: Required. Human readable name for this profile. Max length 1024 bytes.
        :param pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2HumanAgentAssistantConfigArgs']] human_agent_assistant_config: Configuration for agent assistance to use with this profile.
        :param pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2HumanAgentHandoffConfigArgs']] human_agent_handoff_config: Configuration for connecting to a live agent. Currently, this feature is not general available, please contact Google to get access.
        :param pulumi.Input[str] language_code: Language which represents the conversationProfile. If unspecified, the default language code en-us applies. Users need to create a ConversationProfile for each language they want to support.
        :param pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2LoggingConfigArgs']] logging_config: Configuration for logging conversation lifecycle events.
        :param pulumi.Input[str] name: The unique identifier of this conversation profile. Format: `projects//locations//conversationProfiles/`.
        :param pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2NotificationConfigArgs']] new_message_event_notification_config: Configuration for publishing new message events. Event will be sent in format of ConversationEvent
        :param pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2NotificationConfigArgs']] notification_config: Configuration for publishing conversation lifecycle events.
        :param pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2SpeechToTextConfigArgs']] stt_config: Settings for speech transcription.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConversationProfileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a conversation profile in the specified project. ConversationProfile.CreateTime and ConversationProfile.UpdateTime aren't populated in the response. You can retrieve them via GetConversationProfile API.

        :param str resource_name: The name of the resource.
        :param ConversationProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConversationProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automated_agent_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2AutomatedAgentConfigArgs']]] = None,
                 conversation_profiles_id: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 human_agent_assistant_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2HumanAgentAssistantConfigArgs']]] = None,
                 human_agent_handoff_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2HumanAgentHandoffConfigArgs']]] = None,
                 language_code: Optional[pulumi.Input[str]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 logging_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2LoggingConfigArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 new_message_event_notification_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2NotificationConfigArgs']]] = None,
                 notification_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2NotificationConfigArgs']]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 stt_config: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2SpeechToTextConfigArgs']]] = None,
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
            __props__ = ConversationProfileArgs.__new__(ConversationProfileArgs)

            __props__.__dict__["automated_agent_config"] = automated_agent_config
            if conversation_profiles_id is None and not opts.urn:
                raise TypeError("Missing required property 'conversation_profiles_id'")
            __props__.__dict__["conversation_profiles_id"] = conversation_profiles_id
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["human_agent_assistant_config"] = human_agent_assistant_config
            __props__.__dict__["human_agent_handoff_config"] = human_agent_handoff_config
            __props__.__dict__["language_code"] = language_code
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__.__dict__["locations_id"] = locations_id
            __props__.__dict__["logging_config"] = logging_config
            __props__.__dict__["name"] = name
            __props__.__dict__["new_message_event_notification_config"] = new_message_event_notification_config
            __props__.__dict__["notification_config"] = notification_config
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__.__dict__["projects_id"] = projects_id
            __props__.__dict__["stt_config"] = stt_config
            __props__.__dict__["create_time"] = None
            __props__.__dict__["update_time"] = None
        super(ConversationProfile, __self__).__init__(
            'google-native:dialogflow/v2:ConversationProfile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConversationProfile':
        """
        Get an existing ConversationProfile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConversationProfileArgs.__new__(ConversationProfileArgs)

        __props__.__dict__["automated_agent_config"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["human_agent_assistant_config"] = None
        __props__.__dict__["human_agent_handoff_config"] = None
        __props__.__dict__["language_code"] = None
        __props__.__dict__["logging_config"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["new_message_event_notification_config"] = None
        __props__.__dict__["notification_config"] = None
        __props__.__dict__["stt_config"] = None
        __props__.__dict__["update_time"] = None
        return ConversationProfile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="automatedAgentConfig")
    def automated_agent_config(self) -> pulumi.Output['outputs.GoogleCloudDialogflowV2AutomatedAgentConfigResponse']:
        """
        Configuration for an automated agent to use with this profile.
        """
        return pulumi.get(self, "automated_agent_config")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Create time of the conversation profile.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Required. Human readable name for this profile. Max length 1024 bytes.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="humanAgentAssistantConfig")
    def human_agent_assistant_config(self) -> pulumi.Output['outputs.GoogleCloudDialogflowV2HumanAgentAssistantConfigResponse']:
        """
        Configuration for agent assistance to use with this profile.
        """
        return pulumi.get(self, "human_agent_assistant_config")

    @property
    @pulumi.getter(name="humanAgentHandoffConfig")
    def human_agent_handoff_config(self) -> pulumi.Output['outputs.GoogleCloudDialogflowV2HumanAgentHandoffConfigResponse']:
        """
        Configuration for connecting to a live agent. Currently, this feature is not general available, please contact Google to get access.
        """
        return pulumi.get(self, "human_agent_handoff_config")

    @property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Output[str]:
        """
        Language which represents the conversationProfile. If unspecified, the default language code en-us applies. Users need to create a ConversationProfile for each language they want to support.
        """
        return pulumi.get(self, "language_code")

    @property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> pulumi.Output['outputs.GoogleCloudDialogflowV2LoggingConfigResponse']:
        """
        Configuration for logging conversation lifecycle events.
        """
        return pulumi.get(self, "logging_config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The unique identifier of this conversation profile. Format: `projects//locations//conversationProfiles/`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="newMessageEventNotificationConfig")
    def new_message_event_notification_config(self) -> pulumi.Output['outputs.GoogleCloudDialogflowV2NotificationConfigResponse']:
        """
        Configuration for publishing new message events. Event will be sent in format of ConversationEvent
        """
        return pulumi.get(self, "new_message_event_notification_config")

    @property
    @pulumi.getter(name="notificationConfig")
    def notification_config(self) -> pulumi.Output['outputs.GoogleCloudDialogflowV2NotificationConfigResponse']:
        """
        Configuration for publishing conversation lifecycle events.
        """
        return pulumi.get(self, "notification_config")

    @property
    @pulumi.getter(name="sttConfig")
    def stt_config(self) -> pulumi.Output['outputs.GoogleCloudDialogflowV2SpeechToTextConfigResponse']:
        """
        Settings for speech transcription.
        """
        return pulumi.get(self, "stt_config")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Update time of the conversation profile.
        """
        return pulumi.get(self, "update_time")

