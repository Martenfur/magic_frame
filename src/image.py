#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in3f
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)


DESATURATED_PALETTE = [
    [0, 0, 0],        # Black
    [255, 255, 255],  # White
    [0, 255, 0],      # Green
    [0, 0, 255],      # Blue
    [255, 0, 0],      # Red
    [255, 255, 0],    # Yellow
    [255, 140, 0],    # Orange
    [255, 255, 255]   # Clear
]

SATURATED_PALETTE = [
    [0, 0, 0],        # Black
    [217, 242, 255],  # White
    [3, 124, 76],     # Green
    [27, 46, 198],    # Blue
    [245, 80, 34],    # Red
    [255, 255, 68],   # Yellow
    [239, 121, 44],   # Orange
    [255, 255, 255]   # Clear
]

def _palette_blend(saturation, dtype='uint8'):
    saturation = float(saturation)
    palette = []
    for i in range(7):
        rs, gs, bs = [c * saturation for c in SATURATED_PALETTE[i]]
        rd, gd, bd = [c * (1.0 - saturation) for c in DESATURATED_PALETTE[i]]
        if dtype == 'uint8':
            palette += [int(rs + rd), int(gs + gd), int(bs + bd)]
        if dtype == 'uint24':
            palette += [(int(rs + rd) << 16) | (int(gs + gd) << 8) | int(bs + bd)]
    if dtype == 'uint8':
        palette += [255, 255, 255]
    if dtype == 'uint24':
        palette += [0xffffff]
    return palette


try:
    epd = epd7in3f.EPD()
    logging.info("init and clear")
    epd.init()
    epd.Clear()

    logging.info("reading image")
    Himage = Image.open(os.path.join(picdir, 'demo.jpg'))

    palette = _palette_blend(0.5)
    # Image size doesn't matter since it's just the palette we're using
    palette_image = Image.new("P", (1, 1))
    # Set our 7 colour palette (+ clear) and zero out the other 247 colours
    palette_image.putpalette(palette + [0, 0, 0] * 248)
    # Force source image data to be loaded for `.im` to work
    Himage.load()
    Himage = Himage.im.convert("P", True, palette_image.im)

    epd.display(epd.getbuffer(Himage))
    
    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd7in3f.epdconfig.module_exit()
    exit()
