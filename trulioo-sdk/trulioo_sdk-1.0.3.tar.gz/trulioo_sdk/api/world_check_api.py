"""
Trulioo Python SDK

Package version: 1.0.3
Trulioo OpenAPI version: v1
Generated by OpenAPI Generator version: 5.0.1
"""

import re  # noqa: F401
import sys  # noqa: F401

from trulioo_sdk.api_client import ApiClient, Endpoint as _Endpoint
from trulioo_sdk.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)


class WorldCheckApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_world_check_profile(
            self,
            original_transaction_id,
            reference_id,
            mode="trial",
            **kwargs
        ):
            """Get World Check Profile  # noqa: E501

            Returns the corresponding world-check profile of the specified transaction ID and reference ID.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_world_check_profile(original_transaction_id, reference_id, mode="trial", async_req=True)
            >>> result = thread.get()

            Args:
                original_transaction_id (str):
                reference_id (str):
                mode (str): trial or live. defaults to "trial", must be one of ["trial"]

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['mode'] = \
                mode
            kwargs['original_transaction_id'] = \
                original_transaction_id
            kwargs['reference_id'] = \
                reference_id
            return self.call_with_http_info(**kwargs)

        self.get_world_check_profile = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/{mode}/worldcheck/v1/profile/{originalTransactionID}/{referenceID}',
                'operation_id': 'get_world_check_profile',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'mode',
                    'original_transaction_id',
                    'reference_id',
                ],
                'required': [
                    'mode',
                    'original_transaction_id',
                    'reference_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'mode':
                        (str,),
                    'original_transaction_id':
                        (str,),
                    'reference_id':
                        (str,),
                },
                'attribute_map': {
                    'mode': 'mode',
                    'original_transaction_id': 'originalTransactionID',
                    'reference_id': 'referenceID',
                },
                'location_map': {
                    'mode': 'path',
                    'original_transaction_id': 'path',
                    'reference_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_world_check_profile
        )
