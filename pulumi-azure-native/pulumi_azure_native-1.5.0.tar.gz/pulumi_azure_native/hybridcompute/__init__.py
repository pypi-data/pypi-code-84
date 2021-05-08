# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .get_machine import *
from .get_machine_extension import *
from .get_private_endpoint_connection import *
from .get_private_link_scope import *
from .get_private_link_scoped_resource import *
from .machine import *
from .machine_extension import *
from .private_endpoint_connection import *
from .private_link_scope import *
from .private_link_scoped_resource import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.hybridcompute.v20190318preview as v20190318preview
    import pulumi_azure_native.hybridcompute.v20190802preview as v20190802preview
    import pulumi_azure_native.hybridcompute.v20191212 as v20191212
    import pulumi_azure_native.hybridcompute.v20200730preview as v20200730preview
    import pulumi_azure_native.hybridcompute.v20200802 as v20200802
    import pulumi_azure_native.hybridcompute.v20200815preview as v20200815preview
    import pulumi_azure_native.hybridcompute.v20210128preview as v20210128preview
    import pulumi_azure_native.hybridcompute.v20210325preview as v20210325preview
else:
    v20190318preview = _utilities.lazy_import('pulumi_azure_native.hybridcompute.v20190318preview')
    v20190802preview = _utilities.lazy_import('pulumi_azure_native.hybridcompute.v20190802preview')
    v20191212 = _utilities.lazy_import('pulumi_azure_native.hybridcompute.v20191212')
    v20200730preview = _utilities.lazy_import('pulumi_azure_native.hybridcompute.v20200730preview')
    v20200802 = _utilities.lazy_import('pulumi_azure_native.hybridcompute.v20200802')
    v20200815preview = _utilities.lazy_import('pulumi_azure_native.hybridcompute.v20200815preview')
    v20210128preview = _utilities.lazy_import('pulumi_azure_native.hybridcompute.v20210128preview')
    v20210325preview = _utilities.lazy_import('pulumi_azure_native.hybridcompute.v20210325preview')

