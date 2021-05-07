# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .account import *
from .api_key import *
from .authorizer import *
from .base_path_mapping import *
from .client_certificate import *
from .deployment import *
from .documentation_part import *
from .documentation_version import *
from .domain_name import *
from .get_domain_name import *
from .get_key import *
from .get_resource import *
from .get_rest_api import *
from .get_vpc_link import *
from .integration import *
from .integration_response import *
from .method import *
from .method_response import *
from .method_settings import *
from .model import *
from .request_validator import *
from .resource import *
from .response import *
from .rest_api import *
from .rest_api_policy import *
from .stage import *
from .usage_plan import *
from .usage_plan_key import *
from .vpc_link import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "aws:apigateway/account:Account":
                return Account(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:apigateway/apiKey:ApiKey":
                return ApiKey(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:apigateway/authorizer:Authorizer":
                return Authorizer(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:apigateway/basePathMapping:BasePathMapping":
                return BasePathMapping(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:apigateway/clientCertificate:ClientCertificate":
                return ClientCertificate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:apigateway/deployment:Deployment":
                return Deployment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:apigateway/documentationPart:DocumentationPart":
                return DocumentationPart(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:apigateway/documentationVersion:DocumentationVersion":
                return DocumentationVersion(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:apigateway/domainName:DomainName":
                return DomainName(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:apigateway/integration:Integration":
                return Integration(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:apigateway/integrationResponse:IntegrationResponse":
                return IntegrationResponse(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:apigateway/method:Method":
                return Method(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:apigateway/methodResponse:MethodResponse":
                return MethodResponse(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:apigateway/methodSettings:MethodSettings":
                return MethodSettings(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:apigateway/model:Model":
                return Model(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:apigateway/requestValidator:RequestValidator":
                return RequestValidator(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:apigateway/resource:Resource":
                return Resource(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:apigateway/response:Response":
                return Response(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:apigateway/restApi:RestApi":
                return RestApi(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:apigateway/restApiPolicy:RestApiPolicy":
                return RestApiPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:apigateway/stage:Stage":
                return Stage(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:apigateway/usagePlan:UsagePlan":
                return UsagePlan(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:apigateway/usagePlanKey:UsagePlanKey":
                return UsagePlanKey(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:apigateway/vpcLink:VpcLink":
                return VpcLink(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("aws", "apigateway/account", _module_instance)
    pulumi.runtime.register_resource_module("aws", "apigateway/apiKey", _module_instance)
    pulumi.runtime.register_resource_module("aws", "apigateway/authorizer", _module_instance)
    pulumi.runtime.register_resource_module("aws", "apigateway/basePathMapping", _module_instance)
    pulumi.runtime.register_resource_module("aws", "apigateway/clientCertificate", _module_instance)
    pulumi.runtime.register_resource_module("aws", "apigateway/deployment", _module_instance)
    pulumi.runtime.register_resource_module("aws", "apigateway/documentationPart", _module_instance)
    pulumi.runtime.register_resource_module("aws", "apigateway/documentationVersion", _module_instance)
    pulumi.runtime.register_resource_module("aws", "apigateway/domainName", _module_instance)
    pulumi.runtime.register_resource_module("aws", "apigateway/integration", _module_instance)
    pulumi.runtime.register_resource_module("aws", "apigateway/integrationResponse", _module_instance)
    pulumi.runtime.register_resource_module("aws", "apigateway/method", _module_instance)
    pulumi.runtime.register_resource_module("aws", "apigateway/methodResponse", _module_instance)
    pulumi.runtime.register_resource_module("aws", "apigateway/methodSettings", _module_instance)
    pulumi.runtime.register_resource_module("aws", "apigateway/model", _module_instance)
    pulumi.runtime.register_resource_module("aws", "apigateway/requestValidator", _module_instance)
    pulumi.runtime.register_resource_module("aws", "apigateway/resource", _module_instance)
    pulumi.runtime.register_resource_module("aws", "apigateway/response", _module_instance)
    pulumi.runtime.register_resource_module("aws", "apigateway/restApi", _module_instance)
    pulumi.runtime.register_resource_module("aws", "apigateway/restApiPolicy", _module_instance)
    pulumi.runtime.register_resource_module("aws", "apigateway/stage", _module_instance)
    pulumi.runtime.register_resource_module("aws", "apigateway/usagePlan", _module_instance)
    pulumi.runtime.register_resource_module("aws", "apigateway/usagePlanKey", _module_instance)
    pulumi.runtime.register_resource_module("aws", "apigateway/vpcLink", _module_instance)

_register_module()
