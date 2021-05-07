# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2978
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class CorporateActionSource(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'href': 'str',
        'id': 'ResourceId',
        'version': 'Version',
        'display_name': 'str',
        'description': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'id': 'id',
        'version': 'version',
        'display_name': 'displayName',
        'description': 'description',
        'links': 'links'
    }

    required_map = {
        'href': 'optional',
        'id': 'optional',
        'version': 'optional',
        'display_name': 'optional',
        'description': 'optional',
        'links': 'optional'
    }

    def __init__(self, href=None, id=None, version=None, display_name=None, description=None, links=None):  # noqa: E501
        """
        CorporateActionSource - a model defined in OpenAPI

        :param href: 
        :type href: str
        :param id: 
        :type id: lusid.ResourceId
        :param version: 
        :type version: lusid.Version
        :param display_name: 
        :type display_name: str
        :param description: 
        :type description: str
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501

        self._href = None
        self._id = None
        self._version = None
        self._display_name = None
        self._description = None
        self._links = None
        self.discriminator = None

        self.href = href
        if id is not None:
            self.id = id
        if version is not None:
            self.version = version
        self.display_name = display_name
        self.description = description
        self.links = links

    @property
    def href(self):
        """Gets the href of this CorporateActionSource.  # noqa: E501


        :return: The href of this CorporateActionSource.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this CorporateActionSource.


        :param href: The href of this CorporateActionSource.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this CorporateActionSource.  # noqa: E501


        :return: The id of this CorporateActionSource.  # noqa: E501
        :rtype: ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CorporateActionSource.


        :param id: The id of this CorporateActionSource.  # noqa: E501
        :type: ResourceId
        """

        self._id = id

    @property
    def version(self):
        """Gets the version of this CorporateActionSource.  # noqa: E501


        :return: The version of this CorporateActionSource.  # noqa: E501
        :rtype: Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CorporateActionSource.


        :param version: The version of this CorporateActionSource.  # noqa: E501
        :type: Version
        """

        self._version = version

    @property
    def display_name(self):
        """Gets the display_name of this CorporateActionSource.  # noqa: E501


        :return: The display_name of this CorporateActionSource.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CorporateActionSource.


        :param display_name: The display_name of this CorporateActionSource.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this CorporateActionSource.  # noqa: E501


        :return: The description of this CorporateActionSource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CorporateActionSource.


        :param description: The description of this CorporateActionSource.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def links(self):
        """Gets the links of this CorporateActionSource.  # noqa: E501


        :return: The links of this CorporateActionSource.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CorporateActionSource.


        :param links: The links of this CorporateActionSource.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CorporateActionSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
