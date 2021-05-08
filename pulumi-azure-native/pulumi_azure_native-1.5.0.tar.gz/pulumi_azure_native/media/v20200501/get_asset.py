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
    'GetAssetResult',
    'AwaitableGetAssetResult',
    'get_asset',
]

@pulumi.output_type
class GetAssetResult:
    """
    An Asset.
    """
    def __init__(__self__, alternate_id=None, asset_id=None, container=None, created=None, description=None, id=None, last_modified=None, name=None, storage_account_name=None, storage_encryption_format=None, system_data=None, type=None):
        if alternate_id and not isinstance(alternate_id, str):
            raise TypeError("Expected argument 'alternate_id' to be a str")
        pulumi.set(__self__, "alternate_id", alternate_id)
        if asset_id and not isinstance(asset_id, str):
            raise TypeError("Expected argument 'asset_id' to be a str")
        pulumi.set(__self__, "asset_id", asset_id)
        if container and not isinstance(container, str):
            raise TypeError("Expected argument 'container' to be a str")
        pulumi.set(__self__, "container", container)
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_modified and not isinstance(last_modified, str):
            raise TypeError("Expected argument 'last_modified' to be a str")
        pulumi.set(__self__, "last_modified", last_modified)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if storage_account_name and not isinstance(storage_account_name, str):
            raise TypeError("Expected argument 'storage_account_name' to be a str")
        pulumi.set(__self__, "storage_account_name", storage_account_name)
        if storage_encryption_format and not isinstance(storage_encryption_format, str):
            raise TypeError("Expected argument 'storage_encryption_format' to be a str")
        pulumi.set(__self__, "storage_encryption_format", storage_encryption_format)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="alternateId")
    def alternate_id(self) -> Optional[str]:
        """
        The alternate ID of the Asset.
        """
        return pulumi.get(self, "alternate_id")

    @property
    @pulumi.getter(name="assetId")
    def asset_id(self) -> str:
        """
        The Asset ID.
        """
        return pulumi.get(self, "asset_id")

    @property
    @pulumi.getter
    def container(self) -> Optional[str]:
        """
        The name of the asset blob container.
        """
        return pulumi.get(self, "container")

    @property
    @pulumi.getter
    def created(self) -> str:
        """
        The creation date of the Asset.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The Asset description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> str:
        """
        The last modified date of the Asset.
        """
        return pulumi.get(self, "last_modified")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> Optional[str]:
        """
        The name of the storage account.
        """
        return pulumi.get(self, "storage_account_name")

    @property
    @pulumi.getter(name="storageEncryptionFormat")
    def storage_encryption_format(self) -> str:
        """
        The Asset encryption format. One of None or MediaStorageEncryption.
        """
        return pulumi.get(self, "storage_encryption_format")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetAssetResult(GetAssetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAssetResult(
            alternate_id=self.alternate_id,
            asset_id=self.asset_id,
            container=self.container,
            created=self.created,
            description=self.description,
            id=self.id,
            last_modified=self.last_modified,
            name=self.name,
            storage_account_name=self.storage_account_name,
            storage_encryption_format=self.storage_encryption_format,
            system_data=self.system_data,
            type=self.type)


def get_asset(account_name: Optional[str] = None,
              asset_name: Optional[str] = None,
              resource_group_name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAssetResult:
    """
    An Asset.


    :param str account_name: The Media Services account name.
    :param str asset_name: The Asset name.
    :param str resource_group_name: The name of the resource group within the Azure subscription.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['assetName'] = asset_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:media/v20200501:getAsset', __args__, opts=opts, typ=GetAssetResult).value

    return AwaitableGetAssetResult(
        alternate_id=__ret__.alternate_id,
        asset_id=__ret__.asset_id,
        container=__ret__.container,
        created=__ret__.created,
        description=__ret__.description,
        id=__ret__.id,
        last_modified=__ret__.last_modified,
        name=__ret__.name,
        storage_account_name=__ret__.storage_account_name,
        storage_encryption_format=__ret__.storage_encryption_format,
        system_data=__ret__.system_data,
        type=__ret__.type)
