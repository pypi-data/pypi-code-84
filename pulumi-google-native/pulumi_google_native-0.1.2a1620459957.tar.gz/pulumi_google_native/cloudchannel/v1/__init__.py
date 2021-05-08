# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .account_channel_partner_link import *
from .account_channel_partner_link_customer import *
from .account_customer import *
from .account_customer_entitlement import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from ... import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "google-native:cloudchannel/v1:AccountChannelPartnerLink":
                return AccountChannelPartnerLink(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:cloudchannel/v1:AccountChannelPartnerLinkCustomer":
                return AccountChannelPartnerLinkCustomer(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:cloudchannel/v1:AccountCustomer":
                return AccountCustomer(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:cloudchannel/v1:AccountCustomerEntitlement":
                return AccountCustomerEntitlement(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("google-native", "cloudchannel/v1", _module_instance)

_register_module()
