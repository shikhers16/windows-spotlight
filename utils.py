from filesystem import *
from display import *
from internet import *

def change(data):
	# Get Orientation of main display
	orientation = get_orientation()

	# Download the image
	download_image(data[orientation]['u'])

	# Set as Wallpaper
	set_wallpaper('files/wallpaper.jpeg')

def last(new=False):
	history = read_file('history')
	history['next'] = history['current']
	write_file('history', history)
	if new:
		change(history['last'])
	return history['last']

def next():
	history = read_file('history')
	print("history")
	if 'next' in history.keys():
		print('next')
		data = history['next']
		del history['next']
		write_file('history', history)
		return data
	else:
		return get_spotlight_data()