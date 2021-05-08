# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Network Access - Network Conditions API wrapper.

Copyright (c) 2021 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from builtins import *

from past.builtins import basestring

from ...restsession import RestSession
from ...utils import (
    check_type,
    dict_from_items_with_values,
    apply_path_params,
    dict_of_str,
)


class NetworkAccessNetworkConditions(object):
    """Identity Services Engine Network Access - Network Conditions API (version: 3.0.0).

    Wraps the Identity Services Engine Network Access - Network Conditions
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new NetworkAccessNetworkConditions
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(NetworkAccessNetworkConditions, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_network_access_network_conditions(self,
                                              headers=None,
                                              **query_parameters):
        """Network Access - Returns a list of network conditions.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:
            RestResponse: REST response with following properties:
              - headers(MyDict): response headers.
              - response(list): A list of MyDict objects. Access the object's properties by using the dot notation
                    or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        if headers is not None:
            pass

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/api/v1/policy/network-access/network-condition')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d43fec9e7dc556cbb9bf0ebd1dcd6aad_v3_0_0', _api_response)

    def create_network_access_network_condition(self,
                                                cli_dnis_list=None,
                                                condition_type=None,
                                                description=None,
                                                device_group_list=None,
                                                device_list=None,
                                                id=None,
                                                ip_addr_list=None,
                                                mac_addr_list=None,
                                                name=None,
                                                headers=None,
                                                payload=None,
                                                active_validation=True,
                                                **query_parameters):
        """Network Access - Creates network condition.

        Args:
            cliDnisList(list): cliDnisList, property of the request
                body (list of strings).
            condition_type(string): conditionType, property of the
                request body. Available values are
                'EndstationCondition', 'DeviceCondition'
                and 'DevicePortCondition'.
            description(string): description, property of the
                request body.
            deviceGroupList(list): deviceGroupList, property of the
                request body (list of strings).
            deviceList(list): deviceList, property of the request
                body (list of strings).
            id(string): id, property of the request body.
            ipAddrList(list): ipAddrList, property of the request
                body (list of strings).
            macAddrList(list): macAddrList, property of the request
                body (list of strings).
            name(string): name, property of the request body.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:
            RestResponse: REST response with following properties:
              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                    or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)
        if headers is not None:
            pass

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
                'conditionType':
                    condition_type,
                'ipAddrList':
                    ip_addr_list,
                'macAddrList':
                    mac_addr_list,
                'cliDnisList':
                    cli_dnis_list,
                'deviceList':
                    device_list,
                'deviceGroupList':
                    device_group_list,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f4dbfb874b3b56d7a651d6732f1bd55e_v3_0_0')\
                .validate(_payload)

        e_url = ('/api/v1/policy/network-access/network-condition')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_f4dbfb874b3b56d7a651d6732f1bd55e_v3_0_0', _api_response)

    def get_network_access_network_condition_by_condition_id(self,
                                                             headers=None,
                                                             **query_parameters):
        """Network Access - Returns a network condition.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:
            RestResponse: REST response with following properties:
              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                    or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        if headers is not None:
            pass

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/api/v1/policy/network-access/network-'
                 + 'condition/{conditionId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b06719c4a49753408438f661dd2f6f7e_v3_0_0', _api_response)

    def update_network_access_network_condition_by_condition_id(self,
                                                                cli_dnis_list=None,
                                                                condition_type=None,
                                                                description=None,
                                                                device_group_list=None,
                                                                device_list=None,
                                                                id=None,
                                                                ip_addr_list=None,
                                                                mac_addr_list=None,
                                                                name=None,
                                                                headers=None,
                                                                payload=None,
                                                                active_validation=True,
                                                                **query_parameters):
        """Network Access - Update network condition.

        Args:
            cliDnisList(list): cliDnisList, property of the request
                body (list of strings).
            condition_type(string): conditionType, property of the
                request body. Available values are
                'EndstationCondition', 'DeviceCondition'
                and 'DevicePortCondition'.
            description(string): description, property of the
                request body.
            deviceGroupList(list): deviceGroupList, property of the
                request body (list of strings).
            deviceList(list): deviceList, property of the request
                body (list of strings).
            id(string): id, property of the request body.
            ipAddrList(list): ipAddrList, property of the request
                body (list of strings).
            macAddrList(list): macAddrList, property of the request
                body (list of strings).
            name(string): name, property of the request body.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:
            RestResponse: REST response with following properties:
              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                    or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)
        if headers is not None:
            pass

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
                'conditionType':
                    condition_type,
                'ipAddrList':
                    ip_addr_list,
                'macAddrList':
                    mac_addr_list,
                'cliDnisList':
                    cli_dnis_list,
                'deviceList':
                    device_list,
                'deviceGroupList':
                    device_group_list,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_e313d50be9155acca1082ef11895aeb8_v3_0_0')\
                .validate(_payload)

        e_url = ('/api/v1/policy/network-access/network-'
                 + 'condition/{conditionId}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_e313d50be9155acca1082ef11895aeb8_v3_0_0', _api_response)

    def delete_network_access_network_condition_by_condition_id(self,
                                                                headers=None,
                                                                **query_parameters):
        """Network Access - Delete network condition.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:
            RestResponse: REST response with following properties:
              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                    or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        if headers is not None:
            pass

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/api/v1/policy/network-access/network-'
                 + 'condition/{conditionId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_da7b2773c485400980369a543ddbabf_v3_0_0', _api_response)
