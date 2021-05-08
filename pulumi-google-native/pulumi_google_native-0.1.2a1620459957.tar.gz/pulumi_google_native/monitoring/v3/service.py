# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ServiceArgs', 'Service']

@pulumi.input_type
class ServiceArgs:
    def __init__(__self__, *,
                 services_id: pulumi.Input[str],
                 v3_id: pulumi.Input[str],
                 v3_id1: pulumi.Input[str],
                 app_engine: Optional[pulumi.Input['AppEngineArgs']] = None,
                 cloud_endpoints: Optional[pulumi.Input['CloudEndpointsArgs']] = None,
                 cluster_istio: Optional[pulumi.Input['ClusterIstioArgs']] = None,
                 custom: Optional[pulumi.Input['CustomArgs']] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 istio_canonical_service: Optional[pulumi.Input['IstioCanonicalServiceArgs']] = None,
                 mesh_istio: Optional[pulumi.Input['MeshIstioArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 service_id: Optional[pulumi.Input[str]] = None,
                 telemetry: Optional[pulumi.Input['TelemetryArgs']] = None):
        """
        The set of arguments for constructing a Service resource.
        :param pulumi.Input['AppEngineArgs'] app_engine: Type used for App Engine services.
        :param pulumi.Input['CloudEndpointsArgs'] cloud_endpoints: Type used for Cloud Endpoints services.
        :param pulumi.Input['ClusterIstioArgs'] cluster_istio: Type used for Istio services that live in a Kubernetes cluster.
        :param pulumi.Input['CustomArgs'] custom: Custom service type.
        :param pulumi.Input[str] display_name: Name used for UI elements listing this Service.
        :param pulumi.Input['IstioCanonicalServiceArgs'] istio_canonical_service: Type used for canonical services scoped to an Istio mesh. Metrics for Istio are documented here (https://istio.io/latest/docs/reference/config/metrics/)
        :param pulumi.Input['MeshIstioArgs'] mesh_istio: Type used for Istio services scoped to an Istio mesh.
        :param pulumi.Input[str] name: Resource name for this Service. The format is: projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID] 
        :param pulumi.Input['TelemetryArgs'] telemetry: Configuration for how to query telemetry on a Service.
        """
        pulumi.set(__self__, "services_id", services_id)
        pulumi.set(__self__, "v3_id", v3_id)
        pulumi.set(__self__, "v3_id1", v3_id1)
        if app_engine is not None:
            pulumi.set(__self__, "app_engine", app_engine)
        if cloud_endpoints is not None:
            pulumi.set(__self__, "cloud_endpoints", cloud_endpoints)
        if cluster_istio is not None:
            pulumi.set(__self__, "cluster_istio", cluster_istio)
        if custom is not None:
            pulumi.set(__self__, "custom", custom)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if istio_canonical_service is not None:
            pulumi.set(__self__, "istio_canonical_service", istio_canonical_service)
        if mesh_istio is not None:
            pulumi.set(__self__, "mesh_istio", mesh_istio)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if service_id is not None:
            pulumi.set(__self__, "service_id", service_id)
        if telemetry is not None:
            pulumi.set(__self__, "telemetry", telemetry)

    @property
    @pulumi.getter(name="servicesId")
    def services_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "services_id")

    @services_id.setter
    def services_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "services_id", value)

    @property
    @pulumi.getter(name="v3Id")
    def v3_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "v3_id")

    @v3_id.setter
    def v3_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "v3_id", value)

    @property
    @pulumi.getter(name="v3Id1")
    def v3_id1(self) -> pulumi.Input[str]:
        return pulumi.get(self, "v3_id1")

    @v3_id1.setter
    def v3_id1(self, value: pulumi.Input[str]):
        pulumi.set(self, "v3_id1", value)

    @property
    @pulumi.getter(name="appEngine")
    def app_engine(self) -> Optional[pulumi.Input['AppEngineArgs']]:
        """
        Type used for App Engine services.
        """
        return pulumi.get(self, "app_engine")

    @app_engine.setter
    def app_engine(self, value: Optional[pulumi.Input['AppEngineArgs']]):
        pulumi.set(self, "app_engine", value)

    @property
    @pulumi.getter(name="cloudEndpoints")
    def cloud_endpoints(self) -> Optional[pulumi.Input['CloudEndpointsArgs']]:
        """
        Type used for Cloud Endpoints services.
        """
        return pulumi.get(self, "cloud_endpoints")

    @cloud_endpoints.setter
    def cloud_endpoints(self, value: Optional[pulumi.Input['CloudEndpointsArgs']]):
        pulumi.set(self, "cloud_endpoints", value)

    @property
    @pulumi.getter(name="clusterIstio")
    def cluster_istio(self) -> Optional[pulumi.Input['ClusterIstioArgs']]:
        """
        Type used for Istio services that live in a Kubernetes cluster.
        """
        return pulumi.get(self, "cluster_istio")

    @cluster_istio.setter
    def cluster_istio(self, value: Optional[pulumi.Input['ClusterIstioArgs']]):
        pulumi.set(self, "cluster_istio", value)

    @property
    @pulumi.getter
    def custom(self) -> Optional[pulumi.Input['CustomArgs']]:
        """
        Custom service type.
        """
        return pulumi.get(self, "custom")

    @custom.setter
    def custom(self, value: Optional[pulumi.Input['CustomArgs']]):
        pulumi.set(self, "custom", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name used for UI elements listing this Service.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="istioCanonicalService")
    def istio_canonical_service(self) -> Optional[pulumi.Input['IstioCanonicalServiceArgs']]:
        """
        Type used for canonical services scoped to an Istio mesh. Metrics for Istio are documented here (https://istio.io/latest/docs/reference/config/metrics/)
        """
        return pulumi.get(self, "istio_canonical_service")

    @istio_canonical_service.setter
    def istio_canonical_service(self, value: Optional[pulumi.Input['IstioCanonicalServiceArgs']]):
        pulumi.set(self, "istio_canonical_service", value)

    @property
    @pulumi.getter(name="meshIstio")
    def mesh_istio(self) -> Optional[pulumi.Input['MeshIstioArgs']]:
        """
        Type used for Istio services scoped to an Istio mesh.
        """
        return pulumi.get(self, "mesh_istio")

    @mesh_istio.setter
    def mesh_istio(self, value: Optional[pulumi.Input['MeshIstioArgs']]):
        pulumi.set(self, "mesh_istio", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Resource name for this Service. The format is: projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID] 
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "service_id")

    @service_id.setter
    def service_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_id", value)

    @property
    @pulumi.getter
    def telemetry(self) -> Optional[pulumi.Input['TelemetryArgs']]:
        """
        Configuration for how to query telemetry on a Service.
        """
        return pulumi.get(self, "telemetry")

    @telemetry.setter
    def telemetry(self, value: Optional[pulumi.Input['TelemetryArgs']]):
        pulumi.set(self, "telemetry", value)


class Service(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_engine: Optional[pulumi.Input[pulumi.InputType['AppEngineArgs']]] = None,
                 cloud_endpoints: Optional[pulumi.Input[pulumi.InputType['CloudEndpointsArgs']]] = None,
                 cluster_istio: Optional[pulumi.Input[pulumi.InputType['ClusterIstioArgs']]] = None,
                 custom: Optional[pulumi.Input[pulumi.InputType['CustomArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 istio_canonical_service: Optional[pulumi.Input[pulumi.InputType['IstioCanonicalServiceArgs']]] = None,
                 mesh_istio: Optional[pulumi.Input[pulumi.InputType['MeshIstioArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 service_id: Optional[pulumi.Input[str]] = None,
                 services_id: Optional[pulumi.Input[str]] = None,
                 telemetry: Optional[pulumi.Input[pulumi.InputType['TelemetryArgs']]] = None,
                 v3_id: Optional[pulumi.Input[str]] = None,
                 v3_id1: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Service.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AppEngineArgs']] app_engine: Type used for App Engine services.
        :param pulumi.Input[pulumi.InputType['CloudEndpointsArgs']] cloud_endpoints: Type used for Cloud Endpoints services.
        :param pulumi.Input[pulumi.InputType['ClusterIstioArgs']] cluster_istio: Type used for Istio services that live in a Kubernetes cluster.
        :param pulumi.Input[pulumi.InputType['CustomArgs']] custom: Custom service type.
        :param pulumi.Input[str] display_name: Name used for UI elements listing this Service.
        :param pulumi.Input[pulumi.InputType['IstioCanonicalServiceArgs']] istio_canonical_service: Type used for canonical services scoped to an Istio mesh. Metrics for Istio are documented here (https://istio.io/latest/docs/reference/config/metrics/)
        :param pulumi.Input[pulumi.InputType['MeshIstioArgs']] mesh_istio: Type used for Istio services scoped to an Istio mesh.
        :param pulumi.Input[str] name: Resource name for this Service. The format is: projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID] 
        :param pulumi.Input[pulumi.InputType['TelemetryArgs']] telemetry: Configuration for how to query telemetry on a Service.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServiceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Service.

        :param str resource_name: The name of the resource.
        :param ServiceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_engine: Optional[pulumi.Input[pulumi.InputType['AppEngineArgs']]] = None,
                 cloud_endpoints: Optional[pulumi.Input[pulumi.InputType['CloudEndpointsArgs']]] = None,
                 cluster_istio: Optional[pulumi.Input[pulumi.InputType['ClusterIstioArgs']]] = None,
                 custom: Optional[pulumi.Input[pulumi.InputType['CustomArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 istio_canonical_service: Optional[pulumi.Input[pulumi.InputType['IstioCanonicalServiceArgs']]] = None,
                 mesh_istio: Optional[pulumi.Input[pulumi.InputType['MeshIstioArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 service_id: Optional[pulumi.Input[str]] = None,
                 services_id: Optional[pulumi.Input[str]] = None,
                 telemetry: Optional[pulumi.Input[pulumi.InputType['TelemetryArgs']]] = None,
                 v3_id: Optional[pulumi.Input[str]] = None,
                 v3_id1: Optional[pulumi.Input[str]] = None,
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
            __props__ = ServiceArgs.__new__(ServiceArgs)

            __props__.__dict__["app_engine"] = app_engine
            __props__.__dict__["cloud_endpoints"] = cloud_endpoints
            __props__.__dict__["cluster_istio"] = cluster_istio
            __props__.__dict__["custom"] = custom
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["istio_canonical_service"] = istio_canonical_service
            __props__.__dict__["mesh_istio"] = mesh_istio
            __props__.__dict__["name"] = name
            __props__.__dict__["service_id"] = service_id
            if services_id is None and not opts.urn:
                raise TypeError("Missing required property 'services_id'")
            __props__.__dict__["services_id"] = services_id
            __props__.__dict__["telemetry"] = telemetry
            if v3_id is None and not opts.urn:
                raise TypeError("Missing required property 'v3_id'")
            __props__.__dict__["v3_id"] = v3_id
            if v3_id1 is None and not opts.urn:
                raise TypeError("Missing required property 'v3_id1'")
            __props__.__dict__["v3_id1"] = v3_id1
        super(Service, __self__).__init__(
            'google-native:monitoring/v3:Service',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Service':
        """
        Get an existing Service resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServiceArgs.__new__(ServiceArgs)

        __props__.__dict__["app_engine"] = None
        __props__.__dict__["cloud_endpoints"] = None
        __props__.__dict__["cluster_istio"] = None
        __props__.__dict__["custom"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["istio_canonical_service"] = None
        __props__.__dict__["mesh_istio"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["telemetry"] = None
        return Service(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appEngine")
    def app_engine(self) -> pulumi.Output['outputs.AppEngineResponse']:
        """
        Type used for App Engine services.
        """
        return pulumi.get(self, "app_engine")

    @property
    @pulumi.getter(name="cloudEndpoints")
    def cloud_endpoints(self) -> pulumi.Output['outputs.CloudEndpointsResponse']:
        """
        Type used for Cloud Endpoints services.
        """
        return pulumi.get(self, "cloud_endpoints")

    @property
    @pulumi.getter(name="clusterIstio")
    def cluster_istio(self) -> pulumi.Output['outputs.ClusterIstioResponse']:
        """
        Type used for Istio services that live in a Kubernetes cluster.
        """
        return pulumi.get(self, "cluster_istio")

    @property
    @pulumi.getter
    def custom(self) -> pulumi.Output['outputs.CustomResponse']:
        """
        Custom service type.
        """
        return pulumi.get(self, "custom")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Name used for UI elements listing this Service.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="istioCanonicalService")
    def istio_canonical_service(self) -> pulumi.Output['outputs.IstioCanonicalServiceResponse']:
        """
        Type used for canonical services scoped to an Istio mesh. Metrics for Istio are documented here (https://istio.io/latest/docs/reference/config/metrics/)
        """
        return pulumi.get(self, "istio_canonical_service")

    @property
    @pulumi.getter(name="meshIstio")
    def mesh_istio(self) -> pulumi.Output['outputs.MeshIstioResponse']:
        """
        Type used for Istio services scoped to an Istio mesh.
        """
        return pulumi.get(self, "mesh_istio")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name for this Service. The format is: projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID] 
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def telemetry(self) -> pulumi.Output['outputs.TelemetryResponse']:
        """
        Configuration for how to query telemetry on a Service.
        """
        return pulumi.get(self, "telemetry")

