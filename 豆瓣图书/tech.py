# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     tech
   Description :
   Author :       86138
   date：          2019/2/4
-------------------------------------------------
   Change Activity:
                   2019/2/4:
-------------------------------------------------
"""
import requests
from lxml import etree
import os
import pandas as pd

def get_html(url):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    try:
        html = requests.get(url,headers = headers)
        html.encoding = html.apparent_encoding
        if html.status_code == 200:
            print('成功获取源代码')
            # print(html.text)
    except Exception as e:
        print('抓取代码失败:%s' % e)

    return html.text

def parse_html(html):

    html = etree.HTML(html)
    tables = html.xpath("//div[@class='indent']//table")
    books = []
    imgurls = []

    for t in tables:
        title = t.xpath(".//td[@valign='top']//a/@title")[0]
        author = t.xpath(".//td[@valign='top']//p[1]/text()")[0].split('/')[0]
        price = t.xpath(".//td[@valign='top']//p[1]/text()")[0].split('/')[-1]
        press_time = t.xpath(".//td[@valign='top']//p[1]/text()")[0].split('/')[-2]
        rating_score = t.xpath(".//span[@class='rating_nums']/text()")[0]
        rating_nums = t.xpath(".//div[@class='star clearfix']/span[3]/text()")[0].replace('(','').replace(')','').replace(' ','').replace('\n','')
        produce = t.xpath(".//p[@class='quote']/span/text()")[0]
        imgurl = t.xpath(".//a/img/@src")[0]

        book = {'title':title,'author':author,'price':price,'press_time':press_time,'rating_score':rating_score,'rating_nums':rating_nums,'produce':produce}

        books.append(book)
        imgurls.append(imgurl)

    return books,imgurls

def downloadimg(url,book):

    if 'bookposter' in os.listdir(r'E:\code\python\爬虫练习\豆瓣图书'):
        pass
    else:
        os.mkdir(r'E:\code\python\爬虫练习\豆瓣图书\bookposter')
    os.chdir(r'E:\code\python\爬虫练习\豆瓣图书\bookposter')

    img = requests.request('GET',url).content

    with open(book['title'] + '.jpg','wb') as f:
        print('正在下载：%s' % url)
        f.write(img)

if __name__ == '__main__':

    url = 'https://book.douban.com/top250?start=0'

    html = get_html(url)
    books = parse_html(html)[0]
    imgurls = parse_html(html)[1]

    # for i in range(25):
    #     downloadimg(imgurls[i],books[i])

    bookdata = pd.DataFrame(books)
    bookdata.to_csv('book.csv')
    print('图书信息写入本地成功')