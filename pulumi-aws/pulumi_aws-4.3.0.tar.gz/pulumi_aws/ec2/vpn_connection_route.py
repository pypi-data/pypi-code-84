# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['VpnConnectionRouteArgs', 'VpnConnectionRoute']

@pulumi.input_type
class VpnConnectionRouteArgs:
    def __init__(__self__, *,
                 destination_cidr_block: pulumi.Input[str],
                 vpn_connection_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a VpnConnectionRoute resource.
        :param pulumi.Input[str] destination_cidr_block: The CIDR block associated with the local subnet of the customer network.
        :param pulumi.Input[str] vpn_connection_id: The ID of the VPN connection.
        """
        pulumi.set(__self__, "destination_cidr_block", destination_cidr_block)
        pulumi.set(__self__, "vpn_connection_id", vpn_connection_id)

    @property
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> pulumi.Input[str]:
        """
        The CIDR block associated with the local subnet of the customer network.
        """
        return pulumi.get(self, "destination_cidr_block")

    @destination_cidr_block.setter
    def destination_cidr_block(self, value: pulumi.Input[str]):
        pulumi.set(self, "destination_cidr_block", value)

    @property
    @pulumi.getter(name="vpnConnectionId")
    def vpn_connection_id(self) -> pulumi.Input[str]:
        """
        The ID of the VPN connection.
        """
        return pulumi.get(self, "vpn_connection_id")

    @vpn_connection_id.setter
    def vpn_connection_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpn_connection_id", value)


@pulumi.input_type
class _VpnConnectionRouteState:
    def __init__(__self__, *,
                 destination_cidr_block: Optional[pulumi.Input[str]] = None,
                 vpn_connection_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VpnConnectionRoute resources.
        :param pulumi.Input[str] destination_cidr_block: The CIDR block associated with the local subnet of the customer network.
        :param pulumi.Input[str] vpn_connection_id: The ID of the VPN connection.
        """
        if destination_cidr_block is not None:
            pulumi.set(__self__, "destination_cidr_block", destination_cidr_block)
        if vpn_connection_id is not None:
            pulumi.set(__self__, "vpn_connection_id", vpn_connection_id)

    @property
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> Optional[pulumi.Input[str]]:
        """
        The CIDR block associated with the local subnet of the customer network.
        """
        return pulumi.get(self, "destination_cidr_block")

    @destination_cidr_block.setter
    def destination_cidr_block(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination_cidr_block", value)

    @property
    @pulumi.getter(name="vpnConnectionId")
    def vpn_connection_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the VPN connection.
        """
        return pulumi.get(self, "vpn_connection_id")

    @vpn_connection_id.setter
    def vpn_connection_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpn_connection_id", value)


class VpnConnectionRoute(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination_cidr_block: Optional[pulumi.Input[str]] = None,
                 vpn_connection_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a static route between a VPN connection and a customer gateway.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        vpc = aws.ec2.Vpc("vpc", cidr_block="10.0.0.0/16")
        vpn_gateway = aws.ec2.VpnGateway("vpnGateway", vpc_id=vpc.id)
        customer_gateway = aws.ec2.CustomerGateway("customerGateway",
            bgp_asn="65000",
            ip_address="172.0.0.1",
            type="ipsec.1")
        main = aws.ec2.VpnConnection("main",
            vpn_gateway_id=vpn_gateway.id,
            customer_gateway_id=customer_gateway.id,
            type="ipsec.1",
            static_routes_only=True)
        office = aws.ec2.VpnConnectionRoute("office",
            destination_cidr_block="192.168.10.0/24",
            vpn_connection_id=main.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] destination_cidr_block: The CIDR block associated with the local subnet of the customer network.
        :param pulumi.Input[str] vpn_connection_id: The ID of the VPN connection.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VpnConnectionRouteArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a static route between a VPN connection and a customer gateway.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        vpc = aws.ec2.Vpc("vpc", cidr_block="10.0.0.0/16")
        vpn_gateway = aws.ec2.VpnGateway("vpnGateway", vpc_id=vpc.id)
        customer_gateway = aws.ec2.CustomerGateway("customerGateway",
            bgp_asn="65000",
            ip_address="172.0.0.1",
            type="ipsec.1")
        main = aws.ec2.VpnConnection("main",
            vpn_gateway_id=vpn_gateway.id,
            customer_gateway_id=customer_gateway.id,
            type="ipsec.1",
            static_routes_only=True)
        office = aws.ec2.VpnConnectionRoute("office",
            destination_cidr_block="192.168.10.0/24",
            vpn_connection_id=main.id)
        ```

        :param str resource_name: The name of the resource.
        :param VpnConnectionRouteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VpnConnectionRouteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination_cidr_block: Optional[pulumi.Input[str]] = None,
                 vpn_connection_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VpnConnectionRouteArgs.__new__(VpnConnectionRouteArgs)

            if destination_cidr_block is None and not opts.urn:
                raise TypeError("Missing required property 'destination_cidr_block'")
            __props__.__dict__["destination_cidr_block"] = destination_cidr_block
            if vpn_connection_id is None and not opts.urn:
                raise TypeError("Missing required property 'vpn_connection_id'")
            __props__.__dict__["vpn_connection_id"] = vpn_connection_id
        super(VpnConnectionRoute, __self__).__init__(
            'aws:ec2/vpnConnectionRoute:VpnConnectionRoute',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            destination_cidr_block: Optional[pulumi.Input[str]] = None,
            vpn_connection_id: Optional[pulumi.Input[str]] = None) -> 'VpnConnectionRoute':
        """
        Get an existing VpnConnectionRoute resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] destination_cidr_block: The CIDR block associated with the local subnet of the customer network.
        :param pulumi.Input[str] vpn_connection_id: The ID of the VPN connection.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VpnConnectionRouteState.__new__(_VpnConnectionRouteState)

        __props__.__dict__["destination_cidr_block"] = destination_cidr_block
        __props__.__dict__["vpn_connection_id"] = vpn_connection_id
        return VpnConnectionRoute(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> pulumi.Output[str]:
        """
        The CIDR block associated with the local subnet of the customer network.
        """
        return pulumi.get(self, "destination_cidr_block")

    @property
    @pulumi.getter(name="vpnConnectionId")
    def vpn_connection_id(self) -> pulumi.Output[str]:
        """
        The ID of the VPN connection.
        """
        return pulumi.get(self, "vpn_connection_id")

