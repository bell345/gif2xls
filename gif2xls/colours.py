#!/usr/bin/env python3
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

import xlwt

xls_palette_index_map = {
    0x000000: 0x08, 0x800080: 0x14, 0x000080: 0x20, 0x99CCFF: 0x2C, 0x003366: 0x38,
    0xFFFFFF: 0x09, 0x008080: 0x15, 0xFF00FF: 0x21, 0xFF99CC: 0x2D, 0x339966: 0x39,
    0xFF0000: 0x0A, 0xC0C0C0: 0x16, 0xFFFF00: 0x22, 0xCC99FF: 0x2E, 0x003300: 0x3A,
    0x00FF00: 0x0B, 0x808080: 0x17, 0x00FFFF: 0x23, 0xFFCC99: 0x2F, 0x333300: 0x3B,
    0x0000FF: 0x0C, 0x9999FF: 0x18, 0x800080: 0x24, 0x3366FF: 0x30, 0x993300: 0x3C,
    0xFFFF00: 0x0D, 0x993366: 0x19, 0x800000: 0x25, 0x33CCCC: 0x31, 0x993366: 0x3D,
    0xFF00FF: 0x0E, 0xFFFFCC: 0x1A, 0x008080: 0x26, 0x99CC00: 0x32, 0x333399: 0x3E,
    0x00FFFF: 0x0F, 0xCCFFFF: 0x1B, 0x0000FF: 0x27, 0xFFCC00: 0x33, 0x333333: 0x3F,
    0x800000: 0x10, 0x660066: 0x1C, 0x00CCFF: 0x28, 0xFF9900: 0x34,
    0x008000: 0x11, 0xFF8080: 0x1D, 0xCCFFFF: 0x29, 0xFF6600: 0x35,
    0x000080: 0x12, 0x0066CC: 0x1E, 0xCCFFCC: 0x2A, 0x666699: 0x36,
    0x808000: 0x13, 0xCCCCFF: 0x1F, 0xFFFF99: 0x2B, 0x969696: 0x37,
}
xls_style_palette = {

}

for k,v in xls_palette_index_map.items():
    style = xlwt.XFStyle()
    style.pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    style.pattern.pattern_fore_colour = v
    xls_style_palette[k] = style

def int_to_rgb(i):
    return ((i & 0xFF0000) >> 16, (i & 0x00FF00) >> 8, (i & 0x0000FF))

def closeness(c1, c2):
    if isinstance(c1, int): c1 = int_to_rgb(c1)
    if isinstance(c2, int): c2 = int_to_rgb(c2)

    r1,g1,b1 = c1
    r2,g2,b2 = c2

    res = (r2 - r1)**2 + (g2 - g1)**2 + (b2 - b1)**2
    return res

def closest_style(rgb):
    if len(rgb) > 3: rgb = rgb[:3]
    palette = list(xls_palette_index_map.keys())
    palette.sort(key=lambda c: closeness(rgb, c))

    return xls_style_palette[palette[0]]
