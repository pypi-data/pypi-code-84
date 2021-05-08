# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .queue import *
from .queue_iam_policy import *
from .queue_task import *
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
            if typ == "google-native:cloudtasks/v2beta2:Queue":
                return Queue(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:cloudtasks/v2beta2:QueueIamPolicy":
                return QueueIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:cloudtasks/v2beta2:QueueTask":
                return QueueTask(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("google-native", "cloudtasks/v2beta2", _module_instance)

_register_module()
