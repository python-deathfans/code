import wordcloud
from PIL import Image
import jieba

w = wordcloud.WordCloud(width=1000, height=700,
                        background_color='white', font_path='msyh.ttc',
                        stopwords=set(['是', '之一', "的"]))

txt = '同济大学（Tongji University），简称“同济”，是中华人民共和国教育部直属，由教育部、国家海洋局和上海市共建的全国重点大学，历史悠久、声誉卓著，是国家“双一流”、“211工程”、“985' \
      '工程”重点建设高校，也是收生标准最严格的中国大学之一 '
txt_list = jieba.lcut(txt)
txt = " ".join(txt_list)

w.generate(txt)

w.to_file('output3.png')

img = Image.open("./output3.png")   # type: Image.Image

img.show()
