import requests
from lxml.html import etree
from time import sleep
import random
from fake_useragent import UserAgent
import os


def get_html(url_):

    sleep(random.random() + random.randint(1, 2))

    headers = {'User-Agent': UserAgent().random}

    res = requests.get(url_, headers=headers)
    res.encoding = res.apparent_encoding

    if res.status_code == 200:
        print("成功获取源代码")

        return res.text
    else:
        print("获取源代码失败")

        return None


def parse_html(html_):

    parsed = etree.HTML(html_)
    div_tag_list = parsed.xpath("//div[@class='col-md-6 col-lg-3']")

    for div in div_tag_list:
        img_url = div.xpath(".//img/@src")[0]
        img_title = div.xpath(".//img/@alt")[0]

        IMG_URL.append(img_url)
        IMG_TITLE.append(img_title)


def download_img():

    if 'IMG' not in os.listdir():
        os.mkdir('IMG')
    os.chdir('IMG')

    j = 0
    i_ = 0

    for url_, title in zip(IMG_URL, IMG_TITLE):
        img = requests.get(url_, headers={'User-Agent': UserAgent().random}).content

        suffix = url_.split(".")[-1]

        try:
            with open(title + "." + suffix, 'wb') as f:
                f.write(img)
            j += 1

            if j % 25 == 0:
                i_ += 1
                print(f"第{i_}页图片下载完成")
        except OSError as e:
            print(e)
    print(f"共下载了{j}张图片")


if __name__ == '__main__':

    base_url = 'http://www.xiaohuar.com/daxue/index_{}.html'
    page_num = 964//25 + 1
    IMG_URL = []
    IMG_TITLE = []

    for i in range(1, page_num+1):

        if i == 1:
            url = 'http://www.xiaohuar.com/daxue/index.html'

            html = get_html(url)
            parse_html(html)
        else:
            url = base_url.format(i)
            html = get_html(url)
            parse_html(html)
    print("图片url全部抓取成功")

    download_img()