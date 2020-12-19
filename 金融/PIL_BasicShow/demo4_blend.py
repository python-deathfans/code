from PIL import Image

img1 = Image.open("1.jpg")      # type: Image.Image
img2 = Image.open("2.jpg")      # type: Image.Image

img2_resized = img2.resize(size=img1.size, Image.ANTIALIAS)