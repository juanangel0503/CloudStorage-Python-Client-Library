#!/usr/bin/env python

import sys

from setuptools import setup, find_packages


# azure v0.x is not compatible with this package
# azure v0.x used to have a __version__ attribute (newer versions don't)
try:
    import azure

    try:
        ver = azure.__version__
        raise Exception(
            'This package is incompatible with azure=={}. '.format(ver) +
            'Uninstall it with "pip uninstall azure".'
        )
    except AttributeError:
        pass
except ImportError:
    pass

# azure-storage v0.36.0 and prior are not compatible with this package
try:
    import azure.storage

    try:
        ver = azure.storage.__version__
        raise Exception(
            'This package is incompatible with azure-storage=={}. '.format(ver) +
            ' Uninstall it with "pip uninstall azure-storage".'
        )
    except AttributeError:
        pass
except ImportError:
    pass

setup(
    name='storage-file',
    version='2.1.0',
    description='CloudStorage File Client Library for Python',
    long_description=open('README.rst', 'r').read(),
    license='MIT License',
    author='Juan Angel',
    author_email='devjuanangel0503@gmail.com',
    url='https://github.com/Azure/storage-python',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
    ],
    zip_safe=False,
    packages=find_packages(exclude=[
        # Exclude packages that will be covered by PEP420 or nspkg
        'azure',
        'azure.storage',
    ]),
    install_requires=[
        'azure-common>=1.1.5',
        'storage-common~=2.1'
    ],
    extras_require={
        ":python_version<'3.0'": ['futures'],
    },
)
