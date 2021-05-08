#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.command.build_ext import build_ext as _build_ext
from distutils.core import Extension
import os, stat
import sys
import platform
from codecs import open  # To use a consistent encoding

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


APP_NAME = 'ygctools'

settings = dict()

settings.update(
    name=APP_NAME,
    version=get_version("ygctools/cmd.py"),
    description='tools for jingzhishen',
    author='jingzhishen',
    author_email='jingzhishen@126.com',
    packages=find_packages(),
    install_requires=[
    ],

    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    data_files=[
        ('bin', ['ygctools/alitools/docscope']),
        ('bin', ['ygctools/alitools/duk']),
        ('bin', ['ygctools/alitools/kvdump']),
        ('bin', ['ygctools/alitools/lfs_extrator']),
        ('bin', ['ygctools/alitools/mklfs']),
        ('bin', ['ygctools/alitools/mini_adpcm_ffmpeg']),
        ('bin', ['ygctools/alitools/pyoc.sh']),

        ('/usr/local/bin', ['ygctools/alitools/docscope']),
        ('/usr/local/bin', ['ygctools/alitools/duk']),
        ('/usr/local/bin', ['ygctools/alitools/kvdump']),
        ('/usr/local/bin', ['ygctools/alitools/lfs_extrator']),
        ('/usr/local/bin', ['ygctools/alitools/mklfs']),
        ('/usr/local/bin', ['ygctools/alitools/mini_adpcm_ffmpeg']),
        ('/usr/local/bin', ['ygctools/alitools/pyoc.sh']),
    ],
    entry_points={
        'console_scripts': [
            'yoc = ygctools.cmd:main',
        ],
    },

    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
)

setup(**settings)

try:
    os.chmod('/usr/local/bin/docscope', stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    os.chmod('/usr/local/bin/duk', stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    os.chmod('/usr/local/bin/kvdump', stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    os.chmod('/usr/local/bin/lfs_extrator', stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    os.chmod('/usr/local/bin/mklfs', stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    os.chmod('/usr/local/bin/mini_adpcm_ffmpeg', stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    os.chmod('/usr/local/bin/pyoc', stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    os.chmod('/usr/bin/docscope', stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    os.chmod('/usr/bin/duk', stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    os.chmod('/usr/bin/kvdump', stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    os.chmod('/usr/bin/lfs_extrator', stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    os.chmod('/usr/bin/mklfs', stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    os.chmod('/usr/bin/mini_adpcm_ffmpeg', stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    os.chmod('/usr/bin/pyoc', stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
except:
    pass
