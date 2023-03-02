import sys
import os

libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
	sys.path.append(libdir)
from waveshare_epd import epd7in3f

import io

def display(img):
	try:
		epd = epd7in3f.EPD()
		epd.init()
		epd.Clear()
		epd.display(epd.getbuffer(img))
		epd.sleep()

	except IOError as e:
		print(e)

	except:
		epd7in3f.epdconfig.module_exit()