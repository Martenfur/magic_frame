from image_sources.aggregation import AggregationImageSource
from image_sources.artstation import ArtstationImageSource
from image_sources.deviantart import DeviantartImageSource
from image_sources import img_utils
import orientation

import PIL
from PIL import Image, ImageEnhance
import io

source = DeviantartImageSource()
#source = ArtstationImageSource()
#source = AggregationImageSource()

orientation.update()

if orientation.is_landscape():
	img = source.get_image(True)
	img = img_utils.resize_image(img, 800, 480)
else:
	img = source.get_image(False)
	img = img_utils.resize_image(img, 480, 800)

img = img_utils.rotate_image(img, orientation.get())

#img.show()

#converter = ImageEnhance.Color(img)
#img = converter.enhance(1.3)
#img.show()

pal_image = Image.new("P", (1,1))
pal_image.putpalette( (0,0,0,  255,255,255,  0,255,0,   0,0,255,  255,0,0,  255,255,0, 255,128,0) + (0,0,0)*249)

img.convert("RGB").quantize(palette=pal_image).show()

print("cock")
