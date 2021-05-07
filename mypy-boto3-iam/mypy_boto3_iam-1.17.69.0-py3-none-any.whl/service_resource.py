"""
Type annotations for iam service ServiceResource

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_iam import IAMServiceResource
    import mypy_boto3_iam.service_resource as iam_resources

    resource: IAMServiceResource = boto3.resource("iam")

    my_access_key: iam_resources.AccessKey = resource.AccessKey(...)
    my_access_key_pair: iam_resources.AccessKeyPair = resource.AccessKeyPair(...)
    my_account_password_policy: iam_resources.AccountPasswordPolicy = resource.AccountPasswordPolicy(...)
    my_account_summary: iam_resources.AccountSummary = resource.AccountSummary(...)
    my_assume_role_policy: iam_resources.AssumeRolePolicy = resource.AssumeRolePolicy(...)
    my_current_user: iam_resources.CurrentUser = resource.CurrentUser(...)
    my_group: iam_resources.Group = resource.Group(...)
    my_group_policy: iam_resources.GroupPolicy = resource.GroupPolicy(...)
    my_instance_profile: iam_resources.InstanceProfile = resource.InstanceProfile(...)
    my_login_profile: iam_resources.LoginProfile = resource.LoginProfile(...)
    my_mfa_device: iam_resources.MfaDevice = resource.MfaDevice(...)
    my_policy: iam_resources.Policy = resource.Policy(...)
    my_policy_version: iam_resources.PolicyVersion = resource.PolicyVersion(...)
    my_role: iam_resources.Role = resource.Role(...)
    my_role_policy: iam_resources.RolePolicy = resource.RolePolicy(...)
    my_saml_provider: iam_resources.SamlProvider = resource.SamlProvider(...)
    my_server_certificate: iam_resources.ServerCertificate = resource.ServerCertificate(...)
    my_signing_certificate: iam_resources.SigningCertificate = resource.SigningCertificate(...)
    my_user: iam_resources.User = resource.User(...)
    my_user_policy: iam_resources.UserPolicy = resource.UserPolicy(...)
    my_virtual_mfa_device: iam_resources.VirtualMfaDevice = resource.VirtualMfaDevice(...)
```
"""
from datetime import datetime
from typing import Any, Dict, Iterator, List

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

from mypy_boto3_iam.literals import (
    EntityType,
    PolicyUsageType,
    assignmentStatusType,
    policyScopeType,
    statusType,
)
from mypy_boto3_iam.type_defs import TagTypeDef, UpdateSAMLProviderResponseTypeDef

__all__ = (
    "IAMServiceResource",
    "AccessKey",
    "AccessKeyPair",
    "AccountPasswordPolicy",
    "AccountSummary",
    "AssumeRolePolicy",
    "CurrentUser",
    "Group",
    "GroupPolicy",
    "InstanceProfile",
    "LoginProfile",
    "MfaDevice",
    "Policy",
    "PolicyVersion",
    "Role",
    "RolePolicy",
    "SamlProvider",
    "ServerCertificate",
    "SigningCertificate",
    "User",
    "UserPolicy",
    "VirtualMfaDevice",
    "ServiceResourceGroupsCollection",
    "ServiceResourceInstanceProfilesCollection",
    "ServiceResourcePoliciesCollection",
    "ServiceResourceRolesCollection",
    "ServiceResourceSamlProvidersCollection",
    "ServiceResourceServerCertificatesCollection",
    "ServiceResourceUsersCollection",
    "ServiceResourceVirtualMfaDevicesCollection",
    "CurrentUserAccessKeysCollection",
    "CurrentUserMfaDevicesCollection",
    "CurrentUserSigningCertificatesCollection",
    "GroupAttachedPoliciesCollection",
    "GroupPoliciesCollection",
    "GroupUsersCollection",
    "PolicyAttachedGroupsCollection",
    "PolicyAttachedRolesCollection",
    "PolicyAttachedUsersCollection",
    "PolicyVersionsCollection",
    "RoleAttachedPoliciesCollection",
    "RoleInstanceProfilesCollection",
    "RolePoliciesCollection",
    "UserAccessKeysCollection",
    "UserAttachedPoliciesCollection",
    "UserGroupsCollection",
    "UserMfaDevicesCollection",
    "UserPoliciesCollection",
    "UserSigningCertificatesCollection",
)


class ServiceResourceGroupsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.groups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#serviceresourcegroupscollection)
    """

    def all(self) -> "ServiceResourceGroupsCollection":
        pass

    def filter(  # type: ignore
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> "ServiceResourceGroupsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceGroupsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceGroupsCollection":
        pass

    def pages(self) -> Iterator[List["Group"]]:
        pass

    def __iter__(self) -> Iterator["Group"]:
        pass


class ServiceResourceInstanceProfilesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.instance_profiles)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#serviceresourceinstanceprofilescollection)
    """

    def all(self) -> "ServiceResourceInstanceProfilesCollection":
        pass

    def filter(  # type: ignore
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> "ServiceResourceInstanceProfilesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceInstanceProfilesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceInstanceProfilesCollection":
        pass

    def pages(self) -> Iterator[List["InstanceProfile"]]:
        pass

    def __iter__(self) -> Iterator["InstanceProfile"]:
        pass


class ServiceResourcePoliciesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.policies)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#serviceresourcepoliciescollection)
    """

    def all(self) -> "ServiceResourcePoliciesCollection":
        pass

    def filter(  # type: ignore
        self,
        Scope: policyScopeType = None,
        OnlyAttached: bool = None,
        PathPrefix: str = None,
        PolicyUsageFilter: PolicyUsageType = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> "ServiceResourcePoliciesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourcePoliciesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourcePoliciesCollection":
        pass

    def pages(self) -> Iterator[List["Policy"]]:
        pass

    def __iter__(self) -> Iterator["Policy"]:
        pass


class ServiceResourceRolesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.roles)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#serviceresourcerolescollection)
    """

    def all(self) -> "ServiceResourceRolesCollection":
        pass

    def filter(  # type: ignore
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> "ServiceResourceRolesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceRolesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceRolesCollection":
        pass

    def pages(self) -> Iterator[List["Role"]]:
        pass

    def __iter__(self) -> Iterator["Role"]:
        pass


class ServiceResourceSamlProvidersCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.saml_providers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#serviceresourcesamlproviderscollection)
    """

    def all(self) -> "ServiceResourceSamlProvidersCollection":
        pass

    def filter(self) -> "ServiceResourceSamlProvidersCollection":  # type: ignore
        pass

    def limit(self, count: int) -> "ServiceResourceSamlProvidersCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceSamlProvidersCollection":
        pass

    def pages(self) -> Iterator[List["SamlProvider"]]:
        pass

    def __iter__(self) -> Iterator["SamlProvider"]:
        pass


class ServiceResourceServerCertificatesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.server_certificates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#serviceresourceservercertificatescollection)
    """

    def all(self) -> "ServiceResourceServerCertificatesCollection":
        pass

    def filter(  # type: ignore
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> "ServiceResourceServerCertificatesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceServerCertificatesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceServerCertificatesCollection":
        pass

    def pages(self) -> Iterator[List["ServerCertificate"]]:
        pass

    def __iter__(self) -> Iterator["ServerCertificate"]:
        pass


class ServiceResourceUsersCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.users)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#serviceresourceuserscollection)
    """

    def all(self) -> "ServiceResourceUsersCollection":
        pass

    def filter(  # type: ignore
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> "ServiceResourceUsersCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceUsersCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceUsersCollection":
        pass

    def pages(self) -> Iterator[List["User"]]:
        pass

    def __iter__(self) -> Iterator["User"]:
        pass


class ServiceResourceVirtualMfaDevicesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.virtual_mfa_devices)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#serviceresourcevirtualmfadevicescollection)
    """

    def all(self) -> "ServiceResourceVirtualMfaDevicesCollection":
        pass

    def filter(  # type: ignore
        self,
        AssignmentStatus: assignmentStatusType = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> "ServiceResourceVirtualMfaDevicesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceVirtualMfaDevicesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceVirtualMfaDevicesCollection":
        pass

    def pages(self) -> Iterator[List["VirtualMfaDevice"]]:
        pass

    def __iter__(self) -> Iterator["VirtualMfaDevice"]:
        pass


class CurrentUserAccessKeysCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.CurrentUser.access_keys)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#currentuseraccesskeyscollection)
    """

    def all(self) -> "CurrentUserAccessKeysCollection":
        pass

    def filter(  # type: ignore
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> "CurrentUserAccessKeysCollection":
        pass

    def limit(self, count: int) -> "CurrentUserAccessKeysCollection":
        pass

    def page_size(self, count: int) -> "CurrentUserAccessKeysCollection":
        pass

    def pages(self) -> Iterator[List["AccessKey"]]:
        pass

    def __iter__(self) -> Iterator["AccessKey"]:
        pass


class CurrentUserMfaDevicesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.CurrentUser.mfa_devices)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#currentusermfadevicescollection)
    """

    def all(self) -> "CurrentUserMfaDevicesCollection":
        pass

    def filter(  # type: ignore
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> "CurrentUserMfaDevicesCollection":
        pass

    def limit(self, count: int) -> "CurrentUserMfaDevicesCollection":
        pass

    def page_size(self, count: int) -> "CurrentUserMfaDevicesCollection":
        pass

    def pages(self) -> Iterator[List["MfaDevice"]]:
        pass

    def __iter__(self) -> Iterator["MfaDevice"]:
        pass


class CurrentUserSigningCertificatesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.CurrentUser.signing_certificates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#currentusersigningcertificatescollection)
    """

    def all(self) -> "CurrentUserSigningCertificatesCollection":
        pass

    def filter(  # type: ignore
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> "CurrentUserSigningCertificatesCollection":
        pass

    def limit(self, count: int) -> "CurrentUserSigningCertificatesCollection":
        pass

    def page_size(self, count: int) -> "CurrentUserSigningCertificatesCollection":
        pass

    def pages(self) -> Iterator[List["SigningCertificate"]]:
        pass

    def __iter__(self) -> Iterator["SigningCertificate"]:
        pass


class GroupAttachedPoliciesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Group.attached_policies)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#groupattachedpoliciescollection)
    """

    def all(self) -> "GroupAttachedPoliciesCollection":
        pass

    def filter(  # type: ignore
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> "GroupAttachedPoliciesCollection":
        pass

    def limit(self, count: int) -> "GroupAttachedPoliciesCollection":
        pass

    def page_size(self, count: int) -> "GroupAttachedPoliciesCollection":
        pass

    def pages(self) -> Iterator[List["Policy"]]:
        pass

    def __iter__(self) -> Iterator["Policy"]:
        pass


class GroupPoliciesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Group.policies)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#grouppoliciescollection)
    """

    def all(self) -> "GroupPoliciesCollection":
        pass

    def filter(  # type: ignore
        self, Marker: str = None, MaxItems: int = None
    ) -> "GroupPoliciesCollection":
        pass

    def limit(self, count: int) -> "GroupPoliciesCollection":
        pass

    def page_size(self, count: int) -> "GroupPoliciesCollection":
        pass

    def pages(self) -> Iterator[List["GroupPolicy"]]:
        pass

    def __iter__(self) -> Iterator["GroupPolicy"]:
        pass


class GroupUsersCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Group.users)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#groupuserscollection)
    """

    def all(self) -> "GroupUsersCollection":
        pass

    def filter(  # type: ignore
        self, Marker: str = None, MaxItems: int = None
    ) -> "GroupUsersCollection":
        pass

    def limit(self, count: int) -> "GroupUsersCollection":
        pass

    def page_size(self, count: int) -> "GroupUsersCollection":
        pass

    def pages(self) -> Iterator[List["User"]]:
        pass

    def __iter__(self) -> Iterator["User"]:
        pass


class PolicyAttachedGroupsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Policy.attached_groups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyattachedgroupscollection)
    """

    def all(self) -> "PolicyAttachedGroupsCollection":
        pass

    def filter(  # type: ignore
        self,
        EntityFilter: EntityType = None,
        PathPrefix: str = None,
        PolicyUsageFilter: PolicyUsageType = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> "PolicyAttachedGroupsCollection":
        pass

    def limit(self, count: int) -> "PolicyAttachedGroupsCollection":
        pass

    def page_size(self, count: int) -> "PolicyAttachedGroupsCollection":
        pass

    def pages(self) -> Iterator[List["Group"]]:
        pass

    def __iter__(self) -> Iterator["Group"]:
        pass


class PolicyAttachedRolesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Policy.attached_roles)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyattachedrolescollection)
    """

    def all(self) -> "PolicyAttachedRolesCollection":
        pass

    def filter(  # type: ignore
        self,
        EntityFilter: EntityType = None,
        PathPrefix: str = None,
        PolicyUsageFilter: PolicyUsageType = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> "PolicyAttachedRolesCollection":
        pass

    def limit(self, count: int) -> "PolicyAttachedRolesCollection":
        pass

    def page_size(self, count: int) -> "PolicyAttachedRolesCollection":
        pass

    def pages(self) -> Iterator[List["Role"]]:
        pass

    def __iter__(self) -> Iterator["Role"]:
        pass


class PolicyAttachedUsersCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Policy.attached_users)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyattacheduserscollection)
    """

    def all(self) -> "PolicyAttachedUsersCollection":
        pass

    def filter(  # type: ignore
        self,
        EntityFilter: EntityType = None,
        PathPrefix: str = None,
        PolicyUsageFilter: PolicyUsageType = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> "PolicyAttachedUsersCollection":
        pass

    def limit(self, count: int) -> "PolicyAttachedUsersCollection":
        pass

    def page_size(self, count: int) -> "PolicyAttachedUsersCollection":
        pass

    def pages(self) -> Iterator[List["User"]]:
        pass

    def __iter__(self) -> Iterator["User"]:
        pass


class PolicyVersionsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Policy.versions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyversionscollection)
    """

    def all(self) -> "PolicyVersionsCollection":
        pass

    def filter(  # type: ignore
        self, Marker: str = None, MaxItems: int = None
    ) -> "PolicyVersionsCollection":
        pass

    def limit(self, count: int) -> "PolicyVersionsCollection":
        pass

    def page_size(self, count: int) -> "PolicyVersionsCollection":
        pass

    def pages(self) -> Iterator[List["PolicyVersion"]]:
        pass

    def __iter__(self) -> Iterator["PolicyVersion"]:
        pass


class RoleAttachedPoliciesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Role.attached_policies)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#roleattachedpoliciescollection)
    """

    def all(self) -> "RoleAttachedPoliciesCollection":
        pass

    def filter(  # type: ignore
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> "RoleAttachedPoliciesCollection":
        pass

    def limit(self, count: int) -> "RoleAttachedPoliciesCollection":
        pass

    def page_size(self, count: int) -> "RoleAttachedPoliciesCollection":
        pass

    def pages(self) -> Iterator[List["Policy"]]:
        pass

    def __iter__(self) -> Iterator["Policy"]:
        pass


class RoleInstanceProfilesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Role.instance_profiles)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#roleinstanceprofilescollection)
    """

    def all(self) -> "RoleInstanceProfilesCollection":
        pass

    def filter(  # type: ignore
        self, Marker: str = None, MaxItems: int = None
    ) -> "RoleInstanceProfilesCollection":
        pass

    def limit(self, count: int) -> "RoleInstanceProfilesCollection":
        pass

    def page_size(self, count: int) -> "RoleInstanceProfilesCollection":
        pass

    def pages(self) -> Iterator[List["InstanceProfile"]]:
        pass

    def __iter__(self) -> Iterator["InstanceProfile"]:
        pass


class RolePoliciesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Role.policies)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#rolepoliciescollection)
    """

    def all(self) -> "RolePoliciesCollection":
        pass

    def filter(  # type: ignore
        self, Marker: str = None, MaxItems: int = None
    ) -> "RolePoliciesCollection":
        pass

    def limit(self, count: int) -> "RolePoliciesCollection":
        pass

    def page_size(self, count: int) -> "RolePoliciesCollection":
        pass

    def pages(self) -> Iterator[List["RolePolicy"]]:
        pass

    def __iter__(self) -> Iterator["RolePolicy"]:
        pass


class UserAccessKeysCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.User.access_keys)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#useraccesskeyscollection)
    """

    def all(self) -> "UserAccessKeysCollection":
        pass

    def filter(  # type: ignore
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> "UserAccessKeysCollection":
        pass

    def limit(self, count: int) -> "UserAccessKeysCollection":
        pass

    def page_size(self, count: int) -> "UserAccessKeysCollection":
        pass

    def pages(self) -> Iterator[List["AccessKey"]]:
        pass

    def __iter__(self) -> Iterator["AccessKey"]:
        pass


class UserAttachedPoliciesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.User.attached_policies)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userattachedpoliciescollection)
    """

    def all(self) -> "UserAttachedPoliciesCollection":
        pass

    def filter(  # type: ignore
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> "UserAttachedPoliciesCollection":
        pass

    def limit(self, count: int) -> "UserAttachedPoliciesCollection":
        pass

    def page_size(self, count: int) -> "UserAttachedPoliciesCollection":
        pass

    def pages(self) -> Iterator[List["Policy"]]:
        pass

    def __iter__(self) -> Iterator["Policy"]:
        pass


class UserGroupsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.User.groups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#usergroupscollection)
    """

    def all(self) -> "UserGroupsCollection":
        pass

    def filter(  # type: ignore
        self, Marker: str = None, MaxItems: int = None
    ) -> "UserGroupsCollection":
        pass

    def limit(self, count: int) -> "UserGroupsCollection":
        pass

    def page_size(self, count: int) -> "UserGroupsCollection":
        pass

    def pages(self) -> Iterator[List["Group"]]:
        pass

    def __iter__(self) -> Iterator["Group"]:
        pass


class UserMfaDevicesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.User.mfa_devices)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#usermfadevicescollection)
    """

    def all(self) -> "UserMfaDevicesCollection":
        pass

    def filter(  # type: ignore
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> "UserMfaDevicesCollection":
        pass

    def limit(self, count: int) -> "UserMfaDevicesCollection":
        pass

    def page_size(self, count: int) -> "UserMfaDevicesCollection":
        pass

    def pages(self) -> Iterator[List["MfaDevice"]]:
        pass

    def __iter__(self) -> Iterator["MfaDevice"]:
        pass


class UserPoliciesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.User.policies)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userpoliciescollection)
    """

    def all(self) -> "UserPoliciesCollection":
        pass

    def filter(  # type: ignore
        self, Marker: str = None, MaxItems: int = None
    ) -> "UserPoliciesCollection":
        pass

    def limit(self, count: int) -> "UserPoliciesCollection":
        pass

    def page_size(self, count: int) -> "UserPoliciesCollection":
        pass

    def pages(self) -> Iterator[List["UserPolicy"]]:
        pass

    def __iter__(self) -> Iterator["UserPolicy"]:
        pass


class UserSigningCertificatesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.User.signing_certificates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#usersigningcertificatescollection)
    """

    def all(self) -> "UserSigningCertificatesCollection":
        pass

    def filter(  # type: ignore
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> "UserSigningCertificatesCollection":
        pass

    def limit(self, count: int) -> "UserSigningCertificatesCollection":
        pass

    def page_size(self, count: int) -> "UserSigningCertificatesCollection":
        pass

    def pages(self) -> Iterator[List["SigningCertificate"]]:
        pass

    def __iter__(self) -> Iterator["SigningCertificate"]:
        pass


class AccessKeyPair(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.AccessKeyPair)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accesskeypair)
    """

    access_key_id: str
    status: str
    secret_access_key: str
    create_date: datetime
    user_name: str
    id: str
    secret: str

    def activate(self, Status: statusType) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.AccessKeyPair.activate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accesskeypairactivatemethod)
        """

    def deactivate(self, Status: statusType) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.AccessKeyPair.deactivate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accesskeypairdeactivatemethod)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.AccessKeyPair.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accesskeypairdeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.AccessKeyPair.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accesskeypairget-available-subresourcesmethod)
        """


_AccessKeyPair = AccessKeyPair


class AccountPasswordPolicy(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.AccountPasswordPolicy)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accountpasswordpolicy)
    """

    minimum_password_length: int
    require_symbols: bool
    require_numbers: bool
    require_uppercase_characters: bool
    require_lowercase_characters: bool
    allow_users_to_change_password: bool
    expire_passwords: bool
    max_password_age: int
    password_reuse_prevention: int
    hard_expiry: bool

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.AccountPasswordPolicy.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accountpasswordpolicydeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.AccountPasswordPolicy.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accountpasswordpolicyget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.AccountPasswordPolicy.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accountpasswordpolicyloadmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.AccountPasswordPolicy.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accountpasswordpolicyreloadmethod)
        """

    def update(
        self,
        MinimumPasswordLength: int = None,
        RequireSymbols: bool = None,
        RequireNumbers: bool = None,
        RequireUppercaseCharacters: bool = None,
        RequireLowercaseCharacters: bool = None,
        AllowUsersToChangePassword: bool = None,
        MaxPasswordAge: int = None,
        PasswordReusePrevention: int = None,
        HardExpiry: bool = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.AccountPasswordPolicy.update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accountpasswordpolicyupdatemethod)
        """


_AccountPasswordPolicy = AccountPasswordPolicy


class AccountSummary(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.AccountSummary)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accountsummary)
    """

    summary_map: Dict[str, Any]

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.AccountSummary.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accountsummaryget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.AccountSummary.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accountsummaryloadmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.AccountSummary.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accountsummaryreloadmethod)
        """


_AccountSummary = AccountSummary


class CurrentUser(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.CurrentUser)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#currentuser)
    """

    path: str
    user_name: str
    user_id: str
    arn: str
    create_date: datetime
    password_last_used: datetime
    permissions_boundary: Dict[str, Any]
    tags: List[Any]
    user: "User"
    access_keys: CurrentUserAccessKeysCollection
    mfa_devices: CurrentUserMfaDevicesCollection
    signing_certificates: CurrentUserSigningCertificatesCollection

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.CurrentUser.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#currentuserget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.CurrentUser.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#currentuserloadmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.CurrentUser.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#currentuserreloadmethod)
        """


_CurrentUser = CurrentUser


class InstanceProfile(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.InstanceProfile)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#instanceprofile)
    """

    path: str
    instance_profile_name: str
    instance_profile_id: str
    arn: str
    create_date: datetime
    roles_attribute: List[Any]
    tags: List[Any]
    name: str
    roles: "Role"

    def add_role(self, RoleName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.InstanceProfile.add_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#instanceprofileadd-rolemethod)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.InstanceProfile.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#instanceprofiledeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.InstanceProfile.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#instanceprofileget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.InstanceProfile.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#instanceprofileloadmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.InstanceProfile.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#instanceprofilereloadmethod)
        """

    def remove_role(self, RoleName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.InstanceProfile.remove_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#instanceprofileremove-rolemethod)
        """


_InstanceProfile = InstanceProfile


class PolicyVersion(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.PolicyVersion)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyversion)
    """

    document: str
    is_default_version: bool
    create_date: datetime
    arn: str
    version_id: str

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.PolicyVersion.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyversiondeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.PolicyVersion.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyversionget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.PolicyVersion.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyversionloadmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.PolicyVersion.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyversionreloadmethod)
        """

    def set_as_default(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.PolicyVersion.set_as_default)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyversionset-as-defaultmethod)
        """


_PolicyVersion = PolicyVersion


class SamlProvider(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.SamlProvider)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#samlprovider)
    """

    saml_metadata_document: str
    create_date: datetime
    valid_until: datetime
    tags: List[Any]
    arn: str

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.SamlProvider.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#samlproviderdeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.SamlProvider.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#samlproviderget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.SamlProvider.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#samlproviderloadmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.SamlProvider.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#samlproviderreloadmethod)
        """

    def update(self, SAMLMetadataDocument: str) -> UpdateSAMLProviderResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.SamlProvider.update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#samlproviderupdatemethod)
        """


_SamlProvider = SamlProvider


class VirtualMfaDevice(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.VirtualMfaDevice)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#virtualmfadevice)
    """

    base32_string_seed: bytes
    qr_code_png: bytes
    user_attribute: Dict[str, Any]
    enable_date: datetime
    tags: List[Any]
    serial_number: str
    user: "User"

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.VirtualMfaDevice.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#virtualmfadevicedeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.VirtualMfaDevice.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#virtualmfadeviceget-available-subresourcesmethod)
        """


_VirtualMfaDevice = VirtualMfaDevice


class AccessKey(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.AccessKey)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accesskey)
    """

    access_key_id: str
    status: str
    create_date: datetime
    user_name: str
    id: str

    def User(self) -> "_User":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.AccessKey.User)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accesskeyusermethod)
        """

    def activate(self, Status: statusType) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.AccessKey.activate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accesskeyactivatemethod)
        """

    def deactivate(self, Status: statusType) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.AccessKey.deactivate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accesskeydeactivatemethod)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.AccessKey.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accesskeydeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.AccessKey.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accesskeyget-available-subresourcesmethod)
        """


_AccessKey = AccessKey


class AssumeRolePolicy(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.AssumeRolePolicy)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#assumerolepolicy)
    """

    role_name: str

    def Role(self) -> "_Role":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.AssumeRolePolicy.Role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#assumerolepolicyrolemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.AssumeRolePolicy.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#assumerolepolicyget-available-subresourcesmethod)
        """

    def update(self, PolicyDocument: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.AssumeRolePolicy.update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#assumerolepolicyupdatemethod)
        """


_AssumeRolePolicy = AssumeRolePolicy


class GroupPolicy(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.GroupPolicy)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#grouppolicy)
    """

    policy_name: str
    policy_document: str
    group_name: str
    name: str

    def Group(self) -> "_Group":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.GroupPolicy.Group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#grouppolicygroupmethod)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.GroupPolicy.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#grouppolicydeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.GroupPolicy.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#grouppolicyget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.GroupPolicy.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#grouppolicyloadmethod)
        """

    def put(self, PolicyDocument: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.GroupPolicy.put)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#grouppolicyputmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.GroupPolicy.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#grouppolicyreloadmethod)
        """


_GroupPolicy = GroupPolicy


class MfaDevice(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.MfaDevice)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#mfadevice)
    """

    enable_date: datetime
    user_name: str
    serial_number: str

    def User(self) -> "_User":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.MfaDevice.User)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#mfadeviceusermethod)
        """

    def associate(self, AuthenticationCode1: str, AuthenticationCode2: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.MfaDevice.associate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#mfadeviceassociatemethod)
        """

    def disassociate(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.MfaDevice.disassociate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#mfadevicedisassociatemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.MfaDevice.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#mfadeviceget-available-subresourcesmethod)
        """

    def resync(self, AuthenticationCode1: str, AuthenticationCode2: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.MfaDevice.resync)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#mfadeviceresyncmethod)
        """


_MfaDevice = MfaDevice


class Policy(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.Policy)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policy)
    """

    policy_name: str
    policy_id: str
    path: str
    default_version_id: str
    attachment_count: int
    permissions_boundary_usage_count: int
    is_attachable: bool
    description: str
    create_date: datetime
    update_date: datetime
    tags: List[Any]
    arn: str
    default_version: "PolicyVersion"
    attached_groups: PolicyAttachedGroupsCollection
    attached_roles: PolicyAttachedRolesCollection
    attached_users: PolicyAttachedUsersCollection
    versions: PolicyVersionsCollection

    def attach_group(self, GroupName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Policy.attach_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyattach-groupmethod)
        """

    def attach_role(self, RoleName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Policy.attach_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyattach-rolemethod)
        """

    def attach_user(self, UserName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Policy.attach_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyattach-usermethod)
        """

    def create_version(self, PolicyDocument: str, SetAsDefault: bool = None) -> _PolicyVersion:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Policy.create_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policycreate-versionmethod)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Policy.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policydeletemethod)
        """

    def detach_group(self, GroupName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Policy.detach_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policydetach-groupmethod)
        """

    def detach_role(self, RoleName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Policy.detach_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policydetach-rolemethod)
        """

    def detach_user(self, UserName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Policy.detach_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policydetach-usermethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Policy.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Policy.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyloadmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Policy.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyreloadmethod)
        """


_Policy = Policy


class RolePolicy(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.RolePolicy)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#rolepolicy)
    """

    policy_name: str
    policy_document: str
    role_name: str
    name: str

    def Role(self) -> "_Role":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.RolePolicy.Role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#rolepolicyrolemethod)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.RolePolicy.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#rolepolicydeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.RolePolicy.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#rolepolicyget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.RolePolicy.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#rolepolicyloadmethod)
        """

    def put(self, PolicyDocument: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.RolePolicy.put)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#rolepolicyputmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.RolePolicy.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#rolepolicyreloadmethod)
        """


_RolePolicy = RolePolicy


class ServerCertificate(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.ServerCertificate)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#servercertificate)
    """

    server_certificate_metadata: Dict[str, Any]
    certificate_body: str
    certificate_chain: str
    tags: List[Any]
    name: str

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServerCertificate.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#servercertificatedeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServerCertificate.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#servercertificateget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServerCertificate.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#servercertificateloadmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServerCertificate.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#servercertificatereloadmethod)
        """

    def update(
        self, NewPath: str = None, NewServerCertificateName: str = None
    ) -> "_ServerCertificate":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServerCertificate.update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#servercertificateupdatemethod)
        """


_ServerCertificate = ServerCertificate


class SigningCertificate(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.SigningCertificate)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#signingcertificate)
    """

    certificate_id: str
    certificate_body: str
    status: str
    upload_date: datetime
    user_name: str
    id: str

    def User(self) -> "_User":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.SigningCertificate.User)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#signingcertificateusermethod)
        """

    def activate(self, Status: statusType) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.SigningCertificate.activate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#signingcertificateactivatemethod)
        """

    def deactivate(self, Status: statusType) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.SigningCertificate.deactivate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#signingcertificatedeactivatemethod)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.SigningCertificate.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#signingcertificatedeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.SigningCertificate.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#signingcertificateget-available-subresourcesmethod)
        """


_SigningCertificate = SigningCertificate


class UserPolicy(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.UserPolicy)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userpolicy)
    """

    policy_name: str
    policy_document: str
    user_name: str
    name: str

    def User(self) -> "_User":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.UserPolicy.User)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userpolicyusermethod)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.UserPolicy.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userpolicydeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.UserPolicy.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userpolicyget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.UserPolicy.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userpolicyloadmethod)
        """

    def put(self, PolicyDocument: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.UserPolicy.put)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userpolicyputmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.UserPolicy.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userpolicyreloadmethod)
        """


_UserPolicy = UserPolicy


class LoginProfile(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.LoginProfile)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#loginprofile)
    """

    create_date: datetime
    password_reset_required: bool
    user_name: str

    def User(self) -> "_User":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.LoginProfile.User)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#loginprofileusermethod)
        """

    def create(self, Password: str, PasswordResetRequired: bool = None) -> "_LoginProfile":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.LoginProfile.create)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#loginprofilecreatemethod)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.LoginProfile.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#loginprofiledeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.LoginProfile.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#loginprofileget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.LoginProfile.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#loginprofileloadmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.LoginProfile.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#loginprofilereloadmethod)
        """

    def update(self, Password: str = None, PasswordResetRequired: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.LoginProfile.update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#loginprofileupdatemethod)
        """


_LoginProfile = LoginProfile


class Role(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.Role)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#role)
    """

    path: str
    role_name: str
    role_id: str
    arn: str
    create_date: datetime
    assume_role_policy_document: str
    description: str
    max_session_duration: int
    permissions_boundary: Dict[str, Any]
    tags: List[Any]
    role_last_used: Dict[str, Any]
    name: str
    attached_policies: RoleAttachedPoliciesCollection
    instance_profiles: RoleInstanceProfilesCollection
    policies: RolePoliciesCollection

    def AssumeRolePolicy(self) -> _AssumeRolePolicy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Role.AssumeRolePolicy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#roleassumerolepolicymethod)
        """

    def Policy(self, name: str) -> _RolePolicy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Role.Policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#rolepolicymethod)
        """

    def attach_policy(self, PolicyArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Role.attach_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#roleattach-policymethod)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Role.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#roledeletemethod)
        """

    def detach_policy(self, PolicyArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Role.detach_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#roledetach-policymethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Role.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#roleget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Role.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#roleloadmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Role.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#rolereloadmethod)
        """


_Role = Role


class Group(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.Group)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#group)
    """

    path: str
    group_name: str
    group_id: str
    arn: str
    create_date: datetime
    name: str
    attached_policies: GroupAttachedPoliciesCollection
    policies: GroupPoliciesCollection
    users: GroupUsersCollection

    def Policy(self, name: str) -> _GroupPolicy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Group.Policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#grouppolicymethod)
        """

    def add_user(self, UserName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Group.add_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#groupadd-usermethod)
        """

    def attach_policy(self, PolicyArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Group.attach_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#groupattach-policymethod)
        """

    def create(self, Path: str = None) -> "_Group":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Group.create)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#groupcreatemethod)
        """

    def create_policy(self, PolicyName: str, PolicyDocument: str) -> _GroupPolicy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Group.create_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#groupcreate-policymethod)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Group.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#groupdeletemethod)
        """

    def detach_policy(self, PolicyArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Group.detach_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#groupdetach-policymethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Group.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#groupget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Group.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#grouploadmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Group.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#groupreloadmethod)
        """

    def remove_user(self, UserName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Group.remove_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#groupremove-usermethod)
        """

    def update(self, NewPath: str = None, NewGroupName: str = None) -> "_Group":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.Group.update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#groupupdatemethod)
        """


_Group = Group


class User(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.User)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#user)
    """

    path: str
    user_name: str
    user_id: str
    arn: str
    create_date: datetime
    password_last_used: datetime
    permissions_boundary: Dict[str, Any]
    tags: List[Any]
    name: str
    access_keys: UserAccessKeysCollection
    attached_policies: UserAttachedPoliciesCollection
    groups: UserGroupsCollection
    mfa_devices: UserMfaDevicesCollection
    policies: UserPoliciesCollection
    signing_certificates: UserSigningCertificatesCollection

    def AccessKey(self, id: str) -> _AccessKey:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.User.AccessKey)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#useraccesskeymethod)
        """

    def LoginProfile(self) -> _LoginProfile:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.User.LoginProfile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userloginprofilemethod)
        """

    def MfaDevice(self, serial_number: str) -> _MfaDevice:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.User.MfaDevice)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#usermfadevicemethod)
        """

    def Policy(self, name: str) -> _UserPolicy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.User.Policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userpolicymethod)
        """

    def SigningCertificate(self, id: str) -> _SigningCertificate:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.User.SigningCertificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#usersigningcertificatemethod)
        """

    def add_group(self, GroupName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.User.add_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#useradd-groupmethod)
        """

    def attach_policy(self, PolicyArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.User.attach_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userattach-policymethod)
        """

    def create(
        self, Path: str = None, PermissionsBoundary: str = None, Tags: List["TagTypeDef"] = None
    ) -> "_User":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.User.create)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#usercreatemethod)
        """

    def create_access_key_pair(self) -> _AccessKeyPair:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.User.create_access_key_pair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#usercreate-access-key-pairmethod)
        """

    def create_login_profile(
        self, Password: str, PasswordResetRequired: bool = None
    ) -> _LoginProfile:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.User.create_login_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#usercreate-login-profilemethod)
        """

    def create_policy(self, PolicyName: str, PolicyDocument: str) -> _UserPolicy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.User.create_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#usercreate-policymethod)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.User.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userdeletemethod)
        """

    def detach_policy(self, PolicyArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.User.detach_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userdetach-policymethod)
        """

    def enable_mfa(
        self, SerialNumber: str, AuthenticationCode1: str, AuthenticationCode2: str
    ) -> _MfaDevice:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.User.enable_mfa)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userenable-mfamethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.User.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.User.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userloadmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.User.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userreloadmethod)
        """

    def remove_group(self, GroupName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.User.remove_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userremove-groupmethod)
        """

    def update(self, NewPath: str = None, NewUserName: str = None) -> "_User":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.User.update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userupdatemethod)
        """


_User = User


class IAMServiceResource(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html)
    """

    groups: ServiceResourceGroupsCollection
    instance_profiles: ServiceResourceInstanceProfilesCollection
    policies: ServiceResourcePoliciesCollection
    roles: ServiceResourceRolesCollection
    saml_providers: ServiceResourceSamlProvidersCollection
    server_certificates: ServiceResourceServerCertificatesCollection
    users: ServiceResourceUsersCollection
    virtual_mfa_devices: ServiceResourceVirtualMfaDevicesCollection

    def AccessKey(self, user_name: str, id: str) -> _AccessKey:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.AccessKey)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceaccesskeymethod)
        """

    def AccessKeyPair(self, user_name: str, id: str, secret: str) -> _AccessKeyPair:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.AccessKeyPair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceaccesskeypairmethod)
        """

    def AccountPasswordPolicy(self) -> _AccountPasswordPolicy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.AccountPasswordPolicy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceaccountpasswordpolicymethod)
        """

    def AccountSummary(self) -> _AccountSummary:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.AccountSummary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceaccountsummarymethod)
        """

    def AssumeRolePolicy(self, role_name: str) -> _AssumeRolePolicy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.AssumeRolePolicy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceassumerolepolicymethod)
        """

    def CurrentUser(self) -> _CurrentUser:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.CurrentUser)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcecurrentusermethod)
        """

    def Group(self, name: str) -> _Group:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.Group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcegroupmethod)
        """

    def GroupPolicy(self, group_name: str, name: str) -> _GroupPolicy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.GroupPolicy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcegrouppolicymethod)
        """

    def InstanceProfile(self, name: str) -> _InstanceProfile:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.InstanceProfile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceinstanceprofilemethod)
        """

    def LoginProfile(self, user_name: str) -> _LoginProfile:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.LoginProfile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceloginprofilemethod)
        """

    def MfaDevice(self, user_name: str, serial_number: str) -> _MfaDevice:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.MfaDevice)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcemfadevicemethod)
        """

    def Policy(self, policy_arn: str) -> _Policy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.Policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcepolicymethod)
        """

    def PolicyVersion(self, arn: str, version_id: str) -> _PolicyVersion:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.PolicyVersion)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcepolicyversionmethod)
        """

    def Role(self, name: str) -> _Role:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.Role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcerolemethod)
        """

    def RolePolicy(self, role_name: str, name: str) -> _RolePolicy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.RolePolicy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcerolepolicymethod)
        """

    def SamlProvider(self, arn: str) -> _SamlProvider:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.SamlProvider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcesamlprovidermethod)
        """

    def ServerCertificate(self, name: str) -> _ServerCertificate:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.ServerCertificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceservercertificatemethod)
        """

    def SigningCertificate(self, user_name: str, id: str) -> _SigningCertificate:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.SigningCertificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcesigningcertificatemethod)
        """

    def User(self, name: str) -> _User:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.User)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceusermethod)
        """

    def UserPolicy(self, user_name: str, name: str) -> _UserPolicy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.UserPolicy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceuserpolicymethod)
        """

    def VirtualMfaDevice(self, serial_number: str) -> _VirtualMfaDevice:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.VirtualMfaDevice)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcevirtualmfadevicemethod)
        """

    def change_password(self, OldPassword: str, NewPassword: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.change_password)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcechange-passwordmethod)
        """

    def create_account_alias(self, AccountAlias: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.create_account_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcecreate-account-aliasmethod)
        """

    def create_account_password_policy(
        self,
        MinimumPasswordLength: int = None,
        RequireSymbols: bool = None,
        RequireNumbers: bool = None,
        RequireUppercaseCharacters: bool = None,
        RequireLowercaseCharacters: bool = None,
        AllowUsersToChangePassword: bool = None,
        MaxPasswordAge: int = None,
        PasswordReusePrevention: int = None,
        HardExpiry: bool = None,
    ) -> _AccountPasswordPolicy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.create_account_password_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcecreate-account-password-policymethod)
        """

    def create_group(self, GroupName: str, Path: str = None) -> _Group:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.create_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcecreate-groupmethod)
        """

    def create_instance_profile(
        self, InstanceProfileName: str, Path: str = None, Tags: List["TagTypeDef"] = None
    ) -> _InstanceProfile:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.create_instance_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcecreate-instance-profilemethod)
        """

    def create_policy(
        self,
        PolicyName: str,
        PolicyDocument: str,
        Path: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> _Policy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.create_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcecreate-policymethod)
        """

    def create_role(
        self,
        RoleName: str,
        AssumeRolePolicyDocument: str,
        Path: str = None,
        Description: str = None,
        MaxSessionDuration: int = None,
        PermissionsBoundary: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> _Role:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.create_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcecreate-rolemethod)
        """

    def create_saml_provider(
        self, SAMLMetadataDocument: str, Name: str, Tags: List["TagTypeDef"] = None
    ) -> _SamlProvider:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.create_saml_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcecreate-saml-providermethod)
        """

    def create_server_certificate(
        self,
        ServerCertificateName: str,
        CertificateBody: str,
        PrivateKey: str,
        Path: str = None,
        CertificateChain: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> _ServerCertificate:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.create_server_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcecreate-server-certificatemethod)
        """

    def create_signing_certificate(
        self, CertificateBody: str, UserName: str = None
    ) -> _SigningCertificate:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.create_signing_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcecreate-signing-certificatemethod)
        """

    def create_user(
        self,
        UserName: str,
        Path: str = None,
        PermissionsBoundary: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> _User:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.create_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcecreate-usermethod)
        """

    def create_virtual_mfa_device(
        self, VirtualMFADeviceName: str, Path: str = None, Tags: List["TagTypeDef"] = None
    ) -> _VirtualMfaDevice:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.create_virtual_mfa_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcecreate-virtual-mfa-devicemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/iam.html#IAM.ServiceResource.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceget-available-subresourcesmethod)
        """
