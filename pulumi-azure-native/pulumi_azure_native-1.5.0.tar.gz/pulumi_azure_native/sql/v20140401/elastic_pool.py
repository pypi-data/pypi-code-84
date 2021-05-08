# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = ['ElasticPoolArgs', 'ElasticPool']

@pulumi.input_type
class ElasticPoolArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 server_name: pulumi.Input[str],
                 database_dtu_max: Optional[pulumi.Input[int]] = None,
                 database_dtu_min: Optional[pulumi.Input[int]] = None,
                 dtu: Optional[pulumi.Input[int]] = None,
                 edition: Optional[pulumi.Input[Union[str, 'ElasticPoolEdition']]] = None,
                 elastic_pool_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 storage_mb: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zone_redundant: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a ElasticPool resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input[int] database_dtu_max: The maximum DTU any one database can consume.
        :param pulumi.Input[int] database_dtu_min: The minimum DTU all databases are guaranteed.
        :param pulumi.Input[int] dtu: The total shared DTU for the database elastic pool.
        :param pulumi.Input[Union[str, 'ElasticPoolEdition']] edition: The edition of the elastic pool.
        :param pulumi.Input[str] elastic_pool_name: The name of the elastic pool to be operated on (updated or created).
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[int] storage_mb: Gets storage limit for the database elastic pool in MB.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[bool] zone_redundant: Whether or not this database elastic pool is zone redundant, which means the replicas of this database will be spread across multiple availability zones.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "server_name", server_name)
        if database_dtu_max is not None:
            pulumi.set(__self__, "database_dtu_max", database_dtu_max)
        if database_dtu_min is not None:
            pulumi.set(__self__, "database_dtu_min", database_dtu_min)
        if dtu is not None:
            pulumi.set(__self__, "dtu", dtu)
        if edition is not None:
            pulumi.set(__self__, "edition", edition)
        if elastic_pool_name is not None:
            pulumi.set(__self__, "elastic_pool_name", elastic_pool_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if storage_mb is not None:
            pulumi.set(__self__, "storage_mb", storage_mb)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zone_redundant is not None:
            pulumi.set(__self__, "zone_redundant", zone_redundant)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[str]:
        """
        The name of the server.
        """
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter(name="databaseDtuMax")
    def database_dtu_max(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum DTU any one database can consume.
        """
        return pulumi.get(self, "database_dtu_max")

    @database_dtu_max.setter
    def database_dtu_max(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "database_dtu_max", value)

    @property
    @pulumi.getter(name="databaseDtuMin")
    def database_dtu_min(self) -> Optional[pulumi.Input[int]]:
        """
        The minimum DTU all databases are guaranteed.
        """
        return pulumi.get(self, "database_dtu_min")

    @database_dtu_min.setter
    def database_dtu_min(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "database_dtu_min", value)

    @property
    @pulumi.getter
    def dtu(self) -> Optional[pulumi.Input[int]]:
        """
        The total shared DTU for the database elastic pool.
        """
        return pulumi.get(self, "dtu")

    @dtu.setter
    def dtu(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "dtu", value)

    @property
    @pulumi.getter
    def edition(self) -> Optional[pulumi.Input[Union[str, 'ElasticPoolEdition']]]:
        """
        The edition of the elastic pool.
        """
        return pulumi.get(self, "edition")

    @edition.setter
    def edition(self, value: Optional[pulumi.Input[Union[str, 'ElasticPoolEdition']]]):
        pulumi.set(self, "edition", value)

    @property
    @pulumi.getter(name="elasticPoolName")
    def elastic_pool_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the elastic pool to be operated on (updated or created).
        """
        return pulumi.get(self, "elastic_pool_name")

    @elastic_pool_name.setter
    def elastic_pool_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "elastic_pool_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="storageMB")
    def storage_mb(self) -> Optional[pulumi.Input[int]]:
        """
        Gets storage limit for the database elastic pool in MB.
        """
        return pulumi.get(self, "storage_mb")

    @storage_mb.setter
    def storage_mb(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "storage_mb", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether or not this database elastic pool is zone redundant, which means the replicas of this database will be spread across multiple availability zones.
        """
        return pulumi.get(self, "zone_redundant")

    @zone_redundant.setter
    def zone_redundant(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "zone_redundant", value)


class ElasticPool(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_dtu_max: Optional[pulumi.Input[int]] = None,
                 database_dtu_min: Optional[pulumi.Input[int]] = None,
                 dtu: Optional[pulumi.Input[int]] = None,
                 edition: Optional[pulumi.Input[Union[str, 'ElasticPoolEdition']]] = None,
                 elastic_pool_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 storage_mb: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zone_redundant: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Represents a database elastic pool.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] database_dtu_max: The maximum DTU any one database can consume.
        :param pulumi.Input[int] database_dtu_min: The minimum DTU all databases are guaranteed.
        :param pulumi.Input[int] dtu: The total shared DTU for the database elastic pool.
        :param pulumi.Input[Union[str, 'ElasticPoolEdition']] edition: The edition of the elastic pool.
        :param pulumi.Input[str] elastic_pool_name: The name of the elastic pool to be operated on (updated or created).
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input[int] storage_mb: Gets storage limit for the database elastic pool in MB.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[bool] zone_redundant: Whether or not this database elastic pool is zone redundant, which means the replicas of this database will be spread across multiple availability zones.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ElasticPoolArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a database elastic pool.

        :param str resource_name: The name of the resource.
        :param ElasticPoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ElasticPoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_dtu_max: Optional[pulumi.Input[int]] = None,
                 database_dtu_min: Optional[pulumi.Input[int]] = None,
                 dtu: Optional[pulumi.Input[int]] = None,
                 edition: Optional[pulumi.Input[Union[str, 'ElasticPoolEdition']]] = None,
                 elastic_pool_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 storage_mb: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zone_redundant: Optional[pulumi.Input[bool]] = None,
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
            __props__ = ElasticPoolArgs.__new__(ElasticPoolArgs)

            __props__.__dict__["database_dtu_max"] = database_dtu_max
            __props__.__dict__["database_dtu_min"] = database_dtu_min
            __props__.__dict__["dtu"] = dtu
            __props__.__dict__["edition"] = edition
            __props__.__dict__["elastic_pool_name"] = elastic_pool_name
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if server_name is None and not opts.urn:
                raise TypeError("Missing required property 'server_name'")
            __props__.__dict__["server_name"] = server_name
            __props__.__dict__["storage_mb"] = storage_mb
            __props__.__dict__["tags"] = tags
            __props__.__dict__["zone_redundant"] = zone_redundant
            __props__.__dict__["creation_date"] = None
            __props__.__dict__["kind"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:sql/v20140401:ElasticPool"), pulumi.Alias(type_="azure-native:sql:ElasticPool"), pulumi.Alias(type_="azure-nextgen:sql:ElasticPool"), pulumi.Alias(type_="azure-native:sql/v20171001preview:ElasticPool"), pulumi.Alias(type_="azure-nextgen:sql/v20171001preview:ElasticPool"), pulumi.Alias(type_="azure-native:sql/v20200202preview:ElasticPool"), pulumi.Alias(type_="azure-nextgen:sql/v20200202preview:ElasticPool"), pulumi.Alias(type_="azure-native:sql/v20200801preview:ElasticPool"), pulumi.Alias(type_="azure-nextgen:sql/v20200801preview:ElasticPool"), pulumi.Alias(type_="azure-native:sql/v20201101preview:ElasticPool"), pulumi.Alias(type_="azure-nextgen:sql/v20201101preview:ElasticPool")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ElasticPool, __self__).__init__(
            'azure-native:sql/v20140401:ElasticPool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ElasticPool':
        """
        Get an existing ElasticPool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ElasticPoolArgs.__new__(ElasticPoolArgs)

        __props__.__dict__["creation_date"] = None
        __props__.__dict__["database_dtu_max"] = None
        __props__.__dict__["database_dtu_min"] = None
        __props__.__dict__["dtu"] = None
        __props__.__dict__["edition"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["storage_mb"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["zone_redundant"] = None
        return ElasticPool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[str]:
        """
        The creation date of the elastic pool (ISO8601 format).
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter(name="databaseDtuMax")
    def database_dtu_max(self) -> pulumi.Output[Optional[int]]:
        """
        The maximum DTU any one database can consume.
        """
        return pulumi.get(self, "database_dtu_max")

    @property
    @pulumi.getter(name="databaseDtuMin")
    def database_dtu_min(self) -> pulumi.Output[Optional[int]]:
        """
        The minimum DTU all databases are guaranteed.
        """
        return pulumi.get(self, "database_dtu_min")

    @property
    @pulumi.getter
    def dtu(self) -> pulumi.Output[Optional[int]]:
        """
        The total shared DTU for the database elastic pool.
        """
        return pulumi.get(self, "dtu")

    @property
    @pulumi.getter
    def edition(self) -> pulumi.Output[Optional[str]]:
        """
        The edition of the elastic pool.
        """
        return pulumi.get(self, "edition")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Kind of elastic pool.  This is metadata used for the Azure portal experience.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of the elastic pool.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="storageMB")
    def storage_mb(self) -> pulumi.Output[Optional[int]]:
        """
        Gets storage limit for the database elastic pool in MB.
        """
        return pulumi.get(self, "storage_mb")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether or not this database elastic pool is zone redundant, which means the replicas of this database will be spread across multiple availability zones.
        """
        return pulumi.get(self, "zone_redundant")

