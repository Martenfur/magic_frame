from art import Art

# This is a test file meant to be run manually on a desktop
# to test out importers and other features.
# Run from src directory.

downloaded_art = Art()

downloaded_art.original_image.show()
downloaded_art.processed_image.show()

pal_image = Image.new("P", (1,1))
pal_image.putpalette((0,0,0,  255,255,255,  0,255,0,   0,0,255,  255,0,0,  255,255,0, 255,128,0) + (0,0,0)*249)

img.convert("RGB").quantize(palette=pal_image).show()
