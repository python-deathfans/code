import requests
from lxml import etree

def get_html(url):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}

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

    lis = html.xpath("//ol[@class='commentlist']/li[@id]")  #每个li标签包含每张图片的所有信息

    for li in lis:
        imgurl = li.xpath(".//img/@src")[0]
        print(imgurl)

if __name__ == '__main__':

    url = 'http://jandan.net/ooxx/page-1#comments'

    html = get_html(url)
    imgurls = parse_html(html)