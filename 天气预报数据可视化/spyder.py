"""

2019年3月2日07:08:57
安徽省主要城市天气抓取
做一个可视化

"""

import requests
from lxml import etree
from time import sleep
import random
import pandas as pd

BASEURL = 'http://www.tianqihoubao.com/weather/'
WEATHER = []

def get_html(url):

    sleep(random.randint(1,3) + random.random())

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}

    try:
        html = requests.get(url,headers = headers,timeout = 40)
        html.encoding = html.apparent_encoding

        if html.status_code == 200:
            print('成功获取源代码')

            return html.text
    except Exception as e:
        print('获取源代码失败:%s' %e)

        return None

def parse_html(html):

    html = etree.HTML(html)
    url_suffixs = []

    td_tags = html.xpath("//td[@align='center']")

    for td_tag in td_tags:
        url_suffix = td_tag.xpath(".//a/@href")[0]
        url_suffixs.append(url_suffix)

    return url_suffixs

def get_weather(html):

    html = etree.HTML(html)
    weather = []

    tr_tags = html.xpath("//tr")[2:]

    global city

    for tr_tag in tr_tags:
        city = tr_tag.xpath(".//td[1]/b/text()")[0]
        date = tr_tag.xpath(".//a/text()")[0].split('(')[0]
        temperature = tr_tag.xpath(".//td[last()]/text()")[0]
        temperature = ''.join(temperature.split())[:-1]
        type = city + '最低气温'

        city_weather = {'name':city,'type':type,'value':temperature,'time':date}
        weather.append(city_weather)

    return weather

if __name__ == '__main__':

    url = 'http://www.tianqihoubao.com/weather/province.aspx?id=340000'

    html = get_html(url)
    city_list = parse_html(html)

    for ci in city_list:

        if ci == '黄山风景区':
            pass
        else:
            html = get_html(BASEURL + ci)

            if html:
                weather = get_weather(html)
                WEATHER.extend(weather)
            else:
                pass
    weather_data = pd.DataFrame(WEATHER)
    weather_data.to_csv('weather.csv',index=False,encoding='GBK')
    print('天气数据成功下载到本地')
