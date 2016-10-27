#!/usr/bin/env python

import sys
if not sys.version_info[0] >= 3:
    print("Sorry, Python 2 is not supported")
    exit(255)

from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()
    
setup(
    name              = 'unsplash-download',
    version           = '1.2.0',
    description       = 'unsplash.com image downloader',
    long_description  = long_description,
    author            = 'Maik Kulbe',
    author_email      = 'info@linux-web-development.de',
    license           = 'MIT',
    packages          = ['unsplash_download'],
	scripts			  = ['unsplash_download/unsplash_download.py'],
    install_requires = 
    [
        'docopt'
    ],
)
