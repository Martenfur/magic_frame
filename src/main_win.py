import config
config.load()

from art import Art
from PIL import Image
from epaper import epd 

# This is a test file meant to be run manually on a desktop
# to test out importers and other features.
# Run from src directory.

art = Art()

epd.display(art.original_image)
epd.display(art.processed_image)

pal_image = Image.new("P", (1,1))
pal_image.putpalette((0,0,0,  255,255,255,  0,255,0,   0,0,255,  255,0,0,  255,255,0, 255,128,0) + (0,0,0)*249)

epd.display(art.processed_image.convert("RGB").quantize(palette=pal_image))
