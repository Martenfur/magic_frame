import os

_loaded = False
_ids = None

def load():
	global _ids, _loaded
	if _loaded:
		return
	_loaded = True
	_ids = set()

	if not os.path.isfile("id.txt"):
		return

	with open("id.txt", "r") as file:
		for line in file:
			_ids.add(line.replace("\n", ""))

def add(id):
	global _ids
	load()
	_ids.add(id)
	with open("id.txt", "w") as file:
		file.write('\n'.join(_ids) + '\n')


def contains(id):
	global _ids
	load()
	return id in _ids
