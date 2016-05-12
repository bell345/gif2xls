gif2xls
=======

Inspired by xkcd_.

Converts GIF encoded images into Microsoft Excel formatted workbooks.

Each frame is assigned a worksheet, and each pixel is assigned a cell. In each cell is a 25-bit integer that describes the colour of that pixel in ARGB format - 8 bits per colour channel, 1 bit for transparency.

An additional sheet named "Info" contains some header information, where each row contains a Name, Value pair.

Installation
------------

To install, either run the following as root inside the repo directory:

::

    pip install .

or the following to install as a user package (making sure to add ~/.local/bin/ to your $PATH):

::

    pip install . --user

Usage
-----

Usage is super simple: run `gif2xls` from anywhere in your terminal, passing your input GIF formatted image and your output spreadsheet like this:

::

    gif2xls input.gif -o out.xls

The output file can either have a `.xls` or a `.xlsx` file extension - signalling to pyexcel_ your output file format.

**NOTE:** You must use `.xlsx` output files for GIF images that are larger than 256 pixels wide - classic `.xls` worksheets, at least in the `pyexcel implementation`_, do not support more than 256 columns per worksheet. This limitation may be removed in the future.

\(C) Thomas Bell 2016, `MIT License`_.

.. _xkcd: http://xkcd.com/1678/
.. _MIT License: https://opensource.org/licenses/MIT
.. _pyexcel: https://pythonhosted.org/pyexcel/
.. _pyexcel implementation: https://github.com/pyexcel/pyexcel-xls
