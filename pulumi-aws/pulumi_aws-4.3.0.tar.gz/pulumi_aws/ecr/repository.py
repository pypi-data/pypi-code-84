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

__all__ = ['RepositoryArgs', 'Repository']

@pulumi.input_type
class RepositoryArgs:
    def __init__(__self__, *,
                 encryption_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['RepositoryEncryptionConfigurationArgs']]]] = None,
                 image_scanning_configuration: Optional[pulumi.Input['RepositoryImageScanningConfigurationArgs']] = None,
                 image_tag_mutability: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Repository resource.
        :param pulumi.Input[Sequence[pulumi.Input['RepositoryEncryptionConfigurationArgs']]] encryption_configurations: Encryption configuration for the repository. See below for schema.
        :param pulumi.Input['RepositoryImageScanningConfigurationArgs'] image_scanning_configuration: Configuration block that defines image scanning configuration for the repository. By default, image scanning must be manually triggered. See the [ECR User Guide](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html) for more information about image scanning.
        :param pulumi.Input[str] image_tag_mutability: The tag mutability setting for the repository. Must be one of: `MUTABLE` or `IMMUTABLE`. Defaults to `MUTABLE`.
        :param pulumi.Input[str] name: Name of the repository.
        """
        if encryption_configurations is not None:
            pulumi.set(__self__, "encryption_configurations", encryption_configurations)
        if image_scanning_configuration is not None:
            pulumi.set(__self__, "image_scanning_configuration", image_scanning_configuration)
        if image_tag_mutability is not None:
            pulumi.set(__self__, "image_tag_mutability", image_tag_mutability)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter(name="encryptionConfigurations")
    def encryption_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RepositoryEncryptionConfigurationArgs']]]]:
        """
        Encryption configuration for the repository. See below for schema.
        """
        return pulumi.get(self, "encryption_configurations")

    @encryption_configurations.setter
    def encryption_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RepositoryEncryptionConfigurationArgs']]]]):
        pulumi.set(self, "encryption_configurations", value)

    @property
    @pulumi.getter(name="imageScanningConfiguration")
    def image_scanning_configuration(self) -> Optional[pulumi.Input['RepositoryImageScanningConfigurationArgs']]:
        """
        Configuration block that defines image scanning configuration for the repository. By default, image scanning must be manually triggered. See the [ECR User Guide](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html) for more information about image scanning.
        """
        return pulumi.get(self, "image_scanning_configuration")

    @image_scanning_configuration.setter
    def image_scanning_configuration(self, value: Optional[pulumi.Input['RepositoryImageScanningConfigurationArgs']]):
        pulumi.set(self, "image_scanning_configuration", value)

    @property
    @pulumi.getter(name="imageTagMutability")
    def image_tag_mutability(self) -> Optional[pulumi.Input[str]]:
        """
        The tag mutability setting for the repository. Must be one of: `MUTABLE` or `IMMUTABLE`. Defaults to `MUTABLE`.
        """
        return pulumi.get(self, "image_tag_mutability")

    @image_tag_mutability.setter
    def image_tag_mutability(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image_tag_mutability", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the repository.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)


@pulumi.input_type
class _RepositoryState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 encryption_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['RepositoryEncryptionConfigurationArgs']]]] = None,
                 image_scanning_configuration: Optional[pulumi.Input['RepositoryImageScanningConfigurationArgs']] = None,
                 image_tag_mutability: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 registry_id: Optional[pulumi.Input[str]] = None,
                 repository_url: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Repository resources.
        :param pulumi.Input[str] arn: Full ARN of the repository.
        :param pulumi.Input[Sequence[pulumi.Input['RepositoryEncryptionConfigurationArgs']]] encryption_configurations: Encryption configuration for the repository. See below for schema.
        :param pulumi.Input['RepositoryImageScanningConfigurationArgs'] image_scanning_configuration: Configuration block that defines image scanning configuration for the repository. By default, image scanning must be manually triggered. See the [ECR User Guide](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html) for more information about image scanning.
        :param pulumi.Input[str] image_tag_mutability: The tag mutability setting for the repository. Must be one of: `MUTABLE` or `IMMUTABLE`. Defaults to `MUTABLE`.
        :param pulumi.Input[str] name: Name of the repository.
        :param pulumi.Input[str] registry_id: The registry ID where the repository was created.
        :param pulumi.Input[str] repository_url: The URL of the repository (in the form `aws_account_id.dkr.ecr.region.amazonaws.com/repositoryName`).
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if encryption_configurations is not None:
            pulumi.set(__self__, "encryption_configurations", encryption_configurations)
        if image_scanning_configuration is not None:
            pulumi.set(__self__, "image_scanning_configuration", image_scanning_configuration)
        if image_tag_mutability is not None:
            pulumi.set(__self__, "image_tag_mutability", image_tag_mutability)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if registry_id is not None:
            pulumi.set(__self__, "registry_id", registry_id)
        if repository_url is not None:
            pulumi.set(__self__, "repository_url", repository_url)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        Full ARN of the repository.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="encryptionConfigurations")
    def encryption_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RepositoryEncryptionConfigurationArgs']]]]:
        """
        Encryption configuration for the repository. See below for schema.
        """
        return pulumi.get(self, "encryption_configurations")

    @encryption_configurations.setter
    def encryption_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RepositoryEncryptionConfigurationArgs']]]]):
        pulumi.set(self, "encryption_configurations", value)

    @property
    @pulumi.getter(name="imageScanningConfiguration")
    def image_scanning_configuration(self) -> Optional[pulumi.Input['RepositoryImageScanningConfigurationArgs']]:
        """
        Configuration block that defines image scanning configuration for the repository. By default, image scanning must be manually triggered. See the [ECR User Guide](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html) for more information about image scanning.
        """
        return pulumi.get(self, "image_scanning_configuration")

    @image_scanning_configuration.setter
    def image_scanning_configuration(self, value: Optional[pulumi.Input['RepositoryImageScanningConfigurationArgs']]):
        pulumi.set(self, "image_scanning_configuration", value)

    @property
    @pulumi.getter(name="imageTagMutability")
    def image_tag_mutability(self) -> Optional[pulumi.Input[str]]:
        """
        The tag mutability setting for the repository. Must be one of: `MUTABLE` or `IMMUTABLE`. Defaults to `MUTABLE`.
        """
        return pulumi.get(self, "image_tag_mutability")

    @image_tag_mutability.setter
    def image_tag_mutability(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image_tag_mutability", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the repository.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> Optional[pulumi.Input[str]]:
        """
        The registry ID where the repository was created.
        """
        return pulumi.get(self, "registry_id")

    @registry_id.setter
    def registry_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "registry_id", value)

    @property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL of the repository (in the form `aws_account_id.dkr.ecr.region.amazonaws.com/repositoryName`).
        """
        return pulumi.get(self, "repository_url")

    @repository_url.setter
    def repository_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repository_url", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)


class Repository(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 encryption_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RepositoryEncryptionConfigurationArgs']]]]] = None,
                 image_scanning_configuration: Optional[pulumi.Input[pulumi.InputType['RepositoryImageScanningConfigurationArgs']]] = None,
                 image_tag_mutability: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides an Elastic Container Registry Repository.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        foo = aws.ecr.Repository("foo",
            image_scanning_configuration=aws.ecr.RepositoryImageScanningConfigurationArgs(
                scan_on_push=True,
            ),
            image_tag_mutability="MUTABLE")
        ```

        ## Import

        ECR Repositories can be imported using the `name`, e.g.

        ```sh
         $ pulumi import aws:ecr/repository:Repository service test-service
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RepositoryEncryptionConfigurationArgs']]]] encryption_configurations: Encryption configuration for the repository. See below for schema.
        :param pulumi.Input[pulumi.InputType['RepositoryImageScanningConfigurationArgs']] image_scanning_configuration: Configuration block that defines image scanning configuration for the repository. By default, image scanning must be manually triggered. See the [ECR User Guide](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html) for more information about image scanning.
        :param pulumi.Input[str] image_tag_mutability: The tag mutability setting for the repository. Must be one of: `MUTABLE` or `IMMUTABLE`. Defaults to `MUTABLE`.
        :param pulumi.Input[str] name: Name of the repository.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[RepositoryArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an Elastic Container Registry Repository.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        foo = aws.ecr.Repository("foo",
            image_scanning_configuration=aws.ecr.RepositoryImageScanningConfigurationArgs(
                scan_on_push=True,
            ),
            image_tag_mutability="MUTABLE")
        ```

        ## Import

        ECR Repositories can be imported using the `name`, e.g.

        ```sh
         $ pulumi import aws:ecr/repository:Repository service test-service
        ```

        :param str resource_name: The name of the resource.
        :param RepositoryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RepositoryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 encryption_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RepositoryEncryptionConfigurationArgs']]]]] = None,
                 image_scanning_configuration: Optional[pulumi.Input[pulumi.InputType['RepositoryImageScanningConfigurationArgs']]] = None,
                 image_tag_mutability: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = RepositoryArgs.__new__(RepositoryArgs)

            __props__.__dict__["encryption_configurations"] = encryption_configurations
            __props__.__dict__["image_scanning_configuration"] = image_scanning_configuration
            __props__.__dict__["image_tag_mutability"] = image_tag_mutability
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tags_all"] = tags_all
            __props__.__dict__["arn"] = None
            __props__.__dict__["registry_id"] = None
            __props__.__dict__["repository_url"] = None
        super(Repository, __self__).__init__(
            'aws:ecr/repository:Repository',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            encryption_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RepositoryEncryptionConfigurationArgs']]]]] = None,
            image_scanning_configuration: Optional[pulumi.Input[pulumi.InputType['RepositoryImageScanningConfigurationArgs']]] = None,
            image_tag_mutability: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            registry_id: Optional[pulumi.Input[str]] = None,
            repository_url: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Repository':
        """
        Get an existing Repository resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Full ARN of the repository.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RepositoryEncryptionConfigurationArgs']]]] encryption_configurations: Encryption configuration for the repository. See below for schema.
        :param pulumi.Input[pulumi.InputType['RepositoryImageScanningConfigurationArgs']] image_scanning_configuration: Configuration block that defines image scanning configuration for the repository. By default, image scanning must be manually triggered. See the [ECR User Guide](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html) for more information about image scanning.
        :param pulumi.Input[str] image_tag_mutability: The tag mutability setting for the repository. Must be one of: `MUTABLE` or `IMMUTABLE`. Defaults to `MUTABLE`.
        :param pulumi.Input[str] name: Name of the repository.
        :param pulumi.Input[str] registry_id: The registry ID where the repository was created.
        :param pulumi.Input[str] repository_url: The URL of the repository (in the form `aws_account_id.dkr.ecr.region.amazonaws.com/repositoryName`).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RepositoryState.__new__(_RepositoryState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["encryption_configurations"] = encryption_configurations
        __props__.__dict__["image_scanning_configuration"] = image_scanning_configuration
        __props__.__dict__["image_tag_mutability"] = image_tag_mutability
        __props__.__dict__["name"] = name
        __props__.__dict__["registry_id"] = registry_id
        __props__.__dict__["repository_url"] = repository_url
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        return Repository(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Full ARN of the repository.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="encryptionConfigurations")
    def encryption_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.RepositoryEncryptionConfiguration']]]:
        """
        Encryption configuration for the repository. See below for schema.
        """
        return pulumi.get(self, "encryption_configurations")

    @property
    @pulumi.getter(name="imageScanningConfiguration")
    def image_scanning_configuration(self) -> pulumi.Output[Optional['outputs.RepositoryImageScanningConfiguration']]:
        """
        Configuration block that defines image scanning configuration for the repository. By default, image scanning must be manually triggered. See the [ECR User Guide](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html) for more information about image scanning.
        """
        return pulumi.get(self, "image_scanning_configuration")

    @property
    @pulumi.getter(name="imageTagMutability")
    def image_tag_mutability(self) -> pulumi.Output[Optional[str]]:
        """
        The tag mutability setting for the repository. Must be one of: `MUTABLE` or `IMMUTABLE`. Defaults to `MUTABLE`.
        """
        return pulumi.get(self, "image_tag_mutability")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the repository.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> pulumi.Output[str]:
        """
        The registry ID where the repository was created.
        """
        return pulumi.get(self, "registry_id")

    @property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> pulumi.Output[str]:
        """
        The URL of the repository (in the form `aws_account_id.dkr.ecr.region.amazonaws.com/repositoryName`).
        """
        return pulumi.get(self, "repository_url")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        return pulumi.get(self, "tags_all")

