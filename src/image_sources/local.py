import os
from . import img_utils
from . import duplicates
import random
from PIL import Image
import config

class LocalImageSource:
	name = "local"
	last_image_url = "none"
	last_image_name = "none"

	def get_image(self, is_landscape):
		files = os.listdir(config.current.local_images_path)
		random.shuffle(files)
		for file in files:
			full_path = os.path.join(config.current.local_images_path, file)
			print(full_path)
			if not os.path.isfile(full_path):
				print("Not a file!")
				continue
			if not config.current.local_allow_repeats:
				if duplicates.contains(full_path):
					continue
				duplicates.add(full_path)
			self.last_image_url = full_path
			self.last_image_name = full_path
			return Image.open(full_path)
		return None