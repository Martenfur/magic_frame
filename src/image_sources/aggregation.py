from .deviantart import DeviantartImageSource
from .artstation import ArtstationImageSource
from .local import LocalImageSource

from PIL import Image
import config

class AggregationImageSource:

	name = "aggregation"
	last_image_url = "none"
	last_image_name = "none"


	_sources = { 
		"deviantart" : DeviantartImageSource(),
		"artstation" : ArtstationImageSource(), 
		"local" : LocalImageSource()
	}
	_used_sources = []

	_retry_count = 5

	def __init__(self):
		for src in config.current.image_sources:
			if src in self._sources:
				self._used_sources.append(self._sources[src])
		if len(self._used_sources) == 0:
			self._used_sources.append(_sources["local"])

	def get_image(self, is_landscape):
		for src in self._used_sources:
			for i in range(0, self._retry_count):
				try:
					img = src.get_image(is_landscape)
					if img == None:
						raise TypeError()
					self.name = src.name
					self.last_image_url = src.last_image_url
					self.last_image_name = src.last_image_name
					return img
				except Exception as e:
					print("Error getting an image! Trying again... Error: " + str(e))

