from img_tool import multi_text, ImageFactory
from PIL import Image

background_size = (300, 300)
img = ImageFactory(Image.new('RGBA', background_size, color='white'))
text = 'Hello World!'
text_img = multi_text(text, default_size=30, default_color='red')
img.img_paste(text_img, align='center')
img.show()
