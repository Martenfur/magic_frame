import config

lines = []

def log(s):
	global lines
	print(s)
	lines.append(s + "\n")

def dump():
	global lines
	with open(config.current.log_file, "a") as file:
		file.writelines(lines)
