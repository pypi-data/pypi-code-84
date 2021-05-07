# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .cluster import *
from .event_subscription import *
from .get_cluster import *
from .get_orderable_cluster import *
from .get_service_account import *
from .parameter_group import *
from .security_group import *
from .snapshot_copy_grant import *
from .snapshot_schedule import *
from .snapshot_schedule_association import *
from .subnet_group import *
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
            if typ == "aws:redshift/cluster:Cluster":
                return Cluster(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:redshift/eventSubscription:EventSubscription":
                return EventSubscription(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:redshift/parameterGroup:ParameterGroup":
                return ParameterGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:redshift/securityGroup:SecurityGroup":
                return SecurityGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:redshift/snapshotCopyGrant:SnapshotCopyGrant":
                return SnapshotCopyGrant(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:redshift/snapshotSchedule:SnapshotSchedule":
                return SnapshotSchedule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:redshift/snapshotScheduleAssociation:SnapshotScheduleAssociation":
                return SnapshotScheduleAssociation(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:redshift/subnetGroup:SubnetGroup":
                return SubnetGroup(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("aws", "redshift/cluster", _module_instance)
    pulumi.runtime.register_resource_module("aws", "redshift/eventSubscription", _module_instance)
    pulumi.runtime.register_resource_module("aws", "redshift/parameterGroup", _module_instance)
    pulumi.runtime.register_resource_module("aws", "redshift/securityGroup", _module_instance)
    pulumi.runtime.register_resource_module("aws", "redshift/snapshotCopyGrant", _module_instance)
    pulumi.runtime.register_resource_module("aws", "redshift/snapshotSchedule", _module_instance)
    pulumi.runtime.register_resource_module("aws", "redshift/snapshotScheduleAssociation", _module_instance)
    pulumi.runtime.register_resource_module("aws", "redshift/subnetGroup", _module_instance)

_register_module()
