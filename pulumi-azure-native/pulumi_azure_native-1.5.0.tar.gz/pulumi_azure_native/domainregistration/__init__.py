# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .domain import *
from .domain_ownership_identifier import *
from .get_domain import *
from .get_domain_ownership_identifier import *
from .list_domain_recommendations import *
from .list_top_level_domain_agreements import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.domainregistration.v20150401 as v20150401
    import pulumi_azure_native.domainregistration.v20180201 as v20180201
    import pulumi_azure_native.domainregistration.v20190801 as v20190801
    import pulumi_azure_native.domainregistration.v20200601 as v20200601
    import pulumi_azure_native.domainregistration.v20200901 as v20200901
    import pulumi_azure_native.domainregistration.v20201001 as v20201001
    import pulumi_azure_native.domainregistration.v20201201 as v20201201
else:
    v20150401 = _utilities.lazy_import('pulumi_azure_native.domainregistration.v20150401')
    v20180201 = _utilities.lazy_import('pulumi_azure_native.domainregistration.v20180201')
    v20190801 = _utilities.lazy_import('pulumi_azure_native.domainregistration.v20190801')
    v20200601 = _utilities.lazy_import('pulumi_azure_native.domainregistration.v20200601')
    v20200901 = _utilities.lazy_import('pulumi_azure_native.domainregistration.v20200901')
    v20201001 = _utilities.lazy_import('pulumi_azure_native.domainregistration.v20201001')
    v20201201 = _utilities.lazy_import('pulumi_azure_native.domainregistration.v20201201')

