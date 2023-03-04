import witty.witty as witty
import config
import subprocess
import datetime

def sync_rtc_time():
	now = datetime.datetime.now()
	witty.set_rtc_datetime(now)

def schedule_next_startup():
	now = datetime.datetime.now()

	if config.current.refresh_mode == "hourly":
		time = now + datetime.timedelta(hours = 1)
		time = time.replace(minute = 0, second = 0)
	elif config.current.refresh_mode == "debug":
		time = now + datetime.timedelta(
			hours = 0, 
			minutes = 3, 
			seconds = 0
		)
	else:
		time = now + datetime.timedelta(days = 1)
		split = config.current.daily_refresh_time.split(":")
		time = time.replace(
			hour = int(split[0]), 
			minute = int(split[1]), 
			second = 0
		)
	witty.set_startup_time(time)
	print("Scheduled startup to " + witty.get_startup_time())


def schedule_shutdown(min = 0, sec = 5):
	now = datetime.datetime.now()
	shutdown = now + datetime.timedelta(minutes = min, seconds = sec)
	witty.set_shutdown_time(shutdown)
	print("Scheduled shutdown to " + witty.get_shutdown_time())
