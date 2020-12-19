from PIL import Image
from MyQR import myqr as mq

img = Image.open("6.jpg")   # type: Image.Image

print(img.size)

words = 'https://space.bilibili.com/315510261'

mq.run(words=words, picture='7.gif', colorized=True, save_name='07.gif')

print("二维码成功生成")