import requests
import json
from filesystem import update_history
from datetime import datetime, timezone
import os

def download_image(url):
	# Download and Save the image from the url
	r = requests.get(url, stream=True)
	path = 'files/wallpaper.jpeg'
	if r.status_code == 200:
		with open(path, 'wb') as f:
			for chunk in r:
				f.write(chunk)

def open_link(link):
	os.startfile(link)

def get_spotlight_data():
	# Get data from Windows Spotlight and store the relevant parts
	T = '2017-12-31T23:59:59Z'
	url = f'https://www.shikhersrivastava.com/windowsspotlightapi/wallpaper'
	# url = f'https://arc.msn.com/v3/Delivery/Cache?pid=209567&fmt=json&rafb=0&ua=WindowsShellClient%2F0&disphorzres=1920&dispvertres=1080&lo=80217&pl=en-US&lc=en-US&ctry=us&time={T}'
	print(url)
	response = requests.get(url)
	item = response.json()
	if item['status'] == 200:
		update_history(item)
		return item


def like(item):
	url = f'https://www.shikhersrivastava.com/windowsspotlightapi/like?_id='+item['_id']
	response = requests.get(url)
	data = response.json()
	print("LIKED")
	if(data['status'] == 200):
		return True
	else:
		return False

def dislike(item):
	url = f'https://www.shikhersrivastava.com/windowsspotlightapi/dislike?_id='+item['_id']
	response = requests.get(url)
	data = response.json()
	if(data['status'] == 200):
		return True
	else:
		return False