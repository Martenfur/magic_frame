import os
import json
import re

current = None

class Fields(object):
	def __init__(self, s):
		self.__dict__ = json.loads(s)

def load(path = "config.json"):
	global current

	# Have to strip the comments before parsing because python is a retаrd.
	with open(path, "r") as JSONfile:
		json_string = "".join(re.split(r"(?://|#).*(?=\n)", JSONfile.read())).strip()

	current = Fields(json_string)

	if hasattr(current, "remote_config") and os.path.exists(current.remote_config):
		load(current.remote_config)
		return
