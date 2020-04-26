# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     baiduimag
   Description :
   Author :       86138
   date：          2019/1/27
-------------------------------------------------
   Change Activity:
                   2019/1/27:
-------------------------------------------------
"""
import requests
from lxml import etree
import re
import os
import random
import time

def get_html(url):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    try:
        html = requests.get(url,headers = headers)
        html.encoding = html.apparent_encoding
        if html.status_code == 200:
            print('成功获取源代码')
            # print(html.text)
    except Exception as e:
        print('抓取源代码失败:%s' % e)

    return html.text

def parse_html(html):

    urls = re.findall('"objURL":"(.*?)"',html,re.S)

    return urls

def downloadimg(urls,name):

    if name in os.listdir():
        pass
    else:
        os.mkdir(name)
    os.chdir(name)

    i = 0
    for url in urls:
        time.sleep(random.randint(1,3) + random.random())
        imag = requests.get(url,timeout = 6).content

        if imag:
            with open(str(i) + '.jpg','wb') as f:
                print('正在下载第 %d 张图片：%s' % (i + 1,url))
                f.write(imag)
            i += 1
        else:
            print('链接超时，图片下载失败')
    print('图片下载成功')

if __name__ == '__main__':

    word = input('请您输入您需要下载图片的关键字：')
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&ct=201326592&v=flip'

    html = get_html(url)
    imgurls = parse_html(html)
    downloadimg(imgurls,word)