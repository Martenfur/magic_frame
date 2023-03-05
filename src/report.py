import ilog
import battery
import orientation
import datetime
import witty.witty as witty


def report(art):
	try:
		ilog.log("datetime: " + str(datetime.datetime.now()))
		ilog.log("name: " + art.image_name)
		ilog.log("source: " + art.image_source)
		ilog.log("url: " + art.image_url)
		ilog.log("scheduled_startup: " + witty.get_startup_time())
		ilog.log("battery: " + str(battery.get_battery_percentage()) + "%")
		ilog.log("orientation: " + orientation.get())
	except:
		pass
	ilog.log("==========================================")
	ilog.dump()
