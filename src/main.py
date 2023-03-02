import epaper 
from art import Art

import PIL
from PIL import ImageEnhance

downloaded_art = Art()

converter = ImageEnhance.Color(downloaded_art.processed_image)
img = converter.enhance(1.3)

epaper.display(img)

print("cock")
