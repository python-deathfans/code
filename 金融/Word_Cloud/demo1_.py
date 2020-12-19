import wordcloud
from PIL import Image

w = wordcloud.WordCloud()

w.generate('and that government of the people, by the people, for the people, shall not perish from the earth.')

w.to_file('output1.png')

img = Image.open("./output1.png")   # type: Image.Image

img.show()
