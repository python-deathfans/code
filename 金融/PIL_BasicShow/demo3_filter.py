from PIL import Image
from PIL import ImageFilter

imgF = Image.open("2.jpg")

bluF = imgF.filter(ImageFilter.BLUR)                ##均值滤波
conF = imgF.filter(ImageFilter.CONTOUR)             ##找轮廓
edgeF = imgF.filter(ImageFilter.FIND_EDGES)         ##边缘检测

imgF.show()
bluF.show()
conF.save("2_outline.jpg")
conF.show()
edgeF.show()