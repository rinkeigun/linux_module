#from PIL import Image, ImageFilter
from PIL import Image

kitten = Image.open("kitten.jpg", "r")
resize = kitten.resize((100, 100))
resize.save("pil_resize.jpg", "JPEG", quality=100, optimize=True)
resize.show()
