# -*- encoding: utf8 -*-
from setuptools import find_packages, setup

import frigg_settings


def _read_long_description():
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst', format='markdown')
    except Exception:
        return None

version = frigg_settings.__version__


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
        'frigg-test-discovery>0.0,<1.1',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
    ]
)
