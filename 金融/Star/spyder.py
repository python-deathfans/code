import requests
from fake_useragent import UserAgent
from lxml.html import etree
from time import sleep
import random
import os


class UrlManager(object):

    def __init__(self):

        self.new_url = []
        self.old_url = []

    def get_url(self):

        url = self.new_url.pop()
        self.old_url.append(url)

        return url

    def has_new_url(self):

        return self.get_new_url_size() > 0

    def get_new_url_size(self):

        return len(self.new_url)

    def get_old_url_size(self):

        return len(self.old_url)

    def add_urls(self, urls):

        for url in urls:
            self.add_url(url)

    def add_url(self, url):

        if url and url not in self.new_url and url not in self.old_url:
            self.new_url.append(url)


class Downloader(object):

    @staticmethod
    def download(url):

        # print(url)

        try:

            sleep(random.random() + random.randint(1, 2))

            headers = {'User-Agent': UserAgent().Chrome}

            html = requests.get(url, headers=headers)
            html.encoding = html.apparent_encoding

            if html.status_code == 200:

                num_page = url.split('=')[-1]

                print(f"成功获取{num_page}页源代码")

                return html.text
        except requests.exceptions.ConnectionError as e:
            print("获取源代码失败:", e)

            return None


class Parser(object):

    @staticmethod
    def parse(html):

        parsed = etree.HTML(html)
        base = 'http://www.mingxing.com'

        li_tag_list = parsed.xpath("//li//img[@src]")

        for li in li_tag_list:
            img_url = li.xpath(".//@src")[0]
            img_title = li.xpath(".//@alt")[0]

            IMG_URL.append(img_url)
            IMG_TITLE.append(img_title)

        next_url = base + parsed.xpath("//a[@class='nt' and @title='下一页']/@href")[0]

        return next_url


class Saver(object):

    @staticmethod
    def save():

        if 'IMG' not in os.listdir():
            os.mkdir('IMG')
        os.chdir('IMG')

        j = 0
        i = 0

        for url, title in zip(IMG_URL, IMG_TITLE):
            img = requests.get(url, headers={'User-Agent': UserAgent().random}).content

            suffix = url.split(".")[-1]

            try:
                with open(title + "." + suffix, 'wb') as f:
                    f.write(img)
                j += 1

                if j % 24 == 0:
                    i += 1
                    print(f"第{i}页图片下载完成")
            except OSError as e:
                print(e)
        print(f"共下载了{j}张图片")


class Scheduler(object):

    def __init__(self):

        self.url_manager = UrlManager()
        self.downloader = Downloader()
        self.parser = Parser()
        self.saver = Saver()

    def run(self, url):

        html = self.downloader.download(url)
        next_url = self.parser.parse(html)

        while next_url:
            html = self.downloader.download(next_url)
            next_url = self.parser.parse(html)

            if next_url.split('=')[-1] == '149':
                break

        self.saver.save()


if __name__ == '__main__':

    base_url = 'http://www.mingxing.com/tuku/index?type=mxxz&p=1'
    IMG_URL = []
    IMG_TITLE = []

    scheduler = Scheduler()
    scheduler.run(base_url)


