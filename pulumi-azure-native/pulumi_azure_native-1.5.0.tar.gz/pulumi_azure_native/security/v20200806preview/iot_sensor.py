# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = ['IotSensorArgs', 'IotSensor']

@pulumi.input_type
class IotSensorArgs:
    def __init__(__self__, *,
                 scope: pulumi.Input[str],
                 iot_sensor_name: Optional[pulumi.Input[str]] = None,
                 sensor_type: Optional[pulumi.Input[Union[str, 'SensorType']]] = None,
                 ti_automatic_updates: Optional[pulumi.Input[bool]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IotSensor resource.
        :param pulumi.Input[str] scope: Scope of the query (IoT Hub, /providers/Microsoft.Devices/iotHubs/myHub)
        :param pulumi.Input[str] iot_sensor_name: Name of the IoT sensor
        :param pulumi.Input[Union[str, 'SensorType']] sensor_type: Type of sensor
        :param pulumi.Input[bool] ti_automatic_updates: TI Automatic mode status of the IoT sensor
        :param pulumi.Input[str] zone: Zone of the IoT sensor
        """
        pulumi.set(__self__, "scope", scope)
        if iot_sensor_name is not None:
            pulumi.set(__self__, "iot_sensor_name", iot_sensor_name)
        if sensor_type is not None:
            pulumi.set(__self__, "sensor_type", sensor_type)
        if ti_automatic_updates is not None:
            pulumi.set(__self__, "ti_automatic_updates", ti_automatic_updates)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input[str]:
        """
        Scope of the query (IoT Hub, /providers/Microsoft.Devices/iotHubs/myHub)
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter(name="iotSensorName")
    def iot_sensor_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the IoT sensor
        """
        return pulumi.get(self, "iot_sensor_name")

    @iot_sensor_name.setter
    def iot_sensor_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "iot_sensor_name", value)

    @property
    @pulumi.getter(name="sensorType")
    def sensor_type(self) -> Optional[pulumi.Input[Union[str, 'SensorType']]]:
        """
        Type of sensor
        """
        return pulumi.get(self, "sensor_type")

    @sensor_type.setter
    def sensor_type(self, value: Optional[pulumi.Input[Union[str, 'SensorType']]]):
        pulumi.set(self, "sensor_type", value)

    @property
    @pulumi.getter(name="tiAutomaticUpdates")
    def ti_automatic_updates(self) -> Optional[pulumi.Input[bool]]:
        """
        TI Automatic mode status of the IoT sensor
        """
        return pulumi.get(self, "ti_automatic_updates")

    @ti_automatic_updates.setter
    def ti_automatic_updates(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ti_automatic_updates", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        Zone of the IoT sensor
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


class IotSensor(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 iot_sensor_name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 sensor_type: Optional[pulumi.Input[Union[str, 'SensorType']]] = None,
                 ti_automatic_updates: Optional[pulumi.Input[bool]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        IoT sensor model

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] iot_sensor_name: Name of the IoT sensor
        :param pulumi.Input[str] scope: Scope of the query (IoT Hub, /providers/Microsoft.Devices/iotHubs/myHub)
        :param pulumi.Input[Union[str, 'SensorType']] sensor_type: Type of sensor
        :param pulumi.Input[bool] ti_automatic_updates: TI Automatic mode status of the IoT sensor
        :param pulumi.Input[str] zone: Zone of the IoT sensor
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IotSensorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        IoT sensor model

        :param str resource_name: The name of the resource.
        :param IotSensorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IotSensorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 iot_sensor_name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 sensor_type: Optional[pulumi.Input[Union[str, 'SensorType']]] = None,
                 ti_automatic_updates: Optional[pulumi.Input[bool]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
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
            __props__ = IotSensorArgs.__new__(IotSensorArgs)

            __props__.__dict__["iot_sensor_name"] = iot_sensor_name
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
            __props__.__dict__["sensor_type"] = sensor_type
            __props__.__dict__["ti_automatic_updates"] = ti_automatic_updates
            __props__.__dict__["zone"] = zone
            __props__.__dict__["connectivity_time"] = None
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["dynamic_learning"] = None
            __props__.__dict__["learning_mode"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["sensor_status"] = None
            __props__.__dict__["sensor_version"] = None
            __props__.__dict__["ti_status"] = None
            __props__.__dict__["ti_version"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:security/v20200806preview:IotSensor"), pulumi.Alias(type_="azure-native:security:IotSensor"), pulumi.Alias(type_="azure-nextgen:security:IotSensor")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(IotSensor, __self__).__init__(
            'azure-native:security/v20200806preview:IotSensor',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IotSensor':
        """
        Get an existing IotSensor resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IotSensorArgs.__new__(IotSensorArgs)

        __props__.__dict__["connectivity_time"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["dynamic_learning"] = None
        __props__.__dict__["learning_mode"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["sensor_status"] = None
        __props__.__dict__["sensor_type"] = None
        __props__.__dict__["sensor_version"] = None
        __props__.__dict__["ti_automatic_updates"] = None
        __props__.__dict__["ti_status"] = None
        __props__.__dict__["ti_version"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["zone"] = None
        return IotSensor(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="connectivityTime")
    def connectivity_time(self) -> pulumi.Output[str]:
        """
        Last connectivity time of the IoT sensor
        """
        return pulumi.get(self, "connectivity_time")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        Creation time of the IoT sensor
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="dynamicLearning")
    def dynamic_learning(self) -> pulumi.Output[bool]:
        """
        Dynamic mode status of the IoT sensor
        """
        return pulumi.get(self, "dynamic_learning")

    @property
    @pulumi.getter(name="learningMode")
    def learning_mode(self) -> pulumi.Output[bool]:
        """
        Learning mode status of the IoT sensor
        """
        return pulumi.get(self, "learning_mode")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sensorStatus")
    def sensor_status(self) -> pulumi.Output[str]:
        """
        Status of the IoT sensor
        """
        return pulumi.get(self, "sensor_status")

    @property
    @pulumi.getter(name="sensorType")
    def sensor_type(self) -> pulumi.Output[Optional[str]]:
        """
        Type of sensor
        """
        return pulumi.get(self, "sensor_type")

    @property
    @pulumi.getter(name="sensorVersion")
    def sensor_version(self) -> pulumi.Output[str]:
        """
        Version of the IoT sensor
        """
        return pulumi.get(self, "sensor_version")

    @property
    @pulumi.getter(name="tiAutomaticUpdates")
    def ti_automatic_updates(self) -> pulumi.Output[Optional[bool]]:
        """
        TI Automatic mode status of the IoT sensor
        """
        return pulumi.get(self, "ti_automatic_updates")

    @property
    @pulumi.getter(name="tiStatus")
    def ti_status(self) -> pulumi.Output[str]:
        """
        TI Status of the IoT sensor
        """
        return pulumi.get(self, "ti_status")

    @property
    @pulumi.getter(name="tiVersion")
    def ti_version(self) -> pulumi.Output[str]:
        """
        TI Version of the IoT sensor
        """
        return pulumi.get(self, "ti_version")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[Optional[str]]:
        """
        Zone of the IoT sensor
        """
        return pulumi.get(self, "zone")

