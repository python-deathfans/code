import wordcloud
from PIL import Image
import numpy as np

mask = Image.open("alice.png")
mask = np.array(mask)

w = wordcloud.WordCloud(width=1000, height=700, background_color='white', mask=mask, contour_width=1, contour_color='steelblue')

with open("alice.txt", encoding='utf-8') as f:
    txt = f.read()

w.generate(txt)

w.to_file('勾勒轮廓.png')

img = Image.open("./勾勒轮廓.png")   # type: Image.Image

img.show()
