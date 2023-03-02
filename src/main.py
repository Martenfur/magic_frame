import config
config.load()

from epaper import epd 
from art import Art

# This file is meant to be run on a Raspberry Pi with all hardware installed.
# Run this from src directory.

downloaded_art = Art()

epd.display(downloaded_art.processed_image)
