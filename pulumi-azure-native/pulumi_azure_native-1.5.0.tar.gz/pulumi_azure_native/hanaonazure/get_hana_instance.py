# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetHanaInstanceResult',
    'AwaitableGetHanaInstanceResult',
    'get_hana_instance',
]

@pulumi.output_type
class GetHanaInstanceResult:
    """
    HANA instance info on Azure (ARM properties and HANA properties)
    """
    def __init__(__self__, hana_instance_id=None, hardware_profile=None, hw_revision=None, id=None, location=None, name=None, network_profile=None, os_profile=None, partner_node_id=None, power_state=None, provisioning_state=None, proximity_placement_group=None, storage_profile=None, tags=None, type=None):
        if hana_instance_id and not isinstance(hana_instance_id, str):
            raise TypeError("Expected argument 'hana_instance_id' to be a str")
        pulumi.set(__self__, "hana_instance_id", hana_instance_id)
        if hardware_profile and not isinstance(hardware_profile, dict):
            raise TypeError("Expected argument 'hardware_profile' to be a dict")
        pulumi.set(__self__, "hardware_profile", hardware_profile)
        if hw_revision and not isinstance(hw_revision, str):
            raise TypeError("Expected argument 'hw_revision' to be a str")
        pulumi.set(__self__, "hw_revision", hw_revision)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_profile and not isinstance(network_profile, dict):
            raise TypeError("Expected argument 'network_profile' to be a dict")
        pulumi.set(__self__, "network_profile", network_profile)
        if os_profile and not isinstance(os_profile, dict):
            raise TypeError("Expected argument 'os_profile' to be a dict")
        pulumi.set(__self__, "os_profile", os_profile)
        if partner_node_id and not isinstance(partner_node_id, str):
            raise TypeError("Expected argument 'partner_node_id' to be a str")
        pulumi.set(__self__, "partner_node_id", partner_node_id)
        if power_state and not isinstance(power_state, str):
            raise TypeError("Expected argument 'power_state' to be a str")
        pulumi.set(__self__, "power_state", power_state)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if proximity_placement_group and not isinstance(proximity_placement_group, str):
            raise TypeError("Expected argument 'proximity_placement_group' to be a str")
        pulumi.set(__self__, "proximity_placement_group", proximity_placement_group)
        if storage_profile and not isinstance(storage_profile, dict):
            raise TypeError("Expected argument 'storage_profile' to be a dict")
        pulumi.set(__self__, "storage_profile", storage_profile)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="hanaInstanceId")
    def hana_instance_id(self) -> Optional[str]:
        """
        Specifies the HANA instance unique ID.
        """
        return pulumi.get(self, "hana_instance_id")

    @property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> Optional['outputs.HardwareProfileResponse']:
        """
        Specifies the hardware settings for the HANA instance.
        """
        return pulumi.get(self, "hardware_profile")

    @property
    @pulumi.getter(name="hwRevision")
    def hw_revision(self) -> Optional[str]:
        """
        Hardware revision of a HANA instance
        """
        return pulumi.get(self, "hw_revision")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
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
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional['outputs.NetworkProfileResponse']:
        """
        Specifies the network settings for the HANA instance.
        """
        return pulumi.get(self, "network_profile")

    @property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional['outputs.OSProfileResponse']:
        """
        Specifies the operating system settings for the HANA instance.
        """
        return pulumi.get(self, "os_profile")

    @property
    @pulumi.getter(name="partnerNodeId")
    def partner_node_id(self) -> Optional[str]:
        """
        ARM ID of another HanaInstance that will share a network with this HanaInstance
        """
        return pulumi.get(self, "partner_node_id")

    @property
    @pulumi.getter(name="powerState")
    def power_state(self) -> Optional[str]:
        """
        Resource power state
        """
        return pulumi.get(self, "power_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[str]:
        """
        State of provisioning of the HanaInstance
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="proximityPlacementGroup")
    def proximity_placement_group(self) -> Optional[str]:
        """
        Resource proximity placement group
        """
        return pulumi.get(self, "proximity_placement_group")

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional['outputs.StorageProfileResponse']:
        """
        Specifies the storage settings for the HANA instance disks.
        """
        return pulumi.get(self, "storage_profile")

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


class AwaitableGetHanaInstanceResult(GetHanaInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetHanaInstanceResult(
            hana_instance_id=self.hana_instance_id,
            hardware_profile=self.hardware_profile,
            hw_revision=self.hw_revision,
            id=self.id,
            location=self.location,
            name=self.name,
            network_profile=self.network_profile,
            os_profile=self.os_profile,
            partner_node_id=self.partner_node_id,
            power_state=self.power_state,
            provisioning_state=self.provisioning_state,
            proximity_placement_group=self.proximity_placement_group,
            storage_profile=self.storage_profile,
            tags=self.tags,
            type=self.type)


def get_hana_instance(hana_instance_name: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetHanaInstanceResult:
    """
    HANA instance info on Azure (ARM properties and HANA properties)
    API Version: 2017-11-03-preview.


    :param str hana_instance_name: Name of the SAP HANA on Azure instance.
    :param str resource_group_name: Name of the resource group.
    """
    __args__ = dict()
    __args__['hanaInstanceName'] = hana_instance_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:hanaonazure:getHanaInstance', __args__, opts=opts, typ=GetHanaInstanceResult).value

    return AwaitableGetHanaInstanceResult(
        hana_instance_id=__ret__.hana_instance_id,
        hardware_profile=__ret__.hardware_profile,
        hw_revision=__ret__.hw_revision,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        network_profile=__ret__.network_profile,
        os_profile=__ret__.os_profile,
        partner_node_id=__ret__.partner_node_id,
        power_state=__ret__.power_state,
        provisioning_state=__ret__.provisioning_state,
        proximity_placement_group=__ret__.proximity_placement_group,
        storage_profile=__ret__.storage_profile,
        tags=__ret__.tags,
        type=__ret__.type)
