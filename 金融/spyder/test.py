import requests
from fake_useragent import UserAgent
from lxml import html
from time import sleep
import random

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
    def download(url):

        sleep(random.randint(1, 3)+random.random())

        headers = {"User-Agent": str(UserAgent().random)}

        response = requests.get(url, headers=headers, timeout=10)
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


# 数据处理
class DataProcessing(object):

    def save(self, data):
        pass


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
            html = self.downloader.download(url)
            data, urls = self.parser.parse(html)
            self.data_processing.save(data)
            self.url_manager.add_urls(urls)


if __name__ == '__main__':

    url = 'https://book.douban.com/top250?start=0'

    scheduler = Scheduler()

    scheduler.run(url)