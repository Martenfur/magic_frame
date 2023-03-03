import subprocess
import witty.witty_const as witty_const

def i2c_write(address, value):
	for i in range(5):
		try:
			cmd = "i2cset -y 0x01 " + witty_const.I2C_MC_ADDRESS + " " + str(address) + " " + str(value)
			subprocess.run(cmd, shell = True)
			return
		except:
			pass

def i2c_read(address):
	for i in range(5):
		try:
			cmd = "i2cget -y 0x01 " + witty_const.I2C_MC_ADDRESS + " " + str(address)
			out = subprocess.check_output(cmd, shell = True).decode('utf8')
			return out
		except:
			return "0x00"


def read_register_hex(address):
	out = i2c_read(address)
	return int(out.replace("0x", ""), 16)

def read_register_bcd(address):
	out = i2c_read(address)
	# Ok so, this is not a mistake, there is no conversion from HEX to decimal
	# because Witty Pi stores its registers in a weird format that is actually 
	# HEX but visually, represents a base-10 number. So, for example, 
	# 0x23 is actually 23. 
	# Why? No fucking idea!
	return int(out.replace("0x", ""))

def write_register_bcd(address, value):
	i2c_write(address, "0x" + str(value))
