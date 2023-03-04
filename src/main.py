import config
config.load()

from epaper import epd 
from art import Art
import startup_scheduler

# This file is meant to be run on a Raspberry Pi with all hardware installed.
# Run this from src directory.

# RTC time on Witty Pi should be the same as the onboard time.
startup_scheduler.sync_rtc_time()
# Schedule shutdown in 10 minutes jsut in case something goes wrong 
# and the script doesn't finish properly.
startup_scheduler.schedule_shutdown(min = 10, sec = 0)
startup_scheduler.schedule_next_startup()


downloaded_art = Art()
epd.display(downloaded_art.processed_image)

# Shutting down...
startup_scheduler.schedule_shutdown(sec = 30)
