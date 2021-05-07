# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'RepositoryCatalogData',
]

@pulumi.output_type
class RepositoryCatalogData(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "aboutText":
            suggest = "about_text"
        elif key == "logoImageBlob":
            suggest = "logo_image_blob"
        elif key == "operatingSystems":
            suggest = "operating_systems"
        elif key == "usageText":
            suggest = "usage_text"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RepositoryCatalogData. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RepositoryCatalogData.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RepositoryCatalogData.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 about_text: Optional[str] = None,
                 architectures: Optional[Sequence[str]] = None,
                 description: Optional[str] = None,
                 logo_image_blob: Optional[str] = None,
                 operating_systems: Optional[Sequence[str]] = None,
                 usage_text: Optional[str] = None):
        """
        :param str about_text: A detailed description of the contents of the repository. It is publicly visible in the Amazon ECR Public Gallery. The text must be in markdown format.
        :param Sequence[str] architectures: The system architecture that the images in the repository are compatible with. On the Amazon ECR Public Gallery, the following supported architectures will appear as badges on the repository and are used as search filters: `Linux`, `Windows`
        :param str description: A short description of the contents of the repository. This text appears in both the image details and also when searching for repositories on the Amazon ECR Public Gallery.
        :param str logo_image_blob: The base64-encoded repository logo payload. (Only visible for verified accounts) Note that drift detection is disabled for this attribute.
        :param Sequence[str] operating_systems: The operating systems that the images in the repository are compatible with. On the Amazon ECR Public Gallery, the following supported operating systems will appear as badges on the repository and are used as search filters. `ARM`, `ARM 64`, `x86`, `x86-64`
        :param str usage_text: Detailed information on how to use the contents of the repository. It is publicly visible in the Amazon ECR Public Gallery. The usage text provides context, support information, and additional usage details for users of the repository. The text must be in markdown format.
        """
        if about_text is not None:
            pulumi.set(__self__, "about_text", about_text)
        if architectures is not None:
            pulumi.set(__self__, "architectures", architectures)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if logo_image_blob is not None:
            pulumi.set(__self__, "logo_image_blob", logo_image_blob)
        if operating_systems is not None:
            pulumi.set(__self__, "operating_systems", operating_systems)
        if usage_text is not None:
            pulumi.set(__self__, "usage_text", usage_text)

    @property
    @pulumi.getter(name="aboutText")
    def about_text(self) -> Optional[str]:
        """
        A detailed description of the contents of the repository. It is publicly visible in the Amazon ECR Public Gallery. The text must be in markdown format.
        """
        return pulumi.get(self, "about_text")

    @property
    @pulumi.getter
    def architectures(self) -> Optional[Sequence[str]]:
        """
        The system architecture that the images in the repository are compatible with. On the Amazon ECR Public Gallery, the following supported architectures will appear as badges on the repository and are used as search filters: `Linux`, `Windows`
        """
        return pulumi.get(self, "architectures")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A short description of the contents of the repository. This text appears in both the image details and also when searching for repositories on the Amazon ECR Public Gallery.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="logoImageBlob")
    def logo_image_blob(self) -> Optional[str]:
        """
        The base64-encoded repository logo payload. (Only visible for verified accounts) Note that drift detection is disabled for this attribute.
        """
        return pulumi.get(self, "logo_image_blob")

    @property
    @pulumi.getter(name="operatingSystems")
    def operating_systems(self) -> Optional[Sequence[str]]:
        """
        The operating systems that the images in the repository are compatible with. On the Amazon ECR Public Gallery, the following supported operating systems will appear as badges on the repository and are used as search filters. `ARM`, `ARM 64`, `x86`, `x86-64`
        """
        return pulumi.get(self, "operating_systems")

    @property
    @pulumi.getter(name="usageText")
    def usage_text(self) -> Optional[str]:
        """
        Detailed information on how to use the contents of the repository. It is publicly visible in the Amazon ECR Public Gallery. The usage text provides context, support information, and additional usage details for users of the repository. The text must be in markdown format.
        """
        return pulumi.get(self, "usage_text")


