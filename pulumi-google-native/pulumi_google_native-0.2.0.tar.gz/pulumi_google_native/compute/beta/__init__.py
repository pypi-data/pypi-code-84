# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .address import *
from .autoscaler import *
from .backend_bucket import *
from .backend_bucket_iam_policy import *
from .backend_service import *
from .disk import *
from .disk_iam_policy import *
from .external_vpn_gateway import *
from .firewall import *
from .firewall_policy import *
from .firewall_policy_iam_policy import *
from .forwarding_rule import *
from .global_address import *
from .global_forwarding_rule import *
from .global_network_endpoint_group import *
from .global_public_delegated_prefix import *
from .health_check import *
from .http_health_check import *
from .https_health_check import *
from .image import *
from .image_iam_policy import *
from .instance import *
from .instance_group import *
from .instance_group_manager import *
from .instance_iam_policy import *
from .instance_template import *
from .instance_template_iam_policy import *
from .interconnect import *
from .interconnect_attachment import *
from .license import *
from .license_iam_policy import *
from .machine_image import *
from .machine_image_iam_policy import *
from .network import *
from .network_endpoint_group import *
from .node_group import *
from .node_group_iam_policy import *
from .node_template import *
from .node_template_iam_policy import *
from .organization_security_policy import *
from .packet_mirroring import *
from .public_advertised_prefix import *
from .public_delegated_prefix import *
from .region_autoscaler import *
from .region_backend_service import *
from .region_commitment import *
from .region_disk import *
from .region_disk_iam_policy import *
from .region_health_check import *
from .region_health_check_service import *
from .region_instance_group_manager import *
from .region_network_endpoint_group import *
from .region_notification_endpoint import *
from .region_ssl_certificate import *
from .region_target_http_proxy import *
from .region_target_https_proxy import *
from .region_url_map import *
from .reservation import *
from .reservation_iam_policy import *
from .resource_policy import *
from .resource_policy_iam_policy import *
from .route import *
from .router import *
from .security_policy import *
from .service_attachment import *
from .service_attachment_iam_policy import *
from .snapshot import *
from .snapshot_iam_policy import *
from .ssl_certificate import *
from .ssl_policy import *
from .subnetwork import *
from .subnetwork_iam_policy import *
from .target_grpc_proxy import *
from .target_http_proxy import *
from .target_https_proxy import *
from .target_instance import *
from .target_pool import *
from .target_ssl_proxy import *
from .target_tcp_proxy import *
from .target_vpn_gateway import *
from .url_map import *
from .vpn_gateway import *
from .vpn_tunnel import *
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
            if typ == "google-native:compute/beta:Address":
                return Address(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:Autoscaler":
                return Autoscaler(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:BackendBucket":
                return BackendBucket(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:BackendBucketIamPolicy":
                return BackendBucketIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:BackendService":
                return BackendService(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:Disk":
                return Disk(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:DiskIamPolicy":
                return DiskIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:ExternalVpnGateway":
                return ExternalVpnGateway(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:Firewall":
                return Firewall(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:FirewallPolicy":
                return FirewallPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:FirewallPolicyIamPolicy":
                return FirewallPolicyIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:ForwardingRule":
                return ForwardingRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:GlobalAddress":
                return GlobalAddress(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:GlobalForwardingRule":
                return GlobalForwardingRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:GlobalNetworkEndpointGroup":
                return GlobalNetworkEndpointGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:GlobalPublicDelegatedPrefix":
                return GlobalPublicDelegatedPrefix(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:HealthCheck":
                return HealthCheck(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:HttpHealthCheck":
                return HttpHealthCheck(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:HttpsHealthCheck":
                return HttpsHealthCheck(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:Image":
                return Image(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:ImageIamPolicy":
                return ImageIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:Instance":
                return Instance(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:InstanceGroup":
                return InstanceGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:InstanceGroupManager":
                return InstanceGroupManager(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:InstanceIamPolicy":
                return InstanceIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:InstanceTemplate":
                return InstanceTemplate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:InstanceTemplateIamPolicy":
                return InstanceTemplateIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:Interconnect":
                return Interconnect(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:InterconnectAttachment":
                return InterconnectAttachment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:License":
                return License(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:LicenseIamPolicy":
                return LicenseIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:MachineImage":
                return MachineImage(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:MachineImageIamPolicy":
                return MachineImageIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:Network":
                return Network(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:NetworkEndpointGroup":
                return NetworkEndpointGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:NodeGroup":
                return NodeGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:NodeGroupIamPolicy":
                return NodeGroupIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:NodeTemplate":
                return NodeTemplate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:NodeTemplateIamPolicy":
                return NodeTemplateIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:OrganizationSecurityPolicy":
                return OrganizationSecurityPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:PacketMirroring":
                return PacketMirroring(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:PublicAdvertisedPrefix":
                return PublicAdvertisedPrefix(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:PublicDelegatedPrefix":
                return PublicDelegatedPrefix(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:RegionAutoscaler":
                return RegionAutoscaler(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:RegionBackendService":
                return RegionBackendService(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:RegionCommitment":
                return RegionCommitment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:RegionDisk":
                return RegionDisk(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:RegionDiskIamPolicy":
                return RegionDiskIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:RegionHealthCheck":
                return RegionHealthCheck(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:RegionHealthCheckService":
                return RegionHealthCheckService(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:RegionInstanceGroupManager":
                return RegionInstanceGroupManager(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:RegionNetworkEndpointGroup":
                return RegionNetworkEndpointGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:RegionNotificationEndpoint":
                return RegionNotificationEndpoint(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:RegionSslCertificate":
                return RegionSslCertificate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:RegionTargetHttpProxy":
                return RegionTargetHttpProxy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:RegionTargetHttpsProxy":
                return RegionTargetHttpsProxy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:RegionUrlMap":
                return RegionUrlMap(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:Reservation":
                return Reservation(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:ReservationIamPolicy":
                return ReservationIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:ResourcePolicy":
                return ResourcePolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:ResourcePolicyIamPolicy":
                return ResourcePolicyIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:Route":
                return Route(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:Router":
                return Router(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:SecurityPolicy":
                return SecurityPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:ServiceAttachment":
                return ServiceAttachment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:ServiceAttachmentIamPolicy":
                return ServiceAttachmentIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:Snapshot":
                return Snapshot(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:SnapshotIamPolicy":
                return SnapshotIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:SslCertificate":
                return SslCertificate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:SslPolicy":
                return SslPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:Subnetwork":
                return Subnetwork(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:SubnetworkIamPolicy":
                return SubnetworkIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:TargetGrpcProxy":
                return TargetGrpcProxy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:TargetHttpProxy":
                return TargetHttpProxy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:TargetHttpsProxy":
                return TargetHttpsProxy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:TargetInstance":
                return TargetInstance(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:TargetPool":
                return TargetPool(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:TargetSslProxy":
                return TargetSslProxy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:TargetTcpProxy":
                return TargetTcpProxy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:TargetVpnGateway":
                return TargetVpnGateway(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:UrlMap":
                return UrlMap(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:VpnGateway":
                return VpnGateway(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:compute/beta:VpnTunnel":
                return VpnTunnel(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("google-native", "compute/beta", _module_instance)

_register_module()
