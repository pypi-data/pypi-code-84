# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from .get_service import *
from .service import *

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.windowsiot.v20180216preview as v20180216preview
    import pulumi_azure_native.windowsiot.v20190601 as v20190601
else:
    v20180216preview = _utilities.lazy_import('pulumi_azure_native.windowsiot.v20180216preview')
    v20190601 = _utilities.lazy_import('pulumi_azure_native.windowsiot.v20190601')

