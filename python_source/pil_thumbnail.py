from PIL import Image

img = Image.open("kitten.jpg", "r")
img.thumbnail((100, 100), Image.ANTIALIAS)
img.save("pil_thumbnail.jpg")
