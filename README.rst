gif2xls
=======

Inspired by xkcd_.

Converts GIF encoded images into Microsoft Excel formatted workbooks.

Each frame is assigned a worksheet, and each pixel is assigned a cell. In each cell is a 32-bit integer that describes the colour of that pixel in ARGB format.

An additional sheet named "Info" contains some header information, where each row contains a Name, Value pair.

Any images greater than 256 pixels wide need to use the newer .xlsx format - older .xls workbooks do not support more than 256 columns in a worksheet. Support may be added for such images in the future.

\(C) Thomas Bell 2016, `MIT License`_.

.. _xkcd: http://xkcd.com/1678/
.. _MIT License: https://opensource.org/licenses/MIT
