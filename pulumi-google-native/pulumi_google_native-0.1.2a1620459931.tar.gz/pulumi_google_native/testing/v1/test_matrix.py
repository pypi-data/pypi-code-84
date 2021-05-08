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

__all__ = ['TestMatrixArgs', 'TestMatrix']

@pulumi.input_type
class TestMatrixArgs:
    def __init__(__self__, *,
                 project_id: pulumi.Input[str],
                 test_matrix_id: pulumi.Input[str],
                 client_info: Optional[pulumi.Input['ClientInfoArgs']] = None,
                 environment_matrix: Optional[pulumi.Input['EnvironmentMatrixArgs']] = None,
                 fail_fast: Optional[pulumi.Input[bool]] = None,
                 flaky_test_attempts: Optional[pulumi.Input[int]] = None,
                 invalid_matrix_details: Optional[pulumi.Input[str]] = None,
                 outcome_summary: Optional[pulumi.Input[str]] = None,
                 result_storage: Optional[pulumi.Input['ResultStorageArgs']] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 test_executions: Optional[pulumi.Input[Sequence[pulumi.Input['TestExecutionArgs']]]] = None,
                 test_specification: Optional[pulumi.Input['TestSpecificationArgs']] = None,
                 timestamp: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a TestMatrix resource.
        :param pulumi.Input[str] project_id: The cloud project that owns the test matrix.
        :param pulumi.Input[str] test_matrix_id: Unique id set by the service.
        :param pulumi.Input['ClientInfoArgs'] client_info: Information about the client which invoked the test.
        :param pulumi.Input['EnvironmentMatrixArgs'] environment_matrix: Required. The devices the tests are being executed on.
        :param pulumi.Input[bool] fail_fast: If true, only a single attempt at most will be made to run each execution/shard in the matrix. Flaky test attempts are not affected. Normally, 2 or more attempts are made if a potential infrastructure issue is detected. This feature is for latency sensitive workloads. The incidence of execution failures may be significantly greater for fail-fast matrices and support is more limited because of that expectation.
        :param pulumi.Input[int] flaky_test_attempts: The number of times a TestExecution should be re-attempted if one or more of its test cases fail for any reason. The maximum number of reruns allowed is 10. Default is 0, which implies no reruns.
        :param pulumi.Input[str] invalid_matrix_details: Describes why the matrix is considered invalid. Only useful for matrices in the INVALID state.
        :param pulumi.Input[str] outcome_summary: Output Only. The overall outcome of the test. Only set when the test matrix state is FINISHED.
        :param pulumi.Input['ResultStorageArgs'] result_storage: Required. Where the results for the matrix are written.
        :param pulumi.Input[str] state: Indicates the current progress of the test matrix.
        :param pulumi.Input[Sequence[pulumi.Input['TestExecutionArgs']]] test_executions: The list of test executions that the service creates for this matrix.
        :param pulumi.Input['TestSpecificationArgs'] test_specification: Required. How to run the test.
        :param pulumi.Input[str] timestamp: The time this test matrix was initially created.
        """
        pulumi.set(__self__, "project_id", project_id)
        pulumi.set(__self__, "test_matrix_id", test_matrix_id)
        if client_info is not None:
            pulumi.set(__self__, "client_info", client_info)
        if environment_matrix is not None:
            pulumi.set(__self__, "environment_matrix", environment_matrix)
        if fail_fast is not None:
            pulumi.set(__self__, "fail_fast", fail_fast)
        if flaky_test_attempts is not None:
            pulumi.set(__self__, "flaky_test_attempts", flaky_test_attempts)
        if invalid_matrix_details is not None:
            pulumi.set(__self__, "invalid_matrix_details", invalid_matrix_details)
        if outcome_summary is not None:
            pulumi.set(__self__, "outcome_summary", outcome_summary)
        if result_storage is not None:
            pulumi.set(__self__, "result_storage", result_storage)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if test_executions is not None:
            pulumi.set(__self__, "test_executions", test_executions)
        if test_specification is not None:
            pulumi.set(__self__, "test_specification", test_specification)
        if timestamp is not None:
            pulumi.set(__self__, "timestamp", timestamp)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[str]:
        """
        The cloud project that owns the test matrix.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="testMatrixId")
    def test_matrix_id(self) -> pulumi.Input[str]:
        """
        Unique id set by the service.
        """
        return pulumi.get(self, "test_matrix_id")

    @test_matrix_id.setter
    def test_matrix_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "test_matrix_id", value)

    @property
    @pulumi.getter(name="clientInfo")
    def client_info(self) -> Optional[pulumi.Input['ClientInfoArgs']]:
        """
        Information about the client which invoked the test.
        """
        return pulumi.get(self, "client_info")

    @client_info.setter
    def client_info(self, value: Optional[pulumi.Input['ClientInfoArgs']]):
        pulumi.set(self, "client_info", value)

    @property
    @pulumi.getter(name="environmentMatrix")
    def environment_matrix(self) -> Optional[pulumi.Input['EnvironmentMatrixArgs']]:
        """
        Required. The devices the tests are being executed on.
        """
        return pulumi.get(self, "environment_matrix")

    @environment_matrix.setter
    def environment_matrix(self, value: Optional[pulumi.Input['EnvironmentMatrixArgs']]):
        pulumi.set(self, "environment_matrix", value)

    @property
    @pulumi.getter(name="failFast")
    def fail_fast(self) -> Optional[pulumi.Input[bool]]:
        """
        If true, only a single attempt at most will be made to run each execution/shard in the matrix. Flaky test attempts are not affected. Normally, 2 or more attempts are made if a potential infrastructure issue is detected. This feature is for latency sensitive workloads. The incidence of execution failures may be significantly greater for fail-fast matrices and support is more limited because of that expectation.
        """
        return pulumi.get(self, "fail_fast")

    @fail_fast.setter
    def fail_fast(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "fail_fast", value)

    @property
    @pulumi.getter(name="flakyTestAttempts")
    def flaky_test_attempts(self) -> Optional[pulumi.Input[int]]:
        """
        The number of times a TestExecution should be re-attempted if one or more of its test cases fail for any reason. The maximum number of reruns allowed is 10. Default is 0, which implies no reruns.
        """
        return pulumi.get(self, "flaky_test_attempts")

    @flaky_test_attempts.setter
    def flaky_test_attempts(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "flaky_test_attempts", value)

    @property
    @pulumi.getter(name="invalidMatrixDetails")
    def invalid_matrix_details(self) -> Optional[pulumi.Input[str]]:
        """
        Describes why the matrix is considered invalid. Only useful for matrices in the INVALID state.
        """
        return pulumi.get(self, "invalid_matrix_details")

    @invalid_matrix_details.setter
    def invalid_matrix_details(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "invalid_matrix_details", value)

    @property
    @pulumi.getter(name="outcomeSummary")
    def outcome_summary(self) -> Optional[pulumi.Input[str]]:
        """
        Output Only. The overall outcome of the test. Only set when the test matrix state is FINISHED.
        """
        return pulumi.get(self, "outcome_summary")

    @outcome_summary.setter
    def outcome_summary(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "outcome_summary", value)

    @property
    @pulumi.getter(name="resultStorage")
    def result_storage(self) -> Optional[pulumi.Input['ResultStorageArgs']]:
        """
        Required. Where the results for the matrix are written.
        """
        return pulumi.get(self, "result_storage")

    @result_storage.setter
    def result_storage(self, value: Optional[pulumi.Input['ResultStorageArgs']]):
        pulumi.set(self, "result_storage", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates the current progress of the test matrix.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="testExecutions")
    def test_executions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TestExecutionArgs']]]]:
        """
        The list of test executions that the service creates for this matrix.
        """
        return pulumi.get(self, "test_executions")

    @test_executions.setter
    def test_executions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TestExecutionArgs']]]]):
        pulumi.set(self, "test_executions", value)

    @property
    @pulumi.getter(name="testSpecification")
    def test_specification(self) -> Optional[pulumi.Input['TestSpecificationArgs']]:
        """
        Required. How to run the test.
        """
        return pulumi.get(self, "test_specification")

    @test_specification.setter
    def test_specification(self, value: Optional[pulumi.Input['TestSpecificationArgs']]):
        pulumi.set(self, "test_specification", value)

    @property
    @pulumi.getter
    def timestamp(self) -> Optional[pulumi.Input[str]]:
        """
        The time this test matrix was initially created.
        """
        return pulumi.get(self, "timestamp")

    @timestamp.setter
    def timestamp(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "timestamp", value)


class TestMatrix(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_info: Optional[pulumi.Input[pulumi.InputType['ClientInfoArgs']]] = None,
                 environment_matrix: Optional[pulumi.Input[pulumi.InputType['EnvironmentMatrixArgs']]] = None,
                 fail_fast: Optional[pulumi.Input[bool]] = None,
                 flaky_test_attempts: Optional[pulumi.Input[int]] = None,
                 invalid_matrix_details: Optional[pulumi.Input[str]] = None,
                 outcome_summary: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 result_storage: Optional[pulumi.Input[pulumi.InputType['ResultStorageArgs']]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 test_executions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TestExecutionArgs']]]]] = None,
                 test_matrix_id: Optional[pulumi.Input[str]] = None,
                 test_specification: Optional[pulumi.Input[pulumi.InputType['TestSpecificationArgs']]] = None,
                 timestamp: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates and runs a matrix of tests according to the given specifications. Unsupported environments will be returned in the state UNSUPPORTED. A test matrix is limited to use at most 2000 devices in parallel. May return any of the following canonical error codes: - PERMISSION_DENIED - if the user is not authorized to write to project - INVALID_ARGUMENT - if the request is malformed or if the matrix tries to use too many simultaneous devices.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ClientInfoArgs']] client_info: Information about the client which invoked the test.
        :param pulumi.Input[pulumi.InputType['EnvironmentMatrixArgs']] environment_matrix: Required. The devices the tests are being executed on.
        :param pulumi.Input[bool] fail_fast: If true, only a single attempt at most will be made to run each execution/shard in the matrix. Flaky test attempts are not affected. Normally, 2 or more attempts are made if a potential infrastructure issue is detected. This feature is for latency sensitive workloads. The incidence of execution failures may be significantly greater for fail-fast matrices and support is more limited because of that expectation.
        :param pulumi.Input[int] flaky_test_attempts: The number of times a TestExecution should be re-attempted if one or more of its test cases fail for any reason. The maximum number of reruns allowed is 10. Default is 0, which implies no reruns.
        :param pulumi.Input[str] invalid_matrix_details: Describes why the matrix is considered invalid. Only useful for matrices in the INVALID state.
        :param pulumi.Input[str] outcome_summary: Output Only. The overall outcome of the test. Only set when the test matrix state is FINISHED.
        :param pulumi.Input[str] project_id: The cloud project that owns the test matrix.
        :param pulumi.Input[pulumi.InputType['ResultStorageArgs']] result_storage: Required. Where the results for the matrix are written.
        :param pulumi.Input[str] state: Indicates the current progress of the test matrix.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TestExecutionArgs']]]] test_executions: The list of test executions that the service creates for this matrix.
        :param pulumi.Input[str] test_matrix_id: Unique id set by the service.
        :param pulumi.Input[pulumi.InputType['TestSpecificationArgs']] test_specification: Required. How to run the test.
        :param pulumi.Input[str] timestamp: The time this test matrix was initially created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TestMatrixArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates and runs a matrix of tests according to the given specifications. Unsupported environments will be returned in the state UNSUPPORTED. A test matrix is limited to use at most 2000 devices in parallel. May return any of the following canonical error codes: - PERMISSION_DENIED - if the user is not authorized to write to project - INVALID_ARGUMENT - if the request is malformed or if the matrix tries to use too many simultaneous devices.

        :param str resource_name: The name of the resource.
        :param TestMatrixArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TestMatrixArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_info: Optional[pulumi.Input[pulumi.InputType['ClientInfoArgs']]] = None,
                 environment_matrix: Optional[pulumi.Input[pulumi.InputType['EnvironmentMatrixArgs']]] = None,
                 fail_fast: Optional[pulumi.Input[bool]] = None,
                 flaky_test_attempts: Optional[pulumi.Input[int]] = None,
                 invalid_matrix_details: Optional[pulumi.Input[str]] = None,
                 outcome_summary: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 result_storage: Optional[pulumi.Input[pulumi.InputType['ResultStorageArgs']]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 test_executions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TestExecutionArgs']]]]] = None,
                 test_matrix_id: Optional[pulumi.Input[str]] = None,
                 test_specification: Optional[pulumi.Input[pulumi.InputType['TestSpecificationArgs']]] = None,
                 timestamp: Optional[pulumi.Input[str]] = None,
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
            __props__ = TestMatrixArgs.__new__(TestMatrixArgs)

            __props__.__dict__["client_info"] = client_info
            __props__.__dict__["environment_matrix"] = environment_matrix
            __props__.__dict__["fail_fast"] = fail_fast
            __props__.__dict__["flaky_test_attempts"] = flaky_test_attempts
            __props__.__dict__["invalid_matrix_details"] = invalid_matrix_details
            __props__.__dict__["outcome_summary"] = outcome_summary
            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__.__dict__["project_id"] = project_id
            __props__.__dict__["result_storage"] = result_storage
            __props__.__dict__["state"] = state
            __props__.__dict__["test_executions"] = test_executions
            if test_matrix_id is None and not opts.urn:
                raise TypeError("Missing required property 'test_matrix_id'")
            __props__.__dict__["test_matrix_id"] = test_matrix_id
            __props__.__dict__["test_specification"] = test_specification
            __props__.__dict__["timestamp"] = timestamp
        super(TestMatrix, __self__).__init__(
            'google-native:testing/v1:TestMatrix',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TestMatrix':
        """
        Get an existing TestMatrix resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TestMatrixArgs.__new__(TestMatrixArgs)

        __props__.__dict__["client_info"] = None
        __props__.__dict__["environment_matrix"] = None
        __props__.__dict__["fail_fast"] = None
        __props__.__dict__["flaky_test_attempts"] = None
        __props__.__dict__["invalid_matrix_details"] = None
        __props__.__dict__["outcome_summary"] = None
        __props__.__dict__["project_id"] = None
        __props__.__dict__["result_storage"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["test_executions"] = None
        __props__.__dict__["test_matrix_id"] = None
        __props__.__dict__["test_specification"] = None
        __props__.__dict__["timestamp"] = None
        return TestMatrix(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clientInfo")
    def client_info(self) -> pulumi.Output['outputs.ClientInfoResponse']:
        """
        Information about the client which invoked the test.
        """
        return pulumi.get(self, "client_info")

    @property
    @pulumi.getter(name="environmentMatrix")
    def environment_matrix(self) -> pulumi.Output['outputs.EnvironmentMatrixResponse']:
        """
        Required. The devices the tests are being executed on.
        """
        return pulumi.get(self, "environment_matrix")

    @property
    @pulumi.getter(name="failFast")
    def fail_fast(self) -> pulumi.Output[bool]:
        """
        If true, only a single attempt at most will be made to run each execution/shard in the matrix. Flaky test attempts are not affected. Normally, 2 or more attempts are made if a potential infrastructure issue is detected. This feature is for latency sensitive workloads. The incidence of execution failures may be significantly greater for fail-fast matrices and support is more limited because of that expectation.
        """
        return pulumi.get(self, "fail_fast")

    @property
    @pulumi.getter(name="flakyTestAttempts")
    def flaky_test_attempts(self) -> pulumi.Output[int]:
        """
        The number of times a TestExecution should be re-attempted if one or more of its test cases fail for any reason. The maximum number of reruns allowed is 10. Default is 0, which implies no reruns.
        """
        return pulumi.get(self, "flaky_test_attempts")

    @property
    @pulumi.getter(name="invalidMatrixDetails")
    def invalid_matrix_details(self) -> pulumi.Output[str]:
        """
        Describes why the matrix is considered invalid. Only useful for matrices in the INVALID state.
        """
        return pulumi.get(self, "invalid_matrix_details")

    @property
    @pulumi.getter(name="outcomeSummary")
    def outcome_summary(self) -> pulumi.Output[str]:
        """
        Output Only. The overall outcome of the test. Only set when the test matrix state is FINISHED.
        """
        return pulumi.get(self, "outcome_summary")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The cloud project that owns the test matrix.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="resultStorage")
    def result_storage(self) -> pulumi.Output['outputs.ResultStorageResponse']:
        """
        Required. Where the results for the matrix are written.
        """
        return pulumi.get(self, "result_storage")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        Indicates the current progress of the test matrix.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="testExecutions")
    def test_executions(self) -> pulumi.Output[Sequence['outputs.TestExecutionResponse']]:
        """
        The list of test executions that the service creates for this matrix.
        """
        return pulumi.get(self, "test_executions")

    @property
    @pulumi.getter(name="testMatrixId")
    def test_matrix_id(self) -> pulumi.Output[str]:
        """
        Unique id set by the service.
        """
        return pulumi.get(self, "test_matrix_id")

    @property
    @pulumi.getter(name="testSpecification")
    def test_specification(self) -> pulumi.Output['outputs.TestSpecificationResponse']:
        """
        Required. How to run the test.
        """
        return pulumi.get(self, "test_specification")

    @property
    @pulumi.getter
    def timestamp(self) -> pulumi.Output[str]:
        """
        The time this test matrix was initially created.
        """
        return pulumi.get(self, "timestamp")

