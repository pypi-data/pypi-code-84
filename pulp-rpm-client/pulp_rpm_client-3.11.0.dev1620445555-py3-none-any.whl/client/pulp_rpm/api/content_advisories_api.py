# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pulpcore.client.pulp_rpm.api_client import ApiClient
from pulpcore.client.pulp_rpm.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ContentAdvisoriesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create(self, **kwargs):  # noqa: E501
        """Create an update record  # noqa: E501

        Trigger an asynchronous task to create content,optionally create new repository version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param file file: An uploaded file that may be turned into the artifact of the content unit.
        :param str repository: A URI of a repository the new content unit should be associated with.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AsyncOperationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_with_http_info(**kwargs)  # noqa: E501

    def create_with_http_info(self, **kwargs):  # noqa: E501
        """Create an update record  # noqa: E501

        Trigger an asynchronous task to create content,optionally create new repository version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param file file: An uploaded file that may be turned into the artifact of the content unit.
        :param str repository: A URI of a repository the new content unit should be associated with.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AsyncOperationResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'file',
            'repository'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in local_var_params:
            local_var_files['file'] = local_var_params['file']  # noqa: E501
        if 'repository' in local_var_params:
            form_params.append(('repository', local_var_params['repository']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/pulp/api/v3/content/rpm/advisories/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncOperationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list(self, **kwargs):  # noqa: E501
        """List update records  # noqa: E501

        A ViewSet for UpdateRecord.  Define endpoint name which will appear in the API endpoint for this content type. For example::     http://pulp.example.com/pulp/api/v3/content/rpm/advisories/  Also specify queryset and serializer for UpdateRecord.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Filter results where id matches value
        :param list[str] id__in: Filter results where id is in a comma-separated list of values
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :param str ordering: Which field to use when ordering the results.
        :param str repository_version: Repository Version referenced by HREF
        :param str repository_version_added: Repository Version referenced by HREF
        :param str repository_version_removed: Repository Version referenced by HREF
        :param str severity: Filter results where severity matches value
        :param list[str] severity__in: Filter results where severity is in a comma-separated list of values
        :param str severity__ne: Filter results where severity not equal to value
        :param str status: Filter results where status matches value
        :param list[str] status__in: Filter results where status is in a comma-separated list of values
        :param str status__ne: Filter results where status not equal to value
        :param str type: Filter results where type matches value
        :param list[str] type__in: Filter results where type is in a comma-separated list of values
        :param str type__ne: Filter results where type not equal to value
        :param str fields: A list of fields to include in the response.
        :param str exclude_fields: A list of fields to exclude from the response.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PaginatedrpmUpdateRecordResponseList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_with_http_info(**kwargs)  # noqa: E501

    def list_with_http_info(self, **kwargs):  # noqa: E501
        """List update records  # noqa: E501

        A ViewSet for UpdateRecord.  Define endpoint name which will appear in the API endpoint for this content type. For example::     http://pulp.example.com/pulp/api/v3/content/rpm/advisories/  Also specify queryset and serializer for UpdateRecord.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Filter results where id matches value
        :param list[str] id__in: Filter results where id is in a comma-separated list of values
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :param str ordering: Which field to use when ordering the results.
        :param str repository_version: Repository Version referenced by HREF
        :param str repository_version_added: Repository Version referenced by HREF
        :param str repository_version_removed: Repository Version referenced by HREF
        :param str severity: Filter results where severity matches value
        :param list[str] severity__in: Filter results where severity is in a comma-separated list of values
        :param str severity__ne: Filter results where severity not equal to value
        :param str status: Filter results where status matches value
        :param list[str] status__in: Filter results where status is in a comma-separated list of values
        :param str status__ne: Filter results where status not equal to value
        :param str type: Filter results where type matches value
        :param list[str] type__in: Filter results where type is in a comma-separated list of values
        :param str type__ne: Filter results where type not equal to value
        :param str fields: A list of fields to include in the response.
        :param str exclude_fields: A list of fields to exclude from the response.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PaginatedrpmUpdateRecordResponseList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'id',
            'id__in',
            'limit',
            'offset',
            'ordering',
            'repository_version',
            'repository_version_added',
            'repository_version_removed',
            'severity',
            'severity__in',
            'severity__ne',
            'status',
            'status__in',
            'status__ne',
            'type',
            'type__in',
            'type__ne',
            'fields',
            'exclude_fields'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params and local_var_params['id'] is not None:  # noqa: E501
            query_params.append(('id', local_var_params['id']))  # noqa: E501
        if 'id__in' in local_var_params and local_var_params['id__in'] is not None:  # noqa: E501
            query_params.append(('id__in', local_var_params['id__in']))  # noqa: E501
            collection_formats['id__in'] = 'csv'  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'ordering' in local_var_params and local_var_params['ordering'] is not None:  # noqa: E501
            query_params.append(('ordering', local_var_params['ordering']))  # noqa: E501
        if 'repository_version' in local_var_params and local_var_params['repository_version'] is not None:  # noqa: E501
            query_params.append(('repository_version', local_var_params['repository_version']))  # noqa: E501
        if 'repository_version_added' in local_var_params and local_var_params['repository_version_added'] is not None:  # noqa: E501
            query_params.append(('repository_version_added', local_var_params['repository_version_added']))  # noqa: E501
        if 'repository_version_removed' in local_var_params and local_var_params['repository_version_removed'] is not None:  # noqa: E501
            query_params.append(('repository_version_removed', local_var_params['repository_version_removed']))  # noqa: E501
        if 'severity' in local_var_params and local_var_params['severity'] is not None:  # noqa: E501
            query_params.append(('severity', local_var_params['severity']))  # noqa: E501
        if 'severity__in' in local_var_params and local_var_params['severity__in'] is not None:  # noqa: E501
            query_params.append(('severity__in', local_var_params['severity__in']))  # noqa: E501
            collection_formats['severity__in'] = 'csv'  # noqa: E501
        if 'severity__ne' in local_var_params and local_var_params['severity__ne'] is not None:  # noqa: E501
            query_params.append(('severity__ne', local_var_params['severity__ne']))  # noqa: E501
        if 'status' in local_var_params and local_var_params['status'] is not None:  # noqa: E501
            query_params.append(('status', local_var_params['status']))  # noqa: E501
        if 'status__in' in local_var_params and local_var_params['status__in'] is not None:  # noqa: E501
            query_params.append(('status__in', local_var_params['status__in']))  # noqa: E501
            collection_formats['status__in'] = 'csv'  # noqa: E501
        if 'status__ne' in local_var_params and local_var_params['status__ne'] is not None:  # noqa: E501
            query_params.append(('status__ne', local_var_params['status__ne']))  # noqa: E501
        if 'type' in local_var_params and local_var_params['type'] is not None:  # noqa: E501
            query_params.append(('type', local_var_params['type']))  # noqa: E501
        if 'type__in' in local_var_params and local_var_params['type__in'] is not None:  # noqa: E501
            query_params.append(('type__in', local_var_params['type__in']))  # noqa: E501
            collection_formats['type__in'] = 'csv'  # noqa: E501
        if 'type__ne' in local_var_params and local_var_params['type__ne'] is not None:  # noqa: E501
            query_params.append(('type__ne', local_var_params['type__ne']))  # noqa: E501
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
        if 'exclude_fields' in local_var_params and local_var_params['exclude_fields'] is not None:  # noqa: E501
            query_params.append(('exclude_fields', local_var_params['exclude_fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/pulp/api/v3/content/rpm/advisories/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedrpmUpdateRecordResponseList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read(self, rpm_update_record_href, **kwargs):  # noqa: E501
        """Inspect an update record  # noqa: E501

        A ViewSet for UpdateRecord.  Define endpoint name which will appear in the API endpoint for this content type. For example::     http://pulp.example.com/pulp/api/v3/content/rpm/advisories/  Also specify queryset and serializer for UpdateRecord.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read(rpm_update_record_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str rpm_update_record_href: (required)
        :param str fields: A list of fields to include in the response.
        :param str exclude_fields: A list of fields to exclude from the response.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: RpmUpdateRecordResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.read_with_http_info(rpm_update_record_href, **kwargs)  # noqa: E501

    def read_with_http_info(self, rpm_update_record_href, **kwargs):  # noqa: E501
        """Inspect an update record  # noqa: E501

        A ViewSet for UpdateRecord.  Define endpoint name which will appear in the API endpoint for this content type. For example::     http://pulp.example.com/pulp/api/v3/content/rpm/advisories/  Also specify queryset and serializer for UpdateRecord.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_with_http_info(rpm_update_record_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str rpm_update_record_href: (required)
        :param str fields: A list of fields to include in the response.
        :param str exclude_fields: A list of fields to exclude from the response.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(RpmUpdateRecordResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'rpm_update_record_href',
            'fields',
            'exclude_fields'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'rpm_update_record_href' is set
        if self.api_client.client_side_validation and ('rpm_update_record_href' not in local_var_params or  # noqa: E501
                                                        local_var_params['rpm_update_record_href'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `rpm_update_record_href` when calling `read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rpm_update_record_href' in local_var_params:
            path_params['rpm_update_record_href'] = local_var_params['rpm_update_record_href']  # noqa: E501

        query_params = []
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
        if 'exclude_fields' in local_var_params and local_var_params['exclude_fields'] is not None:  # noqa: E501
            query_params.append(('exclude_fields', local_var_params['exclude_fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '{rpm_update_record_href}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RpmUpdateRecordResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
