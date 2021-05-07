# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .data_lake_settings import *
from .get_data_lake_settings import *
from .get_permissions import *
from .get_resource import *
from .permissions import *
from .resource import *
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
            if typ == "aws:lakeformation/dataLakeSettings:DataLakeSettings":
                return DataLakeSettings(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:lakeformation/permissions:Permissions":
                return Permissions(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:lakeformation/resource:Resource":
                return Resource(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("aws", "lakeformation/dataLakeSettings", _module_instance)
    pulumi.runtime.register_resource_module("aws", "lakeformation/permissions", _module_instance)
    pulumi.runtime.register_resource_module("aws", "lakeformation/resource", _module_instance)

_register_module()
