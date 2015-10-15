# -*- encoding: utf8 -*-
import re

from setuptools import find_packages, setup


def _read_long_description():
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst', format='markdown')
    except Exception:
        return None


version = ''
with open('frigg_settings/__init__.py', 'r') as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        fd.read(),
        re.MULTILINE
    ).group(1)


setup(
    name='frigg-settings',
    version=version,
    description='A module for parsing and discovery of frigg settings file',
    long_description=_read_long_description(),
    packages=find_packages(exclude='tests'),
    author='The frigg team',
    author_email='hi@frigg.io',
    license='MIT',
    url='https://github.com/frigg/frigg-settings',
    py_modules=['frigg_test_discovery'],
    include_package_data=True,
    install_requires=[
        'pyyaml==3.11',
        'frigg-test-discovery==1.4.1',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
    ]
)
