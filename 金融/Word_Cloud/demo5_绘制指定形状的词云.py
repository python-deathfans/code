import wordcloud
from PIL import Image
import jieba
import numpy as np

mask = Image.open("wujiaoxing.png")
mask = np.array(mask)

w = wordcloud.WordCloud(width=1000, height=700, background_color='white',
                        font_path='msyh.ttc', mask=mask, scale=15,
                        stopwords=set(['的', '和']))

with open("关于实施乡村振兴战略的意见.txt", encoding='utf-8') as f:
    txt = f.read()

txt_list = jieba.lcut(txt)
txt = " ".join(txt_list)

w.generate(txt)

w.to_file('绘制指定形状词云.png')

img = Image.open("./绘制指定形状词云.png")   # type: Image.Image

img.show()
