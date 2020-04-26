import requests
from lxml import etree
import os
import time
import random

VIDEOURLS = []  #定义两个全局变量，把每一页的内容放到这个列表里面来，注意一般全局变量都是大写的
NAMES = []

def get_html(url):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    try:
        html = requests.get(url,headers = headers)
        html.encoding = 'utf-8'
        if html.status_code == 200:
            print('成功获取源代码')
            # print(html.text)
    except Exception as e:
        print('获取源代码失败:%s' % e)

    return html.text

def parse_html(html):

    html = etree.HTML(html)
    names = []
    videourls = []

    lis = html.xpath("//div[@class = 'j-r-list']/ul/li")    #存储每个段子的详细信息

    for li in lis:
        title = li.xpath(".//div[@class='j-r-list-c-desc']/a/text()")[0]    #把每个段子的名字抓取下来，方便存储的时候命名
        videourl = li.xpath(".//li[@title='下载视频']/a/@href")[0]          #把视频的url抓取下来

        names.append(title)
        videourls.append(videourl)

    return videourls,names

def download_video(name,url):

    if '百思不得姐video' in os.listdir(r'E:\code\python\爬虫练习\百思不得姐'):
        pass
    else:
        os.mkdir(r'E:\code\python\爬虫练习\百思不得姐\百思不得姐video')
    os.chdir(r'E:\code\python\爬虫练习\百思不得姐\百思不得姐video')

    video = requests.get(url,timeout = 6).content

    name = name.replace('.','').replace('\n','').replace('<<','').replace('>>','')

    with open(name + '.mp4','wb') as f:
        print('正在下载:%s' % url)
        f.write(video)


if __name__ == '__main__':

    page = int(input('请输入需要下载的页数:'))

    for i in range(page):

        url = 'http://www.budejie.com/video/' + str(i + 1)  #这里是因为range()数组是从零开始的，所以需要加1

        html = get_html(url)
        videourls = parse_html(html)[0]
        names = parse_html(html)[1]

        VIDEOURLS.extend(videourls)
        NAMES.extend(names)             #大家注意一下append和extend的区别

    for i in range(20 * page):
        time.sleep(random.randint(1,4) + random.random())   #使请求时间间隔变得随机一些，防止反扒的一个小细节
        download_video(NAMES[i],VIDEOURLS[i])


""""

2019年2月11日09:26:04

内容：
抓取百思不得姐搞笑视频
问题：
以后遇到循环的时候，路径必须写绝对路径，否则就会出现文件夹套文件夹的现象



"""