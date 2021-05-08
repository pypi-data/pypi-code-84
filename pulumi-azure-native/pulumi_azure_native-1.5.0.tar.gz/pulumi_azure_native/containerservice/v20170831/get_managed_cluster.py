# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetManagedClusterResult',
    'AwaitableGetManagedClusterResult',
    'get_managed_cluster',
]

@pulumi.output_type
class GetManagedClusterResult:
    """
    Managed cluster.
    """
    def __init__(__self__, agent_pool_profiles=None, dns_prefix=None, fqdn=None, id=None, kubernetes_version=None, linux_profile=None, location=None, name=None, provisioning_state=None, service_principal_profile=None, tags=None, type=None):
        if agent_pool_profiles and not isinstance(agent_pool_profiles, list):
            raise TypeError("Expected argument 'agent_pool_profiles' to be a list")
        pulumi.set(__self__, "agent_pool_profiles", agent_pool_profiles)
        if dns_prefix and not isinstance(dns_prefix, str):
            raise TypeError("Expected argument 'dns_prefix' to be a str")
        pulumi.set(__self__, "dns_prefix", dns_prefix)
        if fqdn and not isinstance(fqdn, str):
            raise TypeError("Expected argument 'fqdn' to be a str")
        pulumi.set(__self__, "fqdn", fqdn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kubernetes_version and not isinstance(kubernetes_version, str):
            raise TypeError("Expected argument 'kubernetes_version' to be a str")
        pulumi.set(__self__, "kubernetes_version", kubernetes_version)
        if linux_profile and not isinstance(linux_profile, dict):
            raise TypeError("Expected argument 'linux_profile' to be a dict")
        pulumi.set(__self__, "linux_profile", linux_profile)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if service_principal_profile and not isinstance(service_principal_profile, dict):
            raise TypeError("Expected argument 'service_principal_profile' to be a dict")
        pulumi.set(__self__, "service_principal_profile", service_principal_profile)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="agentPoolProfiles")
    def agent_pool_profiles(self) -> Optional[Sequence['outputs.ContainerServiceAgentPoolProfileResponse']]:
        """
        Properties of the agent pool.
        """
        return pulumi.get(self, "agent_pool_profiles")

    @property
    @pulumi.getter(name="dnsPrefix")
    def dns_prefix(self) -> Optional[str]:
        """
        DNS prefix specified when creating the managed cluster.
        """
        return pulumi.get(self, "dns_prefix")

    @property
    @pulumi.getter
    def fqdn(self) -> str:
        """
        FQDN for the master pool.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> Optional[str]:
        """
        Version of Kubernetes specified when creating the managed cluster.
        """
        return pulumi.get(self, "kubernetes_version")

    @property
    @pulumi.getter(name="linuxProfile")
    def linux_profile(self) -> Optional['outputs.ContainerServiceLinuxProfileResponse']:
        """
        Profile for Linux VMs in the container service cluster.
        """
        return pulumi.get(self, "linux_profile")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The current deployment or provisioning state, which only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="servicePrincipalProfile")
    def service_principal_profile(self) -> Optional['outputs.ContainerServiceServicePrincipalProfileResponse']:
        """
        Information about a service principal identity for the cluster to use for manipulating Azure APIs. Either secret or keyVaultSecretRef must be specified.
        """
        return pulumi.get(self, "service_principal_profile")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetManagedClusterResult(GetManagedClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedClusterResult(
            agent_pool_profiles=self.agent_pool_profiles,
            dns_prefix=self.dns_prefix,
            fqdn=self.fqdn,
            id=self.id,
            kubernetes_version=self.kubernetes_version,
            linux_profile=self.linux_profile,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            service_principal_profile=self.service_principal_profile,
            tags=self.tags,
            type=self.type)


def get_managed_cluster(resource_group_name: Optional[str] = None,
                        resource_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedClusterResult:
    """
    Managed cluster.


    :param str resource_group_name: The name of the resource group.
    :param str resource_name: The name of the managed cluster resource.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:containerservice/v20170831:getManagedCluster', __args__, opts=opts, typ=GetManagedClusterResult).value

    return AwaitableGetManagedClusterResult(
        agent_pool_profiles=__ret__.agent_pool_profiles,
        dns_prefix=__ret__.dns_prefix,
        fqdn=__ret__.fqdn,
        id=__ret__.id,
        kubernetes_version=__ret__.kubernetes_version,
        linux_profile=__ret__.linux_profile,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        service_principal_profile=__ret__.service_principal_profile,
        tags=__ret__.tags,
        type=__ret__.type)
