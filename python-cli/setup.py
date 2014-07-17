try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "author": "Matt Molyneaux",
    "author_email": "moggers87+git@moggers87.co.uk",
    "classifiers": [
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    ],
    "description": "A simple client for the EightySeven",
    "long_description": "Simple client for the EightySeven service",
    "name": "eightyseven_cli",
    "py_modules": ["eightyseven_cli"],
    "license": "GPLv3+",
    "version": "0",
    "entry_points": {
        'console_scripts': ['eightyseven=eightyseven_cli:main'],
    },
    "install_requires": [
        "requests-oauthlib>=0.4.0",
        "requests>=2.3.0",
    ],
}

setup(**config)
