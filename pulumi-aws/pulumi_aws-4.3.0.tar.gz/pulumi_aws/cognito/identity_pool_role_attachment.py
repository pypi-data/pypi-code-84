# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['IdentityPoolRoleAttachmentArgs', 'IdentityPoolRoleAttachment']

@pulumi.input_type
class IdentityPoolRoleAttachmentArgs:
    def __init__(__self__, *,
                 identity_pool_id: pulumi.Input[str],
                 roles: pulumi.Input[Mapping[str, pulumi.Input[str]]],
                 role_mappings: Optional[pulumi.Input[Sequence[pulumi.Input['IdentityPoolRoleAttachmentRoleMappingArgs']]]] = None):
        """
        The set of arguments for constructing a IdentityPoolRoleAttachment resource.
        :param pulumi.Input[str] identity_pool_id: An identity pool ID in the format REGION:GUID.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] roles: The map of roles associated with this pool. For a given role, the key will be either "authenticated" or "unauthenticated" and the value will be the Role ARN.
        :param pulumi.Input[Sequence[pulumi.Input['IdentityPoolRoleAttachmentRoleMappingArgs']]] role_mappings: A List of Role Mapping.
        """
        pulumi.set(__self__, "identity_pool_id", identity_pool_id)
        pulumi.set(__self__, "roles", roles)
        if role_mappings is not None:
            pulumi.set(__self__, "role_mappings", role_mappings)

    @property
    @pulumi.getter(name="identityPoolId")
    def identity_pool_id(self) -> pulumi.Input[str]:
        """
        An identity pool ID in the format REGION:GUID.
        """
        return pulumi.get(self, "identity_pool_id")

    @identity_pool_id.setter
    def identity_pool_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "identity_pool_id", value)

    @property
    @pulumi.getter
    def roles(self) -> pulumi.Input[Mapping[str, pulumi.Input[str]]]:
        """
        The map of roles associated with this pool. For a given role, the key will be either "authenticated" or "unauthenticated" and the value will be the Role ARN.
        """
        return pulumi.get(self, "roles")

    @roles.setter
    def roles(self, value: pulumi.Input[Mapping[str, pulumi.Input[str]]]):
        pulumi.set(self, "roles", value)

    @property
    @pulumi.getter(name="roleMappings")
    def role_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IdentityPoolRoleAttachmentRoleMappingArgs']]]]:
        """
        A List of Role Mapping.
        """
        return pulumi.get(self, "role_mappings")

    @role_mappings.setter
    def role_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IdentityPoolRoleAttachmentRoleMappingArgs']]]]):
        pulumi.set(self, "role_mappings", value)


@pulumi.input_type
class _IdentityPoolRoleAttachmentState:
    def __init__(__self__, *,
                 identity_pool_id: Optional[pulumi.Input[str]] = None,
                 role_mappings: Optional[pulumi.Input[Sequence[pulumi.Input['IdentityPoolRoleAttachmentRoleMappingArgs']]]] = None,
                 roles: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering IdentityPoolRoleAttachment resources.
        :param pulumi.Input[str] identity_pool_id: An identity pool ID in the format REGION:GUID.
        :param pulumi.Input[Sequence[pulumi.Input['IdentityPoolRoleAttachmentRoleMappingArgs']]] role_mappings: A List of Role Mapping.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] roles: The map of roles associated with this pool. For a given role, the key will be either "authenticated" or "unauthenticated" and the value will be the Role ARN.
        """
        if identity_pool_id is not None:
            pulumi.set(__self__, "identity_pool_id", identity_pool_id)
        if role_mappings is not None:
            pulumi.set(__self__, "role_mappings", role_mappings)
        if roles is not None:
            pulumi.set(__self__, "roles", roles)

    @property
    @pulumi.getter(name="identityPoolId")
    def identity_pool_id(self) -> Optional[pulumi.Input[str]]:
        """
        An identity pool ID in the format REGION:GUID.
        """
        return pulumi.get(self, "identity_pool_id")

    @identity_pool_id.setter
    def identity_pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identity_pool_id", value)

    @property
    @pulumi.getter(name="roleMappings")
    def role_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IdentityPoolRoleAttachmentRoleMappingArgs']]]]:
        """
        A List of Role Mapping.
        """
        return pulumi.get(self, "role_mappings")

    @role_mappings.setter
    def role_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IdentityPoolRoleAttachmentRoleMappingArgs']]]]):
        pulumi.set(self, "role_mappings", value)

    @property
    @pulumi.getter
    def roles(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The map of roles associated with this pool. For a given role, the key will be either "authenticated" or "unauthenticated" and the value will be the Role ARN.
        """
        return pulumi.get(self, "roles")

    @roles.setter
    def roles(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "roles", value)


class IdentityPoolRoleAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity_pool_id: Optional[pulumi.Input[str]] = None,
                 role_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IdentityPoolRoleAttachmentRoleMappingArgs']]]]] = None,
                 roles: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides an AWS Cognito Identity Pool Roles Attachment.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        main_identity_pool = aws.cognito.IdentityPool("mainIdentityPool",
            identity_pool_name="identity pool",
            allow_unauthenticated_identities=False,
            supported_login_providers={
                "graph.facebook.com": "7346241598935555",
            })
        authenticated_role = aws.iam.Role("authenticatedRole", assume_role_policy=main_identity_pool.id.apply(lambda id: f\"\"\"{{
          "Version": "2012-10-17",
          "Statement": [
            {{
              "Effect": "Allow",
              "Principal": {{
                "Federated": "cognito-identity.amazonaws.com"
              }},
              "Action": "sts:AssumeRoleWithWebIdentity",
              "Condition": {{
                "StringEquals": {{
                  "cognito-identity.amazonaws.com:aud": "{id}"
                }},
                "ForAnyValue:StringLike": {{
                  "cognito-identity.amazonaws.com:amr": "authenticated"
                }}
              }}
            }}
          ]
        }}
        \"\"\"))
        authenticated_role_policy = aws.iam.RolePolicy("authenticatedRolePolicy",
            role=authenticated_role.id,
            policy=\"\"\"{
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Action": [
                "mobileanalytics:PutEvents",
                "cognito-sync:*",
                "cognito-identity:*"
              ],
              "Resource": [
                "*"
              ]
            }
          ]
        }
        \"\"\")
        main_identity_pool_role_attachment = aws.cognito.IdentityPoolRoleAttachment("mainIdentityPoolRoleAttachment",
            identity_pool_id=main_identity_pool.id,
            role_mappings=[aws.cognito.IdentityPoolRoleAttachmentRoleMappingArgs(
                identity_provider="graph.facebook.com",
                ambiguous_role_resolution="AuthenticatedRole",
                type="Rules",
                mapping_rules=[aws.cognito.IdentityPoolRoleAttachmentRoleMappingMappingRuleArgs(
                    claim="isAdmin",
                    match_type="Equals",
                    role_arn=authenticated_role.arn,
                    value="paid",
                )],
            )],
            roles={
                "authenticated": authenticated_role.arn,
            })
        ```

        ## Import

        Cognito Identity Pool Roles Attachment can be imported using the Identity Pool id, e.g.

        ```sh
         $ pulumi import aws:cognito/identityPoolRoleAttachment:IdentityPoolRoleAttachment example <identity-pool-id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] identity_pool_id: An identity pool ID in the format REGION:GUID.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IdentityPoolRoleAttachmentRoleMappingArgs']]]] role_mappings: A List of Role Mapping.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] roles: The map of roles associated with this pool. For a given role, the key will be either "authenticated" or "unauthenticated" and the value will be the Role ARN.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IdentityPoolRoleAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an AWS Cognito Identity Pool Roles Attachment.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        main_identity_pool = aws.cognito.IdentityPool("mainIdentityPool",
            identity_pool_name="identity pool",
            allow_unauthenticated_identities=False,
            supported_login_providers={
                "graph.facebook.com": "7346241598935555",
            })
        authenticated_role = aws.iam.Role("authenticatedRole", assume_role_policy=main_identity_pool.id.apply(lambda id: f\"\"\"{{
          "Version": "2012-10-17",
          "Statement": [
            {{
              "Effect": "Allow",
              "Principal": {{
                "Federated": "cognito-identity.amazonaws.com"
              }},
              "Action": "sts:AssumeRoleWithWebIdentity",
              "Condition": {{
                "StringEquals": {{
                  "cognito-identity.amazonaws.com:aud": "{id}"
                }},
                "ForAnyValue:StringLike": {{
                  "cognito-identity.amazonaws.com:amr": "authenticated"
                }}
              }}
            }}
          ]
        }}
        \"\"\"))
        authenticated_role_policy = aws.iam.RolePolicy("authenticatedRolePolicy",
            role=authenticated_role.id,
            policy=\"\"\"{
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Action": [
                "mobileanalytics:PutEvents",
                "cognito-sync:*",
                "cognito-identity:*"
              ],
              "Resource": [
                "*"
              ]
            }
          ]
        }
        \"\"\")
        main_identity_pool_role_attachment = aws.cognito.IdentityPoolRoleAttachment("mainIdentityPoolRoleAttachment",
            identity_pool_id=main_identity_pool.id,
            role_mappings=[aws.cognito.IdentityPoolRoleAttachmentRoleMappingArgs(
                identity_provider="graph.facebook.com",
                ambiguous_role_resolution="AuthenticatedRole",
                type="Rules",
                mapping_rules=[aws.cognito.IdentityPoolRoleAttachmentRoleMappingMappingRuleArgs(
                    claim="isAdmin",
                    match_type="Equals",
                    role_arn=authenticated_role.arn,
                    value="paid",
                )],
            )],
            roles={
                "authenticated": authenticated_role.arn,
            })
        ```

        ## Import

        Cognito Identity Pool Roles Attachment can be imported using the Identity Pool id, e.g.

        ```sh
         $ pulumi import aws:cognito/identityPoolRoleAttachment:IdentityPoolRoleAttachment example <identity-pool-id>
        ```

        :param str resource_name: The name of the resource.
        :param IdentityPoolRoleAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IdentityPoolRoleAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity_pool_id: Optional[pulumi.Input[str]] = None,
                 role_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IdentityPoolRoleAttachmentRoleMappingArgs']]]]] = None,
                 roles: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = IdentityPoolRoleAttachmentArgs.__new__(IdentityPoolRoleAttachmentArgs)

            if identity_pool_id is None and not opts.urn:
                raise TypeError("Missing required property 'identity_pool_id'")
            __props__.__dict__["identity_pool_id"] = identity_pool_id
            __props__.__dict__["role_mappings"] = role_mappings
            if roles is None and not opts.urn:
                raise TypeError("Missing required property 'roles'")
            __props__.__dict__["roles"] = roles
        super(IdentityPoolRoleAttachment, __self__).__init__(
            'aws:cognito/identityPoolRoleAttachment:IdentityPoolRoleAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            identity_pool_id: Optional[pulumi.Input[str]] = None,
            role_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IdentityPoolRoleAttachmentRoleMappingArgs']]]]] = None,
            roles: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'IdentityPoolRoleAttachment':
        """
        Get an existing IdentityPoolRoleAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] identity_pool_id: An identity pool ID in the format REGION:GUID.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IdentityPoolRoleAttachmentRoleMappingArgs']]]] role_mappings: A List of Role Mapping.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] roles: The map of roles associated with this pool. For a given role, the key will be either "authenticated" or "unauthenticated" and the value will be the Role ARN.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IdentityPoolRoleAttachmentState.__new__(_IdentityPoolRoleAttachmentState)

        __props__.__dict__["identity_pool_id"] = identity_pool_id
        __props__.__dict__["role_mappings"] = role_mappings
        __props__.__dict__["roles"] = roles
        return IdentityPoolRoleAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="identityPoolId")
    def identity_pool_id(self) -> pulumi.Output[str]:
        """
        An identity pool ID in the format REGION:GUID.
        """
        return pulumi.get(self, "identity_pool_id")

    @property
    @pulumi.getter(name="roleMappings")
    def role_mappings(self) -> pulumi.Output[Optional[Sequence['outputs.IdentityPoolRoleAttachmentRoleMapping']]]:
        """
        A List of Role Mapping.
        """
        return pulumi.get(self, "role_mappings")

    @property
    @pulumi.getter
    def roles(self) -> pulumi.Output[Mapping[str, str]]:
        """
        The map of roles associated with this pool. For a given role, the key will be either "authenticated" or "unauthenticated" and the value will be the Role ARN.
        """
        return pulumi.get(self, "roles")

