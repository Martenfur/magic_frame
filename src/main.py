from image_sources.aggregation import AggregationImageSource
from image_sources.artstation import ArtstationImageSource
from image_sources.deviantart import DeviantartImageSource
from image_sources import img_utils

import PIL
from PIL import Image
import io

source = DeviantartImageSource()
#source = ArtstationImageSource()
#source = AggregationImageSource()

if True:
	img = source.get_image(True)
	img = img_utils.resize_image(img, 800, 480)
else:
	img = source.get_image(False)
	img = img_utils.resize_image(img, 480, 800)


img.show()

pal_image = Image.new("P", (1,1))
pal_image.putpalette( (0,0,0,  255,255,255,  0,255,0,   0,0,255,  255,0,0,  255,255,0, 255,128,0) + (0,0,0)*249)
pal_image1 = Image.new("P", (1,1))
pal_image1.putpalette( (0,0,0, 217,242,255, 3,124,76, 27,46,198, 245,80,34, 255,255,68, 239,121,44) + (0,0,0)*249)


# Convert the soruce image to the 7 colors, dithering if needed

#img.convert("P", colors=4096, dither=0).show()
#img.convert("P", colors=4096, dither=0).convert("RGB").quantize(palette=pal_image).show()
img.convert("RGB").quantize(palette=pal_image).show()
#img.convert("RGB").quantize(palette=pal_image1).show()

#image_7color = img.convert("P", colors=7, dither=1)#.quantize(palette=pal_image)
#image_7color.save("temp_7color.png")
#image_7color.show()


print("cock")
