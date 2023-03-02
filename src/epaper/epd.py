import config

try:
	if config.current.epaper_type == "7.3inch":
		from epaper import waveshare_7_3_epd as epd
	elif config.current.epaper_type == "5.65inch":
		from epaper import dummy_epd as epd
	elif config.current.epaper_type == "4.01inch":
		from epaper import dummy_epd as epd
	else:
		from epaper import dummy_epd as epd
except:
	from epaper import dummy_epd as epd

def get_width():
	return epd.get_width()

def get_height():
	return epd.get_height()

def display(img):
	epd.display(img)
