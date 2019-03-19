import sys
from os import path

from jsonizable import __version__
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

if sys.version_info <= (2, 4):
    error = 'Requires Python Version 2.5 or above... Exiting.'

requirements = []

setup(
    name='jsonizable',
    version=__version__,
    description='Convert your Python classes into JSON objects easily.',
    scripts=[],
    url='https://github.com/pablomartinezm/jsonipy',
    packages=['jsonizable'],
    license='Apache 2.0',
    platforms='Posix; MacOS X; Windows',
    setup_requires=requirements,
    long_description=long_description,
    long_description_content_type='text/markdown',
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
