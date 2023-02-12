import requests
import PIL
from PIL import Image
import io
import os

def is_landscape(w, h):
	return w >= h


def has_acceptable_dimensions(w, h, landscape_preferred):
	return is_landscape(w, h) == landscape_preferred


def get_ratio(w, h):
	if h == 0:
		return 0
	return w / h

def resize_image(img, new_w, new_h):
	ratio = new_w / new_h

	img_w, img_h = img.size
	crop_w = 0
	crop_h = 0
	if is_landscape(img_w, img_h):
			if get_ratio(new_w, new_h) < get_ratio(img_w, img_h):
				crop_h = img_h
				crop_w = ratio * crop_h
			else:
				crop_w = img_w
				crop_h = crop_w / ratio
	else:
			if get_ratio(new_w, new_h) > get_ratio(img_w, img_h):
				crop_w = img_w
				crop_h = crop_w / ratio
			else:
				crop_h = img_h
				crop_w = ratio * crop_h
	
	area = ((img_w - crop_w) / 2, (img_h - crop_h) / 2, crop_w + (img_w - crop_w) / 2, crop_h + (img_h - crop_h) / 2)
	cropped_img = img.resize((new_w, new_h), box=area)
	return cropped_img



def download_image(url):
	img_data = requests.get(url).content
	with open('temp.png', 'wb') as handler:
		handler.write(img_data)

	image_temp = Image.open('temp.png')
	image_temp.load()
	os.remove('temp.png')
	return image_temp
