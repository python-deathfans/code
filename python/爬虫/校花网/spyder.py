import requests
from lxml import etree
import time
import random
import os
import threading

# os.chdir(r"C:\Users\Administrator\Desktop\file\code\Python\爬虫练习\校花网")

IMGURL = []
IMGNAME = []
RLOCK = threading.Lock()


class Spyder:
    def __init__(self, url):
        self.url = url
        self.html = self.gethtml()
        self.imgurl = self.parsehtml()[0]
        self.imgname = self.parsehtml()[1]

    def gethtml(self):

        time.sleep(random.randint(1, 3) + random.random())

        try:
            headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}

            html = requests.get(self.url, headers=headers)
            html.encoding = html.apparent_encoding

            if html.status_code == 200:
                print("成功获取源代码")
                # print(html.text)

                return html.text
        except Exception as e:
            print("获取源代码失败:",e)

    def parsehtml(self):
        html = etree.HTML(self.html)
        imgurllist = []
        imgnamelist = []

        div_tag_list = html.xpath("//div[@class='tp_list']")

        for div in div_tag_list:
            imgurl = div.xpath(".//img/@src")[0]
            imgname = div.xpath(".//img/@alt")[0]

            imgurllist.append(imgurl)
            imgnamelist.append(imgname)

        return imgurllist,imgnamelist


def downloadimg():

    if "校花图片" not in os.listdir(r"C:\Users\Administrator\Desktop\file\code\Python\爬虫练习\校花网"):
        os.mkdir(r"C:\Users\Administrator\Desktop\file\code\Python\爬虫练习\校花网\校花图片")
    os.chdir(r"C:\Users\Administrator\Desktop\file\code\Python\爬虫练习\校花网\校花图片")

    while 1:
        RLOCK.acquire()

        if len(IMGNAME) == 0:
            RLOCK.release()

            break
        else:
            imgurl = IMGURL.pop()
            imgname = IMGNAME.pop()
            img = requests.get(imgurl)

            RLOCK.release()

            suffix = imgurl.split('.')[-1]

            with open(imgname + "." + suffix, "wb") as f:
                print("正在下载:", imgurl)
                f.write(img.content)


def mythread():
    threads = []

    for _ in range(3):
        t = threading.Thread(target=downloadimg)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()



if __name__ == '__main__':
    start = time.time()

    for i in range(1, 10):
        url = "https://nice.ruyile.com/?f=5&p={}".format(i)

        spyder = Spyder(url)
        imgurllist = spyder.imgurl
        imgnamelist = spyder.imgname

        IMGURL.extend(imgurllist)
        IMGNAME.extend(imgnamelist)

    thread = threading.Thread(target=mythread)
    thread.start()
    thread.join()

    end = time.time()

    print("花费了:%d s"% int(end-start))