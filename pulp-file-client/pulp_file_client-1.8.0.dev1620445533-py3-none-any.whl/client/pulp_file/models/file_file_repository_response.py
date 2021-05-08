# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulp_file.configuration import Configuration


class FileFileRepositoryResponse(object):
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
    """
    openapi_types = {
        'pulp_href': 'str',
        'pulp_created': 'datetime',
        'versions_href': 'str',
        'pulp_labels': 'object',
        'latest_version_href': 'str',
        'name': 'str',
        'description': 'str',
        'retained_versions': 'int',
        'remote': 'str',
        'autopublish': 'bool',
        'manifest': 'str'
    }

    attribute_map = {
        'pulp_href': 'pulp_href',
        'pulp_created': 'pulp_created',
        'versions_href': 'versions_href',
        'pulp_labels': 'pulp_labels',
        'latest_version_href': 'latest_version_href',
        'name': 'name',
        'description': 'description',
        'retained_versions': 'retained_versions',
        'remote': 'remote',
        'autopublish': 'autopublish',
        'manifest': 'manifest'
    }

    def __init__(self, pulp_href=None, pulp_created=None, versions_href=None, pulp_labels=None, latest_version_href=None, name=None, description=None, retained_versions=None, remote=None, autopublish=False, manifest='PULP_MANIFEST', local_vars_configuration=None):  # noqa: E501
        """FileFileRepositoryResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pulp_href = None
        self._pulp_created = None
        self._versions_href = None
        self._pulp_labels = None
        self._latest_version_href = None
        self._name = None
        self._description = None
        self._retained_versions = None
        self._remote = None
        self._autopublish = None
        self._manifest = None
        self.discriminator = None

        if pulp_href is not None:
            self.pulp_href = pulp_href
        if pulp_created is not None:
            self.pulp_created = pulp_created
        if versions_href is not None:
            self.versions_href = versions_href
        if pulp_labels is not None:
            self.pulp_labels = pulp_labels
        if latest_version_href is not None:
            self.latest_version_href = latest_version_href
        self.name = name
        self.description = description
        self.retained_versions = retained_versions
        self.remote = remote
        if autopublish is not None:
            self.autopublish = autopublish
        if manifest is not None:
            self.manifest = manifest

    @property
    def pulp_href(self):
        """Gets the pulp_href of this FileFileRepositoryResponse.  # noqa: E501


        :return: The pulp_href of this FileFileRepositoryResponse.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this FileFileRepositoryResponse.


        :param pulp_href: The pulp_href of this FileFileRepositoryResponse.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def pulp_created(self):
        """Gets the pulp_created of this FileFileRepositoryResponse.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The pulp_created of this FileFileRepositoryResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_created

    @pulp_created.setter
    def pulp_created(self, pulp_created):
        """Sets the pulp_created of this FileFileRepositoryResponse.

        Timestamp of creation.  # noqa: E501

        :param pulp_created: The pulp_created of this FileFileRepositoryResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_created = pulp_created

    @property
    def versions_href(self):
        """Gets the versions_href of this FileFileRepositoryResponse.  # noqa: E501


        :return: The versions_href of this FileFileRepositoryResponse.  # noqa: E501
        :rtype: str
        """
        return self._versions_href

    @versions_href.setter
    def versions_href(self, versions_href):
        """Sets the versions_href of this FileFileRepositoryResponse.


        :param versions_href: The versions_href of this FileFileRepositoryResponse.  # noqa: E501
        :type: str
        """

        self._versions_href = versions_href

    @property
    def pulp_labels(self):
        """Gets the pulp_labels of this FileFileRepositoryResponse.  # noqa: E501


        :return: The pulp_labels of this FileFileRepositoryResponse.  # noqa: E501
        :rtype: object
        """
        return self._pulp_labels

    @pulp_labels.setter
    def pulp_labels(self, pulp_labels):
        """Sets the pulp_labels of this FileFileRepositoryResponse.


        :param pulp_labels: The pulp_labels of this FileFileRepositoryResponse.  # noqa: E501
        :type: object
        """

        self._pulp_labels = pulp_labels

    @property
    def latest_version_href(self):
        """Gets the latest_version_href of this FileFileRepositoryResponse.  # noqa: E501


        :return: The latest_version_href of this FileFileRepositoryResponse.  # noqa: E501
        :rtype: str
        """
        return self._latest_version_href

    @latest_version_href.setter
    def latest_version_href(self, latest_version_href):
        """Sets the latest_version_href of this FileFileRepositoryResponse.


        :param latest_version_href: The latest_version_href of this FileFileRepositoryResponse.  # noqa: E501
        :type: str
        """

        self._latest_version_href = latest_version_href

    @property
    def name(self):
        """Gets the name of this FileFileRepositoryResponse.  # noqa: E501

        A unique name for this repository.  # noqa: E501

        :return: The name of this FileFileRepositoryResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileFileRepositoryResponse.

        A unique name for this repository.  # noqa: E501

        :param name: The name of this FileFileRepositoryResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this FileFileRepositoryResponse.  # noqa: E501

        An optional description.  # noqa: E501

        :return: The description of this FileFileRepositoryResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FileFileRepositoryResponse.

        An optional description.  # noqa: E501

        :param description: The description of this FileFileRepositoryResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def retained_versions(self):
        """Gets the retained_versions of this FileFileRepositoryResponse.  # noqa: E501

        Retain X versions of the repository. Default is null which retains all versions. This is provided as a tech preview in Pulp 3 and may change in the future.  # noqa: E501

        :return: The retained_versions of this FileFileRepositoryResponse.  # noqa: E501
        :rtype: int
        """
        return self._retained_versions

    @retained_versions.setter
    def retained_versions(self, retained_versions):
        """Sets the retained_versions of this FileFileRepositoryResponse.

        Retain X versions of the repository. Default is null which retains all versions. This is provided as a tech preview in Pulp 3 and may change in the future.  # noqa: E501

        :param retained_versions: The retained_versions of this FileFileRepositoryResponse.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                retained_versions is not None and retained_versions < 1):  # noqa: E501
            raise ValueError("Invalid value for `retained_versions`, must be a value greater than or equal to `1`")  # noqa: E501

        self._retained_versions = retained_versions

    @property
    def remote(self):
        """Gets the remote of this FileFileRepositoryResponse.  # noqa: E501


        :return: The remote of this FileFileRepositoryResponse.  # noqa: E501
        :rtype: str
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        """Sets the remote of this FileFileRepositoryResponse.


        :param remote: The remote of this FileFileRepositoryResponse.  # noqa: E501
        :type: str
        """

        self._remote = remote

    @property
    def autopublish(self):
        """Gets the autopublish of this FileFileRepositoryResponse.  # noqa: E501

        Whether to automatically create publications for new repository versions, and update any distributions pointing to this repository.  # noqa: E501

        :return: The autopublish of this FileFileRepositoryResponse.  # noqa: E501
        :rtype: bool
        """
        return self._autopublish

    @autopublish.setter
    def autopublish(self, autopublish):
        """Sets the autopublish of this FileFileRepositoryResponse.

        Whether to automatically create publications for new repository versions, and update any distributions pointing to this repository.  # noqa: E501

        :param autopublish: The autopublish of this FileFileRepositoryResponse.  # noqa: E501
        :type: bool
        """

        self._autopublish = autopublish

    @property
    def manifest(self):
        """Gets the manifest of this FileFileRepositoryResponse.  # noqa: E501

        Filename to use for manifest file containing metadata for all the files.  # noqa: E501

        :return: The manifest of this FileFileRepositoryResponse.  # noqa: E501
        :rtype: str
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        """Sets the manifest of this FileFileRepositoryResponse.

        Filename to use for manifest file containing metadata for all the files.  # noqa: E501

        :param manifest: The manifest of this FileFileRepositoryResponse.  # noqa: E501
        :type: str
        """

        self._manifest = manifest

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
        if not isinstance(other, FileFileRepositoryResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileFileRepositoryResponse):
            return True

        return self.to_dict() != other.to_dict()
