from display import *
from internet import *
from utils import *
from gui import *


def new():
	# Get data from Windows Spotlight
	try:
		item = next()
		# Save data to archive
		# archive(item)
		change(item)
	except Exception as e:
		item = last()
	return item

def last():
	item = prev()
	change(item)
	return item

if __name__ == '__main__':
	#Start GUI
	item = new()
	GUI(item)