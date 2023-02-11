import requests
import json
import os
from . import img_utils
from . import censor
from . import duplicates
import random

class ArtstationImageSource:
	trending_url = "https://www.artstation.com/api/v2/community/explore/projects/community.json?page=%page_num%&dimension=2d&per_page=100&medium_ids%5B%5D=1&medium_ids%5B%5D=10&medium_ids%5B%5D=11&medium_ids%5B%5D=12&medium_ids%5B%5D=13&medium_ids%5B%5D=14"
	art_base_url = "https://www.artstation.com/projects/"

	def __get_art_data(self, art, is_landscape):
		if not censor.is_appropriate(art["tags"], art["title"], art["description"]):
			return False

		for asset in art["assets"]:
			# Skipping non-images.
			if asset["asset_type"] != "image":
				continue
			
			# Checking if the image matches preferred
			if not img_utils.has_acceptable_dimensions(asset["width"], asset["height"], is_landscape):
				continue

			print(asset["image_url"])
			print("w: " + str(asset["width"]) + " h: " + str(asset["height"]))
			return img_utils.download_image(asset["image_url"])
		return None


	def get_image(self, is_landscape):
		final_url = self.trending_url.replace("%page_num%", str(random.randint(1, 1000)))
		page = requests.get(final_url)
		json_data = json.loads(page.text)

		shuffled_data = []
		for data in json_data["data"]:
			shuffled_data.append(data)
		random.shuffle(shuffled_data)

		for data in shuffled_data:
			if duplicates.contains(data["hash_id"]):
				print("Skipping duplicate image: " + data["hash_id"])
				continue
			art_url = self.art_base_url + data["hash_id"] + ".json"
			print(data["url"])

			art_response = requests.get(art_url)
			
			art = json.loads(art_response.text)
			img = self.__get_art_data(art, is_landscape)
			if img != None:
				duplicates.add(data["hash_id"])
				return img
		return None