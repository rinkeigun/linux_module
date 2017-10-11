#from PIL import Image, ImageFilter
#from PIL import Image
from PIL import Image, ImageDraw, ImageFont

text_canvas = Image.new("RGB", (80, 40), (250, 250, 250))
draw = ImageDraw.Draw(text_canvas)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf", 15)
draw.text((10,10), "hogehoge", font=font, fill="#000")
text_canvas.save("pil_draw.jpg", "JPEG", quality=100, optimize=True)
