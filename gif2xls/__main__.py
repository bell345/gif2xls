#!/usr/bin/env python3
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

import os
import sys
import imghdr
import argparse

from PIL import Image

from .fancy import gif2xls as fancy
from .boring import gif2xls as boring
from .version import APP_NAME, APP_VERSION

def abort(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)

def main():

    parser = argparse.ArgumentParser(prog=APP_NAME,
            description="A very useful tool that converts GIF encoded images to XLS(X) files.",
            epilog="(C) Thomas Bell 2016, MIT License.")
    parser.add_argument("--version", action="version", version=APP_VERSION)

    parser.add_argument("input", type=argparse.FileType('rb'),
            help="GIF image that is to be transformed into an XLS(X) file.")
    parser.add_argument("-o", "--output", type=str, default="out.xls",
            help="Output XLS(X) file.")
    parser.add_argument("-b", "--boring", action="store_true",
            help="Don't use worksheet formatting and instead store a 25-bit ARGB int in each cell instead.")
    parser.add_argument("-w", "--width", type=int, default=5,
            help="Width and height of worksheet cells in pixels. Ignored if not in fancy mode or using .xls format.")
    args = parser.parse_args()

    if imghdr.what(None, h=args.input.read()) != "gif":
        abort("File is not a GIF encoded image.")

    try:
        gif = Image.open(args.input)

    except IOError:
        abort("Unable to open image.")

    _, ext = os.path.splitext(args.output)
    fmt = ext[1:]

    if fmt == "xls" and gif.width > 256:
        abort("""\
XLS workbooks do not support more than 256 columns per worksheet.
Support may be added in the future - for now, use an XLSX formatted output file.\
""")

    if args.boring:
        content = boring(gif, format=fmt)
    else:
        content = fancy(gif, format=fmt, cell_width=args.width)

    with open(args.output, 'wb') as fp:
        fp.write(content.getvalue())
