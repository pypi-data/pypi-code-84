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
    'GetPacketCaptureResult',
    'AwaitableGetPacketCaptureResult',
    'get_packet_capture',
]

@pulumi.output_type
class GetPacketCaptureResult:
    """
    Information about packet capture session.
    """
    def __init__(__self__, bytes_to_capture_per_packet=None, etag=None, filters=None, id=None, name=None, provisioning_state=None, storage_location=None, target=None, time_limit_in_seconds=None, total_bytes_per_session=None):
        if bytes_to_capture_per_packet and not isinstance(bytes_to_capture_per_packet, int):
            raise TypeError("Expected argument 'bytes_to_capture_per_packet' to be a int")
        pulumi.set(__self__, "bytes_to_capture_per_packet", bytes_to_capture_per_packet)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if storage_location and not isinstance(storage_location, dict):
            raise TypeError("Expected argument 'storage_location' to be a dict")
        pulumi.set(__self__, "storage_location", storage_location)
        if target and not isinstance(target, str):
            raise TypeError("Expected argument 'target' to be a str")
        pulumi.set(__self__, "target", target)
        if time_limit_in_seconds and not isinstance(time_limit_in_seconds, int):
            raise TypeError("Expected argument 'time_limit_in_seconds' to be a int")
        pulumi.set(__self__, "time_limit_in_seconds", time_limit_in_seconds)
        if total_bytes_per_session and not isinstance(total_bytes_per_session, int):
            raise TypeError("Expected argument 'total_bytes_per_session' to be a int")
        pulumi.set(__self__, "total_bytes_per_session", total_bytes_per_session)

    @property
    @pulumi.getter(name="bytesToCapturePerPacket")
    def bytes_to_capture_per_packet(self) -> Optional[int]:
        """
        Number of bytes captured per packet, the remaining bytes are truncated.
        """
        return pulumi.get(self, "bytes_to_capture_per_packet")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.PacketCaptureFilterResponse']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        ID of the packet capture operation.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the packet capture session.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[str]:
        """
        The provisioning state of the packet capture session.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="storageLocation")
    def storage_location(self) -> 'outputs.PacketCaptureStorageLocationResponse':
        """
        Describes the storage location for a packet capture session.
        """
        return pulumi.get(self, "storage_location")

    @property
    @pulumi.getter
    def target(self) -> str:
        """
        The ID of the targeted resource, only VM is currently supported.
        """
        return pulumi.get(self, "target")

    @property
    @pulumi.getter(name="timeLimitInSeconds")
    def time_limit_in_seconds(self) -> Optional[int]:
        """
        Maximum duration of the capture session in seconds.
        """
        return pulumi.get(self, "time_limit_in_seconds")

    @property
    @pulumi.getter(name="totalBytesPerSession")
    def total_bytes_per_session(self) -> Optional[int]:
        """
        Maximum size of the capture output.
        """
        return pulumi.get(self, "total_bytes_per_session")


class AwaitableGetPacketCaptureResult(GetPacketCaptureResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPacketCaptureResult(
            bytes_to_capture_per_packet=self.bytes_to_capture_per_packet,
            etag=self.etag,
            filters=self.filters,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            storage_location=self.storage_location,
            target=self.target,
            time_limit_in_seconds=self.time_limit_in_seconds,
            total_bytes_per_session=self.total_bytes_per_session)


def get_packet_capture(network_watcher_name: Optional[str] = None,
                       packet_capture_name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPacketCaptureResult:
    """
    Information about packet capture session.


    :param str network_watcher_name: The name of the network watcher.
    :param str packet_capture_name: The name of the packet capture session.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['networkWatcherName'] = network_watcher_name
    __args__['packetCaptureName'] = packet_capture_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20170801:getPacketCapture', __args__, opts=opts, typ=GetPacketCaptureResult).value

    return AwaitableGetPacketCaptureResult(
        bytes_to_capture_per_packet=__ret__.bytes_to_capture_per_packet,
        etag=__ret__.etag,
        filters=__ret__.filters,
        id=__ret__.id,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        storage_location=__ret__.storage_location,
        target=__ret__.target,
        time_limit_in_seconds=__ret__.time_limit_in_seconds,
        total_bytes_per_session=__ret__.total_bytes_per_session)
