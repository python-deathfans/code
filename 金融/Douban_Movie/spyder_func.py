import requests
from fake_useragent import UserAgent
import random
from time import sleep
import pandas as pd
import os
from lxml import html


def get_url_list(num):

    base_url = 'https://movie.douban.com/top250?start='
    urls = []

    for i in range(num):
        url = base_url + str(i*25)
        urls.append(url)

    return urls


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


def remove_blank(contents):

    for i, c in enumerate(contents):
        contents[i] = "".join(c.split()).replace("\n", "").replace(" ", "")

    return contents


def parse_html(res):

    etree = html.etree
    parsed = etree.HTML(res)

    li_tags = parsed.xpath("//ol[@class='grid_view']/li")

    for li in li_tags:

        movie_dic = {}

        movie = li.xpath(".//div[@class='hd']/a/span[1]/text()")[0]
        short = li.xpath(".//div[@class='bd']/p[1]/text()")
        short = remove_blank(short)
        director_stars = short[0]
        time_ = short[1].split('/')[0]
        address = short[1].split('/')[1]
        type_ = short[1].split('/')[-1]
        rating_num = li.xpath(".//span[@class='rating_num']/text()")[0]
        rating_people = li.xpath("//div[@class='star']/span[4]/text()")[0]
        short_produce_ = li.xpath(".//span[@class='inq']/text()")
        short_produce = short_produce_[0] if len(short_produce_) > 0 else "空"
        poster_url = li.xpath(".//a/img[@src]/@src")[0]

        movie_dic['movie'] = movie
        movie_dic['director_stars'] = director_stars
        movie_dic['time'] = time_
        movie_dic['address'] = address
        movie_dic['type'] = type_
        movie_dic['rating_num'] = rating_num
        movie_dic['rating_people'] = rating_people
        movie_dic['short_produce'] = short_produce

        POSTER_URLS.append(poster_url)
        MOVIE_DATA.append(movie_dic)


def download_img(title, url_):

    headers = {'User-Agent': UserAgent().random}

    img = requests.get(url_, headers=headers).content

    suffix = url_.split(".")[-1]

    with open(title + '.' + suffix, 'wb') as f:
        f.write(img)
    print("正在下载:", url_)


def save():

    df = pd.DataFrame(MOVIE_DATA, columns=['movie', 'director_stars', 'time', 'address',
                                           'type', 'rating_num', 'rating_people', 'short_produce'])

    print(df)

    df.to_csv('movie_top250.csv', encoding='utf_8_sig', index=None)

    print("电影信息保存成功")

    titles = [i['movie'] for i in MOVIE_DATA]

    if 'poster' not in os.listdir():
        os.mkdir('poster')
    os.chdir('poster')

    for t, url_ in zip(titles, POSTER_URLS):
        download_img(t, url_)


if __name__ == '__main__':

    url_list = get_url_list(10)
    MOVIE_DATA = []
    POSTER_URLS = []

    for url in url_list:
        response = get_html(url)
        parse_html(response)

    print(MOVIE_DATA)

    save()
