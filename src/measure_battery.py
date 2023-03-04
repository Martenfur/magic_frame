import config
config.load()
import witty.witty as witty 
import time
import datetime
import sys

# This utility is used to measure the voltage of the battery
# in order to determine its voltage range.
# Charge the battery to 100%, run this script and let it discharge fully.

filepath = "battery_data.txt"

if len(sys.argv) > 1:
	filepath = sys.argv[1]
print("Writing to " + filepath)

with open(filepath, "w") as myfile:
	myfile.write("time, vin, vout,\n")
while True:
	with open(filepath, "a") as myfile:
		for i in range(0, 10):
			now = datetime.datetime.now()
			in_voltage = witty.get_input_voltage()
			out_voltage = witty.get_output_voltage()
			myfile.write(now.strftime("%H:%M:%S") + ", ")
			myfile.write(str(out_voltage) + ", ")
			myfile.write(str(in_voltage) + ", ")
			myfile.write("\n")
			time.sleep(1)

