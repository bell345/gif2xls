#!/usr/bin/env python3

from io import BytesIO

import xlwt
import xlsxwriter
from PIL import Image

from .common import *
from .colours import closest_style
from .version import APP_NAME, APP_VERSION

def add_frame_xlsx(xlsx, frame, name, cell_width=5):
    width, height = frame.size
    sheet = xlsx.add_worksheet(name)
    sheet.set_column(0, width-1, xlsx_px_to_width(cell_width))
    sheet.set_default_row(xlsx_px_to_height(cell_width))

    for i,j,p in iter_pixels(frame):
        fmt = xlsx.add_format()
        _,_,_,a = p
        if a:
            fmt.set_bg_color('#{:06X}'.format(rgba_to_int(p) & 0xFFFFFF))

        sheet.write(j, i, None, fmt)

    return xlsx

def gif2xls_xlsx(gif, cell_width=5):

    stream = BytesIO()
    xlsx = xlsxwriter.Workbook(stream)
    frames = list(iter_gif_frames(gif))

    for i, frame in enumerate(frames):
        xlsx = add_frame_xlsx(xlsx, frame, "Frame {}".format(i), cell_width=cell_width)

    info_sheet = xlsx.add_worksheet("Info")
    for r,row in enumerate(iter_info_sheet(gif, frames)):
        for c,cell in enumerate(row):
            info_sheet.write(r, c, cell)

    xlsx.close()
    return stream

def add_frame_xls(xls, frame, name):
    width, height = frame.size
    sheet = xls.add_sheet(name)

    # currently cannot change cell height
    # this makes sure that cell width == default cell height
    for i in range(width):
        sheet.col(i).set_width(620) # 17px

    for i,j,p in iter_pixels(frame):
        _,_,_,a = p
        if a:
            style = closest_style(p)
            sheet.write(j, i, None, style)

    return xls

def gif2xls_xls(gif):

    xls = xlwt.Workbook()
    frames = list(iter_gif_frames(gif))

    for i, frame in enumerate(frames):
        xls = add_frame_xls(xls, frame, "Frame {}".format(i))

    info_sheet = xls.add_sheet("Info")
    for r,row in enumerate(iter_info_sheet(gif, frames)):
        for c,cell in enumerate(row):
            info_sheet.write(r, c, cell)

    stream = BytesIO()
    xls.save(stream)
    return stream

def gif2xls(gif, format='xlsx', cell_width=5):
    fmt = format.lower().strip('.')
    supported = 'xlsx', 'xls'
    if fmt not in supported:
        raise ValueError("'{}' formatted output is not supported. Only {} formatted output is supported.".format(fmt, supported))

    elif fmt == 'xls':
        return gif2xls_xls(gif)

    elif fmt == 'xlsx':
        return gif2xls_xlsx(gif, cell_width=cell_width)
