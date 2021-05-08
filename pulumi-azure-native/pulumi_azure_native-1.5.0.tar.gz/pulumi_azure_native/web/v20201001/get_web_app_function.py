# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetWebAppFunctionResult',
    'AwaitableGetWebAppFunctionResult',
    'get_web_app_function',
]

@pulumi.output_type
class GetWebAppFunctionResult:
    """
    Function information.
    """
    def __init__(__self__, config=None, config_href=None, files=None, function_app_id=None, href=None, id=None, invoke_url_template=None, is_disabled=None, kind=None, language=None, name=None, script_href=None, script_root_path_href=None, secrets_file_href=None, system_data=None, test_data=None, test_data_href=None, type=None):
        if config and not isinstance(config, dict):
            raise TypeError("Expected argument 'config' to be a dict")
        pulumi.set(__self__, "config", config)
        if config_href and not isinstance(config_href, str):
            raise TypeError("Expected argument 'config_href' to be a str")
        pulumi.set(__self__, "config_href", config_href)
        if files and not isinstance(files, dict):
            raise TypeError("Expected argument 'files' to be a dict")
        pulumi.set(__self__, "files", files)
        if function_app_id and not isinstance(function_app_id, str):
            raise TypeError("Expected argument 'function_app_id' to be a str")
        pulumi.set(__self__, "function_app_id", function_app_id)
        if href and not isinstance(href, str):
            raise TypeError("Expected argument 'href' to be a str")
        pulumi.set(__self__, "href", href)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if invoke_url_template and not isinstance(invoke_url_template, str):
            raise TypeError("Expected argument 'invoke_url_template' to be a str")
        pulumi.set(__self__, "invoke_url_template", invoke_url_template)
        if is_disabled and not isinstance(is_disabled, bool):
            raise TypeError("Expected argument 'is_disabled' to be a bool")
        pulumi.set(__self__, "is_disabled", is_disabled)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if language and not isinstance(language, str):
            raise TypeError("Expected argument 'language' to be a str")
        pulumi.set(__self__, "language", language)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if script_href and not isinstance(script_href, str):
            raise TypeError("Expected argument 'script_href' to be a str")
        pulumi.set(__self__, "script_href", script_href)
        if script_root_path_href and not isinstance(script_root_path_href, str):
            raise TypeError("Expected argument 'script_root_path_href' to be a str")
        pulumi.set(__self__, "script_root_path_href", script_root_path_href)
        if secrets_file_href and not isinstance(secrets_file_href, str):
            raise TypeError("Expected argument 'secrets_file_href' to be a str")
        pulumi.set(__self__, "secrets_file_href", secrets_file_href)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if test_data and not isinstance(test_data, str):
            raise TypeError("Expected argument 'test_data' to be a str")
        pulumi.set(__self__, "test_data", test_data)
        if test_data_href and not isinstance(test_data_href, str):
            raise TypeError("Expected argument 'test_data_href' to be a str")
        pulumi.set(__self__, "test_data_href", test_data_href)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def config(self) -> Optional[Any]:
        """
        Config information.
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter(name="configHref")
    def config_href(self) -> Optional[str]:
        """
        Config URI.
        """
        return pulumi.get(self, "config_href")

    @property
    @pulumi.getter
    def files(self) -> Optional[Mapping[str, str]]:
        """
        File list.
        """
        return pulumi.get(self, "files")

    @property
    @pulumi.getter(name="functionAppId")
    def function_app_id(self) -> Optional[str]:
        """
        Function App ID.
        """
        return pulumi.get(self, "function_app_id")

    @property
    @pulumi.getter
    def href(self) -> Optional[str]:
        """
        Function URI.
        """
        return pulumi.get(self, "href")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="invokeUrlTemplate")
    def invoke_url_template(self) -> Optional[str]:
        """
        The invocation URL
        """
        return pulumi.get(self, "invoke_url_template")

    @property
    @pulumi.getter(name="isDisabled")
    def is_disabled(self) -> Optional[bool]:
        """
        Gets or sets a value indicating whether the function is disabled
        """
        return pulumi.get(self, "is_disabled")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def language(self) -> Optional[str]:
        """
        The function language
        """
        return pulumi.get(self, "language")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="scriptHref")
    def script_href(self) -> Optional[str]:
        """
        Script URI.
        """
        return pulumi.get(self, "script_href")

    @property
    @pulumi.getter(name="scriptRootPathHref")
    def script_root_path_href(self) -> Optional[str]:
        """
        Script root path URI.
        """
        return pulumi.get(self, "script_root_path_href")

    @property
    @pulumi.getter(name="secretsFileHref")
    def secrets_file_href(self) -> Optional[str]:
        """
        Secrets file URI.
        """
        return pulumi.get(self, "secrets_file_href")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="testData")
    def test_data(self) -> Optional[str]:
        """
        Test data used when testing via the Azure Portal.
        """
        return pulumi.get(self, "test_data")

    @property
    @pulumi.getter(name="testDataHref")
    def test_data_href(self) -> Optional[str]:
        """
        Test data URI.
        """
        return pulumi.get(self, "test_data_href")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetWebAppFunctionResult(GetWebAppFunctionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWebAppFunctionResult(
            config=self.config,
            config_href=self.config_href,
            files=self.files,
            function_app_id=self.function_app_id,
            href=self.href,
            id=self.id,
            invoke_url_template=self.invoke_url_template,
            is_disabled=self.is_disabled,
            kind=self.kind,
            language=self.language,
            name=self.name,
            script_href=self.script_href,
            script_root_path_href=self.script_root_path_href,
            secrets_file_href=self.secrets_file_href,
            system_data=self.system_data,
            test_data=self.test_data,
            test_data_href=self.test_data_href,
            type=self.type)


def get_web_app_function(function_name: Optional[str] = None,
                         name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWebAppFunctionResult:
    """
    Function information.


    :param str function_name: Function name.
    :param str name: Site name.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    __args__ = dict()
    __args__['functionName'] = function_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:web/v20201001:getWebAppFunction', __args__, opts=opts, typ=GetWebAppFunctionResult).value

    return AwaitableGetWebAppFunctionResult(
        config=__ret__.config,
        config_href=__ret__.config_href,
        files=__ret__.files,
        function_app_id=__ret__.function_app_id,
        href=__ret__.href,
        id=__ret__.id,
        invoke_url_template=__ret__.invoke_url_template,
        is_disabled=__ret__.is_disabled,
        kind=__ret__.kind,
        language=__ret__.language,
        name=__ret__.name,
        script_href=__ret__.script_href,
        script_root_path_href=__ret__.script_root_path_href,
        secrets_file_href=__ret__.secrets_file_href,
        system_data=__ret__.system_data,
        test_data=__ret__.test_data,
        test_data_href=__ret__.test_data_href,
        type=__ret__.type)
