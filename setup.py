#!/usr/bin/env python3

from setuptools import setup

setup(
    name='PyHAML',
    version='1.3.0',
    description=
    'Pythonic implementation of HAML, cross compiling to Mako template syntax.',
    url='http://github.com/mikeboers/PyHAML',
    author='Mike Boers',
    author_email='PyHAML@mikeboers.com',
    license='BSD-3',
    packages=['haml'],
    install_requires=[
        'mako',
        'six',
        'lesscpy',
    ],
    scripts=[
        'scripts/haml-preprocess',
        'scripts/haml-render',
    ],
    entry_points={
        'distutils.setup_keywords': [
            "haml_manifests=haml.distutils:validate_manifest",
        ],
        'distutils.setup_commands': [
            "build_haml=haml.distutils:valid_manifest",
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: HTML',
        'Topic :: Text Processing :: Markup :: XML',
    ],
)
