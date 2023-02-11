from image_sources.artstation import ArtstationImageSource
import PIL
from PIL import Image
import io

source = ArtstationImageSource()
img = source.get_image(True)

pal_image = Image.new("P", (1,1))
pal_image.putpalette( (0,0,0,  255,255,255,  0,255,0,   0,0,255,  255,0,0,  255,255,0, 255,128,0) + (0,0,0)*249)

# Convert the soruce image to the 7 colors, dithering if needed
image_7color = img.convert("RGB").quantize(palette=pal_image)
image_7color.save("temp_7color.png")
image_7color.show()
img.show()

print("cock")
