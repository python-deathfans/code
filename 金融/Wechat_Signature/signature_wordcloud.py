import itchat
import jieba
import numpy as np
from PIL import Image
import wordcloud
from wordcloud import ImageColorGenerator


Image.MAX_IMAGE_PIXELS = 2300000000

# 登录微信
itchat.auto_login(hotReload=True)

friends = itchat.get_friends(update=True)[1:]
signature_list = []

for f in friends:
    # 获取个性签名
    signature = f['Signature']

    if 'emoji' in signature:
        pass
    else:
        signature_list.append(signature)

signature_string = " ".join(signature_list)

signature_cut = jieba.lcut(signature_string)
signature_cut_join = " ".join(signature_cut)

# print(signature_cut_join)

# with open('alice.txt', encoding='utf-8') as f:
#     txt = f.read()

mask = np.array(Image.open("4.jpg"))

wc = wordcloud.WordCloud(
    background_color='white',
    width=1000, height=700, font_path='msyh.ttc',
    max_words=500, mask=mask, scale=15,
    stopwords={'你', '的', '是', '我', '有', '了', '都', '就'},
    # contour_width=1,
    # contour_color='steelblue'
)

wc.generate(signature_cut_join)

img_colors = ImageColorGenerator(mask)

wc.recolor(color_func=img_colors)

wc.to_file("qq3.png")

print("词云制作成功")