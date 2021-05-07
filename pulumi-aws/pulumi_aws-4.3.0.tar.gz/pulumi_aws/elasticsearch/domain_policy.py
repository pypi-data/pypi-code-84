# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DomainPolicyArgs', 'DomainPolicy']

@pulumi.input_type
class DomainPolicyArgs:
    def __init__(__self__, *,
                 access_policies: pulumi.Input[str],
                 domain_name: pulumi.Input[str]):
        """
        The set of arguments for constructing a DomainPolicy resource.
        :param pulumi.Input[str] access_policies: IAM policy document specifying the access policies for the domain
        :param pulumi.Input[str] domain_name: Name of the domain.
        """
        pulumi.set(__self__, "access_policies", access_policies)
        pulumi.set(__self__, "domain_name", domain_name)

    @property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> pulumi.Input[str]:
        """
        IAM policy document specifying the access policies for the domain
        """
        return pulumi.get(self, "access_policies")

    @access_policies.setter
    def access_policies(self, value: pulumi.Input[str]):
        pulumi.set(self, "access_policies", value)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        """
        Name of the domain.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)


@pulumi.input_type
class _DomainPolicyState:
    def __init__(__self__, *,
                 access_policies: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DomainPolicy resources.
        :param pulumi.Input[str] access_policies: IAM policy document specifying the access policies for the domain
        :param pulumi.Input[str] domain_name: Name of the domain.
        """
        if access_policies is not None:
            pulumi.set(__self__, "access_policies", access_policies)
        if domain_name is not None:
            pulumi.set(__self__, "domain_name", domain_name)

    @property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> Optional[pulumi.Input[str]]:
        """
        IAM policy document specifying the access policies for the domain
        """
        return pulumi.get(self, "access_policies")

    @access_policies.setter
    def access_policies(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_policies", value)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the domain.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_name", value)


class DomainPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_policies: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Allows setting policy to an Elasticsearch domain while referencing domain attributes (e.g. ARN)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.elasticsearch.Domain("example", elasticsearch_version="2.3")
        main = aws.elasticsearch.DomainPolicy("main",
            domain_name=example.domain_name,
            access_policies=example.arn.apply(lambda arn: f\"\"\"{{
            "Version": "2012-10-17",
            "Statement": [
                {{
                    "Action": "es:*",
                    "Principal": "*",
                    "Effect": "Allow",
                    "Condition": {{
                        "IpAddress": {{"aws:SourceIp": "127.0.0.1/32"}}
                    }},
                    "Resource": "{arn}/*"
                }}
            ]
        }}
        \"\"\"))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_policies: IAM policy document specifying the access policies for the domain
        :param pulumi.Input[str] domain_name: Name of the domain.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DomainPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Allows setting policy to an Elasticsearch domain while referencing domain attributes (e.g. ARN)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.elasticsearch.Domain("example", elasticsearch_version="2.3")
        main = aws.elasticsearch.DomainPolicy("main",
            domain_name=example.domain_name,
            access_policies=example.arn.apply(lambda arn: f\"\"\"{{
            "Version": "2012-10-17",
            "Statement": [
                {{
                    "Action": "es:*",
                    "Principal": "*",
                    "Effect": "Allow",
                    "Condition": {{
                        "IpAddress": {{"aws:SourceIp": "127.0.0.1/32"}}
                    }},
                    "Resource": "{arn}/*"
                }}
            ]
        }}
        \"\"\"))
        ```

        :param str resource_name: The name of the resource.
        :param DomainPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_policies: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = DomainPolicyArgs.__new__(DomainPolicyArgs)

            if access_policies is None and not opts.urn:
                raise TypeError("Missing required property 'access_policies'")
            __props__.__dict__["access_policies"] = access_policies
            if domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name'")
            __props__.__dict__["domain_name"] = domain_name
        super(DomainPolicy, __self__).__init__(
            'aws:elasticsearch/domainPolicy:DomainPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_policies: Optional[pulumi.Input[str]] = None,
            domain_name: Optional[pulumi.Input[str]] = None) -> 'DomainPolicy':
        """
        Get an existing DomainPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_policies: IAM policy document specifying the access policies for the domain
        :param pulumi.Input[str] domain_name: Name of the domain.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DomainPolicyState.__new__(_DomainPolicyState)

        __props__.__dict__["access_policies"] = access_policies
        __props__.__dict__["domain_name"] = domain_name
        return DomainPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> pulumi.Output[str]:
        """
        IAM policy document specifying the access policies for the domain
        """
        return pulumi.get(self, "access_policies")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        Name of the domain.
        """
        return pulumi.get(self, "domain_name")

