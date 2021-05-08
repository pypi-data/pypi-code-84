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

__all__ = ['QueueTaskArgs', 'QueueTask']

@pulumi.input_type
class QueueTaskArgs:
    def __init__(__self__, *,
                 locations_id: pulumi.Input[str],
                 projects_id: pulumi.Input[str],
                 queues_id: pulumi.Input[str],
                 tasks_id: pulumi.Input[str],
                 app_engine_http_request: Optional[pulumi.Input['AppEngineHttpRequestArgs']] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pull_message: Optional[pulumi.Input['PullMessageArgs']] = None,
                 response_view: Optional[pulumi.Input[str]] = None,
                 schedule_time: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input['TaskStatusArgs']] = None,
                 view: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a QueueTask resource.
        :param pulumi.Input['AppEngineHttpRequestArgs'] app_engine_http_request: App Engine HTTP request that is sent to the task's target. Can be set only if app_engine_http_target is set on the queue. An App Engine task is a task that has AppEngineHttpRequest set.
        :param pulumi.Input[str] create_time: The time that the task was created. `create_time` will be truncated to the nearest second.
        :param pulumi.Input[str] name: Optionally caller-specified in CreateTask. The task name. The task name must have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID` * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) * `LOCATION_ID` is the canonical ID for the task's location. The list of available locations can be obtained by calling ListLocations. For more information, see https://cloud.google.com/about/locations/. * `QUEUE_ID` can contain letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). The maximum length is 100 characters. * `TASK_ID` can contain only letters ([A-Za-z]), numbers ([0-9]), hyphens (-), or underscores (_). The maximum length is 500 characters.
        :param pulumi.Input['PullMessageArgs'] pull_message: LeaseTasks to process the task. Can be set only if pull_target is set on the queue. A pull task is a task that has PullMessage set.
        :param pulumi.Input[str] response_view: The response_view specifies which subset of the Task will be returned. By default response_view is BASIC; not all information is retrieved by default because some data, such as payloads, might be desirable to return only when needed because of its large size or because of the sensitivity of data that it contains. Authorization for FULL requires `cloudtasks.tasks.fullView` [Google IAM](https://cloud.google.com/iam/) permission on the Task resource.
        :param pulumi.Input[str] schedule_time: The time when the task is scheduled to be attempted. For App Engine queues, this is when the task will be attempted or retried. For pull queues, this is the time when the task is available to be leased; if a task is currently leased, this is the time when the current lease expires, that is, the time that the task was leased plus the lease_duration. `schedule_time` will be truncated to the nearest microsecond.
        :param pulumi.Input['TaskStatusArgs'] status: The task status.
        :param pulumi.Input[str] view: The view specifies which subset of the Task has been returned.
        """
        pulumi.set(__self__, "locations_id", locations_id)
        pulumi.set(__self__, "projects_id", projects_id)
        pulumi.set(__self__, "queues_id", queues_id)
        pulumi.set(__self__, "tasks_id", tasks_id)
        if app_engine_http_request is not None:
            pulumi.set(__self__, "app_engine_http_request", app_engine_http_request)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if pull_message is not None:
            pulumi.set(__self__, "pull_message", pull_message)
        if response_view is not None:
            pulumi.set(__self__, "response_view", response_view)
        if schedule_time is not None:
            pulumi.set(__self__, "schedule_time", schedule_time)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if view is not None:
            pulumi.set(__self__, "view", view)

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
    @pulumi.getter(name="queuesId")
    def queues_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "queues_id")

    @queues_id.setter
    def queues_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "queues_id", value)

    @property
    @pulumi.getter(name="tasksId")
    def tasks_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "tasks_id")

    @tasks_id.setter
    def tasks_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "tasks_id", value)

    @property
    @pulumi.getter(name="appEngineHttpRequest")
    def app_engine_http_request(self) -> Optional[pulumi.Input['AppEngineHttpRequestArgs']]:
        """
        App Engine HTTP request that is sent to the task's target. Can be set only if app_engine_http_target is set on the queue. An App Engine task is a task that has AppEngineHttpRequest set.
        """
        return pulumi.get(self, "app_engine_http_request")

    @app_engine_http_request.setter
    def app_engine_http_request(self, value: Optional[pulumi.Input['AppEngineHttpRequestArgs']]):
        pulumi.set(self, "app_engine_http_request", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        The time that the task was created. `create_time` will be truncated to the nearest second.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Optionally caller-specified in CreateTask. The task name. The task name must have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID` * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) * `LOCATION_ID` is the canonical ID for the task's location. The list of available locations can be obtained by calling ListLocations. For more information, see https://cloud.google.com/about/locations/. * `QUEUE_ID` can contain letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). The maximum length is 100 characters. * `TASK_ID` can contain only letters ([A-Za-z]), numbers ([0-9]), hyphens (-), or underscores (_). The maximum length is 500 characters.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="pullMessage")
    def pull_message(self) -> Optional[pulumi.Input['PullMessageArgs']]:
        """
        LeaseTasks to process the task. Can be set only if pull_target is set on the queue. A pull task is a task that has PullMessage set.
        """
        return pulumi.get(self, "pull_message")

    @pull_message.setter
    def pull_message(self, value: Optional[pulumi.Input['PullMessageArgs']]):
        pulumi.set(self, "pull_message", value)

    @property
    @pulumi.getter(name="responseView")
    def response_view(self) -> Optional[pulumi.Input[str]]:
        """
        The response_view specifies which subset of the Task will be returned. By default response_view is BASIC; not all information is retrieved by default because some data, such as payloads, might be desirable to return only when needed because of its large size or because of the sensitivity of data that it contains. Authorization for FULL requires `cloudtasks.tasks.fullView` [Google IAM](https://cloud.google.com/iam/) permission on the Task resource.
        """
        return pulumi.get(self, "response_view")

    @response_view.setter
    def response_view(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "response_view", value)

    @property
    @pulumi.getter(name="scheduleTime")
    def schedule_time(self) -> Optional[pulumi.Input[str]]:
        """
        The time when the task is scheduled to be attempted. For App Engine queues, this is when the task will be attempted or retried. For pull queues, this is the time when the task is available to be leased; if a task is currently leased, this is the time when the current lease expires, that is, the time that the task was leased plus the lease_duration. `schedule_time` will be truncated to the nearest microsecond.
        """
        return pulumi.get(self, "schedule_time")

    @schedule_time.setter
    def schedule_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schedule_time", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input['TaskStatusArgs']]:
        """
        The task status.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input['TaskStatusArgs']]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def view(self) -> Optional[pulumi.Input[str]]:
        """
        The view specifies which subset of the Task has been returned.
        """
        return pulumi.get(self, "view")

    @view.setter
    def view(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "view", value)


class QueueTask(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_engine_http_request: Optional[pulumi.Input[pulumi.InputType['AppEngineHttpRequestArgs']]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 pull_message: Optional[pulumi.Input[pulumi.InputType['PullMessageArgs']]] = None,
                 queues_id: Optional[pulumi.Input[str]] = None,
                 response_view: Optional[pulumi.Input[str]] = None,
                 schedule_time: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[pulumi.InputType['TaskStatusArgs']]] = None,
                 tasks_id: Optional[pulumi.Input[str]] = None,
                 view: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a task and adds it to a queue. Tasks cannot be updated after creation; there is no UpdateTask command. * For App Engine queues, the maximum task size is 100KB. * For pull queues, the maximum task size is 1MB.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AppEngineHttpRequestArgs']] app_engine_http_request: App Engine HTTP request that is sent to the task's target. Can be set only if app_engine_http_target is set on the queue. An App Engine task is a task that has AppEngineHttpRequest set.
        :param pulumi.Input[str] create_time: The time that the task was created. `create_time` will be truncated to the nearest second.
        :param pulumi.Input[str] name: Optionally caller-specified in CreateTask. The task name. The task name must have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID` * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) * `LOCATION_ID` is the canonical ID for the task's location. The list of available locations can be obtained by calling ListLocations. For more information, see https://cloud.google.com/about/locations/. * `QUEUE_ID` can contain letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). The maximum length is 100 characters. * `TASK_ID` can contain only letters ([A-Za-z]), numbers ([0-9]), hyphens (-), or underscores (_). The maximum length is 500 characters.
        :param pulumi.Input[pulumi.InputType['PullMessageArgs']] pull_message: LeaseTasks to process the task. Can be set only if pull_target is set on the queue. A pull task is a task that has PullMessage set.
        :param pulumi.Input[str] response_view: The response_view specifies which subset of the Task will be returned. By default response_view is BASIC; not all information is retrieved by default because some data, such as payloads, might be desirable to return only when needed because of its large size or because of the sensitivity of data that it contains. Authorization for FULL requires `cloudtasks.tasks.fullView` [Google IAM](https://cloud.google.com/iam/) permission on the Task resource.
        :param pulumi.Input[str] schedule_time: The time when the task is scheduled to be attempted. For App Engine queues, this is when the task will be attempted or retried. For pull queues, this is the time when the task is available to be leased; if a task is currently leased, this is the time when the current lease expires, that is, the time that the task was leased plus the lease_duration. `schedule_time` will be truncated to the nearest microsecond.
        :param pulumi.Input[pulumi.InputType['TaskStatusArgs']] status: The task status.
        :param pulumi.Input[str] view: The view specifies which subset of the Task has been returned.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: QueueTaskArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a task and adds it to a queue. Tasks cannot be updated after creation; there is no UpdateTask command. * For App Engine queues, the maximum task size is 100KB. * For pull queues, the maximum task size is 1MB.

        :param str resource_name: The name of the resource.
        :param QueueTaskArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(QueueTaskArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_engine_http_request: Optional[pulumi.Input[pulumi.InputType['AppEngineHttpRequestArgs']]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 pull_message: Optional[pulumi.Input[pulumi.InputType['PullMessageArgs']]] = None,
                 queues_id: Optional[pulumi.Input[str]] = None,
                 response_view: Optional[pulumi.Input[str]] = None,
                 schedule_time: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[pulumi.InputType['TaskStatusArgs']]] = None,
                 tasks_id: Optional[pulumi.Input[str]] = None,
                 view: Optional[pulumi.Input[str]] = None,
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
            __props__ = QueueTaskArgs.__new__(QueueTaskArgs)

            __props__.__dict__["app_engine_http_request"] = app_engine_http_request
            __props__.__dict__["create_time"] = create_time
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__.__dict__["locations_id"] = locations_id
            __props__.__dict__["name"] = name
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__.__dict__["projects_id"] = projects_id
            __props__.__dict__["pull_message"] = pull_message
            if queues_id is None and not opts.urn:
                raise TypeError("Missing required property 'queues_id'")
            __props__.__dict__["queues_id"] = queues_id
            __props__.__dict__["response_view"] = response_view
            __props__.__dict__["schedule_time"] = schedule_time
            __props__.__dict__["status"] = status
            if tasks_id is None and not opts.urn:
                raise TypeError("Missing required property 'tasks_id'")
            __props__.__dict__["tasks_id"] = tasks_id
            __props__.__dict__["view"] = view
        super(QueueTask, __self__).__init__(
            'google-native:cloudtasks/v2beta2:QueueTask',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'QueueTask':
        """
        Get an existing QueueTask resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = QueueTaskArgs.__new__(QueueTaskArgs)

        __props__.__dict__["app_engine_http_request"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["pull_message"] = None
        __props__.__dict__["schedule_time"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["view"] = None
        return QueueTask(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appEngineHttpRequest")
    def app_engine_http_request(self) -> pulumi.Output['outputs.AppEngineHttpRequestResponse']:
        """
        App Engine HTTP request that is sent to the task's target. Can be set only if app_engine_http_target is set on the queue. An App Engine task is a task that has AppEngineHttpRequest set.
        """
        return pulumi.get(self, "app_engine_http_request")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time that the task was created. `create_time` will be truncated to the nearest second.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Optionally caller-specified in CreateTask. The task name. The task name must have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID` * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) * `LOCATION_ID` is the canonical ID for the task's location. The list of available locations can be obtained by calling ListLocations. For more information, see https://cloud.google.com/about/locations/. * `QUEUE_ID` can contain letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). The maximum length is 100 characters. * `TASK_ID` can contain only letters ([A-Za-z]), numbers ([0-9]), hyphens (-), or underscores (_). The maximum length is 500 characters.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pullMessage")
    def pull_message(self) -> pulumi.Output['outputs.PullMessageResponse']:
        """
        LeaseTasks to process the task. Can be set only if pull_target is set on the queue. A pull task is a task that has PullMessage set.
        """
        return pulumi.get(self, "pull_message")

    @property
    @pulumi.getter(name="scheduleTime")
    def schedule_time(self) -> pulumi.Output[str]:
        """
        The time when the task is scheduled to be attempted. For App Engine queues, this is when the task will be attempted or retried. For pull queues, this is the time when the task is available to be leased; if a task is currently leased, this is the time when the current lease expires, that is, the time that the task was leased plus the lease_duration. `schedule_time` will be truncated to the nearest microsecond.
        """
        return pulumi.get(self, "schedule_time")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['outputs.TaskStatusResponse']:
        """
        The task status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def view(self) -> pulumi.Output[str]:
        """
        The view specifies which subset of the Task has been returned.
        """
        return pulumi.get(self, "view")

