import os
from . import img_utils
import random
from PIL import Image
import config

class LocalImageSource:

	def get_image(self, is_landscape):
		return Image.open(os.path.join(config.current.local_images_path, 'img.png'))