import config
config.load()
import witty.witty as witty 
import time
import datetime
import sys
from PIL import Image

def battery_low():
	return True

def add_low_battery_icon(img):
	if not battery_low():
		return img

	icon =  Image.open("low_battery_icon.png")

	icon_width, icon_height = icon.size
	img_width, img_height = img.size
	
	img.paste(icon, (0, img_height - icon_height), icon)

	return img

