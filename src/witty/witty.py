import subprocess
import witty.witty_const as witty_const
import witty.witty_io as witty_io

# Returns RTC time in h:m:s format.
def get_rtc_time():
	hour = witty_io.read_register_bcd(witty_const.I2C_RTC_HOURS)
	minute = witty_io.read_register_bcd(witty_const.I2C_RTC_MINUTES)
	second = witty_io.read_register_bcd(witty_const.I2C_RTC_SECONDS)
	return str(hour) + ":" + str(minute) + ":" + str(second)

# Returns RTC time in d:m:yyyy format.
def get_rtc_date():
	year = witty_io.read_register_bcd(witty_const.I2C_RTC_YEARS)
	month = witty_io.read_register_bcd(witty_const.I2C_RTC_MONTHS)
	day = witty_io.read_register_bcd(witty_const.I2C_RTC_DAYS)
	return str(day) + "." + str(month) + ".20" + str(year)

def set_rtc_datetime(time):
	witty_io.write_register_bcd(witty_const.I2C_RTC_YEARS, time.year - 2000)
	witty_io.write_register_bcd(witty_const.I2C_RTC_MONTHS, time.month)
	witty_io.write_register_bcd(witty_const.I2C_RTC_DAYS, time.day)
	witty_io.write_register_bcd(witty_const.I2C_RTC_HOURS, time.hour)
	witty_io.write_register_bcd(witty_const.I2C_RTC_MINUTES, time.minute)
	witty_io.write_register_bcd(witty_const.I2C_RTC_SECONDS, time.second)


# Returns scheduled startup time in d h:m:s format.
def get_startup_time():
	day = witty_io.read_register_bcd(witty_const.I2C_CONF_DAY_ALARM1)
	hour = witty_io.read_register_bcd(witty_const.I2C_CONF_HOUR_ALARM1)
	minute = witty_io.read_register_bcd(witty_const.I2C_CONF_MINUTE_ALARM1)
	second = witty_io.read_register_bcd(witty_const.I2C_CONF_SECOND_ALARM1)
	return str(day) + " " + str(hour) + ":" + str(minute) + ":" + str(second)

def set_startup_time(time):
	witty_io.write_register_bcd(witty_const.I2C_CONF_DAY_ALARM1, time.day)
	witty_io.write_register_bcd(witty_const.I2C_CONF_HOUR_ALARM1, time.hour)
	witty_io.write_register_bcd(witty_const.I2C_CONF_MINUTE_ALARM1, time.minute)
	witty_io.write_register_bcd(witty_const.I2C_CONF_SECOND_ALARM1, time.second)


# Returns scheduled shutdown time in d h:m:s format.
def get_shutdown_time():
	day = witty_io.read_register_bcd(witty_const.I2C_CONF_DAY_ALARM2)
	hour = witty_io.read_register_bcd(witty_const.I2C_CONF_HOUR_ALARM2)
	minute = witty_io.read_register_bcd(witty_const.I2C_CONF_MINUTE_ALARM2)
	second = witty_io.read_register_bcd(witty_const.I2C_CONF_SECOND_ALARM2)
	return str(day) + " " + str(hour) + ":" + str(minute) + ":" + str(second)

def set_shutdown_time(time):
	witty_io.write_register_bcd(witty_const.I2C_CONF_DAY_ALARM2, time.day)
	witty_io.write_register_bcd(witty_const.I2C_CONF_HOUR_ALARM2, time.hour)
	witty_io.write_register_bcd(witty_const.I2C_CONF_MINUTE_ALARM2, time.minute)
	witty_io.write_register_bcd(witty_const.I2C_CONF_SECOND_ALARM2, time.second)


def get_input_voltage():
	i = witty_io.read_register_hex(witty_const.I2C_VOLTAGE_IN_I)
	o = witty_io.read_register_hex(witty_const.I2C_VOLTAGE_IN_D)
	return i + o / 100

def get_output_voltage():
	i = witty_io.read_register_hex(witty_const.I2C_VOLTAGE_OUT_I)
	o = witty_io.read_register_hex(witty_const.I2C_VOLTAGE_OUT_D)
	return i + o / 100
