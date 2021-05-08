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

__all__ = ['BucketAccessControlArgs', 'BucketAccessControl']

@pulumi.input_type
class BucketAccessControlArgs:
    def __init__(__self__, *,
                 bucket: pulumi.Input[str],
                 entity: pulumi.Input[str],
                 domain: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 entity_id: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 project_team: Optional[pulumi.Input['BucketAccessControlProjectTeamArgs']] = None,
                 provisional_user_project: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 user_project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a BucketAccessControl resource.
        :param pulumi.Input[str] bucket: The name of the bucket.
        :param pulumi.Input[str] entity: The entity holding the permission, in one of the following forms: 
               - user-userId 
               - user-email 
               - group-groupId 
               - group-email 
               - domain-domain 
               - project-team-projectId 
               - allUsers 
               - allAuthenticatedUsers Examples: 
               - The user liz@example.com would be user-liz@example.com. 
               - The group example@googlegroups.com would be group-example@googlegroups.com. 
               - To refer to all members of the Google Apps for Business domain example.com, the entity would be domain-example.com.
        :param pulumi.Input[str] domain: The domain associated with the entity, if any.
        :param pulumi.Input[str] email: The email address associated with the entity, if any.
        :param pulumi.Input[str] entity_id: The ID for the entity, if any.
        :param pulumi.Input[str] etag: HTTP 1.1 Entity tag for the access-control entry.
        :param pulumi.Input[str] id: The ID of the access-control entry.
        :param pulumi.Input[str] kind: The kind of item this is. For bucket access control entries, this is always storage#bucketAccessControl.
        :param pulumi.Input['BucketAccessControlProjectTeamArgs'] project_team: The project team associated with the entity, if any.
        :param pulumi.Input[str] role: The access permission for the entity.
        :param pulumi.Input[str] self_link: The link to this access-control entry.
        """
        pulumi.set(__self__, "bucket", bucket)
        pulumi.set(__self__, "entity", entity)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if email is not None:
            pulumi.set(__self__, "email", email)
        if entity_id is not None:
            pulumi.set(__self__, "entity_id", entity_id)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if project_team is not None:
            pulumi.set(__self__, "project_team", project_team)
        if provisional_user_project is not None:
            pulumi.set(__self__, "provisional_user_project", provisional_user_project)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if self_link is not None:
            pulumi.set(__self__, "self_link", self_link)
        if user_project is not None:
            pulumi.set(__self__, "user_project", user_project)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[str]:
        """
        The name of the bucket.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter
    def entity(self) -> pulumi.Input[str]:
        """
        The entity holding the permission, in one of the following forms: 
        - user-userId 
        - user-email 
        - group-groupId 
        - group-email 
        - domain-domain 
        - project-team-projectId 
        - allUsers 
        - allAuthenticatedUsers Examples: 
        - The user liz@example.com would be user-liz@example.com. 
        - The group example@googlegroups.com would be group-example@googlegroups.com. 
        - To refer to all members of the Google Apps for Business domain example.com, the entity would be domain-example.com.
        """
        return pulumi.get(self, "entity")

    @entity.setter
    def entity(self, value: pulumi.Input[str]):
        pulumi.set(self, "entity", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        The domain associated with the entity, if any.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        The email address associated with the entity, if any.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID for the entity, if any.
        """
        return pulumi.get(self, "entity_id")

    @entity_id.setter
    def entity_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "entity_id", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        HTTP 1.1 Entity tag for the access-control entry.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the access-control entry.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        The kind of item this is. For bucket access control entries, this is always storage#bucketAccessControl.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="projectTeam")
    def project_team(self) -> Optional[pulumi.Input['BucketAccessControlProjectTeamArgs']]:
        """
        The project team associated with the entity, if any.
        """
        return pulumi.get(self, "project_team")

    @project_team.setter
    def project_team(self, value: Optional[pulumi.Input['BucketAccessControlProjectTeamArgs']]):
        pulumi.set(self, "project_team", value)

    @property
    @pulumi.getter(name="provisionalUserProject")
    def provisional_user_project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "provisional_user_project")

    @provisional_user_project.setter
    def provisional_user_project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisional_user_project", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        The access permission for the entity.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[str]]:
        """
        The link to this access-control entry.
        """
        return pulumi.get(self, "self_link")

    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "self_link", value)

    @property
    @pulumi.getter(name="userProject")
    def user_project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "user_project")

    @user_project.setter
    def user_project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_project", value)


class BucketAccessControl(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 entity: Optional[pulumi.Input[str]] = None,
                 entity_id: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 project_team: Optional[pulumi.Input[pulumi.InputType['BucketAccessControlProjectTeamArgs']]] = None,
                 provisional_user_project: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 user_project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new ACL entry on the specified bucket.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: The name of the bucket.
        :param pulumi.Input[str] domain: The domain associated with the entity, if any.
        :param pulumi.Input[str] email: The email address associated with the entity, if any.
        :param pulumi.Input[str] entity: The entity holding the permission, in one of the following forms: 
               - user-userId 
               - user-email 
               - group-groupId 
               - group-email 
               - domain-domain 
               - project-team-projectId 
               - allUsers 
               - allAuthenticatedUsers Examples: 
               - The user liz@example.com would be user-liz@example.com. 
               - The group example@googlegroups.com would be group-example@googlegroups.com. 
               - To refer to all members of the Google Apps for Business domain example.com, the entity would be domain-example.com.
        :param pulumi.Input[str] entity_id: The ID for the entity, if any.
        :param pulumi.Input[str] etag: HTTP 1.1 Entity tag for the access-control entry.
        :param pulumi.Input[str] id: The ID of the access-control entry.
        :param pulumi.Input[str] kind: The kind of item this is. For bucket access control entries, this is always storage#bucketAccessControl.
        :param pulumi.Input[pulumi.InputType['BucketAccessControlProjectTeamArgs']] project_team: The project team associated with the entity, if any.
        :param pulumi.Input[str] role: The access permission for the entity.
        :param pulumi.Input[str] self_link: The link to this access-control entry.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BucketAccessControlArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new ACL entry on the specified bucket.

        :param str resource_name: The name of the resource.
        :param BucketAccessControlArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BucketAccessControlArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 entity: Optional[pulumi.Input[str]] = None,
                 entity_id: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 project_team: Optional[pulumi.Input[pulumi.InputType['BucketAccessControlProjectTeamArgs']]] = None,
                 provisional_user_project: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 user_project: Optional[pulumi.Input[str]] = None,
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
            __props__ = BucketAccessControlArgs.__new__(BucketAccessControlArgs)

            if bucket is None and not opts.urn:
                raise TypeError("Missing required property 'bucket'")
            __props__.__dict__["bucket"] = bucket
            __props__.__dict__["domain"] = domain
            __props__.__dict__["email"] = email
            if entity is None and not opts.urn:
                raise TypeError("Missing required property 'entity'")
            __props__.__dict__["entity"] = entity
            __props__.__dict__["entity_id"] = entity_id
            __props__.__dict__["etag"] = etag
            __props__.__dict__["id"] = id
            __props__.__dict__["kind"] = kind
            __props__.__dict__["project_team"] = project_team
            __props__.__dict__["provisional_user_project"] = provisional_user_project
            __props__.__dict__["role"] = role
            __props__.__dict__["self_link"] = self_link
            __props__.__dict__["user_project"] = user_project
        super(BucketAccessControl, __self__).__init__(
            'google-native:storage/v1:BucketAccessControl',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'BucketAccessControl':
        """
        Get an existing BucketAccessControl resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BucketAccessControlArgs.__new__(BucketAccessControlArgs)

        __props__.__dict__["bucket"] = None
        __props__.__dict__["domain"] = None
        __props__.__dict__["email"] = None
        __props__.__dict__["entity"] = None
        __props__.__dict__["entity_id"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["project_team"] = None
        __props__.__dict__["role"] = None
        __props__.__dict__["self_link"] = None
        return BucketAccessControl(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[str]:
        """
        The name of the bucket.
        """
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[str]:
        """
        The domain associated with the entity, if any.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[str]:
        """
        The email address associated with the entity, if any.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def entity(self) -> pulumi.Output[str]:
        """
        The entity holding the permission, in one of the following forms: 
        - user-userId 
        - user-email 
        - group-groupId 
        - group-email 
        - domain-domain 
        - project-team-projectId 
        - allUsers 
        - allAuthenticatedUsers Examples: 
        - The user liz@example.com would be user-liz@example.com. 
        - The group example@googlegroups.com would be group-example@googlegroups.com. 
        - To refer to all members of the Google Apps for Business domain example.com, the entity would be domain-example.com.
        """
        return pulumi.get(self, "entity")

    @property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> pulumi.Output[str]:
        """
        The ID for the entity, if any.
        """
        return pulumi.get(self, "entity_id")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        HTTP 1.1 Entity tag for the access-control entry.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The kind of item this is. For bucket access control entries, this is always storage#bucketAccessControl.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="projectTeam")
    def project_team(self) -> pulumi.Output['outputs.BucketAccessControlProjectTeamResponse']:
        """
        The project team associated with the entity, if any.
        """
        return pulumi.get(self, "project_team")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        """
        The access permission for the entity.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        The link to this access-control entry.
        """
        return pulumi.get(self, "self_link")

