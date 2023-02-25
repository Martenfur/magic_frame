# This code ONLY supports the ADXL34x accelerometers!!!
# You can get one at: https://www.adafruit.com/product/4097
# To enable this feature, run:
# sudo pip3 install adafruit-circuitpython-ADXL34x

import imp
try:
	imp.find_module('adafruit_adxl34x')
	stub = False
	import board
	import busio
	import adafruit_adxl34x
	i2c = busio.I2C(board.SCL, board.SDA)
	accel = adafruit_adxl34x.ADXL345(i2c)
except ImportError:
	# If the hardware is not present, we fall back to stub mode.
	stub = True

# Orientation tells which side is currently the top one.
# With current setup:
#                             
#             top             
#      +---------------+      
#      | +-----------+ |      
#      | |           | |      
#      | |           | |      
#      | |           | |      
# left | |           | | right
#      | |           | |      
#      | |           | |      
#      | |           | |      
#      | +-----------+ |      
#      +---------------+      
#           bottom            
#
# top: +x
# left: -y
# bottom: -x
# right: +y
orientation = "top"


# Polls the accelerometer and caches the orientation value.
def update():
	global stub
	if stub:
		# When operating in stub mode, the function will always return top orientation.
		return

	global accel, orientation
	x = accel.acceleration[0]
	y = accel.acceleration[1]
	z = accel.acceleration[2]

	if abs(z) > 9:
		orientation = "top"
		return

	if abs(x) > abs(y):
		if x < 0:
			orientation = "bottom"
		else:
			orientation = "top"
	else:
		if y < 0:
			orientation = "left"
		else:
			orientation = "right"

def get():
	return orientation

def is_landscape():
	global orientation
	return orientation == "left" or orientation == "right"
