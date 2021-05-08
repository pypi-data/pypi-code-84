# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['metaphor',
 'metaphor.common',
 'metaphor.dbt_extractor',
 'metaphor.google_directory',
 'metaphor.looker',
 'metaphor.postgresql',
 'metaphor.snowflake_extractor']

package_data = \
{'': ['*']}

install_requires = \
['aws-assume-role-lib>=1.3.0,<2.0.0',
 'boto3>=1.17.53,<1.18.0',
 'botocore>=1.20.53,<1.21.0',
 'dataclasses-json>=0.5.2,<0.6.0',
 'fastjsonschema>=2.15.1,<2.16.0',
 'python-dateutil>=2.8.1,<2.9.0',
 'requests>=2.25.1,<3.0.0',
 'smart-open>=5.0.0,<6.0.0']

extras_require = \
{'all': ['asyncpg>=0.22.0,<0.23.0',
         'google-api-python-client>=2.2.0,<2.3.0',
         'google-auth-oauthlib>=0.4.4,<0.5.0',
         'looker-sdk>=21.4.1,<22.0.0',
         'snowflake-connector-python>=2.4.1,<2.5.0'],
 'google': ['google-api-python-client>=2.2.0,<2.3.0',
            'google-auth-oauthlib>=0.4.4,<0.5.0'],
 'looker': ['looker-sdk>=21.4.1,<22.0.0'],
 'postgresql': ['asyncpg>=0.22.0,<0.23.0'],
 'snowflake': ['snowflake-connector-python>=2.4.1,<2.5.0']}

setup_kwargs = {
    'name': 'metaphor-connectors',
    'version': '0.2.6',
    'description': '',
    'long_description': None,
    'author': 'Metaphor',
    'author_email': 'dev@metaphor.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
