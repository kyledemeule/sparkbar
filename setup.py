#!/usr/bin/env python

import setuptools

setuptools.setup(
    name='sparkbar',
    version='1.0',
    description='A useful module',
    author='Kyle Demeule',
    author_email='kyle.demeule@gmail.com',
    packages=setuptools.find_packages(exclude='test'),
    install_requires=[
        "pytest"
    ],
)