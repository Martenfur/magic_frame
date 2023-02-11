import requests
import PIL
from PIL import Image
import io

def is_landscape(w, h):
	return w >= h


def has_acceptable_dimensions(w, h, landscape_preferred):
	return is_landscape(w, h) == landscape_preferred


def get_ratio(w, h):
	if h == 0:
		return 0
	return w / h

def resize_image(img):
	pass

def download_image(url):
	img_data = requests.get(url).content
	with open('temp.png', 'wb') as handler:
		handler.write(img_data)

	image_temp = Image.open('temp.png')

	return image_temp
