# Test script for driving an accelerometer. 
# Before running, run:
# sudo pip3 install adafruit-circuitpython-ADXL34x


import time
import board
import busio
import adafruit_adxl34x

i2c = busio.I2C(board.SCL, board.SDA)
accel = adafruit_adxl34x.ADXL345(i2c)

def get_orientation():
	global accel
	x = accel.acceleration[0]
	y = accel.acceleration[1]
	z = accel.acceleration[2]
	#print("x: " + str(x) + " y: " + str(y) +" z: " + str(z))

	if abs(z) > 9:
		print("top")
		return

	if abs(x) > abs(y):
		if x < 0:
			print("left")
		else:
			print("right")
	else:
		if y < 0:
			print("bottom")
		else:
			print("top")

while True:
	get_orientation()
	time.sleep(0.1)