gif2xls
=======

Inspired by xkcd_.

Converts GIF encoded images into Microsoft Excel formatted workbooks.

Each frame is assigned a worksheet, and each pixel is assigned a cell.

There are two modes: fancy mode (the default) and boring mode. In boring mode (using -b or --boring at the command line), each cell is assigned a 25-bit integer, with bits 0-23 for an RGB value and bit 24 as transparency. In fancy mode, each cell is made square and is assigned a background colour that is as close to the original pixel value as possible.

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

Syntax:

::

    gif2xls input_file [-b|--boring] [--width cell_width] [-o output_file.xls(x)]

The default mode is "fancy" mode - use the --boring flag to use "boring" mode which doesn't use any colour formatting.

In "fancy" mode when using a `.xlsx` formatted output file, you can use the --width flag to specify how wide and high each cell will be in pixels. For example, `--width=5` will generate cells that are 5 pixels wide and high each so that the image appears scaled up 5 times.

The output file can either have a `.xls` or a `.xlsx` file extension - signalling to gif2xls your output file format.

**NOTE:** You must use `.xlsx` output files for GIF images that are larger than 256 pixels wide - classic `.xls` worksheets do not support more than 256 columns per worksheet. However, you can still use `.xls` worksheets for fancy mode images, just as long as they are not wider than 256 pixels.

\(C) Thomas Bell 2016, `MIT License`_.

.. _xkcd: http://xkcd.com/1678/
.. _MIT License: https://opensource.org/licenses/MIT
