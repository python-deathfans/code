import requests
from lxml import etree
import os
import pandas as pd

BOOKS = []
IMGURLS = []

def get_html(url):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    try:
        html = requests.get(url,headers = headers)
        html.encoding = html.apparent_encoding
        if html.status_code == 200:
            print('成功获取源代码')
            # print(html.text)
    except Exception as e:
        print('获取源代码失败:%s' % e)

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
        rating_num = t.xpath(".//div[@class='star clearfix']/span[3]/text()")[0].replace('(','').replace(')','').replace(' ','').replace('\n','')
        produce = t.xpath(".//p[@class='quote']/span/text()")

        if produce:
            book = {'title': title, 'author': author, 'price': price, 'press_time': press_time,
                    'rating_score': rating_score, 'rating_num': rating_num, 'produce': produce[0]}
        else:
            book = {'title':title,'author':author,'price':price,'press_time':press_time,'rating_score':rating_score,'rating_num':rating_num,'produce':None}

        imgurl = t.xpath(".//a/img/@src")[0]
        books.append(book)
        imgurls.append(imgurl)

    return books,imgurls

def downloadimg(url,name):

    if 'bookposter' in os.listdir(r'E:\code\python\爬虫练习\豆瓣图书'):
        pass
    else:
        os.mkdir(r'E:\code\python\爬虫练习\豆瓣图书\bookposter')
    os.chdir(r'E:\code\python\爬虫练习\豆瓣图书\bookposter')

    img = requests.get(url).content

    with open(name['title'] + '.jpg','wb')as f:
        print('正在下载:%s' % url)
        f.write(img)


if __name__ == '__main__':

    for i in range(10):

        url = 'https://book.douban.com/top250?start=' + str(i * 25)

        html = get_html(url)
        books = parse_html(html)[0]
        imgurls = parse_html(html)[1]

        BOOKS.extend(books)
        IMGURLS.extend(imgurls)

    for i in range(250):
        downloadimg(IMGURLS[i],BOOKS[i])

    os.chdir(r'E:\code\python\爬虫练习\豆瓣图书')

    bookdata = pd.DataFrame(BOOKS)
    bookdata.to_csv('book.csv',index=False)
    print('图书信息成功保存到本地')

