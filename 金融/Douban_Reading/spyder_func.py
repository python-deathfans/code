import requests
from fake_useragent import UserAgent
import random
from time import sleep
import pandas as pd
import os
from lxml import html


def get_url_list(num):

    base_url = 'https://book.douban.com/top250?start='
    url_list_ = []

    for i in range(num):
        url = base_url + str(i*25)
        url_list_.append(url)

    return url_list_


def get_html(url_):
    sleep(random.randint(1, 3) + random.random())

    headers = {"User-Agent": str(UserAgent().random)}

    response = requests.get(url_, headers=headers, timeout=60)
    response.encoding = response.apparent_encoding

    if response.status_code == 200:
        print("成功获取源代码")

        return response.text
    else:
        print("获取源代码失败")

        return None


def parse_html(html_):

    etree = html.etree
    html_ = etree.HTML(html_)

    table_tag_list = html_.xpath("//table[@width='100%']")
    # print(table_tag_list)

    parse_book_data(table_tag_list)
    urls = html_.xpath("//div[@class='paginator']/a/@href")

    return urls


def parse_book_data(table_tag):

    for table in table_tag:

        book = {}

        title = table.xpath(".//a/@title")[0]
        produce = table.xpath(".//td[@valign='top']/p[1]/text()")[0].strip().split('/')
        author = produce[0]
        press_time = produce[-2] if "-" in produce[-2] else produce[-3]
        money = produce[-1]
        rating_num = table.xpath(".//span[@class='rating_nums']/text()")[0]
        rating_people = table.xpath(".//div[@class='star clearfix']/span[3]/text()")[0].replace(" ", "").replace("(",
                                                                                                                 "").replace(
            ")", "").replace("\n", "")
        short_produce_ = table.xpath(".//span[@class='inq']/text()")
        short_produce = short_produce_[0] if len(short_produce_) > 0 else "空"
        poster_url = table.xpath(".//td[@width='100']//img/@src")[0]

        # print(poster_url)

        book['title'] = title
        book['author'] = author
        book['press_time'] = press_time
        book['money'] = money
        book['rating_num'] = rating_num
        book['rating_people'] = rating_people
        book['short_produce'] = short_produce

        POSTER_URLS.append(poster_url)
        DATA.append(book)


def download_img(title, url_):

    headers = {'User-Agent': UserAgent().random}

    img = requests.get(url_, headers=headers).content

    suffix = url_.split(".")[-1]

    with open(title + '.' + suffix, 'wb') as f:
        f.write(img)
    print("正在下载:", url_)


def save_data():

    df = pd.DataFrame(DATA, columns=['title', 'author', 'press_time', 'money',
                                     'rating_num', 'rating_people', 'short_produce'])
    df.to_csv('book_top250.csv', encoding='utf_8_sig', index=None)

    print("书籍保存成功")

    titles = [i['title'] for i in DATA]

    if 'poster' not in os.listdir():
        os.mkdir('poster')
    os.chdir('poster')

    for t, url_ in zip(titles, POSTER_URLS):
        download_img(t, url_)


if __name__ == '__main__':

    url_list = get_url_list(10)
    DATA = []
    POSTER_URLS = []

    for url in url_list:
        html_ = get_html(url)
        parse_html(html_)

    print(len(POSTER_URLS))
    save_data()
