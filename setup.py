#!/usr/bin/env python3

from setuptools import setup, find_packages

from .version import APP_NAME, APP_VERSION, APP_AUTHOR

setup(
    name=APP_NAME,
    version=APP_VERSION,
    packages=find_packages(),
    author=APP_AUTHOR,
    author_email="tom.aus@outlook.com",
    url="https://github.com/bell345/gif2xls",
    description="Convert GIF images into XLS files.",
    long_description = """
    Inspired by http://xkcd.com/1678/.

    Converts GIF encoded images into Microsoft Excel formatted workbooks.

    Each frame is assigned a worksheet, and each pixel is assigned a cell. In each cell is a 32-bit integer that describes the colour of that pixel in ARGB format.

    An additional sheet named "Info" contains some header information, where each row contains a Name, Value pair.

    Any images greater than 256 pixels wide need to use the newer .xlsx format - older .xls workbooks do not support more than 256 columns in a worksheet.
""",
    install_requires=["pyexcel>=0.2", "pyexcel-xls>=0.1", "pyexcel-xlsx>=0.1", "Pillow>=3.0"],
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5"
    ],
    keywords="xls gif convert xkcd"
)
