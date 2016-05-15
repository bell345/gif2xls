#!/usr/bin/env python3
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

from PIL import Image

from .version import APP_NAME, APP_VERSION

def rgba_to_int(rgba):
    r,g,b,a = rgba
    return ((a&1) << 24) | (r << 16) | (g << 8) | b

def iter_gif_frames(gif):

    size      = gif.size
    lastframe = gif.convert("RGBA")
    palette   = gif.getpalette()

    # general structure of reading GIF files using PIL from:
    # https://stackoverflow.com/questions/10269099/pil-convert-gif-frames-to-jpg

    try:
        while True:
            new_img = gif.copy()
            gif.putpalette(palette)

            bg = Image.new("RGBA", size)

            bg.paste(lastframe)
            bg.paste(new_img)

            yield bg

            lastframe = bg

            gif.seek(gif.tell() + 1)

    except EOFError:
        pass # after final frame

def iter_pixels(img):

    width, height = img.size

    for x in range(width):
        for y in range(height):
            yield (x, y, img.getpixel((x, y)))

def iter_info_sheet(gif, frames):
    yield "Frames", len(frames)
    yield "Version", gif.info["version"].decode('ascii')
    if "loop" in gif.info:     yield "Loop", gif.info["loop"]
    if "duration" in gif.info: yield "Frame Duration", gif.info["duration"]
    yield "Encoded With", "{} v{}".format(APP_NAME, APP_VERSION)

def xlsx_px_to_width(px):
    if px < 12:
        return (px / 12)
    else:
        return (px - 5)/7

def xlsx_px_to_height(px):
    return px * (3/4)
