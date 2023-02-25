import requests
import json
import os
from . import img_utils
from . import censor
from . import duplicates
import random
from datetime import date
from datetime import timedelta

class DeviantartImageSource:

	_login_endpoint = "https://www.deviantart.com/oauth2/token?client_id=%client_id%&client_secret=%client_secret%&grant_type=client_credentials"
	_daily_endpoint = "https://www.deviantart.com/api/v1/oauth2/browse/dailydeviations?access_token=%access_token%&date=%date%"
	_metadata_endpoint = "https://www.deviantart.com/api/v1/oauth2/deviation/metadata?access_token=%access_token%&deviationids=%deviationids%"

	_access_token = ""


	def __get_art_data(self, art, is_landscape):

		response = self._get_auth(self._metadata_endpoint.replace("%deviationids%", art["deviationid"]))
		art_data = json.loads(response.text)["metadata"][0]
		tags = []
		for tag in art_data["tags"]:
			tags.append(tag["tag_name"])

		if not censor.is_appropriate(tags, art_data["title"], art_data["description"]):
			return None

		# Checking if the image matches preferred size.
		if not img_utils.has_acceptable_dimensions(art["content"]["width"], art["content"]["height"], is_landscape):
			print("The image does not fit!")
			return None

		print("Downloading " + art_data["title"])
		return img_utils.download_image(art["content"]["src"])

	def _login(self):

		f = open('deviantart_config.json')
		config = json.load(f)
		f.close()

		final_url = self._login_endpoint.replace("%client_id%", config["client_id"]).replace("%client_secret%", config["client_secret"])
		response = requests.get(final_url, verify=False)
		json_data = json.loads(response.text)
		self._access_token = json_data["access_token"]


	def _get_auth(self, url):
		auth_url = url.replace("%access_token%", self._access_token)
		response = requests.get(auth_url, verify=False)
		if response.status_code == 401:
			self._login()
			auth_url = url.replace("%access_token%", self._access_token)
			response = requests.get(auth_url, verify=False)
		return response

	def get_image(self, is_landscape):
		picked_date = date.today() - timedelta(days = random.randint(0, 365))
		formatted_date = picked_date.strftime("%Y-%m-%d")

		response = self._get_auth(self._daily_endpoint.replace("%date%", formatted_date))
		json_data = json.loads(response.text)
		for data in json_data["results"]:
			if data["category"] != "Visual Art":
				continue
			img = self.__get_art_data(data, is_landscape)
			if img != None:
				duplicates.add(data["deviationid"])
				return img
		return None




