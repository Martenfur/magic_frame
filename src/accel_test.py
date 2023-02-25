# Test script for driving an accelerometer. 
# Before running, run:
# sudo pip3 install adafruit-circuitpython-ADXL34x

import time
import orientation


while True:
	orientation.update()
	print(orientation.get())
	time.sleep(0.1)