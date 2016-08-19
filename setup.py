#!/usr/bin/env python3

import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

from gif2xls.version import APP_NAME, APP_VERSION

def read(filename):
    with open(filename) as fp:
        return fp.read()

setup(
    name=APP_NAME,
    version=APP_VERSION,
    packages=find_packages(),
    author="Thomas Bell",
    author_email="tom.aus@outlook.com",
    url="https://github.com/bell345/gif2xls",
    description="Convert GIF images into XLS files.",
    long_description=read("README.rst"),
    install_requires=[
        "pyexcel>=0.2",
        "pyexcel-xls>=0.1",
        "pyexcel-xlsx>=0.1",
        "XlsxWriter>=0.8",
        "xlwt>=1.0",
        "Pillow>=3.0",
        "future>=0.15"
    ],
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Topic :: Office/Business :: Financial :: Spreadsheet"
    ],
    keywords="xls gif convert xkcd",
    entry_points={
        'console_scripts': [
            'gif2xls=gif2xls:main'
        ]
    }
)
