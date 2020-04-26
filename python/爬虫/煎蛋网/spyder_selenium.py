# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     spyder_selenium
   Description :
   Author :       86138
   date：          2019/2/20
-------------------------------------------------
   Change Activity:
                   2019/2/20:
-------------------------------------------------
"""

from selenium import webdriver
from lxml import etree

def get_html(url):

    option = webdriver.ChromeOptions()
    option.add_argument('--user-data-dir = C:\\Users\\86138\\AppData\\Local\\Google\\Chrome\\User Data')
    broswer = webdriver.Chrome(chrome_options=option)

    try:
        broswer.get(url)
    finally:
        broswer.close()

    return broswer.page_source

if __name__ == '__main__':

    url = 'http://www.baidu.com'

    html = get_html(url)