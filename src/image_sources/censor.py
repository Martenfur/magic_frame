_blacklist = None

def load_blacklist():
	global _blacklist
	_blacklist = set()
	with open("blacklist.txt", "r") as file:
		for line in file:
			_blacklist.add(line.replace("\n", "").lower())

def is_text_appropriate(text):
	global _blacklist
	for tag in _blacklist:
		if tag in text.lower():
			print("Inappropriate text: " + text + "\n Blacklisted word: " + tag)
			return False
	return True

def is_tags_appropriate(tags):
	global _blacklist
	for tag in tags:
		if tag.lower() in _blacklist:
			print("Inappropriate tag: " + tag)
			return False
	return True


# Detects unwanted images.
def is_appropriate(tags, title, description):
	global _blacklist
	if _blacklist == None:
		load_blacklist()
	if not is_text_appropriate(title):
		return False
	if not is_text_appropriate(description):
		return False
	if not is_tags_appropriate(tags):
		return False
	return True