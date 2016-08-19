#!/usr/bin/env python3
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

from io import BytesIO

import pyexcel
from PIL import Image

from .common import *
from .version import APP_NAME, APP_VERSION

def add_frame(xls, frame, name):
    width, height = frame.size
    buf = [x[:] for x in [[0]*width]*height]

    for i,j,p in iter_pixels(frame):
        buf[j][i] = rgba_to_int(p)

    sheet = pyexcel.Sheet(sheet=buf, name=name)
    xls += sheet

# Uses pyexcel to create a generic worksheet that can either be an XLS file or an XLSX file.
def gif2xls(gif, format='xls'):
    fmt = format.lower().strip(".")
    supported = 'xls', 'xlsx', 'ods'
    if fmt not in supported:
        raise ValueError("'{}' formatted output is not supported. Only {} formats are supported.".format(fmt, supported))

    xls = pyexcel.Book()
    frames = list(iter_gif_frames(gif))

    for i, frame in enumerate(frames):
        add_frame(xls, frame, "Frame {}".format(i))

    info_buf = []
    for row in iter_info_sheet(gif, frames):
        info_buf += [row]

    info = pyexcel.Sheet(sheet=info_buf, name="Info")
    xls += info

    stream = BytesIO()
    xls.save_to_memory(fmt, stream)
    return stream
