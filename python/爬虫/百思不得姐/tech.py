import requests
from lxml import etree
import os

def get_html(url):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}

    try:
        html = requests.get(url,headers = headers)
        html.encoding = html.apparent_encoding
        if html.status_code == 200:
            print('获取源代码成功')
            # print(html.text)
    except Exception as e:
        print('获取源代码失败:%s' % e)

    return html.text

def parse_html(html):

    html = etree.HTML(html)
    lis = html.xpath("//div[@class='j-r-list']/ul/li")  #每个li标签代表一个段子
    videourls = []
    names = []

    for li in lis:
        title = li.xpath(".//div[@class='j-r-list-c-desc']/a/text()")[0]
        videourl = li.xpath(".//li[@title = '下载视频']/a/@href")[0]

        videourls.append(videourl)
        names.append(title)

    return videourls,names

def downloadvideo(url,name):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}

    if '百思不得姐video' in os.listdir(r'E:\code\python\爬虫练习\百思不得姐'):
        pass
    else:
        os.mkdir(r'E:\code\python\爬虫练习\百思不得姐\百思不得姐video')
    os.chdir(r'E:\code\python\爬虫练习\百思不得姐\百思不得姐video')

    video = requests.get(url,headers = headers).content

    with open(name + '.mp4','wb') as f:
        print('正在下载:%s' % url)
        f.write(video)

if __name__ == '__main__':

    url = 'http://www.budejie.com/video/'

    html = get_html(url)
    videourls = parse_html(html)[0]
    names = parse_html(html)[1]

    for i in range(20):
        downloadvideo(videourls[i],names[i])