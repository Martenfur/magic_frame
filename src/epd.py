#from epaper import waveshare_7_3_epd
from epaper import dummy_epd

def __get_display():
	return dummy_epd

def get_width():
	return __get_display().get_width()

def get_height():
	return __get_display().get_height()

def display(img):
	__get_display().display(img)

