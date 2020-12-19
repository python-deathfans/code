import wordcloud
from PIL import Image

w = wordcloud.WordCloud(width=1000, height=700, background_color='white', font_path='msyh.ttc')

with open("./关于实施乡村振兴战略的意见.txt", encoding='utf-8') as f:
    txt = f.read()

w.generate(txt)

w.to_file('output3.png')

img = Image.open("./output3.png")   # type: Image.Image

img.show()
