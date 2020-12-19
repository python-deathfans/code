import wordcloud
from PIL import Image

w = wordcloud.WordCloud(width=1000, height=700, background_color='white', font_path='msyh.ttc')

w.generate('从明天起，做一个幸福的人。喂马、劈柴，周游世界。从明天起，关心粮食和蔬菜。我有一所房子，面朝大海，春暖花开')

w.to_file('output2.png')

img = Image.open("./output2.png")   # type: Image.Image

img.show()
