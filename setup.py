#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pressurecooker
from setuptools import setup, find_packages
import sys


with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    "beautifulsoup4>=4.6.3",
    "ffmpy>=0.2.2",
    "le-utils>=0.1.20",
    "matplotlib==2.2.3",    # the last with py27 support
    "numpy==1.15.4",        # pinned to avoid surprizes
    "Pillow==5.4.1",        # pinned to avoid surprizes
    "youtube-dl>=2019.11.5",
    "pdf2image>=1.4.0",     # needs system dependency poppler lib
    "le-pycaption>=2.0.0a3",
    "EbookLib>=0.17.1",
]
if sys.version_info < (3, 0, 0):
    requirements.append("pathlib>=1.0.1")

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pressurecooker',
    version=pressurecooker.__version__,
    description="A collection of utilities for media processing.",
    long_description=readme + '\n\n',
    long_description_content_type="text/markdown",
    author="Learning Equality",
    author_email='dev@learningequality.org',
    url='https://github.com/learningequality/pressurecooker',
    packages=find_packages(),
    package_dir={'presurecooker':
                 'presurecooker'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords=['media', 'mediaprocessing', 'video',
              'compression', 'thumbnails', 'pressurecooker'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
