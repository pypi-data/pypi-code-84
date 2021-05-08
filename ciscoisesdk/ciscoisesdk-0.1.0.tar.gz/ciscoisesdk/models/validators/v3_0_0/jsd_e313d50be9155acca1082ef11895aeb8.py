# -*- coding: utf-8 -*-
"""Identity Services Engine updateNetworkAccessNetworkConditionByConditionId data model.

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

import fastjsonschema
import json
from ciscoisesdk.exceptions import MalformedRequest

from builtins import *


class JSONSchemaValidatorE313D50BE9155AccA1082Ef11895Aeb8(object):
    """updateNetworkAccessNetworkConditionByConditionId request schema
    definition."""
    def __init__(self):
        super(JSONSchemaValidatorE313D50BE9155AccA1082Ef11895Aeb8, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "cliDnisList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "conditionType": {
                "enum": [
                "EndstationCondition",
                "DeviceCondition",
                "DevicePortCondition"
                ],
                "type": "string"
                },
                "description":
                 {
                "type": "string"
                },
                "deviceGroupList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "deviceList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "id": {
                "readOnly": true,
                "type": "string"
                },
                "ipAddrList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "macAddrList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "name": {
                "type": "string"
                }
                },
                "type": "object"
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )
