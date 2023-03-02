import os

current = None

class Fields(object):
	def __init__(self, f):
		self.__dict__ = json.load(f)

def init(path = "config.json"):
	global current

	f = open(path)
	current = Fields(f)
	f.close()

	if hasattr(current, "remote_config") and os.path.exists(current.remote_config):
		init(current.remote_config)
		return
