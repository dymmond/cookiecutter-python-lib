#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
{{ cookiecutter.project_name }}
"""
import os
import re
import sys

from setuptools import find_packages

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    try:
        import wheel

        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()


def find_version(fname):
    """Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    """
    version = ""
    with open(fname, "r") as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError("Cannot find version information")
    return version


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content


setup(
    name='{{ cookiecutter.project_name }}',
    version=find_version("src/__init__.py"),
    url='{{ cookiecutter.github }}',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    license='{{ cookiecutter.license }}',
    author='{{ cookiecutter.author }}',
    author_email='{{ cookiecutter.email }}',
    description='{{ cookiecutter.description }}',
    py_modules=[],
    packages=find_packages("src"),
    package_dir={"": "src"},
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: {{ cookiecutter.license }} License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
