import os
from . import img_utils
from . import duplicates
import random
from PIL import Image
import config

class LocalImageSource:

	def get_image(self, is_landscape):
		files = os.listdir(config.current.local_images_path)
		random.shuffle(files)
		for file in files
			if not os.isfile(file):
				continue
			full_path = os.path.join(config.current.local_images_path, file)
			if not config.current.local_allow_repeats:
				if duplicates.contains(full_path):
					continue
				duplicates.add(full_path)
			return Image.open(full_path)
		return None