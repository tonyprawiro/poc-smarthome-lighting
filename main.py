import sys
import mss
from PIL import Image
from time import sleep
from tplight import LB130
import colorsys
from pprint import pprint

# Refresh interval
refresh_interval = int(sys.argv[1])

# Target monitor number (main monitor = 1, then 2, 3, and so on)
target_num = int(sys.argv[2])

# Smart LED bulb IP address (TP Link Kasa LB130) 
bulb_ip_address = sys.argv[3]

light = LB130(bulb_ip_address)

light.transition_period = 0
light.brightness = 80

while True:

	# Enumerate monitors
	with mss.mss() as sct:

		# Get rid of the first, as it represents the "All in One" monitor:
		for num, monitor in enumerate(sct.monitors[1:], 1):

			if num == target_num:

				# Get raw pixels from the screen
				sct_img = sct.grab(monitor)

				# Create the Image
				img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")

				# Resize to 1x1 pixel
				img2 = img.resize((1,1))

				# Get the color of the only pixel
				color = img2.getpixel((0, 0))

				hue, saturation, value = colorsys.rgb_to_hsv(color[0], color[1], color[2])

				try:
					light.hue = value
					light.saturation = int(saturation * 100)
				except:
					pass

				r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)

				# Display color info (RGB tuple)
				print(color)

	sleep(refresh_interval)