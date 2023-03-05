import config
config.load()
import witty.witty as witty 
import sys
from PIL import Image

def get_battery_percentage():
	high = config.current.battery_voltage["high"]
	low = config.current.battery_voltage["low"]

	current_voltage = witty.get_input_voltage()
	current_voltage = max(low, min(high, current_voltage))

	percentage = ((current_voltage - low) / (high - low)) * 100
	return round(percentage)


def battery_low():
	return get_battery_percentage() <= config.current.low_battery_alert_percentage


def add_low_battery_icon(img):
	if not battery_low():
		return img

	icon =  Image.open("low_battery_icon.png")

	icon_width, icon_height = icon.size
	img_width, img_height = img.size
	
	img.paste(icon, (0, img_height - icon_height), icon)

	return img

