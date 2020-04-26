import requests
import time

def translate(word):

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    data = {}

    data['i'] = word
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'
    data['typoResult'] = 'false'

    html=requests.post(url,data = data)
    html.encoding = html.apparent_encoding

    return html.json()['translateResult'][0][0]['tgt']

if __name__=='__main__':

    while True:
        info = input('请输入需要翻译的内容（支持英汉互译（输入q退出））：')
        if info == 'q':
            break
        else:
            print(translate(info))
            time.sleep(3)
            continue




