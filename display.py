import ctypes
from win32api import GetMonitorInfo, MonitorFromPoint
import os
# screensize1 = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) #Gets size of main display
# screensize_virtual = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79) Gets total size of virtual display in multi-monitor setup 
# screensize2 = screensize_virtual[0]- screensize1[0], screensize_virtual[1]- screensize1[1]

def get_orientation():
	# user32 = ctypes.windll.user32
	# width = user32.GetSystemMetrics(0)
	# height = user32.GetSystemMetrics(1)
	monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
	_, _, width, height = monitor_info.get("Monitor")
	print(width, height)
	if(width > height): orientation = 'landscape'
	else:  orientation = 'portrait'
	return orientation

def get_resolution():
	monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
	_, taskbar_height, width, height = monitor_info.get("Work")
	print(width, height, taskbar_height)
	return width, height, taskbar_height

def set_wallpaper(wallpaper):
	path = os.path.join(os.getcwd(), wallpaper)
	ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)