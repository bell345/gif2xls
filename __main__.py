#!/usr/bin/env python3

import os
import sys
import imghdr
import argparse
import pyexcel
import pyexcel.ext.xls
import pyexcel.ext.xlsx
from PIL import Image

from .version import APP_NAME, APP_VERSION

def abort(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)

def rgba_to_int(rgba):
    r,g,b,a = rgba
    return (a << 24) | (r << 16) | (g << 8) | b

def add_frame_to_xls(xls, frame, name):
    width, height = frame.size
    buf = [[0]*width]*height

    for i in range(width):
        for j in range(height):
            buf[j][i] = rgba_to_int(frame.getpixel((i, j)))

    sheet = pyexcel.Sheet(sheet=buf, name=name)
    xls += sheet
    return xls

def gif2xls(gif):

    size      = gif.size
    lastframe = gif.convert("RGBA")
    palette   = gif.getpalette()

    xls = pyexcel.Book()

    i = 0
    try:
        while True:
            new_img = gif.copy()
            gif.putpalette(palette)

            bg = Image.new("RGBA", size)

            bg.paste(lastframe)
            bg.paste(new_img)

            add_frame_to_xls(xls, bg, "Frame {}".format(i))

            lastframe = bg

            i += 1
            gif.seek(gif.tell() + 1)

    except EOFError:
        pass # after final frame

    frames = i

    info_buf  = []
    info_buf += [["Frames", frames]]
    info_buf += [["Version", gif.info["version"]]]
    info_buf += [["Loop", gif.info["loop"]]]
    info_buf += [["Frame Duration", gif.info["duration"]]]
    info_buf += [["Encoded With", "{} v{}".format(APP_NAME, APP_VERSION)]]

    info = pyexcel.Sheet(sheet=info_buf, name="Info")
    xls += info

    return xls

def main():

    parser = argparse.ArgumentParser(prog=APP_NAME,
            description="A very useful tool that converts GIF encoded images to XLS(X) files.",
            epilog="(C) Thomas Bell 2016, MIT License.")
    parser.add_argument("--version", action="version", version=APP_VERSION)

    parser.add_argument("input", type=argparse.FileType('rb'),
            help="GIF image that is to be transformed into an XLS(X) file.")
    parser.add_argument("-o", "--output", type=str,
            help="Output XLS(X) file.")
    args = parser.parse_args()



    if imghdr.what("", h=args.input.read()) != "gif":
        abort("File is not a GIF encoded image.")

    try:
        gif = Image.open(args.input)

    except IOError:
        abort("Unable to open image.")

    _, ext = os.path.splitext(args.output)
    if ext == "xls" and gif.width > 256:
        abort("XLS workbooks do not support more than 256 columns per worksheet. Support may be added in the future - for now, use an XLSX formatted output file.")

    xls = gif2xls(gif)

    xls.save_as(args.output)

if __name__ == "__main__":
    main()
