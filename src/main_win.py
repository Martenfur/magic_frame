from art import Art

import PIL
from PIL import Image, ImageEnhance

downloaded_art = Art()

converter = ImageEnhance.Color(downloaded_art.processed_image)
img = converter.enhance(1.3)

downloaded_art.original_image.show()
downloaded_art.processed_image.show()

pal_image = Image.new("P", (1,1))
pal_image.putpalette((0,0,0,  255,255,255,  0,255,0,   0,0,255,  255,0,0,  255,255,0, 255,128,0) + (0,0,0)*249)

img.convert("RGB").quantize(palette=pal_image).show()

print("cock")
