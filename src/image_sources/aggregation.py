from .artstation import ArtstationImageSource
from PIL import Image

class AggregationImageSource:

	_artstation = None
	_retry_count = 5

	def __init__(self):
		self._artstation = ArtstationImageSource()


	def get_image(self, is_landscape):
		for i in range(0, self._retry_count):
			try:
				img = self._artstation.get_image(is_landscape)
				if img == None:
					raise TypeError()
				return img
			except:
				print("Error getting an image! Trying again...")

