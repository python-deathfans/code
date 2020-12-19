import requests
from fake_useragent import UserAgent
from lxml import html
from time import sleep
import random
import pandas as pd
import os

"""
测试：爬虫类的写法
"""


# url管理器
class UrlManager(object):

    def __init__(self):
        self.new_url = []
        self.old_url = []

    # 获取一个url
    def get_url(self):
        url = self.new_url.pop()
        self.old_url.append(url)

        return url

    # 增加一个url
    def add_new_url(self, url):
        if url not in self.new_url and url and url not in self.old_url:
            self.new_url.append(url)

    # 增加多个url
    def add_urls(self, urls):
        for url in urls:
            self.add_new_url(url)

    # 判断是否还有可以抓取的url
    def has_new_url(self):
        return self.get_new_url_size() > 0

    # 获取已经爬取的数量
    def get_old_url_size(self):
        return len(self.old_url)

    # 获取还能爬取的数量
    def get_new_url_size(self):
        return len(self.new_url)


# 网络请求
class Downloader(object):

    @staticmethod
    def download(url_):

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


# 数据解析
class Parser(object):

    def parse(self, html_):

        etree = html.etree
        html_ = etree.HTML(html_)

        table_tag_list = html_.xpath("//table[@width='100%']")
        # print(table_tag_list)

        self.parse_book_data(table_tag_list)
        urls = html_.xpath("//div[@class='paginator']/a/@href")

        return urls

    def parse_book_data(self, table_tag):

        for table in table_tag:
            title = table.xpath(".//a/@title")[0]
            produce = table.xpath(".//td[@valign='top']/p[1]/text()")[0].strip().split('/')
            author = produce[0]

            for i, p in enumerate(produce):
                if "出版" in p or "书店" in p:
                    press = produce[i]

            press_time = produce[-2] if "-" in produce[-2] else produce[-3]
            money = produce[-1]
            rating_num = table.xpath(".//span[@class='rating_nums']/text()")[0]
            rating_people = table.xpath(".//div[@class='star clearfix']/span[3]/text()")[0].replace(" ", "").replace("(", "").replace(")", "").replace("\n", "")
            short_produce = table.xpath(".//span[@class='inq']/text()")[0]
            poster_url = table.xpath(".//td[@width='100']//img/@src")[0]

            DATA['title'].append(title)
            DATA['author'].append(author)
            DATA['press'].append(press)
            DATA['press_time'].append(press_time)
            DATA['money'].append(money)
            DATA['rating_num'].append(rating_num)
            DATA['rating_people'].append(rating_people)
            DATA['short_produce'].append(short_produce)

            POSTER_URLS.add(poster_url)


# 数据处理
class DataProcessing(object):

    def save(self):

        df = pd.DataFrame(DATA)
        df.to_csv('book_top250.csv', encoding='utf_8_sig', index=False)

        print("书籍保存成功")

        titles = DATA['title']

        if 'poster' not in os.listdir():
            os.mkdir('poster')
        os.chdir('poster')

        for t, url in zip(titles, POSTER_URLS):
            self.download_img(t, url)

    def download_img(self, title, url):

        headers = {'User-Agent': UserAgent().random}

        img = requests.get(url, headers=headers).content

        suffix = url.split(".")[-1]

        with open(title + '.' + suffix, 'wb') as f:
            f.write(img)
        print("正在下载:", url)


# 调度
class Scheduler(object):

    def __init__(self):
        self.url_manager = UrlManager()
        self.downloader = Downloader()
        self.parser = Parser()
        self.data_processing = DataProcessing()

    def run(self, url_):
        self.url_manager.add_new_url(url_)

        while self.url_manager.has_new_url():
            url_ = self.url_manager.get_url()
            html_ = self.downloader.download(url)
            urls = self.parser.parse(html_)
            self.url_manager.add_urls(urls)

        print(POSTER_URLS)

        self.data_processing.save()


if __name__ == '__main__':
    url = 'https://book.douban.com/top250?start=0'
    DATA = {'title': list(), 'author': list(), 'rating_num': list(),
            'rating_people': list(), 'short_produce': list(),
            'press': list(), 'press_time': list(), 'money': list()}
    POSTER_URLS = set()

    scheduler = Scheduler()

    scheduler.run(url)
