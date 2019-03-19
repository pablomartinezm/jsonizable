import sys

from jsonipy import __version__

try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

if sys.version_info <= (2, 4):
    error = 'Requires Python Version 2.5 or above... Exiting.'

requirements = []

setup(
    name='jsonipy',
    version=__version__,
    description='Convert your Python classes into JSON objects easily.',
    scripts=[],
    url='https://github.com/pablomartinezm/jsonipy',
    packages=['jsonipy'],
    license='Apache 2.0',
    platforms='Posix; MacOS X; Windows',
    setup_requires=requirements,
    install_requires=requirements,
    test_suite='googlemaps.test',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
