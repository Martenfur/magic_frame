import subprocess
import witty_const

def read_register(address):
	cmd = "i2cget -y 0x01 " + witty_const.I2C_MC_ADDRESS + " " + str(address)
	print(cmd)
	out = subprocess.check_output(cmd, shell = True).decode('utf8')
	return int(out.replace("0x", ""))


def print_rtc_time():
	year = read_register(witty_const.I2C_RTC_YEARS)
	month = read_register(witty_const.I2C_RTC_MONTHS)
	day = read_register(witty_const.I2C_RTC_DAYS)
	hour = read_register(witty_const.I2C_RTC_HOURS)
	minute = read_register(witty_const.I2C_RTC_MINUTES)
	second = read_register(witty_const.I2C_RTC_SECONDS)
	print("Current RTC date: " + str(hour) + ":" + str(minute) + ":" + str(second) + " " + str(day) + "." + str(month) + ".20" + str(year))

print_rtc_time()