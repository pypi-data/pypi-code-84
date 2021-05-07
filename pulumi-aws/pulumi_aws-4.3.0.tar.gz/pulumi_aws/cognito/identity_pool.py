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

__all__ = ['IdentityPoolArgs', 'IdentityPool']

@pulumi.input_type
class IdentityPoolArgs:
    def __init__(__self__, *,
                 identity_pool_name: pulumi.Input[str],
                 allow_classic_flow: Optional[pulumi.Input[bool]] = None,
                 allow_unauthenticated_identities: Optional[pulumi.Input[bool]] = None,
                 cognito_identity_providers: Optional[pulumi.Input[Sequence[pulumi.Input['IdentityPoolCognitoIdentityProviderArgs']]]] = None,
                 developer_provider_name: Optional[pulumi.Input[str]] = None,
                 openid_connect_provider_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 saml_provider_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 supported_login_providers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a IdentityPool resource.
        :param pulumi.Input[str] identity_pool_name: The Cognito Identity Pool name.
        :param pulumi.Input[bool] allow_classic_flow: Enables or disables the classic / basic authentication flow. Default is `false`.
        :param pulumi.Input[bool] allow_unauthenticated_identities: Whether the identity pool supports unauthenticated logins or not.
        :param pulumi.Input[Sequence[pulumi.Input['IdentityPoolCognitoIdentityProviderArgs']]] cognito_identity_providers: An array of Amazon Cognito Identity user pools and their client IDs.
        :param pulumi.Input[str] developer_provider_name: The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
               backend and the Cognito service to communicate about the developer provider.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] openid_connect_provider_arns: Set of OpendID Connect provider ARNs.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] saml_provider_arns: An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] supported_login_providers: Key-Value pairs mapping provider names to provider app IDs.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the Identity Pool. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider .
        """
        pulumi.set(__self__, "identity_pool_name", identity_pool_name)
        if allow_classic_flow is not None:
            pulumi.set(__self__, "allow_classic_flow", allow_classic_flow)
        if allow_unauthenticated_identities is not None:
            pulumi.set(__self__, "allow_unauthenticated_identities", allow_unauthenticated_identities)
        if cognito_identity_providers is not None:
            pulumi.set(__self__, "cognito_identity_providers", cognito_identity_providers)
        if developer_provider_name is not None:
            pulumi.set(__self__, "developer_provider_name", developer_provider_name)
        if openid_connect_provider_arns is not None:
            pulumi.set(__self__, "openid_connect_provider_arns", openid_connect_provider_arns)
        if saml_provider_arns is not None:
            pulumi.set(__self__, "saml_provider_arns", saml_provider_arns)
        if supported_login_providers is not None:
            pulumi.set(__self__, "supported_login_providers", supported_login_providers)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter(name="identityPoolName")
    def identity_pool_name(self) -> pulumi.Input[str]:
        """
        The Cognito Identity Pool name.
        """
        return pulumi.get(self, "identity_pool_name")

    @identity_pool_name.setter
    def identity_pool_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "identity_pool_name", value)

    @property
    @pulumi.getter(name="allowClassicFlow")
    def allow_classic_flow(self) -> Optional[pulumi.Input[bool]]:
        """
        Enables or disables the classic / basic authentication flow. Default is `false`.
        """
        return pulumi.get(self, "allow_classic_flow")

    @allow_classic_flow.setter
    def allow_classic_flow(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_classic_flow", value)

    @property
    @pulumi.getter(name="allowUnauthenticatedIdentities")
    def allow_unauthenticated_identities(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the identity pool supports unauthenticated logins or not.
        """
        return pulumi.get(self, "allow_unauthenticated_identities")

    @allow_unauthenticated_identities.setter
    def allow_unauthenticated_identities(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_unauthenticated_identities", value)

    @property
    @pulumi.getter(name="cognitoIdentityProviders")
    def cognito_identity_providers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IdentityPoolCognitoIdentityProviderArgs']]]]:
        """
        An array of Amazon Cognito Identity user pools and their client IDs.
        """
        return pulumi.get(self, "cognito_identity_providers")

    @cognito_identity_providers.setter
    def cognito_identity_providers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IdentityPoolCognitoIdentityProviderArgs']]]]):
        pulumi.set(self, "cognito_identity_providers", value)

    @property
    @pulumi.getter(name="developerProviderName")
    def developer_provider_name(self) -> Optional[pulumi.Input[str]]:
        """
        The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
        backend and the Cognito service to communicate about the developer provider.
        """
        return pulumi.get(self, "developer_provider_name")

    @developer_provider_name.setter
    def developer_provider_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "developer_provider_name", value)

    @property
    @pulumi.getter(name="openidConnectProviderArns")
    def openid_connect_provider_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Set of OpendID Connect provider ARNs.
        """
        return pulumi.get(self, "openid_connect_provider_arns")

    @openid_connect_provider_arns.setter
    def openid_connect_provider_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "openid_connect_provider_arns", value)

    @property
    @pulumi.getter(name="samlProviderArns")
    def saml_provider_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
        """
        return pulumi.get(self, "saml_provider_arns")

    @saml_provider_arns.setter
    def saml_provider_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "saml_provider_arns", value)

    @property
    @pulumi.getter(name="supportedLoginProviders")
    def supported_login_providers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-Value pairs mapping provider names to provider app IDs.
        """
        return pulumi.get(self, "supported_login_providers")

    @supported_login_providers.setter
    def supported_login_providers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "supported_login_providers", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the Identity Pool. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider .
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)


@pulumi.input_type
class _IdentityPoolState:
    def __init__(__self__, *,
                 allow_classic_flow: Optional[pulumi.Input[bool]] = None,
                 allow_unauthenticated_identities: Optional[pulumi.Input[bool]] = None,
                 arn: Optional[pulumi.Input[str]] = None,
                 cognito_identity_providers: Optional[pulumi.Input[Sequence[pulumi.Input['IdentityPoolCognitoIdentityProviderArgs']]]] = None,
                 developer_provider_name: Optional[pulumi.Input[str]] = None,
                 identity_pool_name: Optional[pulumi.Input[str]] = None,
                 openid_connect_provider_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 saml_provider_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 supported_login_providers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering IdentityPool resources.
        :param pulumi.Input[bool] allow_classic_flow: Enables or disables the classic / basic authentication flow. Default is `false`.
        :param pulumi.Input[bool] allow_unauthenticated_identities: Whether the identity pool supports unauthenticated logins or not.
        :param pulumi.Input[str] arn: The ARN of the identity pool.
        :param pulumi.Input[Sequence[pulumi.Input['IdentityPoolCognitoIdentityProviderArgs']]] cognito_identity_providers: An array of Amazon Cognito Identity user pools and their client IDs.
        :param pulumi.Input[str] developer_provider_name: The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
               backend and the Cognito service to communicate about the developer provider.
        :param pulumi.Input[str] identity_pool_name: The Cognito Identity Pool name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] openid_connect_provider_arns: Set of OpendID Connect provider ARNs.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] saml_provider_arns: An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] supported_login_providers: Key-Value pairs mapping provider names to provider app IDs.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the Identity Pool. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider .
        """
        if allow_classic_flow is not None:
            pulumi.set(__self__, "allow_classic_flow", allow_classic_flow)
        if allow_unauthenticated_identities is not None:
            pulumi.set(__self__, "allow_unauthenticated_identities", allow_unauthenticated_identities)
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if cognito_identity_providers is not None:
            pulumi.set(__self__, "cognito_identity_providers", cognito_identity_providers)
        if developer_provider_name is not None:
            pulumi.set(__self__, "developer_provider_name", developer_provider_name)
        if identity_pool_name is not None:
            pulumi.set(__self__, "identity_pool_name", identity_pool_name)
        if openid_connect_provider_arns is not None:
            pulumi.set(__self__, "openid_connect_provider_arns", openid_connect_provider_arns)
        if saml_provider_arns is not None:
            pulumi.set(__self__, "saml_provider_arns", saml_provider_arns)
        if supported_login_providers is not None:
            pulumi.set(__self__, "supported_login_providers", supported_login_providers)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter(name="allowClassicFlow")
    def allow_classic_flow(self) -> Optional[pulumi.Input[bool]]:
        """
        Enables or disables the classic / basic authentication flow. Default is `false`.
        """
        return pulumi.get(self, "allow_classic_flow")

    @allow_classic_flow.setter
    def allow_classic_flow(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_classic_flow", value)

    @property
    @pulumi.getter(name="allowUnauthenticatedIdentities")
    def allow_unauthenticated_identities(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the identity pool supports unauthenticated logins or not.
        """
        return pulumi.get(self, "allow_unauthenticated_identities")

    @allow_unauthenticated_identities.setter
    def allow_unauthenticated_identities(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_unauthenticated_identities", value)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the identity pool.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="cognitoIdentityProviders")
    def cognito_identity_providers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IdentityPoolCognitoIdentityProviderArgs']]]]:
        """
        An array of Amazon Cognito Identity user pools and their client IDs.
        """
        return pulumi.get(self, "cognito_identity_providers")

    @cognito_identity_providers.setter
    def cognito_identity_providers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IdentityPoolCognitoIdentityProviderArgs']]]]):
        pulumi.set(self, "cognito_identity_providers", value)

    @property
    @pulumi.getter(name="developerProviderName")
    def developer_provider_name(self) -> Optional[pulumi.Input[str]]:
        """
        The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
        backend and the Cognito service to communicate about the developer provider.
        """
        return pulumi.get(self, "developer_provider_name")

    @developer_provider_name.setter
    def developer_provider_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "developer_provider_name", value)

    @property
    @pulumi.getter(name="identityPoolName")
    def identity_pool_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Cognito Identity Pool name.
        """
        return pulumi.get(self, "identity_pool_name")

    @identity_pool_name.setter
    def identity_pool_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identity_pool_name", value)

    @property
    @pulumi.getter(name="openidConnectProviderArns")
    def openid_connect_provider_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Set of OpendID Connect provider ARNs.
        """
        return pulumi.get(self, "openid_connect_provider_arns")

    @openid_connect_provider_arns.setter
    def openid_connect_provider_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "openid_connect_provider_arns", value)

    @property
    @pulumi.getter(name="samlProviderArns")
    def saml_provider_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
        """
        return pulumi.get(self, "saml_provider_arns")

    @saml_provider_arns.setter
    def saml_provider_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "saml_provider_arns", value)

    @property
    @pulumi.getter(name="supportedLoginProviders")
    def supported_login_providers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-Value pairs mapping provider names to provider app IDs.
        """
        return pulumi.get(self, "supported_login_providers")

    @supported_login_providers.setter
    def supported_login_providers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "supported_login_providers", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the Identity Pool. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider .
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)


class IdentityPool(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_classic_flow: Optional[pulumi.Input[bool]] = None,
                 allow_unauthenticated_identities: Optional[pulumi.Input[bool]] = None,
                 cognito_identity_providers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IdentityPoolCognitoIdentityProviderArgs']]]]] = None,
                 developer_provider_name: Optional[pulumi.Input[str]] = None,
                 identity_pool_name: Optional[pulumi.Input[str]] = None,
                 openid_connect_provider_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 saml_provider_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 supported_login_providers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides an AWS Cognito Identity Pool.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        default = aws.iam.SamlProvider("default", saml_metadata_document=(lambda path: open(path).read())("saml-metadata.xml"))
        main = aws.cognito.IdentityPool("main",
            identity_pool_name="identity pool",
            allow_unauthenticated_identities=False,
            allow_classic_flow=False,
            cognito_identity_providers=[
                aws.cognito.IdentityPoolCognitoIdentityProviderArgs(
                    client_id="6lhlkkfbfb4q5kpp90urffae",
                    provider_name="cognito-idp.us-east-1.amazonaws.com/us-east-1_Tv0493apJ",
                    server_side_token_check=False,
                ),
                aws.cognito.IdentityPoolCognitoIdentityProviderArgs(
                    client_id="7kodkvfqfb4qfkp39eurffae",
                    provider_name="cognito-idp.us-east-1.amazonaws.com/eu-west-1_Zr231apJu",
                    server_side_token_check=False,
                ),
            ],
            supported_login_providers={
                "graph.facebook.com": "7346241598935552",
                "accounts.google.com": "123456789012.apps.googleusercontent.com",
            },
            saml_provider_arns=[default.arn],
            openid_connect_provider_arns=["arn:aws:iam::123456789012:oidc-provider/id.example.com"])
        ```

        ## Import

        Cognito Identity Pool can be imported using the name, e.g.

        ```sh
         $ pulumi import aws:cognito/identityPool:IdentityPool mypool <identity-pool-id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_classic_flow: Enables or disables the classic / basic authentication flow. Default is `false`.
        :param pulumi.Input[bool] allow_unauthenticated_identities: Whether the identity pool supports unauthenticated logins or not.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IdentityPoolCognitoIdentityProviderArgs']]]] cognito_identity_providers: An array of Amazon Cognito Identity user pools and their client IDs.
        :param pulumi.Input[str] developer_provider_name: The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
               backend and the Cognito service to communicate about the developer provider.
        :param pulumi.Input[str] identity_pool_name: The Cognito Identity Pool name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] openid_connect_provider_arns: Set of OpendID Connect provider ARNs.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] saml_provider_arns: An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] supported_login_providers: Key-Value pairs mapping provider names to provider app IDs.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the Identity Pool. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider .
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IdentityPoolArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an AWS Cognito Identity Pool.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        default = aws.iam.SamlProvider("default", saml_metadata_document=(lambda path: open(path).read())("saml-metadata.xml"))
        main = aws.cognito.IdentityPool("main",
            identity_pool_name="identity pool",
            allow_unauthenticated_identities=False,
            allow_classic_flow=False,
            cognito_identity_providers=[
                aws.cognito.IdentityPoolCognitoIdentityProviderArgs(
                    client_id="6lhlkkfbfb4q5kpp90urffae",
                    provider_name="cognito-idp.us-east-1.amazonaws.com/us-east-1_Tv0493apJ",
                    server_side_token_check=False,
                ),
                aws.cognito.IdentityPoolCognitoIdentityProviderArgs(
                    client_id="7kodkvfqfb4qfkp39eurffae",
                    provider_name="cognito-idp.us-east-1.amazonaws.com/eu-west-1_Zr231apJu",
                    server_side_token_check=False,
                ),
            ],
            supported_login_providers={
                "graph.facebook.com": "7346241598935552",
                "accounts.google.com": "123456789012.apps.googleusercontent.com",
            },
            saml_provider_arns=[default.arn],
            openid_connect_provider_arns=["arn:aws:iam::123456789012:oidc-provider/id.example.com"])
        ```

        ## Import

        Cognito Identity Pool can be imported using the name, e.g.

        ```sh
         $ pulumi import aws:cognito/identityPool:IdentityPool mypool <identity-pool-id>
        ```

        :param str resource_name: The name of the resource.
        :param IdentityPoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IdentityPoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_classic_flow: Optional[pulumi.Input[bool]] = None,
                 allow_unauthenticated_identities: Optional[pulumi.Input[bool]] = None,
                 cognito_identity_providers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IdentityPoolCognitoIdentityProviderArgs']]]]] = None,
                 developer_provider_name: Optional[pulumi.Input[str]] = None,
                 identity_pool_name: Optional[pulumi.Input[str]] = None,
                 openid_connect_provider_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 saml_provider_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 supported_login_providers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = IdentityPoolArgs.__new__(IdentityPoolArgs)

            __props__.__dict__["allow_classic_flow"] = allow_classic_flow
            __props__.__dict__["allow_unauthenticated_identities"] = allow_unauthenticated_identities
            __props__.__dict__["cognito_identity_providers"] = cognito_identity_providers
            __props__.__dict__["developer_provider_name"] = developer_provider_name
            if identity_pool_name is None and not opts.urn:
                raise TypeError("Missing required property 'identity_pool_name'")
            __props__.__dict__["identity_pool_name"] = identity_pool_name
            __props__.__dict__["openid_connect_provider_arns"] = openid_connect_provider_arns
            __props__.__dict__["saml_provider_arns"] = saml_provider_arns
            __props__.__dict__["supported_login_providers"] = supported_login_providers
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tags_all"] = tags_all
            __props__.__dict__["arn"] = None
        super(IdentityPool, __self__).__init__(
            'aws:cognito/identityPool:IdentityPool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allow_classic_flow: Optional[pulumi.Input[bool]] = None,
            allow_unauthenticated_identities: Optional[pulumi.Input[bool]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            cognito_identity_providers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IdentityPoolCognitoIdentityProviderArgs']]]]] = None,
            developer_provider_name: Optional[pulumi.Input[str]] = None,
            identity_pool_name: Optional[pulumi.Input[str]] = None,
            openid_connect_provider_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            saml_provider_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            supported_login_providers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'IdentityPool':
        """
        Get an existing IdentityPool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_classic_flow: Enables or disables the classic / basic authentication flow. Default is `false`.
        :param pulumi.Input[bool] allow_unauthenticated_identities: Whether the identity pool supports unauthenticated logins or not.
        :param pulumi.Input[str] arn: The ARN of the identity pool.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IdentityPoolCognitoIdentityProviderArgs']]]] cognito_identity_providers: An array of Amazon Cognito Identity user pools and their client IDs.
        :param pulumi.Input[str] developer_provider_name: The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
               backend and the Cognito service to communicate about the developer provider.
        :param pulumi.Input[str] identity_pool_name: The Cognito Identity Pool name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] openid_connect_provider_arns: Set of OpendID Connect provider ARNs.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] saml_provider_arns: An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] supported_login_providers: Key-Value pairs mapping provider names to provider app IDs.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the Identity Pool. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider .
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IdentityPoolState.__new__(_IdentityPoolState)

        __props__.__dict__["allow_classic_flow"] = allow_classic_flow
        __props__.__dict__["allow_unauthenticated_identities"] = allow_unauthenticated_identities
        __props__.__dict__["arn"] = arn
        __props__.__dict__["cognito_identity_providers"] = cognito_identity_providers
        __props__.__dict__["developer_provider_name"] = developer_provider_name
        __props__.__dict__["identity_pool_name"] = identity_pool_name
        __props__.__dict__["openid_connect_provider_arns"] = openid_connect_provider_arns
        __props__.__dict__["saml_provider_arns"] = saml_provider_arns
        __props__.__dict__["supported_login_providers"] = supported_login_providers
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        return IdentityPool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowClassicFlow")
    def allow_classic_flow(self) -> pulumi.Output[Optional[bool]]:
        """
        Enables or disables the classic / basic authentication flow. Default is `false`.
        """
        return pulumi.get(self, "allow_classic_flow")

    @property
    @pulumi.getter(name="allowUnauthenticatedIdentities")
    def allow_unauthenticated_identities(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether the identity pool supports unauthenticated logins or not.
        """
        return pulumi.get(self, "allow_unauthenticated_identities")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the identity pool.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="cognitoIdentityProviders")
    def cognito_identity_providers(self) -> pulumi.Output[Optional[Sequence['outputs.IdentityPoolCognitoIdentityProvider']]]:
        """
        An array of Amazon Cognito Identity user pools and their client IDs.
        """
        return pulumi.get(self, "cognito_identity_providers")

    @property
    @pulumi.getter(name="developerProviderName")
    def developer_provider_name(self) -> pulumi.Output[Optional[str]]:
        """
        The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
        backend and the Cognito service to communicate about the developer provider.
        """
        return pulumi.get(self, "developer_provider_name")

    @property
    @pulumi.getter(name="identityPoolName")
    def identity_pool_name(self) -> pulumi.Output[str]:
        """
        The Cognito Identity Pool name.
        """
        return pulumi.get(self, "identity_pool_name")

    @property
    @pulumi.getter(name="openidConnectProviderArns")
    def openid_connect_provider_arns(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Set of OpendID Connect provider ARNs.
        """
        return pulumi.get(self, "openid_connect_provider_arns")

    @property
    @pulumi.getter(name="samlProviderArns")
    def saml_provider_arns(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
        """
        return pulumi.get(self, "saml_provider_arns")

    @property
    @pulumi.getter(name="supportedLoginProviders")
    def supported_login_providers(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-Value pairs mapping provider names to provider app IDs.
        """
        return pulumi.get(self, "supported_login_providers")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the Identity Pool. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider .
        """
        return pulumi.get(self, "tags_all")

