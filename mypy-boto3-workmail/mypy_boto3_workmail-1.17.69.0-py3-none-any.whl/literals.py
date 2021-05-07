"""
Type annotations for workmail service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/literals.html)

Usage::

    ```python
    from mypy_boto3_workmail.literals import AccessControlRuleEffect

    data: AccessControlRuleEffect = "ALLOW"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AccessControlRuleEffect",
    "EntityState",
    "FolderName",
    "ListAliasesPaginatorName",
    "ListGroupMembersPaginatorName",
    "ListGroupsPaginatorName",
    "ListMailboxPermissionsPaginatorName",
    "ListOrganizationsPaginatorName",
    "ListResourceDelegatesPaginatorName",
    "ListResourcesPaginatorName",
    "ListUsersPaginatorName",
    "MailboxExportJobState",
    "MemberType",
    "MobileDeviceAccessRuleEffect",
    "PermissionType",
    "ResourceType",
    "RetentionAction",
    "UserRole",
)


AccessControlRuleEffect = Literal["ALLOW", "DENY"]
EntityState = Literal["DELETED", "DISABLED", "ENABLED"]
FolderName = Literal["DELETED_ITEMS", "DRAFTS", "INBOX", "JUNK_EMAIL", "SENT_ITEMS"]
ListAliasesPaginatorName = Literal["list_aliases"]
ListGroupMembersPaginatorName = Literal["list_group_members"]
ListGroupsPaginatorName = Literal["list_groups"]
ListMailboxPermissionsPaginatorName = Literal["list_mailbox_permissions"]
ListOrganizationsPaginatorName = Literal["list_organizations"]
ListResourceDelegatesPaginatorName = Literal["list_resource_delegates"]
ListResourcesPaginatorName = Literal["list_resources"]
ListUsersPaginatorName = Literal["list_users"]
MailboxExportJobState = Literal["CANCELLED", "COMPLETED", "FAILED", "RUNNING"]
MemberType = Literal["GROUP", "USER"]
MobileDeviceAccessRuleEffect = Literal["ALLOW", "DENY"]
PermissionType = Literal["FULL_ACCESS", "SEND_AS", "SEND_ON_BEHALF"]
ResourceType = Literal["EQUIPMENT", "ROOM"]
RetentionAction = Literal["DELETE", "NONE", "PERMANENTLY_DELETE"]
UserRole = Literal["RESOURCE", "SYSTEM_USER", "USER"]
