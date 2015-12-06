# skyplus
# Copyright (C) 2015 James Scholes
# This is free software, licensed under the terms of the GNU General Public License (version 3 or later).
# See the file LICENSE for more details.
from setuptools import setup

def readme():
    with open('README.rst', 'r') as f:
        return f.read()

setup(
    name='skyplus',
    version='0.1',
    author='James Scholes',
    author_email='james@jamesscholes.com',
    description='Python library for controlling a Sky Plus set-top box',
    long_description=readme(),
    url='https://github.com/jscholes/skyplus',
    license='GPLv3',
    packages=['skyplus'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'requests',
        'xmltodict',
    ],
    include_package_data=True,
    zip_safe=False
)
