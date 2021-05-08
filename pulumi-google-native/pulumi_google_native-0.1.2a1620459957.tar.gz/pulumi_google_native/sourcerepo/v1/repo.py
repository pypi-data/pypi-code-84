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

__all__ = ['RepoArgs', 'Repo']

@pulumi.input_type
class RepoArgs:
    def __init__(__self__, *,
                 projects_id: pulumi.Input[str],
                 repos_id: pulumi.Input[str],
                 mirror_config: Optional[pulumi.Input['MirrorConfigArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pubsub_configs: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Repo resource.
        :param pulumi.Input['MirrorConfigArgs'] mirror_config: How this repository mirrors a repository managed by another service. Read-only field.
        :param pulumi.Input[str] name: Resource name of the repository, of the form `projects//repos/`. The repo name may contain slashes. eg, `projects/myproject/repos/name/with/slash`
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] pubsub_configs: How this repository publishes a change in the repository through Cloud Pub/Sub. Keyed by the topic names.
        :param pulumi.Input[str] size: The disk usage of the repo, in bytes. Read-only field. Size is only returned by GetRepo.
        :param pulumi.Input[str] url: URL to clone the repository from Google Cloud Source Repositories. Read-only field.
        """
        pulumi.set(__self__, "projects_id", projects_id)
        pulumi.set(__self__, "repos_id", repos_id)
        if mirror_config is not None:
            pulumi.set(__self__, "mirror_config", mirror_config)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if pubsub_configs is not None:
            pulumi.set(__self__, "pubsub_configs", pubsub_configs)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter(name="projectsId")
    def projects_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "projects_id")

    @projects_id.setter
    def projects_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "projects_id", value)

    @property
    @pulumi.getter(name="reposId")
    def repos_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "repos_id")

    @repos_id.setter
    def repos_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "repos_id", value)

    @property
    @pulumi.getter(name="mirrorConfig")
    def mirror_config(self) -> Optional[pulumi.Input['MirrorConfigArgs']]:
        """
        How this repository mirrors a repository managed by another service. Read-only field.
        """
        return pulumi.get(self, "mirror_config")

    @mirror_config.setter
    def mirror_config(self, value: Optional[pulumi.Input['MirrorConfigArgs']]):
        pulumi.set(self, "mirror_config", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Resource name of the repository, of the form `projects//repos/`. The repo name may contain slashes. eg, `projects/myproject/repos/name/with/slash`
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="pubsubConfigs")
    def pubsub_configs(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        How this repository publishes a change in the repository through Cloud Pub/Sub. Keyed by the topic names.
        """
        return pulumi.get(self, "pubsub_configs")

    @pubsub_configs.setter
    def pubsub_configs(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "pubsub_configs", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[str]]:
        """
        The disk usage of the repo, in bytes. Read-only field. Size is only returned by GetRepo.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        URL to clone the repository from Google Cloud Source Repositories. Read-only field.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class Repo(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 mirror_config: Optional[pulumi.Input[pulumi.InputType['MirrorConfigArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 pubsub_configs: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 repos_id: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a repo in the given project with the given name. If the named repository already exists, `CreateRepo` returns `ALREADY_EXISTS`.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['MirrorConfigArgs']] mirror_config: How this repository mirrors a repository managed by another service. Read-only field.
        :param pulumi.Input[str] name: Resource name of the repository, of the form `projects//repos/`. The repo name may contain slashes. eg, `projects/myproject/repos/name/with/slash`
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] pubsub_configs: How this repository publishes a change in the repository through Cloud Pub/Sub. Keyed by the topic names.
        :param pulumi.Input[str] size: The disk usage of the repo, in bytes. Read-only field. Size is only returned by GetRepo.
        :param pulumi.Input[str] url: URL to clone the repository from Google Cloud Source Repositories. Read-only field.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RepoArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a repo in the given project with the given name. If the named repository already exists, `CreateRepo` returns `ALREADY_EXISTS`.

        :param str resource_name: The name of the resource.
        :param RepoArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RepoArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 mirror_config: Optional[pulumi.Input[pulumi.InputType['MirrorConfigArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 pubsub_configs: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 repos_id: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
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
            __props__ = RepoArgs.__new__(RepoArgs)

            __props__.__dict__["mirror_config"] = mirror_config
            __props__.__dict__["name"] = name
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__.__dict__["projects_id"] = projects_id
            __props__.__dict__["pubsub_configs"] = pubsub_configs
            if repos_id is None and not opts.urn:
                raise TypeError("Missing required property 'repos_id'")
            __props__.__dict__["repos_id"] = repos_id
            __props__.__dict__["size"] = size
            __props__.__dict__["url"] = url
        super(Repo, __self__).__init__(
            'google-native:sourcerepo/v1:Repo',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Repo':
        """
        Get an existing Repo resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RepoArgs.__new__(RepoArgs)

        __props__.__dict__["mirror_config"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["pubsub_configs"] = None
        __props__.__dict__["size"] = None
        __props__.__dict__["url"] = None
        return Repo(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="mirrorConfig")
    def mirror_config(self) -> pulumi.Output['outputs.MirrorConfigResponse']:
        """
        How this repository mirrors a repository managed by another service. Read-only field.
        """
        return pulumi.get(self, "mirror_config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name of the repository, of the form `projects//repos/`. The repo name may contain slashes. eg, `projects/myproject/repos/name/with/slash`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pubsubConfigs")
    def pubsub_configs(self) -> pulumi.Output[Mapping[str, str]]:
        """
        How this repository publishes a change in the repository through Cloud Pub/Sub. Keyed by the topic names.
        """
        return pulumi.get(self, "pubsub_configs")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[str]:
        """
        The disk usage of the repo, in bytes. Read-only field. Size is only returned by GetRepo.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        URL to clone the repository from Google Cloud Source Repositories. Read-only field.
        """
        return pulumi.get(self, "url")

