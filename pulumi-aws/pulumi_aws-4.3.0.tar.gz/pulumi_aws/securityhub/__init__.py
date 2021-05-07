# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .account import *
from .action_target import *
from .insight import *
from .invite_accepter import *
from .member import *
from .organization_admin_account import *
from .product_subscription import *
from .standards_subscription import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "aws:securityhub/account:Account":
                return Account(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:securityhub/actionTarget:ActionTarget":
                return ActionTarget(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:securityhub/insight:Insight":
                return Insight(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:securityhub/inviteAccepter:InviteAccepter":
                return InviteAccepter(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:securityhub/member:Member":
                return Member(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:securityhub/organizationAdminAccount:OrganizationAdminAccount":
                return OrganizationAdminAccount(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:securityhub/productSubscription:ProductSubscription":
                return ProductSubscription(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:securityhub/standardsSubscription:StandardsSubscription":
                return StandardsSubscription(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("aws", "securityhub/account", _module_instance)
    pulumi.runtime.register_resource_module("aws", "securityhub/actionTarget", _module_instance)
    pulumi.runtime.register_resource_module("aws", "securityhub/insight", _module_instance)
    pulumi.runtime.register_resource_module("aws", "securityhub/inviteAccepter", _module_instance)
    pulumi.runtime.register_resource_module("aws", "securityhub/member", _module_instance)
    pulumi.runtime.register_resource_module("aws", "securityhub/organizationAdminAccount", _module_instance)
    pulumi.runtime.register_resource_module("aws", "securityhub/productSubscription", _module_instance)
    pulumi.runtime.register_resource_module("aws", "securityhub/standardsSubscription", _module_instance)

_register_module()
