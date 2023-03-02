from epaper.drivers import epd7in3f

def get_width():
	return epd7in3f.EPD_WIDTH

def get_height():
	return epd7in3f.EPD_HEIGHT

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