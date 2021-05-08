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

__all__ = ['SubscriptionArgs', 'Subscription']

@pulumi.input_type
class SubscriptionArgs:
    def __init__(__self__, *,
                 subscriptions_id: pulumi.Input[str],
                 ack_deadline_seconds: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 push_config: Optional[pulumi.Input['PushConfigArgs']] = None,
                 topic: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Subscription resource.
        :param pulumi.Input[int] ack_deadline_seconds: For either push or pull delivery, the value is the maximum time after a subscriber receives a message before the subscriber should acknowledge or Nack the message. If the Ack deadline for a message passes without an Ack or a Nack, the Pub/Sub system will eventually redeliver the message. If a subscriber acknowledges after the deadline, the Pub/Sub system may accept the Ack, but it is possible that the message has been already delivered again. Multiple Acks to the message are allowed and will succeed. For push delivery, this value is used to set the request timeout for the call to the push endpoint. For pull delivery, this value is used as the initial value for the Ack deadline. It may be overridden for each message using its corresponding ack_id with ModifyAckDeadline. While a message is outstanding (i.e. it has been delivered to a pull subscriber and the subscriber has not yet Acked or Nacked), the Pub/Sub system will not deliver that message to another pull subscriber (on a best-effort basis).
        :param pulumi.Input[str] name: Name of the subscription.
        :param pulumi.Input['PushConfigArgs'] push_config: If push delivery is used with this subscription, this field is used to configure it.
        :param pulumi.Input[str] topic: The name of the topic from which this subscription is receiving messages.
        """
        pulumi.set(__self__, "subscriptions_id", subscriptions_id)
        if ack_deadline_seconds is not None:
            pulumi.set(__self__, "ack_deadline_seconds", ack_deadline_seconds)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if push_config is not None:
            pulumi.set(__self__, "push_config", push_config)
        if topic is not None:
            pulumi.set(__self__, "topic", topic)

    @property
    @pulumi.getter(name="subscriptionsId")
    def subscriptions_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "subscriptions_id")

    @subscriptions_id.setter
    def subscriptions_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subscriptions_id", value)

    @property
    @pulumi.getter(name="ackDeadlineSeconds")
    def ack_deadline_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        For either push or pull delivery, the value is the maximum time after a subscriber receives a message before the subscriber should acknowledge or Nack the message. If the Ack deadline for a message passes without an Ack or a Nack, the Pub/Sub system will eventually redeliver the message. If a subscriber acknowledges after the deadline, the Pub/Sub system may accept the Ack, but it is possible that the message has been already delivered again. Multiple Acks to the message are allowed and will succeed. For push delivery, this value is used to set the request timeout for the call to the push endpoint. For pull delivery, this value is used as the initial value for the Ack deadline. It may be overridden for each message using its corresponding ack_id with ModifyAckDeadline. While a message is outstanding (i.e. it has been delivered to a pull subscriber and the subscriber has not yet Acked or Nacked), the Pub/Sub system will not deliver that message to another pull subscriber (on a best-effort basis).
        """
        return pulumi.get(self, "ack_deadline_seconds")

    @ack_deadline_seconds.setter
    def ack_deadline_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ack_deadline_seconds", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the subscription.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="pushConfig")
    def push_config(self) -> Optional[pulumi.Input['PushConfigArgs']]:
        """
        If push delivery is used with this subscription, this field is used to configure it.
        """
        return pulumi.get(self, "push_config")

    @push_config.setter
    def push_config(self, value: Optional[pulumi.Input['PushConfigArgs']]):
        pulumi.set(self, "push_config", value)

    @property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the topic from which this subscription is receiving messages.
        """
        return pulumi.get(self, "topic")

    @topic.setter
    def topic(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "topic", value)


class Subscription(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ack_deadline_seconds: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 push_config: Optional[pulumi.Input[pulumi.InputType['PushConfigArgs']]] = None,
                 subscriptions_id: Optional[pulumi.Input[str]] = None,
                 topic: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a subscription on a given topic for a given subscriber. If the subscription already exists, returns ALREADY_EXISTS. If the corresponding topic doesn't exist, returns NOT_FOUND. If the name is not provided in the request, the server will assign a random name for this subscription on the same project as the topic.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] ack_deadline_seconds: For either push or pull delivery, the value is the maximum time after a subscriber receives a message before the subscriber should acknowledge or Nack the message. If the Ack deadline for a message passes without an Ack or a Nack, the Pub/Sub system will eventually redeliver the message. If a subscriber acknowledges after the deadline, the Pub/Sub system may accept the Ack, but it is possible that the message has been already delivered again. Multiple Acks to the message are allowed and will succeed. For push delivery, this value is used to set the request timeout for the call to the push endpoint. For pull delivery, this value is used as the initial value for the Ack deadline. It may be overridden for each message using its corresponding ack_id with ModifyAckDeadline. While a message is outstanding (i.e. it has been delivered to a pull subscriber and the subscriber has not yet Acked or Nacked), the Pub/Sub system will not deliver that message to another pull subscriber (on a best-effort basis).
        :param pulumi.Input[str] name: Name of the subscription.
        :param pulumi.Input[pulumi.InputType['PushConfigArgs']] push_config: If push delivery is used with this subscription, this field is used to configure it.
        :param pulumi.Input[str] topic: The name of the topic from which this subscription is receiving messages.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SubscriptionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a subscription on a given topic for a given subscriber. If the subscription already exists, returns ALREADY_EXISTS. If the corresponding topic doesn't exist, returns NOT_FOUND. If the name is not provided in the request, the server will assign a random name for this subscription on the same project as the topic.

        :param str resource_name: The name of the resource.
        :param SubscriptionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SubscriptionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ack_deadline_seconds: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 push_config: Optional[pulumi.Input[pulumi.InputType['PushConfigArgs']]] = None,
                 subscriptions_id: Optional[pulumi.Input[str]] = None,
                 topic: Optional[pulumi.Input[str]] = None,
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
            __props__ = SubscriptionArgs.__new__(SubscriptionArgs)

            __props__.__dict__["ack_deadline_seconds"] = ack_deadline_seconds
            __props__.__dict__["name"] = name
            __props__.__dict__["push_config"] = push_config
            if subscriptions_id is None and not opts.urn:
                raise TypeError("Missing required property 'subscriptions_id'")
            __props__.__dict__["subscriptions_id"] = subscriptions_id
            __props__.__dict__["topic"] = topic
        super(Subscription, __self__).__init__(
            'google-native:pubsub/v1beta1a:Subscription',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Subscription':
        """
        Get an existing Subscription resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SubscriptionArgs.__new__(SubscriptionArgs)

        __props__.__dict__["ack_deadline_seconds"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["push_config"] = None
        __props__.__dict__["topic"] = None
        return Subscription(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="ackDeadlineSeconds")
    def ack_deadline_seconds(self) -> pulumi.Output[int]:
        """
        For either push or pull delivery, the value is the maximum time after a subscriber receives a message before the subscriber should acknowledge or Nack the message. If the Ack deadline for a message passes without an Ack or a Nack, the Pub/Sub system will eventually redeliver the message. If a subscriber acknowledges after the deadline, the Pub/Sub system may accept the Ack, but it is possible that the message has been already delivered again. Multiple Acks to the message are allowed and will succeed. For push delivery, this value is used to set the request timeout for the call to the push endpoint. For pull delivery, this value is used as the initial value for the Ack deadline. It may be overridden for each message using its corresponding ack_id with ModifyAckDeadline. While a message is outstanding (i.e. it has been delivered to a pull subscriber and the subscriber has not yet Acked or Nacked), the Pub/Sub system will not deliver that message to another pull subscriber (on a best-effort basis).
        """
        return pulumi.get(self, "ack_deadline_seconds")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the subscription.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pushConfig")
    def push_config(self) -> pulumi.Output['outputs.PushConfigResponse']:
        """
        If push delivery is used with this subscription, this field is used to configure it.
        """
        return pulumi.get(self, "push_config")

    @property
    @pulumi.getter
    def topic(self) -> pulumi.Output[str]:
        """
        The name of the topic from which this subscription is receiving messages.
        """
        return pulumi.get(self, "topic")

