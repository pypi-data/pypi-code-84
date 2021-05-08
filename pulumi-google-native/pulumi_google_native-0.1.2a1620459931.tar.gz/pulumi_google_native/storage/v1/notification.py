# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['NotificationArgs', 'Notification']

@pulumi.input_type
class NotificationArgs:
    def __init__(__self__, *,
                 bucket: pulumi.Input[str],
                 notification: pulumi.Input[str],
                 custom_attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 event_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 object_name_prefix: Optional[pulumi.Input[str]] = None,
                 payload_format: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 topic: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Notification resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] custom_attributes: An optional list of additional attributes to attach to each Cloud PubSub message published for this notification subscription.
        :param pulumi.Input[str] etag: HTTP 1.1 Entity tag for this subscription notification.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] event_types: If present, only send notifications about listed event types. If empty, sent notifications for all event types.
        :param pulumi.Input[str] id: The ID of the notification.
        :param pulumi.Input[str] kind: The kind of item this is. For notifications, this is always storage#notification.
        :param pulumi.Input[str] object_name_prefix: If present, only apply this notification configuration to object names that begin with this prefix.
        :param pulumi.Input[str] payload_format: The desired content of the Payload.
        :param pulumi.Input[str] self_link: The canonical URL of this notification.
        :param pulumi.Input[str] topic: The Cloud PubSub topic to which this subscription publishes. Formatted as: '//pubsub.googleapis.com/projects/{project-identifier}/topics/{my-topic}'
        """
        pulumi.set(__self__, "bucket", bucket)
        pulumi.set(__self__, "notification", notification)
        if custom_attributes is not None:
            pulumi.set(__self__, "custom_attributes", custom_attributes)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if event_types is not None:
            pulumi.set(__self__, "event_types", event_types)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if object_name_prefix is not None:
            pulumi.set(__self__, "object_name_prefix", object_name_prefix)
        if payload_format is not None:
            pulumi.set(__self__, "payload_format", payload_format)
        if self_link is not None:
            pulumi.set(__self__, "self_link", self_link)
        if topic is not None:
            pulumi.set(__self__, "topic", topic)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[str]:
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter
    def notification(self) -> pulumi.Input[str]:
        return pulumi.get(self, "notification")

    @notification.setter
    def notification(self, value: pulumi.Input[str]):
        pulumi.set(self, "notification", value)

    @property
    @pulumi.getter
    def custom_attributes(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        An optional list of additional attributes to attach to each Cloud PubSub message published for this notification subscription.
        """
        return pulumi.get(self, "custom_attributes")

    @custom_attributes.setter
    def custom_attributes(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "custom_attributes", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        HTTP 1.1 Entity tag for this subscription notification.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter
    def event_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        If present, only send notifications about listed event types. If empty, sent notifications for all event types.
        """
        return pulumi.get(self, "event_types")

    @event_types.setter
    def event_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "event_types", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the notification.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        The kind of item this is. For notifications, this is always storage#notification.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def object_name_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        If present, only apply this notification configuration to object names that begin with this prefix.
        """
        return pulumi.get(self, "object_name_prefix")

    @object_name_prefix.setter
    def object_name_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "object_name_prefix", value)

    @property
    @pulumi.getter
    def payload_format(self) -> Optional[pulumi.Input[str]]:
        """
        The desired content of the Payload.
        """
        return pulumi.get(self, "payload_format")

    @payload_format.setter
    def payload_format(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "payload_format", value)

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[str]]:
        """
        The canonical URL of this notification.
        """
        return pulumi.get(self, "self_link")

    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "self_link", value)

    @property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[str]]:
        """
        The Cloud PubSub topic to which this subscription publishes. Formatted as: '//pubsub.googleapis.com/projects/{project-identifier}/topics/{my-topic}'
        """
        return pulumi.get(self, "topic")

    @topic.setter
    def topic(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "topic", value)


class Notification(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 custom_attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 event_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 notification: Optional[pulumi.Input[str]] = None,
                 object_name_prefix: Optional[pulumi.Input[str]] = None,
                 payload_format: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 topic: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a notification subscription for a given bucket.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] custom_attributes: An optional list of additional attributes to attach to each Cloud PubSub message published for this notification subscription.
        :param pulumi.Input[str] etag: HTTP 1.1 Entity tag for this subscription notification.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] event_types: If present, only send notifications about listed event types. If empty, sent notifications for all event types.
        :param pulumi.Input[str] id: The ID of the notification.
        :param pulumi.Input[str] kind: The kind of item this is. For notifications, this is always storage#notification.
        :param pulumi.Input[str] object_name_prefix: If present, only apply this notification configuration to object names that begin with this prefix.
        :param pulumi.Input[str] payload_format: The desired content of the Payload.
        :param pulumi.Input[str] self_link: The canonical URL of this notification.
        :param pulumi.Input[str] topic: The Cloud PubSub topic to which this subscription publishes. Formatted as: '//pubsub.googleapis.com/projects/{project-identifier}/topics/{my-topic}'
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NotificationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a notification subscription for a given bucket.

        :param str resource_name: The name of the resource.
        :param NotificationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NotificationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 custom_attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 event_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 notification: Optional[pulumi.Input[str]] = None,
                 object_name_prefix: Optional[pulumi.Input[str]] = None,
                 payload_format: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
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
            __props__ = NotificationArgs.__new__(NotificationArgs)

            if bucket is None and not opts.urn:
                raise TypeError("Missing required property 'bucket'")
            __props__.__dict__["bucket"] = bucket
            __props__.__dict__["custom_attributes"] = custom_attributes
            __props__.__dict__["etag"] = etag
            __props__.__dict__["event_types"] = event_types
            __props__.__dict__["id"] = id
            __props__.__dict__["kind"] = kind
            if notification is None and not opts.urn:
                raise TypeError("Missing required property 'notification'")
            __props__.__dict__["notification"] = notification
            __props__.__dict__["object_name_prefix"] = object_name_prefix
            __props__.__dict__["payload_format"] = payload_format
            __props__.__dict__["self_link"] = self_link
            __props__.__dict__["topic"] = topic
        super(Notification, __self__).__init__(
            'google-native:storage/v1:Notification',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Notification':
        """
        Get an existing Notification resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NotificationArgs.__new__(NotificationArgs)

        __props__.__dict__["custom_attributes"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["event_types"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["object_name_prefix"] = None
        __props__.__dict__["payload_format"] = None
        __props__.__dict__["self_link"] = None
        __props__.__dict__["topic"] = None
        return Notification(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def custom_attributes(self) -> pulumi.Output[Mapping[str, str]]:
        """
        An optional list of additional attributes to attach to each Cloud PubSub message published for this notification subscription.
        """
        return pulumi.get(self, "custom_attributes")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        HTTP 1.1 Entity tag for this subscription notification.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def event_types(self) -> pulumi.Output[Sequence[str]]:
        """
        If present, only send notifications about listed event types. If empty, sent notifications for all event types.
        """
        return pulumi.get(self, "event_types")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The kind of item this is. For notifications, this is always storage#notification.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def object_name_prefix(self) -> pulumi.Output[str]:
        """
        If present, only apply this notification configuration to object names that begin with this prefix.
        """
        return pulumi.get(self, "object_name_prefix")

    @property
    @pulumi.getter
    def payload_format(self) -> pulumi.Output[str]:
        """
        The desired content of the Payload.
        """
        return pulumi.get(self, "payload_format")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        The canonical URL of this notification.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def topic(self) -> pulumi.Output[str]:
        """
        The Cloud PubSub topic to which this subscription publishes. Formatted as: '//pubsub.googleapis.com/projects/{project-identifier}/topics/{my-topic}'
        """
        return pulumi.get(self, "topic")

