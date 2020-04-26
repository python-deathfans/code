# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     jiangjie_fanyi
   Description :
   Author :       86138
   date：          2019/1/21
-------------------------------------------------
   Change Activity:
                   2019/1/21:
-------------------------------------------------
"""

import requests

def translate(url,info):

    data = {}

    data['i'] = info
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_REALTIME'
    data['typoResult'] = 'false'

    result = requests.post(url,data = data)
    result.encoding = result.apparent_encoding

    return result.json()['translateResult'][0][0]['tgt']


def main():

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    while 1:
        info = input('请输入您想要查的内容(q结束):')

        if info == 'q':
            break
        else:
            result = translate(url,info)
            print(result)
            continue

main()