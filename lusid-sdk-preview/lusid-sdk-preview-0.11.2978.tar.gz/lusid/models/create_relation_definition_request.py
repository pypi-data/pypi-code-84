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

class CreateRelationDefinitionRequest(object):
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
        'scope': 'str',
        'code': 'str',
        'source_entity_domain': 'str',
        'target_entity_domain': 'str',
        'display_name': 'str',
        'outward_description': 'str',
        'inward_description': 'str',
        'life_time': 'str',
        'constraint_style': 'str'
    }

    attribute_map = {
        'scope': 'scope',
        'code': 'code',
        'source_entity_domain': 'sourceEntityDomain',
        'target_entity_domain': 'targetEntityDomain',
        'display_name': 'displayName',
        'outward_description': 'outwardDescription',
        'inward_description': 'inwardDescription',
        'life_time': 'lifeTime',
        'constraint_style': 'constraintStyle'
    }

    required_map = {
        'scope': 'required',
        'code': 'required',
        'source_entity_domain': 'required',
        'target_entity_domain': 'required',
        'display_name': 'required',
        'outward_description': 'required',
        'inward_description': 'required',
        'life_time': 'optional',
        'constraint_style': 'optional'
    }

    def __init__(self, scope=None, code=None, source_entity_domain=None, target_entity_domain=None, display_name=None, outward_description=None, inward_description=None, life_time=None, constraint_style=None):  # noqa: E501
        """
        CreateRelationDefinitionRequest - a model defined in OpenAPI

        :param scope:  The scope that the relation exists in. (required)
        :type scope: str
        :param code:  The code of the relation. Together with the scope this uniquely defines the relation. (required)
        :type code: str
        :param source_entity_domain:  The entity domain of the source entity object must be, allowed values are \"Portfolio\" and \"Person\" (required)
        :type source_entity_domain: str
        :param target_entity_domain:  The entity domain of the target entity object must be, allowed values are \"Portfolio\" and \"Person\" (required)
        :type target_entity_domain: str
        :param display_name:  The display name of the relation. (required)
        :type display_name: str
        :param outward_description:  The description to relate source entity object and target entity object. (required)
        :type outward_description: str
        :param inward_description:  The description to relate target entity object and source entity object. (required)
        :type inward_description: str
        :param life_time:  Describes how the relations can change over time, allowed values are \"Perpetual\" and \"TimeVariant\"
        :type life_time: str
        :param constraint_style:  Describes the uniqueness and cardinality for relations with a specific source entity object and relations under this definition. Allowed values are \"Property\" and \"Collection\", defaults to \"Collection\" if not specified.
        :type constraint_style: str

        """  # noqa: E501

        self._scope = None
        self._code = None
        self._source_entity_domain = None
        self._target_entity_domain = None
        self._display_name = None
        self._outward_description = None
        self._inward_description = None
        self._life_time = None
        self._constraint_style = None
        self.discriminator = None

        self.scope = scope
        self.code = code
        self.source_entity_domain = source_entity_domain
        self.target_entity_domain = target_entity_domain
        self.display_name = display_name
        self.outward_description = outward_description
        self.inward_description = inward_description
        self.life_time = life_time
        self.constraint_style = constraint_style

    @property
    def scope(self):
        """Gets the scope of this CreateRelationDefinitionRequest.  # noqa: E501

        The scope that the relation exists in.  # noqa: E501

        :return: The scope of this CreateRelationDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this CreateRelationDefinitionRequest.

        The scope that the relation exists in.  # noqa: E501

        :param scope: The scope of this CreateRelationDefinitionRequest.  # noqa: E501
        :type: str
        """
        if scope is None:
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501

        self._scope = scope

    @property
    def code(self):
        """Gets the code of this CreateRelationDefinitionRequest.  # noqa: E501

        The code of the relation. Together with the scope this uniquely defines the relation.  # noqa: E501

        :return: The code of this CreateRelationDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CreateRelationDefinitionRequest.

        The code of the relation. Together with the scope this uniquely defines the relation.  # noqa: E501

        :param code: The code of this CreateRelationDefinitionRequest.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def source_entity_domain(self):
        """Gets the source_entity_domain of this CreateRelationDefinitionRequest.  # noqa: E501

        The entity domain of the source entity object must be, allowed values are \"Portfolio\" and \"Person\"  # noqa: E501

        :return: The source_entity_domain of this CreateRelationDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._source_entity_domain

    @source_entity_domain.setter
    def source_entity_domain(self, source_entity_domain):
        """Sets the source_entity_domain of this CreateRelationDefinitionRequest.

        The entity domain of the source entity object must be, allowed values are \"Portfolio\" and \"Person\"  # noqa: E501

        :param source_entity_domain: The source_entity_domain of this CreateRelationDefinitionRequest.  # noqa: E501
        :type: str
        """
        if source_entity_domain is None:
            raise ValueError("Invalid value for `source_entity_domain`, must not be `None`")  # noqa: E501

        self._source_entity_domain = source_entity_domain

    @property
    def target_entity_domain(self):
        """Gets the target_entity_domain of this CreateRelationDefinitionRequest.  # noqa: E501

        The entity domain of the target entity object must be, allowed values are \"Portfolio\" and \"Person\"  # noqa: E501

        :return: The target_entity_domain of this CreateRelationDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._target_entity_domain

    @target_entity_domain.setter
    def target_entity_domain(self, target_entity_domain):
        """Sets the target_entity_domain of this CreateRelationDefinitionRequest.

        The entity domain of the target entity object must be, allowed values are \"Portfolio\" and \"Person\"  # noqa: E501

        :param target_entity_domain: The target_entity_domain of this CreateRelationDefinitionRequest.  # noqa: E501
        :type: str
        """
        if target_entity_domain is None:
            raise ValueError("Invalid value for `target_entity_domain`, must not be `None`")  # noqa: E501

        self._target_entity_domain = target_entity_domain

    @property
    def display_name(self):
        """Gets the display_name of this CreateRelationDefinitionRequest.  # noqa: E501

        The display name of the relation.  # noqa: E501

        :return: The display_name of this CreateRelationDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CreateRelationDefinitionRequest.

        The display name of the relation.  # noqa: E501

        :param display_name: The display_name of this CreateRelationDefinitionRequest.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def outward_description(self):
        """Gets the outward_description of this CreateRelationDefinitionRequest.  # noqa: E501

        The description to relate source entity object and target entity object.  # noqa: E501

        :return: The outward_description of this CreateRelationDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._outward_description

    @outward_description.setter
    def outward_description(self, outward_description):
        """Sets the outward_description of this CreateRelationDefinitionRequest.

        The description to relate source entity object and target entity object.  # noqa: E501

        :param outward_description: The outward_description of this CreateRelationDefinitionRequest.  # noqa: E501
        :type: str
        """
        if outward_description is None:
            raise ValueError("Invalid value for `outward_description`, must not be `None`")  # noqa: E501

        self._outward_description = outward_description

    @property
    def inward_description(self):
        """Gets the inward_description of this CreateRelationDefinitionRequest.  # noqa: E501

        The description to relate target entity object and source entity object.  # noqa: E501

        :return: The inward_description of this CreateRelationDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._inward_description

    @inward_description.setter
    def inward_description(self, inward_description):
        """Sets the inward_description of this CreateRelationDefinitionRequest.

        The description to relate target entity object and source entity object.  # noqa: E501

        :param inward_description: The inward_description of this CreateRelationDefinitionRequest.  # noqa: E501
        :type: str
        """
        if inward_description is None:
            raise ValueError("Invalid value for `inward_description`, must not be `None`")  # noqa: E501

        self._inward_description = inward_description

    @property
    def life_time(self):
        """Gets the life_time of this CreateRelationDefinitionRequest.  # noqa: E501

        Describes how the relations can change over time, allowed values are \"Perpetual\" and \"TimeVariant\"  # noqa: E501

        :return: The life_time of this CreateRelationDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._life_time

    @life_time.setter
    def life_time(self, life_time):
        """Sets the life_time of this CreateRelationDefinitionRequest.

        Describes how the relations can change over time, allowed values are \"Perpetual\" and \"TimeVariant\"  # noqa: E501

        :param life_time: The life_time of this CreateRelationDefinitionRequest.  # noqa: E501
        :type: str
        """

        self._life_time = life_time

    @property
    def constraint_style(self):
        """Gets the constraint_style of this CreateRelationDefinitionRequest.  # noqa: E501

        Describes the uniqueness and cardinality for relations with a specific source entity object and relations under this definition. Allowed values are \"Property\" and \"Collection\", defaults to \"Collection\" if not specified.  # noqa: E501

        :return: The constraint_style of this CreateRelationDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._constraint_style

    @constraint_style.setter
    def constraint_style(self, constraint_style):
        """Sets the constraint_style of this CreateRelationDefinitionRequest.

        Describes the uniqueness and cardinality for relations with a specific source entity object and relations under this definition. Allowed values are \"Property\" and \"Collection\", defaults to \"Collection\" if not specified.  # noqa: E501

        :param constraint_style: The constraint_style of this CreateRelationDefinitionRequest.  # noqa: E501
        :type: str
        """

        self._constraint_style = constraint_style

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
        if not isinstance(other, CreateRelationDefinitionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
