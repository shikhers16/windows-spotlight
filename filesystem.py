import json
from glob import glob

def read_file(filename):
	with open(f"files/{filename}.json", "r") as file:
		content = json.loads(file.read())
	return content

def write_file(filename, content):
	file = open(f"files/{filename}.json", "w")
	file.write(json.dumps(content))
	file.close()

def update_history(current):
	print("UPDATING HISTORY")
	history = read_file('history')
	history['last'] = history['current']
	history['current'] = current
	write_file('history', history)