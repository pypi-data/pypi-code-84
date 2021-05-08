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

__all__ = ['ExecutionArgs', 'Execution']

@pulumi.input_type
class ExecutionArgs:
    def __init__(__self__, *,
                 executions_id: pulumi.Input[str],
                 locations_id: pulumi.Input[str],
                 projects_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 execution_template: Optional[pulumi.Input['ExecutionTemplateArgs']] = None,
                 output_notebook_file: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Execution resource.
        :param pulumi.Input[str] description: A brief description of this execution.
        :param pulumi.Input['ExecutionTemplateArgs'] execution_template: execute metadata including name, hardware spec, region, labels, etc.
        :param pulumi.Input[str] output_notebook_file: Output notebook file generated by this execution
        """
        pulumi.set(__self__, "executions_id", executions_id)
        pulumi.set(__self__, "locations_id", locations_id)
        pulumi.set(__self__, "projects_id", projects_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if execution_template is not None:
            pulumi.set(__self__, "execution_template", execution_template)
        if output_notebook_file is not None:
            pulumi.set(__self__, "output_notebook_file", output_notebook_file)

    @property
    @pulumi.getter(name="executionsId")
    def executions_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "executions_id")

    @executions_id.setter
    def executions_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "executions_id", value)

    @property
    @pulumi.getter(name="locationsId")
    def locations_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "locations_id")

    @locations_id.setter
    def locations_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "locations_id", value)

    @property
    @pulumi.getter(name="projectsId")
    def projects_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "projects_id")

    @projects_id.setter
    def projects_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "projects_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A brief description of this execution.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="executionTemplate")
    def execution_template(self) -> Optional[pulumi.Input['ExecutionTemplateArgs']]:
        """
        execute metadata including name, hardware spec, region, labels, etc.
        """
        return pulumi.get(self, "execution_template")

    @execution_template.setter
    def execution_template(self, value: Optional[pulumi.Input['ExecutionTemplateArgs']]):
        pulumi.set(self, "execution_template", value)

    @property
    @pulumi.getter(name="outputNotebookFile")
    def output_notebook_file(self) -> Optional[pulumi.Input[str]]:
        """
        Output notebook file generated by this execution
        """
        return pulumi.get(self, "output_notebook_file")

    @output_notebook_file.setter
    def output_notebook_file(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "output_notebook_file", value)


class Execution(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 execution_template: Optional[pulumi.Input[pulumi.InputType['ExecutionTemplateArgs']]] = None,
                 executions_id: Optional[pulumi.Input[str]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 output_notebook_file: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new Scheduled Notebook in a given project and location.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A brief description of this execution.
        :param pulumi.Input[pulumi.InputType['ExecutionTemplateArgs']] execution_template: execute metadata including name, hardware spec, region, labels, etc.
        :param pulumi.Input[str] output_notebook_file: Output notebook file generated by this execution
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExecutionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new Scheduled Notebook in a given project and location.

        :param str resource_name: The name of the resource.
        :param ExecutionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExecutionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 execution_template: Optional[pulumi.Input[pulumi.InputType['ExecutionTemplateArgs']]] = None,
                 executions_id: Optional[pulumi.Input[str]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 output_notebook_file: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = ExecutionArgs.__new__(ExecutionArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["execution_template"] = execution_template
            if executions_id is None and not opts.urn:
                raise TypeError("Missing required property 'executions_id'")
            __props__.__dict__["executions_id"] = executions_id
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__.__dict__["locations_id"] = locations_id
            __props__.__dict__["output_notebook_file"] = output_notebook_file
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__.__dict__["projects_id"] = projects_id
            __props__.__dict__["create_time"] = None
            __props__.__dict__["display_name"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["update_time"] = None
        super(Execution, __self__).__init__(
            'google-native:notebooks/v1:Execution',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Execution':
        """
        Get an existing Execution resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ExecutionArgs.__new__(ExecutionArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["execution_template"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["output_notebook_file"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["update_time"] = None
        return Execution(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Time the Execution was instantiated.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        A brief description of this execution.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Name used for UI purposes. Name can only contain alphanumeric characters and underscores '_'.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="executionTemplate")
    def execution_template(self) -> pulumi.Output['outputs.ExecutionTemplateResponse']:
        """
        execute metadata including name, hardware spec, region, labels, etc.
        """
        return pulumi.get(self, "execution_template")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the execute. Format: `projects/{project_id}/locations/{location}/execution/{execution_id}
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="outputNotebookFile")
    def output_notebook_file(self) -> pulumi.Output[str]:
        """
        Output notebook file generated by this execution
        """
        return pulumi.get(self, "output_notebook_file")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        State of the underlying AI Platform job.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Time the Execution was last updated.
        """
        return pulumi.get(self, "update_time")

