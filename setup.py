#!/usr/bin/env python

import setuptools
from distutils.core import setup

with open('getotp/version.py') as infile:
    exec(infile.read())

with open('requirements.txt') as requirements:
    required = requirements.read().splitlines()

kwargs = {
    "name": "getotp",
    "version": str(__version__),
    "packages": ["getotp"],
    "scripts": ["bin/getotp"],
    "description": "Store and retrieve TOTP secrets/tokens.",
    # PyPi, despite not parsing markdown, will prefer the README.md to the
    # standard README. Explicitly read it here.
    "long_description": open("README").read(),
    "author": "Gary M. Josack",
    "maintainer": "Gary M. Josack",
    "author_email": "gary@byoteki.com",
    "maintainer_email": "gary@byoteki.com",
    "license": "MIT",
    "install_requires": required,
    "url": "https://github.com/gmjosack/getotp",
    "download_url": "https://github.com/gmjosack/getotp/archive/master.tar.gz",
    "classifiers": [
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
}

setup(**kwargs)
