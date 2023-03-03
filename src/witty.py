import subprocess
import witty_const

def read_register(address):
	cmd = "i2cget -y 0x01 " + witty_const.I2C_MC_ADDRESS + " " + str(address)
	out = subprocess.check_output(cmd, shell = True).decode('utf8')
	# Ok so, this is not a mistake, there is no conversion from HEX to decimal
	# because Witty Pi stores its registers in a weird format that is actually 
	# HEX but visually, represents a base-10 number. So, for example, 
	# 0x23 is actually 23. 
	# Why? No fucking idea!
	return int(out.replace("0x", ""))


def print_rtc_time():
	year = read_register(witty_const.I2C_RTC_YEARS)
	month = read_register(witty_const.I2C_RTC_MONTHS)
	day = read_register(witty_const.I2C_RTC_DAYS)
	hour = read_register(witty_const.I2C_RTC_HOURS)
	minute = read_register(witty_const.I2C_RTC_MINUTES)
	second = read_register(witty_const.I2C_RTC_SECONDS)
	print("Current RTC date: " + str(hour) + ":" + str(minute) + ":" + str(second) + " " + str(day) + "." + str(month) + ".20" + str(year))

def print_startup_time():
	day = read_register(witty_const.I2C_CONF_DAY_ALARM1)
	hour = read_register(witty_const.I2C_CONF_HOUR_ALARM1)
	minute = read_register(witty_const.I2C_CONF_MINUTE_ALARM1)
	second = read_register(witty_const.I2C_CONF_SECOND_ALARM1)
	print("Scheduled startup date: " + str(hour) + ":" + str(minute) + ":" + str(second) + " " + str(day))

def print_shutdown_time():
	day = read_register(witty_const.I2C_CONF_DAY_ALARM2)
	hour = read_register(witty_const.I2C_CONF_HOUR_ALARM2)
	minute = read_register(witty_const.I2C_CONF_MINUTE_ALARM2)
	second = read_register(witty_const.I2C_CONF_SECOND_ALARM2)
	print("Scheduled startup date: " + str(hour) + ":" + str(minute) + ":" + str(second) + " " + str(day))


print_rtc_time()
print_startup_time()
print_shutdown_time()
