# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetVpcPeeringConnectionResult',
    'AwaitableGetVpcPeeringConnectionResult',
    'get_vpc_peering_connection',
]

@pulumi.output_type
class GetVpcPeeringConnectionResult:
    """
    A collection of values returned by getVpcPeeringConnection.
    """
    def __init__(__self__, accepter=None, cidr_block=None, cidr_block_sets=None, filters=None, id=None, owner_id=None, peer_cidr_block=None, peer_cidr_block_sets=None, peer_owner_id=None, peer_region=None, peer_vpc_id=None, region=None, requester=None, status=None, tags=None, vpc_id=None):
        if accepter and not isinstance(accepter, dict):
            raise TypeError("Expected argument 'accepter' to be a dict")
        pulumi.set(__self__, "accepter", accepter)
        if cidr_block and not isinstance(cidr_block, str):
            raise TypeError("Expected argument 'cidr_block' to be a str")
        pulumi.set(__self__, "cidr_block", cidr_block)
        if cidr_block_sets and not isinstance(cidr_block_sets, list):
            raise TypeError("Expected argument 'cidr_block_sets' to be a list")
        pulumi.set(__self__, "cidr_block_sets", cidr_block_sets)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if owner_id and not isinstance(owner_id, str):
            raise TypeError("Expected argument 'owner_id' to be a str")
        pulumi.set(__self__, "owner_id", owner_id)
        if peer_cidr_block and not isinstance(peer_cidr_block, str):
            raise TypeError("Expected argument 'peer_cidr_block' to be a str")
        pulumi.set(__self__, "peer_cidr_block", peer_cidr_block)
        if peer_cidr_block_sets and not isinstance(peer_cidr_block_sets, list):
            raise TypeError("Expected argument 'peer_cidr_block_sets' to be a list")
        pulumi.set(__self__, "peer_cidr_block_sets", peer_cidr_block_sets)
        if peer_owner_id and not isinstance(peer_owner_id, str):
            raise TypeError("Expected argument 'peer_owner_id' to be a str")
        pulumi.set(__self__, "peer_owner_id", peer_owner_id)
        if peer_region and not isinstance(peer_region, str):
            raise TypeError("Expected argument 'peer_region' to be a str")
        pulumi.set(__self__, "peer_region", peer_region)
        if peer_vpc_id and not isinstance(peer_vpc_id, str):
            raise TypeError("Expected argument 'peer_vpc_id' to be a str")
        pulumi.set(__self__, "peer_vpc_id", peer_vpc_id)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if requester and not isinstance(requester, dict):
            raise TypeError("Expected argument 'requester' to be a dict")
        pulumi.set(__self__, "requester", requester)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if vpc_id and not isinstance(vpc_id, str):
            raise TypeError("Expected argument 'vpc_id' to be a str")
        pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter
    def accepter(self) -> Mapping[str, bool]:
        """
        A configuration block that describes [VPC Peering Connection]
        (https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) options set for the accepter VPC.
        """
        return pulumi.get(self, "accepter")

    @property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> str:
        """
        A CIDR block associated to the VPC of the specific VPC Peering Connection.
        """
        return pulumi.get(self, "cidr_block")

    @property
    @pulumi.getter(name="cidrBlockSets")
    def cidr_block_sets(self) -> Sequence['outputs.GetVpcPeeringConnectionCidrBlockSetResult']:
        """
        List of objects with CIDR blocks of the requester VPC.
        """
        return pulumi.get(self, "cidr_block_sets")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetVpcPeeringConnectionFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> str:
        return pulumi.get(self, "owner_id")

    @property
    @pulumi.getter(name="peerCidrBlock")
    def peer_cidr_block(self) -> str:
        return pulumi.get(self, "peer_cidr_block")

    @property
    @pulumi.getter(name="peerCidrBlockSets")
    def peer_cidr_block_sets(self) -> Sequence['outputs.GetVpcPeeringConnectionPeerCidrBlockSetResult']:
        """
        List of objects with CIDR blocks of the accepter VPC.
        """
        return pulumi.get(self, "peer_cidr_block_sets")

    @property
    @pulumi.getter(name="peerOwnerId")
    def peer_owner_id(self) -> str:
        return pulumi.get(self, "peer_owner_id")

    @property
    @pulumi.getter(name="peerRegion")
    def peer_region(self) -> str:
        return pulumi.get(self, "peer_region")

    @property
    @pulumi.getter(name="peerVpcId")
    def peer_vpc_id(self) -> str:
        return pulumi.get(self, "peer_vpc_id")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def requester(self) -> Mapping[str, bool]:
        """
        A configuration block that describes [VPC Peering Connection]
        (https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) options set for the requester VPC.
        """
        return pulumi.get(self, "requester")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        return pulumi.get(self, "vpc_id")


class AwaitableGetVpcPeeringConnectionResult(GetVpcPeeringConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpcPeeringConnectionResult(
            accepter=self.accepter,
            cidr_block=self.cidr_block,
            cidr_block_sets=self.cidr_block_sets,
            filters=self.filters,
            id=self.id,
            owner_id=self.owner_id,
            peer_cidr_block=self.peer_cidr_block,
            peer_cidr_block_sets=self.peer_cidr_block_sets,
            peer_owner_id=self.peer_owner_id,
            peer_region=self.peer_region,
            peer_vpc_id=self.peer_vpc_id,
            region=self.region,
            requester=self.requester,
            status=self.status,
            tags=self.tags,
            vpc_id=self.vpc_id)


def get_vpc_peering_connection(cidr_block: Optional[str] = None,
                               filters: Optional[Sequence[pulumi.InputType['GetVpcPeeringConnectionFilterArgs']]] = None,
                               id: Optional[str] = None,
                               owner_id: Optional[str] = None,
                               peer_cidr_block: Optional[str] = None,
                               peer_owner_id: Optional[str] = None,
                               peer_region: Optional[str] = None,
                               peer_vpc_id: Optional[str] = None,
                               region: Optional[str] = None,
                               status: Optional[str] = None,
                               tags: Optional[Mapping[str, str]] = None,
                               vpc_id: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVpcPeeringConnectionResult:
    """
    The VPC Peering Connection data source provides details about
    a specific VPC peering connection.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    pc = aws.ec2.get_vpc_peering_connection(vpc_id=aws_vpc["foo"]["id"],
        peer_cidr_block="10.0.1.0/22")
    # Create a route table
    rt = aws.ec2.RouteTable("rt", vpc_id=aws_vpc["foo"]["id"])
    # Create a route
    route = aws.ec2.Route("route",
        route_table_id=rt.id,
        destination_cidr_block=pc.peer_cidr_block,
        vpc_peering_connection_id=pc.id)
    ```


    :param str cidr_block: The primary CIDR block of the requester VPC of the specific VPC Peering Connection to retrieve.
    :param Sequence[pulumi.InputType['GetVpcPeeringConnectionFilterArgs']] filters: Custom filter block as described below.
    :param str id: The ID of the specific VPC Peering Connection to retrieve.
    :param str owner_id: The AWS account ID of the owner of the requester VPC of the specific VPC Peering Connection to retrieve.
    :param str peer_cidr_block: The primary CIDR block of the accepter VPC of the specific VPC Peering Connection to retrieve.
    :param str peer_owner_id: The AWS account ID of the owner of the accepter VPC of the specific VPC Peering Connection to retrieve.
    :param str peer_region: The region of the accepter VPC of the specific VPC Peering Connection to retrieve.
    :param str peer_vpc_id: The ID of the accepter VPC of the specific VPC Peering Connection to retrieve.
    :param str region: The region of the requester VPC of the specific VPC Peering Connection to retrieve.
    :param str status: The status of the specific VPC Peering Connection to retrieve.
    :param Mapping[str, str] tags: A map of tags, each pair of which must exactly match
           a pair on the desired VPC Peering Connection.
    :param str vpc_id: The ID of the requester VPC of the specific VPC Peering Connection to retrieve.
    """
    __args__ = dict()
    __args__['cidrBlock'] = cidr_block
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['ownerId'] = owner_id
    __args__['peerCidrBlock'] = peer_cidr_block
    __args__['peerOwnerId'] = peer_owner_id
    __args__['peerRegion'] = peer_region
    __args__['peerVpcId'] = peer_vpc_id
    __args__['region'] = region
    __args__['status'] = status
    __args__['tags'] = tags
    __args__['vpcId'] = vpc_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:ec2/getVpcPeeringConnection:getVpcPeeringConnection', __args__, opts=opts, typ=GetVpcPeeringConnectionResult).value

    return AwaitableGetVpcPeeringConnectionResult(
        accepter=__ret__.accepter,
        cidr_block=__ret__.cidr_block,
        cidr_block_sets=__ret__.cidr_block_sets,
        filters=__ret__.filters,
        id=__ret__.id,
        owner_id=__ret__.owner_id,
        peer_cidr_block=__ret__.peer_cidr_block,
        peer_cidr_block_sets=__ret__.peer_cidr_block_sets,
        peer_owner_id=__ret__.peer_owner_id,
        peer_region=__ret__.peer_region,
        peer_vpc_id=__ret__.peer_vpc_id,
        region=__ret__.region,
        requester=__ret__.requester,
        status=__ret__.status,
        tags=__ret__.tags,
        vpc_id=__ret__.vpc_id)
