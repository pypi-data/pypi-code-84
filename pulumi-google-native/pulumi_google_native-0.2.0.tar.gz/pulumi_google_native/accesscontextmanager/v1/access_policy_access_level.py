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

__all__ = ['AccessPolicyAccessLevelArgs', 'AccessPolicyAccessLevel']

@pulumi.input_type
class AccessPolicyAccessLevelArgs:
    def __init__(__self__, *,
                 access_levels_id: pulumi.Input[str],
                 access_policies_id: pulumi.Input[str],
                 basic: Optional[pulumi.Input['BasicLevelArgs']] = None,
                 custom: Optional[pulumi.Input['CustomLevelArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AccessPolicyAccessLevel resource.
        :param pulumi.Input['BasicLevelArgs'] basic: A `BasicLevel` composed of `Conditions`.
        :param pulumi.Input['CustomLevelArgs'] custom: A `CustomLevel` written in the Common Expression Language.
        :param pulumi.Input[str] description: Description of the `AccessLevel` and its use. Does not affect behavior.
        :param pulumi.Input[str] name: Required. Resource name for the Access Level. The `short_name` component must begin with a letter and only include alphanumeric and '_'. Format: `accessPolicies/{policy_id}/accessLevels/{short_name}`. The maximum length of the `short_name` component is 50 characters.
        :param pulumi.Input[str] title: Human readable title. Must be unique within the Policy.
        """
        pulumi.set(__self__, "access_levels_id", access_levels_id)
        pulumi.set(__self__, "access_policies_id", access_policies_id)
        if basic is not None:
            pulumi.set(__self__, "basic", basic)
        if custom is not None:
            pulumi.set(__self__, "custom", custom)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if title is not None:
            pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter(name="accessLevelsId")
    def access_levels_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "access_levels_id")

    @access_levels_id.setter
    def access_levels_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "access_levels_id", value)

    @property
    @pulumi.getter(name="accessPoliciesId")
    def access_policies_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "access_policies_id")

    @access_policies_id.setter
    def access_policies_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "access_policies_id", value)

    @property
    @pulumi.getter
    def basic(self) -> Optional[pulumi.Input['BasicLevelArgs']]:
        """
        A `BasicLevel` composed of `Conditions`.
        """
        return pulumi.get(self, "basic")

    @basic.setter
    def basic(self, value: Optional[pulumi.Input['BasicLevelArgs']]):
        pulumi.set(self, "basic", value)

    @property
    @pulumi.getter
    def custom(self) -> Optional[pulumi.Input['CustomLevelArgs']]:
        """
        A `CustomLevel` written in the Common Expression Language.
        """
        return pulumi.get(self, "custom")

    @custom.setter
    def custom(self, value: Optional[pulumi.Input['CustomLevelArgs']]):
        pulumi.set(self, "custom", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the `AccessLevel` and its use. Does not affect behavior.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Required. Resource name for the Access Level. The `short_name` component must begin with a letter and only include alphanumeric and '_'. Format: `accessPolicies/{policy_id}/accessLevels/{short_name}`. The maximum length of the `short_name` component is 50 characters.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        Human readable title. Must be unique within the Policy.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)


class AccessPolicyAccessLevel(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_levels_id: Optional[pulumi.Input[str]] = None,
                 access_policies_id: Optional[pulumi.Input[str]] = None,
                 basic: Optional[pulumi.Input[pulumi.InputType['BasicLevelArgs']]] = None,
                 custom: Optional[pulumi.Input[pulumi.InputType['CustomLevelArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create an Access Level. The longrunning operation from this RPC will have a successful status once the Access Level has propagated to long-lasting storage. Access Levels containing errors will result in an error response for the first error encountered.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['BasicLevelArgs']] basic: A `BasicLevel` composed of `Conditions`.
        :param pulumi.Input[pulumi.InputType['CustomLevelArgs']] custom: A `CustomLevel` written in the Common Expression Language.
        :param pulumi.Input[str] description: Description of the `AccessLevel` and its use. Does not affect behavior.
        :param pulumi.Input[str] name: Required. Resource name for the Access Level. The `short_name` component must begin with a letter and only include alphanumeric and '_'. Format: `accessPolicies/{policy_id}/accessLevels/{short_name}`. The maximum length of the `short_name` component is 50 characters.
        :param pulumi.Input[str] title: Human readable title. Must be unique within the Policy.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccessPolicyAccessLevelArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create an Access Level. The longrunning operation from this RPC will have a successful status once the Access Level has propagated to long-lasting storage. Access Levels containing errors will result in an error response for the first error encountered.

        :param str resource_name: The name of the resource.
        :param AccessPolicyAccessLevelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccessPolicyAccessLevelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_levels_id: Optional[pulumi.Input[str]] = None,
                 access_policies_id: Optional[pulumi.Input[str]] = None,
                 basic: Optional[pulumi.Input[pulumi.InputType['BasicLevelArgs']]] = None,
                 custom: Optional[pulumi.Input[pulumi.InputType['CustomLevelArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
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
            __props__ = AccessPolicyAccessLevelArgs.__new__(AccessPolicyAccessLevelArgs)

            if access_levels_id is None and not opts.urn:
                raise TypeError("Missing required property 'access_levels_id'")
            __props__.__dict__["access_levels_id"] = access_levels_id
            if access_policies_id is None and not opts.urn:
                raise TypeError("Missing required property 'access_policies_id'")
            __props__.__dict__["access_policies_id"] = access_policies_id
            __props__.__dict__["basic"] = basic
            __props__.__dict__["custom"] = custom
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["title"] = title
        super(AccessPolicyAccessLevel, __self__).__init__(
            'google-native:accesscontextmanager/v1:AccessPolicyAccessLevel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AccessPolicyAccessLevel':
        """
        Get an existing AccessPolicyAccessLevel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AccessPolicyAccessLevelArgs.__new__(AccessPolicyAccessLevelArgs)

        __props__.__dict__["basic"] = None
        __props__.__dict__["custom"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["title"] = None
        return AccessPolicyAccessLevel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def basic(self) -> pulumi.Output['outputs.BasicLevelResponse']:
        """
        A `BasicLevel` composed of `Conditions`.
        """
        return pulumi.get(self, "basic")

    @property
    @pulumi.getter
    def custom(self) -> pulumi.Output['outputs.CustomLevelResponse']:
        """
        A `CustomLevel` written in the Common Expression Language.
        """
        return pulumi.get(self, "custom")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Description of the `AccessLevel` and its use. Does not affect behavior.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Required. Resource name for the Access Level. The `short_name` component must begin with a letter and only include alphanumeric and '_'. Format: `accessPolicies/{policy_id}/accessLevels/{short_name}`. The maximum length of the `short_name` component is 50 characters.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[str]:
        """
        Human readable title. Must be unique within the Policy.
        """
        return pulumi.get(self, "title")

