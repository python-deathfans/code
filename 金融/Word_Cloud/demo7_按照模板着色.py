import wordcloud
from PIL import Image
from wordcloud import ImageColorGenerator
import numpy as np

mask = Image.open("alice_color.png")
mask = np.array(mask)

w = wordcloud.WordCloud(width=1000, height=700, background_color='white', mask=mask)

with open("alice.txt", encoding='utf-8') as f:
    txt = f.read()

w.generate(txt)

img_color = ImageColorGenerator(mask)

w.recolor(color_func=img_color)

w.to_file('按照模板着色.png')

img = Image.open("./按照模板着色.png")   # type: Image.Image

img.show()
