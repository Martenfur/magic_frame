from image_sources.aggregation import AggregationImageSource
from image_sources.artstation import ArtstationImageSource
from image_sources.deviantart import DeviantartImageSource
from image_sources import img_utils
import orientation

import PIL
from PIL import Image, ImageEnhance

class Art:
	image_name = ""
	image_url = ""
	
	# Original image in its native resolution.
	original_image = None
	
	# Resized and rotated image that fits the display.
	processed_image = None

	def __init__(self):
		orientation.update()

		source = AggregationImageSource()

		if orientation.is_landscape():
			self.original_image = source.get_image(True)
			self.processed_image = img_utils.resize_image(self.original_image, 800, 480)
		else:
			self.original_image = source.get_image(False)
			self.processed_image = img_utils.resize_image(self.original_image, 480, 800)

		self.processed_image = img_utils.rotate_image(self.processed_image, orientation.get())

		self.__adjust_color()


	def __adjust_color(self):
		# Since the colors of epaper displays are fairly bleak, 
		# we're brightening them up just a little bit.
		converter = ImageEnhance.Color(self.processed_image)
		self.processed_image = converter.enhance(1.3)
