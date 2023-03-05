import ilog
import battery
import orientation
import datetime
import witty.witty as witty
import config
import unicodedata
import re
import os

def slugify(value, allow_unicode=True):
	"""
	Taken from https://github.com/django/django/blob/master/django/utils/text.py
	Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
	dashes to single dashes. Remove characters that aren't alphanumerics,
	underscores, or hyphens. Convert to lowercase. Also strip leading and
	trailing whitespace, dashes, and underscores.
	"""
	value = str(value)
	if allow_unicode:
		value = unicodedata.normalize('NFKC', value)
	else:
		value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
	value = re.sub(r'[^\w\s-]', '', value.lower())
	return re.sub(r'[-\s]+', '-', value).strip('-_')

def report(art):
	now = datetime.datetime.now()
	secs = str(now.timestamp())
	if not os.path.exists(config.current.pictures_directory):
		os.makedirs(config.current.pictures_directory)
	art.original_image.save(config.current.pictures_directory + "/" + slugify(art.image_name) + "_" + secs + ".jpg")
	try:
		ilog.log("datetime: " + str(now))
		ilog.log("name: " + art.image_name)
		ilog.log("source: " + art.image_source)
		ilog.log("url: " + art.image_url)
		ilog.log("scheduled_startup: " + witty.get_startup_time())
		ilog.log("battery: " + str(battery.get_battery_percentage()) + "%")
		ilog.log("orientation: " + orientation.get())
	except:
		pass
	ilog.log("==========================================")
	ilog.dump()
