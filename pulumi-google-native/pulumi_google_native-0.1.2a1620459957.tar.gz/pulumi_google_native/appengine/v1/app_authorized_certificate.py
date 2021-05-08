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

__all__ = ['AppAuthorizedCertificateArgs', 'AppAuthorizedCertificate']

@pulumi.input_type
class AppAuthorizedCertificateArgs:
    def __init__(__self__, *,
                 apps_id: pulumi.Input[str],
                 authorized_certificates_id: pulumi.Input[str],
                 certificate_raw_data: Optional[pulumi.Input['CertificateRawDataArgs']] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 domain_mappings_count: Optional[pulumi.Input[int]] = None,
                 domain_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 expire_time: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 managed_certificate: Optional[pulumi.Input['ManagedCertificateArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 visible_domain_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a AppAuthorizedCertificate resource.
        :param pulumi.Input['CertificateRawDataArgs'] certificate_raw_data: The SSL certificate serving the AuthorizedCertificate resource. This must be obtained independently from a certificate authority.
        :param pulumi.Input[str] display_name: The user-specified display name of the certificate. This is not guaranteed to be unique. Example: My Certificate.
        :param pulumi.Input[int] domain_mappings_count: Aggregate count of the domain mappings with this certificate mapped. This count includes domain mappings on applications for which the user does not have VIEWER permissions.Only returned by GET or LIST requests when specifically requested by the view=FULL_CERTIFICATE option.@OutputOnly
        :param pulumi.Input[Sequence[pulumi.Input[str]]] domain_names: Topmost applicable domains of this certificate. This certificate applies to these domains and their subdomains. Example: example.com.@OutputOnly
        :param pulumi.Input[str] expire_time: The time when this certificate expires. To update the renewal time on this certificate, upload an SSL certificate with a different expiration time using AuthorizedCertificates.UpdateAuthorizedCertificate.@OutputOnly
        :param pulumi.Input[str] id: Relative name of the certificate. This is a unique value autogenerated on AuthorizedCertificate resource creation. Example: 12345.@OutputOnly
        :param pulumi.Input['ManagedCertificateArgs'] managed_certificate: Only applicable if this certificate is managed by App Engine. Managed certificates are tied to the lifecycle of a DomainMapping and cannot be updated or deleted via the AuthorizedCertificates API. If this certificate is manually administered by the user, this field will be empty.@OutputOnly
        :param pulumi.Input[str] name: Full path to the AuthorizedCertificate resource in the API. Example: apps/myapp/authorizedCertificates/12345.@OutputOnly
        :param pulumi.Input[Sequence[pulumi.Input[str]]] visible_domain_mappings: The full paths to user visible Domain Mapping resources that have this certificate mapped. Example: apps/myapp/domainMappings/example.com.This may not represent the full list of mapped domain mappings if the user does not have VIEWER permissions on all of the applications that have this certificate mapped. See domain_mappings_count for a complete count.Only returned by GET or LIST requests when specifically requested by the view=FULL_CERTIFICATE option.@OutputOnly
        """
        pulumi.set(__self__, "apps_id", apps_id)
        pulumi.set(__self__, "authorized_certificates_id", authorized_certificates_id)
        if certificate_raw_data is not None:
            pulumi.set(__self__, "certificate_raw_data", certificate_raw_data)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if domain_mappings_count is not None:
            pulumi.set(__self__, "domain_mappings_count", domain_mappings_count)
        if domain_names is not None:
            pulumi.set(__self__, "domain_names", domain_names)
        if expire_time is not None:
            pulumi.set(__self__, "expire_time", expire_time)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if managed_certificate is not None:
            pulumi.set(__self__, "managed_certificate", managed_certificate)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if visible_domain_mappings is not None:
            pulumi.set(__self__, "visible_domain_mappings", visible_domain_mappings)

    @property
    @pulumi.getter(name="appsId")
    def apps_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "apps_id")

    @apps_id.setter
    def apps_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "apps_id", value)

    @property
    @pulumi.getter(name="authorizedCertificatesId")
    def authorized_certificates_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "authorized_certificates_id")

    @authorized_certificates_id.setter
    def authorized_certificates_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "authorized_certificates_id", value)

    @property
    @pulumi.getter(name="certificateRawData")
    def certificate_raw_data(self) -> Optional[pulumi.Input['CertificateRawDataArgs']]:
        """
        The SSL certificate serving the AuthorizedCertificate resource. This must be obtained independently from a certificate authority.
        """
        return pulumi.get(self, "certificate_raw_data")

    @certificate_raw_data.setter
    def certificate_raw_data(self, value: Optional[pulumi.Input['CertificateRawDataArgs']]):
        pulumi.set(self, "certificate_raw_data", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The user-specified display name of the certificate. This is not guaranteed to be unique. Example: My Certificate.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="domainMappingsCount")
    def domain_mappings_count(self) -> Optional[pulumi.Input[int]]:
        """
        Aggregate count of the domain mappings with this certificate mapped. This count includes domain mappings on applications for which the user does not have VIEWER permissions.Only returned by GET or LIST requests when specifically requested by the view=FULL_CERTIFICATE option.@OutputOnly
        """
        return pulumi.get(self, "domain_mappings_count")

    @domain_mappings_count.setter
    def domain_mappings_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "domain_mappings_count", value)

    @property
    @pulumi.getter(name="domainNames")
    def domain_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Topmost applicable domains of this certificate. This certificate applies to these domains and their subdomains. Example: example.com.@OutputOnly
        """
        return pulumi.get(self, "domain_names")

    @domain_names.setter
    def domain_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "domain_names", value)

    @property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[pulumi.Input[str]]:
        """
        The time when this certificate expires. To update the renewal time on this certificate, upload an SSL certificate with a different expiration time using AuthorizedCertificates.UpdateAuthorizedCertificate.@OutputOnly
        """
        return pulumi.get(self, "expire_time")

    @expire_time.setter
    def expire_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expire_time", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Relative name of the certificate. This is a unique value autogenerated on AuthorizedCertificate resource creation. Example: 12345.@OutputOnly
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="managedCertificate")
    def managed_certificate(self) -> Optional[pulumi.Input['ManagedCertificateArgs']]:
        """
        Only applicable if this certificate is managed by App Engine. Managed certificates are tied to the lifecycle of a DomainMapping and cannot be updated or deleted via the AuthorizedCertificates API. If this certificate is manually administered by the user, this field will be empty.@OutputOnly
        """
        return pulumi.get(self, "managed_certificate")

    @managed_certificate.setter
    def managed_certificate(self, value: Optional[pulumi.Input['ManagedCertificateArgs']]):
        pulumi.set(self, "managed_certificate", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Full path to the AuthorizedCertificate resource in the API. Example: apps/myapp/authorizedCertificates/12345.@OutputOnly
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="visibleDomainMappings")
    def visible_domain_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The full paths to user visible Domain Mapping resources that have this certificate mapped. Example: apps/myapp/domainMappings/example.com.This may not represent the full list of mapped domain mappings if the user does not have VIEWER permissions on all of the applications that have this certificate mapped. See domain_mappings_count for a complete count.Only returned by GET or LIST requests when specifically requested by the view=FULL_CERTIFICATE option.@OutputOnly
        """
        return pulumi.get(self, "visible_domain_mappings")

    @visible_domain_mappings.setter
    def visible_domain_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "visible_domain_mappings", value)


class AppAuthorizedCertificate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 apps_id: Optional[pulumi.Input[str]] = None,
                 authorized_certificates_id: Optional[pulumi.Input[str]] = None,
                 certificate_raw_data: Optional[pulumi.Input[pulumi.InputType['CertificateRawDataArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 domain_mappings_count: Optional[pulumi.Input[int]] = None,
                 domain_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 expire_time: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 managed_certificate: Optional[pulumi.Input[pulumi.InputType['ManagedCertificateArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 visible_domain_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Uploads the specified SSL certificate.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['CertificateRawDataArgs']] certificate_raw_data: The SSL certificate serving the AuthorizedCertificate resource. This must be obtained independently from a certificate authority.
        :param pulumi.Input[str] display_name: The user-specified display name of the certificate. This is not guaranteed to be unique. Example: My Certificate.
        :param pulumi.Input[int] domain_mappings_count: Aggregate count of the domain mappings with this certificate mapped. This count includes domain mappings on applications for which the user does not have VIEWER permissions.Only returned by GET or LIST requests when specifically requested by the view=FULL_CERTIFICATE option.@OutputOnly
        :param pulumi.Input[Sequence[pulumi.Input[str]]] domain_names: Topmost applicable domains of this certificate. This certificate applies to these domains and their subdomains. Example: example.com.@OutputOnly
        :param pulumi.Input[str] expire_time: The time when this certificate expires. To update the renewal time on this certificate, upload an SSL certificate with a different expiration time using AuthorizedCertificates.UpdateAuthorizedCertificate.@OutputOnly
        :param pulumi.Input[str] id: Relative name of the certificate. This is a unique value autogenerated on AuthorizedCertificate resource creation. Example: 12345.@OutputOnly
        :param pulumi.Input[pulumi.InputType['ManagedCertificateArgs']] managed_certificate: Only applicable if this certificate is managed by App Engine. Managed certificates are tied to the lifecycle of a DomainMapping and cannot be updated or deleted via the AuthorizedCertificates API. If this certificate is manually administered by the user, this field will be empty.@OutputOnly
        :param pulumi.Input[str] name: Full path to the AuthorizedCertificate resource in the API. Example: apps/myapp/authorizedCertificates/12345.@OutputOnly
        :param pulumi.Input[Sequence[pulumi.Input[str]]] visible_domain_mappings: The full paths to user visible Domain Mapping resources that have this certificate mapped. Example: apps/myapp/domainMappings/example.com.This may not represent the full list of mapped domain mappings if the user does not have VIEWER permissions on all of the applications that have this certificate mapped. See domain_mappings_count for a complete count.Only returned by GET or LIST requests when specifically requested by the view=FULL_CERTIFICATE option.@OutputOnly
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AppAuthorizedCertificateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Uploads the specified SSL certificate.

        :param str resource_name: The name of the resource.
        :param AppAuthorizedCertificateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AppAuthorizedCertificateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 apps_id: Optional[pulumi.Input[str]] = None,
                 authorized_certificates_id: Optional[pulumi.Input[str]] = None,
                 certificate_raw_data: Optional[pulumi.Input[pulumi.InputType['CertificateRawDataArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 domain_mappings_count: Optional[pulumi.Input[int]] = None,
                 domain_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 expire_time: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 managed_certificate: Optional[pulumi.Input[pulumi.InputType['ManagedCertificateArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 visible_domain_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
            __props__ = AppAuthorizedCertificateArgs.__new__(AppAuthorizedCertificateArgs)

            if apps_id is None and not opts.urn:
                raise TypeError("Missing required property 'apps_id'")
            __props__.__dict__["apps_id"] = apps_id
            if authorized_certificates_id is None and not opts.urn:
                raise TypeError("Missing required property 'authorized_certificates_id'")
            __props__.__dict__["authorized_certificates_id"] = authorized_certificates_id
            __props__.__dict__["certificate_raw_data"] = certificate_raw_data
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["domain_mappings_count"] = domain_mappings_count
            __props__.__dict__["domain_names"] = domain_names
            __props__.__dict__["expire_time"] = expire_time
            __props__.__dict__["id"] = id
            __props__.__dict__["managed_certificate"] = managed_certificate
            __props__.__dict__["name"] = name
            __props__.__dict__["visible_domain_mappings"] = visible_domain_mappings
        super(AppAuthorizedCertificate, __self__).__init__(
            'google-native:appengine/v1:AppAuthorizedCertificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AppAuthorizedCertificate':
        """
        Get an existing AppAuthorizedCertificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AppAuthorizedCertificateArgs.__new__(AppAuthorizedCertificateArgs)

        __props__.__dict__["certificate_raw_data"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["domain_mappings_count"] = None
        __props__.__dict__["domain_names"] = None
        __props__.__dict__["expire_time"] = None
        __props__.__dict__["managed_certificate"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["visible_domain_mappings"] = None
        return AppAuthorizedCertificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="certificateRawData")
    def certificate_raw_data(self) -> pulumi.Output['outputs.CertificateRawDataResponse']:
        """
        The SSL certificate serving the AuthorizedCertificate resource. This must be obtained independently from a certificate authority.
        """
        return pulumi.get(self, "certificate_raw_data")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The user-specified display name of the certificate. This is not guaranteed to be unique. Example: My Certificate.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="domainMappingsCount")
    def domain_mappings_count(self) -> pulumi.Output[int]:
        """
        Aggregate count of the domain mappings with this certificate mapped. This count includes domain mappings on applications for which the user does not have VIEWER permissions.Only returned by GET or LIST requests when specifically requested by the view=FULL_CERTIFICATE option.@OutputOnly
        """
        return pulumi.get(self, "domain_mappings_count")

    @property
    @pulumi.getter(name="domainNames")
    def domain_names(self) -> pulumi.Output[Sequence[str]]:
        """
        Topmost applicable domains of this certificate. This certificate applies to these domains and their subdomains. Example: example.com.@OutputOnly
        """
        return pulumi.get(self, "domain_names")

    @property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> pulumi.Output[str]:
        """
        The time when this certificate expires. To update the renewal time on this certificate, upload an SSL certificate with a different expiration time using AuthorizedCertificates.UpdateAuthorizedCertificate.@OutputOnly
        """
        return pulumi.get(self, "expire_time")

    @property
    @pulumi.getter(name="managedCertificate")
    def managed_certificate(self) -> pulumi.Output['outputs.ManagedCertificateResponse']:
        """
        Only applicable if this certificate is managed by App Engine. Managed certificates are tied to the lifecycle of a DomainMapping and cannot be updated or deleted via the AuthorizedCertificates API. If this certificate is manually administered by the user, this field will be empty.@OutputOnly
        """
        return pulumi.get(self, "managed_certificate")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Full path to the AuthorizedCertificate resource in the API. Example: apps/myapp/authorizedCertificates/12345.@OutputOnly
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="visibleDomainMappings")
    def visible_domain_mappings(self) -> pulumi.Output[Sequence[str]]:
        """
        The full paths to user visible Domain Mapping resources that have this certificate mapped. Example: apps/myapp/domainMappings/example.com.This may not represent the full list of mapped domain mappings if the user does not have VIEWER permissions on all of the applications that have this certificate mapped. See domain_mappings_count for a complete count.Only returned by GET or LIST requests when specifically requested by the view=FULL_CERTIFICATE option.@OutputOnly
        """
        return pulumi.get(self, "visible_domain_mappings")

