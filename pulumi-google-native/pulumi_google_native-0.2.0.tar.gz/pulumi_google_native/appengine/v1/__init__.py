# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .app import *
from .app_authorized_certificate import *
from .app_domain_mapping import *
from .app_firewall_ingress_rule import *
from .app_service_version import *
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
            if typ == "google-native:appengine/v1:App":
                return App(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:appengine/v1:AppAuthorizedCertificate":
                return AppAuthorizedCertificate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:appengine/v1:AppDomainMapping":
                return AppDomainMapping(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:appengine/v1:AppFirewallIngressRule":
                return AppFirewallIngressRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:appengine/v1:AppServiceVersion":
                return AppServiceVersion(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("google-native", "appengine/v1", _module_instance)

_register_module()
