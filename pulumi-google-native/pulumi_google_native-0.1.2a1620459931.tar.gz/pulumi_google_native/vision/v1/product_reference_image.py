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

__all__ = ['ProductReferenceImageArgs', 'ProductReferenceImage']

@pulumi.input_type
class ProductReferenceImageArgs:
    def __init__(__self__, *,
                 locations_id: pulumi.Input[str],
                 products_id: pulumi.Input[str],
                 projects_id: pulumi.Input[str],
                 reference_images_id: pulumi.Input[str],
                 bounding_polys: Optional[pulumi.Input[Sequence[pulumi.Input['BoundingPolyArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 uri: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ProductReferenceImage resource.
        :param pulumi.Input[Sequence[pulumi.Input['BoundingPolyArgs']]] bounding_polys: Optional. Bounding polygons around the areas of interest in the reference image. If this field is empty, the system will try to detect regions of interest. At most 10 bounding polygons will be used. The provided shape is converted into a non-rotated rectangle. Once converted, the small edge of the rectangle must be greater than or equal to 300 pixels. The aspect ratio must be 1:4 or less (i.e. 1:3 is ok; 1:5 is not).
        :param pulumi.Input[str] name: The resource name of the reference image. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID/referenceImages/IMAGE_ID`. This field is ignored when creating a reference image.
        :param pulumi.Input[str] uri: Required. The Google Cloud Storage URI of the reference image. The URI must start with `gs://`.
        """
        pulumi.set(__self__, "locations_id", locations_id)
        pulumi.set(__self__, "products_id", products_id)
        pulumi.set(__self__, "projects_id", projects_id)
        pulumi.set(__self__, "reference_images_id", reference_images_id)
        if bounding_polys is not None:
            pulumi.set(__self__, "bounding_polys", bounding_polys)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if uri is not None:
            pulumi.set(__self__, "uri", uri)

    @property
    @pulumi.getter(name="locationsId")
    def locations_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "locations_id")

    @locations_id.setter
    def locations_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "locations_id", value)

    @property
    @pulumi.getter(name="productsId")
    def products_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "products_id")

    @products_id.setter
    def products_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "products_id", value)

    @property
    @pulumi.getter(name="projectsId")
    def projects_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "projects_id")

    @projects_id.setter
    def projects_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "projects_id", value)

    @property
    @pulumi.getter(name="referenceImagesId")
    def reference_images_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "reference_images_id")

    @reference_images_id.setter
    def reference_images_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "reference_images_id", value)

    @property
    @pulumi.getter(name="boundingPolys")
    def bounding_polys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BoundingPolyArgs']]]]:
        """
        Optional. Bounding polygons around the areas of interest in the reference image. If this field is empty, the system will try to detect regions of interest. At most 10 bounding polygons will be used. The provided shape is converted into a non-rotated rectangle. Once converted, the small edge of the rectangle must be greater than or equal to 300 pixels. The aspect ratio must be 1:4 or less (i.e. 1:3 is ok; 1:5 is not).
        """
        return pulumi.get(self, "bounding_polys")

    @bounding_polys.setter
    def bounding_polys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BoundingPolyArgs']]]]):
        pulumi.set(self, "bounding_polys", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name of the reference image. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID/referenceImages/IMAGE_ID`. This field is ignored when creating a reference image.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[str]]:
        """
        Required. The Google Cloud Storage URI of the reference image. The URI must start with `gs://`.
        """
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uri", value)


class ProductReferenceImage(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bounding_polys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BoundingPolyArgs']]]]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 products_id: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 reference_images_id: Optional[pulumi.Input[str]] = None,
                 uri: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates and returns a new ReferenceImage resource. The `bounding_poly` field is optional. If `bounding_poly` is not specified, the system will try to detect regions of interest in the image that are compatible with the product_category on the parent product. If it is specified, detection is ALWAYS skipped. The system converts polygons into non-rotated rectangles. Note that the pipeline will resize the image if the image resolution is too large to process (above 50MP). Possible errors: * Returns INVALID_ARGUMENT if the image_uri is missing or longer than 4096 characters. * Returns INVALID_ARGUMENT if the product does not exist. * Returns INVALID_ARGUMENT if bounding_poly is not provided, and nothing compatible with the parent product's product_category is detected. * Returns INVALID_ARGUMENT if bounding_poly contains more than 10 polygons.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BoundingPolyArgs']]]] bounding_polys: Optional. Bounding polygons around the areas of interest in the reference image. If this field is empty, the system will try to detect regions of interest. At most 10 bounding polygons will be used. The provided shape is converted into a non-rotated rectangle. Once converted, the small edge of the rectangle must be greater than or equal to 300 pixels. The aspect ratio must be 1:4 or less (i.e. 1:3 is ok; 1:5 is not).
        :param pulumi.Input[str] name: The resource name of the reference image. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID/referenceImages/IMAGE_ID`. This field is ignored when creating a reference image.
        :param pulumi.Input[str] uri: Required. The Google Cloud Storage URI of the reference image. The URI must start with `gs://`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProductReferenceImageArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates and returns a new ReferenceImage resource. The `bounding_poly` field is optional. If `bounding_poly` is not specified, the system will try to detect regions of interest in the image that are compatible with the product_category on the parent product. If it is specified, detection is ALWAYS skipped. The system converts polygons into non-rotated rectangles. Note that the pipeline will resize the image if the image resolution is too large to process (above 50MP). Possible errors: * Returns INVALID_ARGUMENT if the image_uri is missing or longer than 4096 characters. * Returns INVALID_ARGUMENT if the product does not exist. * Returns INVALID_ARGUMENT if bounding_poly is not provided, and nothing compatible with the parent product's product_category is detected. * Returns INVALID_ARGUMENT if bounding_poly contains more than 10 polygons.

        :param str resource_name: The name of the resource.
        :param ProductReferenceImageArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProductReferenceImageArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bounding_polys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BoundingPolyArgs']]]]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 products_id: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 reference_images_id: Optional[pulumi.Input[str]] = None,
                 uri: Optional[pulumi.Input[str]] = None,
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
            __props__ = ProductReferenceImageArgs.__new__(ProductReferenceImageArgs)

            __props__.__dict__["bounding_polys"] = bounding_polys
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__.__dict__["locations_id"] = locations_id
            __props__.__dict__["name"] = name
            if products_id is None and not opts.urn:
                raise TypeError("Missing required property 'products_id'")
            __props__.__dict__["products_id"] = products_id
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__.__dict__["projects_id"] = projects_id
            if reference_images_id is None and not opts.urn:
                raise TypeError("Missing required property 'reference_images_id'")
            __props__.__dict__["reference_images_id"] = reference_images_id
            __props__.__dict__["uri"] = uri
        super(ProductReferenceImage, __self__).__init__(
            'google-native:vision/v1:ProductReferenceImage',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ProductReferenceImage':
        """
        Get an existing ProductReferenceImage resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ProductReferenceImageArgs.__new__(ProductReferenceImageArgs)

        __props__.__dict__["bounding_polys"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["uri"] = None
        return ProductReferenceImage(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="boundingPolys")
    def bounding_polys(self) -> pulumi.Output[Sequence['outputs.BoundingPolyResponse']]:
        """
        Optional. Bounding polygons around the areas of interest in the reference image. If this field is empty, the system will try to detect regions of interest. At most 10 bounding polygons will be used. The provided shape is converted into a non-rotated rectangle. Once converted, the small edge of the rectangle must be greater than or equal to 300 pixels. The aspect ratio must be 1:4 or less (i.e. 1:3 is ok; 1:5 is not).
        """
        return pulumi.get(self, "bounding_polys")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the reference image. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID/referenceImages/IMAGE_ID`. This field is ignored when creating a reference image.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def uri(self) -> pulumi.Output[str]:
        """
        Required. The Google Cloud Storage URI of the reference image. The URI must start with `gs://`.
        """
        return pulumi.get(self, "uri")

