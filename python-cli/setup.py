try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "author": "Matt Molyneaux",
    "author_email": "moggers87+git@moggers87.co.uk",
    "classifiers": [
        "Development Status :: 3 - Alpha",
    ],
    "description": "A simple client for the EightySeven",
    "long_description": "Simple client for the EightySeven service",
    "name": "eightyseven_cli",
    "py_modules": ["eightyseven_cli"],
    "scripts": ["bin/eightyseven"],
    "version": "0",
}

setup(**config)
