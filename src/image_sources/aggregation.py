from .deviantart import DeviantartImageSource
from .artstation import ArtstationImageSource
from .local import LocalImageSource

from PIL import Image
import config

class AggregationImageSource:

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
		print(self._used_sources)

	def get_image(self, is_landscape):
		for src in self._used_sources:
			for i in range(0, self._retry_count):
				try:
					img = src.get_image(is_landscape)
					if img == None:
						raise TypeError()
					return img
				except:
					print("Error getting an image! Trying again...")

