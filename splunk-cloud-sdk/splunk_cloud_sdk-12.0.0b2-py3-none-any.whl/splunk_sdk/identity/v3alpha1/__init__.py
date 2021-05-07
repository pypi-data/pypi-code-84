# coding: utf-8

# flake8: noqa

# Copyright © 2021 Splunk, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"): you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# [http://www.apache.org/licenses/LICENSE-2.0]
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

############# This file is auto-generated.  Do not edit! #############

"""
    SDC Service: Identity

    With the Identity service in Splunk Cloud Services, you can authenticate and authorize Splunk Cloud Services users.

    OpenAPI spec version: v3alpha1.1 
    Generated by: https://openapi-generator.tech
"""


__version__ = "1.0.0"

# import apis into sdk package
from splunk_sdk.identity.v3alpha1.gen_identity_api import Identity

# import models into sdk package
from splunk_sdk.identity.v3alpha1.gen_models import AddGroupMemberBody, \
    AddGroupRoleBody, \
    AddMemberBody, \
    AddRolePermissionBody, \
    CreateGroupBody, \
    CreateRoleBody, \
    ECJwk, \
    Group, \
    GroupList, \
    GroupMember, \
    GroupMemberList, \
    GroupRole, \
    GroupRoleList, \
    IdentityProviderBodyConfig, \
    IdentityProviderBody, \
    IdentityProviderConfigBodyConfig, \
    IdentityProviderConfigBody, \
    PrincipalProfile, \
    Member, \
    MemberList, \
    PermissionList, \
    PrincipalKind, \
    Principal, \
    PrincipalList, \
    PrincipalPublicKey, \
    PrincipalPublicKeyStatusBody, \
    ResetPasswordBody, \
    Role, \
    RoleList, \
    RolePermission, \
    RolePermissionList, \
    TenantStatus, \
    Tenant, \
    UpdatePasswordBody, \
    ValidateInfo
