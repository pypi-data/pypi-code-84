# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Network Access - Conditions API wrapper.

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


class NetworkAccessConditions(object):
    """Identity Services Engine Network Access - Conditions API (version: 3.0.0).

    Wraps the Identity Services Engine Network Access - Conditions
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new NetworkAccessConditions
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(NetworkAccessConditions, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_network_access_conditions(self,
                                      headers=None,
                                      **query_parameters):
        """Network Access - Returns list of library conditions.

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

        e_url = ('/api/v1/policy/network-access/condition')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_df4fb303a3e5661ba12058f18b225af_v3_0_0', _api_response)

    def create_network_access_condition(self,
                                        attribute_id=None,
                                        attribute_name=None,
                                        attribute_value=None,
                                        children=None,
                                        condition_type=None,
                                        dates_range=None,
                                        dates_range_exception=None,
                                        description=None,
                                        dictionary_name=None,
                                        dictionary_value=None,
                                        hours_range=None,
                                        hours_range_exception=None,
                                        id=None,
                                        is_negate=None,
                                        name=None,
                                        operator=None,
                                        week_days=None,
                                        week_days_exception=None,
                                        headers=None,
                                        payload=None,
                                        active_validation=True,
                                        **query_parameters):
        """Network Access - Creates a library condition.

        Args:
            attribute_id(string): attributeId, property of the
                request body.
            attribute_name(string): attributeName, property of the
                request body.
            attribute_value(string): attributeValue, property of the
                request body.
            children(list): children, property of the request body
                (list of objects).
            condition_type(string): conditionType, property of the
                request body. Available values are
                'ConditionReference',
                'ConditionAttributes',
                'LibraryConditionAttributes',
                'ConditionAndBlock',
                'LibraryConditionAndBlock',
                'ConditionOrBlock',
                'LibraryConditionOrBlock' and
                'TimeAndDateCondition'.
            dates_range(object): datesRange, property of the request
                body.
            dates_range_exception(object): datesRangeException,
                property of the request body.
            description(string): description, property of the
                request body.
            dictionary_name(string): dictionaryName, property of the
                request body.
            dictionary_value(string): dictionaryValue, property of
                the request body.
            hours_range(object): hoursRange, property of the request
                body.
            hours_range_exception(object): hoursRangeException,
                property of the request body.
            id(string): id, property of the request body.
            is_negate(boolean): isNegate, property of the request
                body.
            name(string): name, property of the request body.
            operator(string): operator, property of the request
                body. Available values are 'equals',
                'notEquals', 'contains', 'notContains',
                'matches', 'in', 'notIn', 'startsWith',
                'notStartsWith', 'endsWith',
                'notEndsWith', 'greaterThan',
                'lessThan', 'greaterOrEquals',
                'lessOrEquals', 'macEquals',
                'macNotEquals', 'macNotIn', 'macIn',
                'macStartsWith', 'macNotStartsWith',
                'macEndsWith', 'macNotEndsWith',
                'macContains', 'macNotContains',
                'ipGreaterThan', 'ipLessThan',
                'ipEquals', 'ipNotEquals',
                'dateTimeMatches', 'dateLessThan',
                'dateLessThanOrEquals',
                'dateGreaterThan',
                'dateGreaterThanOrEquals', 'dateEquals'
                and 'dateNotEquals'.
            weekDays(list): weekDays, property of the request body
                (list of strings. Available values are
                'Sunday', 'Monday', 'Tuesday',
                'Wednesday', 'Thursday', 'Friday' and
                'Saturday').
            weekDaysException(list): weekDaysException, property of
                the request body (list of strings.
                Available values are 'Sunday', 'Monday',
                'Tuesday', 'Wednesday', 'Thursday',
                'Friday' and 'Saturday').
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
                'conditionType':
                    condition_type,
                'isNegate':
                    is_negate,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
                'dictionaryName':
                    dictionary_name,
                'attributeName':
                    attribute_name,
                'attributeId':
                    attribute_id,
                'operator':
                    operator,
                'dictionaryValue':
                    dictionary_value,
                'attributeValue':
                    attribute_value,
                'children':
                    children,
                'hoursRange':
                    hours_range,
                'hoursRangeException':
                    hours_range_exception,
                'weekDays':
                    week_days,
                'weekDaysException':
                    week_days_exception,
                'datesRange':
                    dates_range,
                'datesRangeException':
                    dates_range_exception,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_e7bd468ee94f53869e52e84454efd0e6_v3_0_0')\
                .validate(_payload)

        e_url = ('/api/v1/policy/network-access/condition')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_e7bd468ee94f53869e52e84454efd0e6_v3_0_0', _api_response)

    def get_network_access_conditions_for_policy_set(self,
                                                     headers=None,
                                                     **query_parameters):
        """Network Access - Returns list of library conditions for
        PolicySet scope.

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

        e_url = ('/api/v1/policy/network-access/condition/policyset')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c0984cde5e925c209ab87472ab905476_v3_0_0', _api_response)

    def get_network_access_conditions_for_authentication_rules(self,
                                                               headers=None,
                                                               **query_parameters):
        """Network Access - Returns list of library conditions for
        Authentication rules scope.

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

        e_url = ('/api/v1/policy/network-access/condition/authentication')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e34177d675622acd0a532f5b7c41b_v3_0_0', _api_response)

    def get_network_access_conditions_for_authorization_rule(self,
                                                             headers=None,
                                                             **query_parameters):
        """Network Access - Returns list of library conditions for
        Authorization rules scope.

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

        e_url = ('/api/v1/policy/network-access/condition/authorization')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fff985b5159a0aa52bfe9e62ba7_v3_0_0', _api_response)

    def get_network_access_condition_by_condition_id(self,
                                                     headers=None,
                                                     **query_parameters):
        """Network Access - Returns a library condition.

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

        e_url = ('/api/v1/policy/network-access/condition/{conditionId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e4686a7511884fd3eee7c582efb_v3_0_0', _api_response)

    def update_network_access_condition_by_condition_id(self,
                                                        attribute_id=None,
                                                        attribute_name=None,
                                                        attribute_value=None,
                                                        children=None,
                                                        condition_type=None,
                                                        dates_range=None,
                                                        dates_range_exception=None,
                                                        description=None,
                                                        dictionary_name=None,
                                                        dictionary_value=None,
                                                        hours_range=None,
                                                        hours_range_exception=None,
                                                        id=None,
                                                        is_negate=None,
                                                        name=None,
                                                        operator=None,
                                                        week_days=None,
                                                        week_days_exception=None,
                                                        headers=None,
                                                        payload=None,
                                                        active_validation=True,
                                                        **query_parameters):
        """Network Access - Update library condition.

        Args:
            attribute_id(string): attributeId, property of the
                request body.
            attribute_name(string): attributeName, property of the
                request body.
            attribute_value(string): attributeValue, property of the
                request body.
            children(list): children, property of the request body
                (list of objects).
            condition_type(string): conditionType, property of the
                request body. Available values are
                'ConditionReference',
                'ConditionAttributes',
                'LibraryConditionAttributes',
                'ConditionAndBlock',
                'LibraryConditionAndBlock',
                'ConditionOrBlock',
                'LibraryConditionOrBlock' and
                'TimeAndDateCondition'.
            dates_range(object): datesRange, property of the request
                body.
            dates_range_exception(object): datesRangeException,
                property of the request body.
            description(string): description, property of the
                request body.
            dictionary_name(string): dictionaryName, property of the
                request body.
            dictionary_value(string): dictionaryValue, property of
                the request body.
            hours_range(object): hoursRange, property of the request
                body.
            hours_range_exception(object): hoursRangeException,
                property of the request body.
            id(string): id, property of the request body.
            is_negate(boolean): isNegate, property of the request
                body.
            name(string): name, property of the request body.
            operator(string): operator, property of the request
                body. Available values are 'equals',
                'notEquals', 'contains', 'notContains',
                'matches', 'in', 'notIn', 'startsWith',
                'notStartsWith', 'endsWith',
                'notEndsWith', 'greaterThan',
                'lessThan', 'greaterOrEquals',
                'lessOrEquals', 'macEquals',
                'macNotEquals', 'macNotIn', 'macIn',
                'macStartsWith', 'macNotStartsWith',
                'macEndsWith', 'macNotEndsWith',
                'macContains', 'macNotContains',
                'ipGreaterThan', 'ipLessThan',
                'ipEquals', 'ipNotEquals',
                'dateTimeMatches', 'dateLessThan',
                'dateLessThanOrEquals',
                'dateGreaterThan',
                'dateGreaterThanOrEquals', 'dateEquals'
                and 'dateNotEquals'.
            weekDays(list): weekDays, property of the request body
                (list of strings. Available values are
                'Sunday', 'Monday', 'Tuesday',
                'Wednesday', 'Thursday', 'Friday' and
                'Saturday').
            weekDaysException(list): weekDaysException, property of
                the request body (list of strings.
                Available values are 'Sunday', 'Monday',
                'Tuesday', 'Wednesday', 'Thursday',
                'Friday' and 'Saturday').
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
                'conditionType':
                    condition_type,
                'isNegate':
                    is_negate,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
                'dictionaryName':
                    dictionary_name,
                'attributeName':
                    attribute_name,
                'attributeId':
                    attribute_id,
                'operator':
                    operator,
                'dictionaryValue':
                    dictionary_value,
                'attributeValue':
                    attribute_value,
                'children':
                    children,
                'hoursRange':
                    hours_range,
                'hoursRangeException':
                    hours_range_exception,
                'weekDays':
                    week_days,
                'weekDaysException':
                    week_days_exception,
                'datesRange':
                    dates_range,
                'datesRangeException':
                    dates_range_exception,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_3bfe54779ae1b3edccb16fa7_v3_0_0')\
                .validate(_payload)

        e_url = ('/api/v1/policy/network-access/condition/{conditionId}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_3bfe54779ae1b3edccb16fa7_v3_0_0', _api_response)

    def delete_network_access_condition_by_condition_id(self,
                                                        headers=None,
                                                        **query_parameters):
        """Network Access - Delete a library condition.

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

        e_url = ('/api/v1/policy/network-access/condition/{conditionId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d6d09f7a5084ac7036167214b0e1_v3_0_0', _api_response)

    def get_network_access_condition_by_condition_name(self,
                                                       headers=None,
                                                       **query_parameters):
        """Network Access - Returns a library condition.

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

        e_url = ('/api/v1/policy/network-access/condition-by-'
                 + 'name/{conditionName}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a70be83785373b264d21e84fbfa7d_v3_0_0', _api_response)

    def delete_network_access_condition_by_condition_name(self,
                                                          headers=None,
                                                          **query_parameters):
        """Network Access - Delete a library condition using condition
        Name.

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

        e_url = ('/api/v1/policy/network-access/condition-by-'
                 + 'name/{conditionName}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c052306febd5865ada5df348e18a889_v3_0_0', _api_response)

    def update_network_access_condition_by_condition_name(self,
                                                          attribute_id=None,
                                                          attribute_name=None,
                                                          attribute_value=None,
                                                          children=None,
                                                          condition_type=None,
                                                          dates_range=None,
                                                          dates_range_exception=None,
                                                          description=None,
                                                          dictionary_name=None,
                                                          dictionary_value=None,
                                                          hours_range=None,
                                                          hours_range_exception=None,
                                                          id=None,
                                                          is_negate=None,
                                                          name=None,
                                                          operator=None,
                                                          week_days=None,
                                                          week_days_exception=None,
                                                          headers=None,
                                                          payload=None,
                                                          active_validation=True,
                                                          **query_parameters):
        """Network Access - Update library condition using condition name.

        Args:
            attribute_id(string): attributeId, property of the
                request body.
            attribute_name(string): attributeName, property of the
                request body.
            attribute_value(string): attributeValue, property of the
                request body.
            children(list): children, property of the request body
                (list of objects).
            condition_type(string): conditionType, property of the
                request body. Available values are
                'ConditionReference',
                'ConditionAttributes',
                'LibraryConditionAttributes',
                'ConditionAndBlock',
                'LibraryConditionAndBlock',
                'ConditionOrBlock',
                'LibraryConditionOrBlock' and
                'TimeAndDateCondition'.
            dates_range(object): datesRange, property of the request
                body.
            dates_range_exception(object): datesRangeException,
                property of the request body.
            description(string): description, property of the
                request body.
            dictionary_name(string): dictionaryName, property of the
                request body.
            dictionary_value(string): dictionaryValue, property of
                the request body.
            hours_range(object): hoursRange, property of the request
                body.
            hours_range_exception(object): hoursRangeException,
                property of the request body.
            id(string): id, property of the request body.
            is_negate(boolean): isNegate, property of the request
                body.
            name(string): name, property of the request body.
            operator(string): operator, property of the request
                body. Available values are 'equals',
                'notEquals', 'contains', 'notContains',
                'matches', 'in', 'notIn', 'startsWith',
                'notStartsWith', 'endsWith',
                'notEndsWith', 'greaterThan',
                'lessThan', 'greaterOrEquals',
                'lessOrEquals', 'macEquals',
                'macNotEquals', 'macNotIn', 'macIn',
                'macStartsWith', 'macNotStartsWith',
                'macEndsWith', 'macNotEndsWith',
                'macContains', 'macNotContains',
                'ipGreaterThan', 'ipLessThan',
                'ipEquals', 'ipNotEquals',
                'dateTimeMatches', 'dateLessThan',
                'dateLessThanOrEquals',
                'dateGreaterThan',
                'dateGreaterThanOrEquals', 'dateEquals'
                and 'dateNotEquals'.
            weekDays(list): weekDays, property of the request body
                (list of strings. Available values are
                'Sunday', 'Monday', 'Tuesday',
                'Wednesday', 'Thursday', 'Friday' and
                'Saturday').
            weekDaysException(list): weekDaysException, property of
                the request body (list of strings.
                Available values are 'Sunday', 'Monday',
                'Tuesday', 'Wednesday', 'Thursday',
                'Friday' and 'Saturday').
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
                'conditionType':
                    condition_type,
                'isNegate':
                    is_negate,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
                'dictionaryName':
                    dictionary_name,
                'attributeName':
                    attribute_name,
                'attributeId':
                    attribute_id,
                'operator':
                    operator,
                'dictionaryValue':
                    dictionary_value,
                'attributeValue':
                    attribute_value,
                'children':
                    children,
                'hoursRange':
                    hours_range,
                'hoursRangeException':
                    hours_range_exception,
                'weekDays':
                    week_days,
                'weekDaysException':
                    week_days_exception,
                'datesRange':
                    dates_range,
                'datesRangeException':
                    dates_range_exception,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_dee8ff57265324a99fa2011bb4dc5f_v3_0_0')\
                .validate(_payload)

        e_url = ('/api/v1/policy/network-access/condition-by-'
                 + 'name/{conditionName}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_dee8ff57265324a99fa2011bb4dc5f_v3_0_0', _api_response)
