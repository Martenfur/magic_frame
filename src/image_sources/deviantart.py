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

	_access_token = ""


	def _login(self):

		f = open('deviantart_config.json')
		config = json.load(f)
		f.close()

		final_url = self._login_endpoint.replace("%client_id%", config["client_id"]).replace("%client_secret%", config["client_secret"])
		response = requests.get(final_url)
		json_data = json.loads(response.text)
		self._access_token = json_data["access_token"]


	def _get_auth(self, url):
		auth_url = url.replace("%access_token%", self._access_token)
		response = requests.get(auth_url)
		print(auth_url)
		if response.status_code == 401:
			self._login()
			auth_url = url.replace("%access_token%", self._access_token)
			response = requests.get(auth_url)
		return response


	def get_image(self, is_landscape):
		picked_date = date.today() - timedelta(days = random.randint(0, 365))
		formatted_date = picked_date.strftime("%Y-%m-%d")

		response = self._get_auth(self._daily_endpoint.replace("%date%", formatted_date))
		json_data = json.loads(response.text)
		for data in json_data["results"]:
			print(data["title"] + " " + str(len(json_data["results"])))




