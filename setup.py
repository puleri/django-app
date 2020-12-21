"""Sets up the package"""

#!/usr/bin/env python
 # -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()

with open('LICENSE.md') as f:
    LICENSE = f.read()

setup(
    name='django-app',
    version='0.1.0',
    description='Back-end for zone application',
    long_description=README,
    author='Matthew Puleri',
    author_email='puleri.mp4@gmail.com',
    url='https://github.com/puleri/django-app',
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs'))
)
