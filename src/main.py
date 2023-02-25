import sys
import os
import numpy

libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
	sys.path.append(libdir)

from waveshare_epd import epd7in3f
import time
import traceback

from image_sources.aggregation import AggregationImageSource
from image_sources.artstation import ArtstationImageSource
from image_sources.deviantart import DeviantartImageSource
from image_sources import img_utils
import orientation

import PIL
from PIL import Image, ImageEnhance
import io

orientation.update()

#source = DeviantartImageSource()
source = ArtstationImageSource()
#source = AggregationImageSource()

if orientation.is_landscape():
	img = source.get_image(True)
	img = img_utils.resize_image(img, 800, 480)
else:
	img = source.get_image(False)
	img = img_utils.resize_image(img, 480, 800)

img = img_utils.rotate_image(img, orientation.get())


converter = ImageEnhance.Color(img)
img = converter.enhance(1.3)

try:
	epd = epd7in3f.EPD()
	epd.init()
	epd.Clear()
	epd.display(epd.getbuffer(img))
	epd.sleep()

except IOError as e:
	print(e)

except KeyboardInterrupt:
	epd7in3f.epdconfig.module_exit()
	exit()


print("cock")
