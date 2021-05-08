# coding: utf-8

"""
    Nomad Pilot

    This is the API descriptor for the Nomad Pilot API, responsible for shipping and logistics processing. Developed by [Samarkand Global](https://www.samarkand.global/) in partnership with [SF Express](https://www.sf-express.com/), [eSinotrans](http://air.esinotrans.com/), [sto](http://sto-express.co.uk/). Read the documentation online at [Nomad API Suite](https://api.samarkand.io/). - Install for node with `npm install nomad_pilot_cli` - Install for python with `pip install nomad-pilot-cli` - Install for Maven users `groupId, com.gitlab.samarkand-nomad; artifactId, nomad-pilot-cli`  # noqa: E501

    The version of the OpenAPI document: 1.39.0
    Contact: paul@samarkand.global
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "nomad-pilot-cli"
VERSION = "1.39.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Nomad Pilot",
    author="OpenAPI Generator community",
    author_email="paul@samarkand.global",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Nomad Pilot"],
    install_requires=REQUIRES + ["querystring==0.1.0"],
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,

    long_description_content_type='text/markdown',
    long_description=open('README.md', encoding='utf-8').read(),
)
