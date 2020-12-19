import requests
import itchat
from itchat.content import *
import datetime
import time


def get_response(question):

    apikey = '9d19f2f79b0f43ec9406fc8ecdd91dab'
    url = 'http://www.tuling123.com/openapi/api?key=' + apikey + '&info=' + question

    res = requests.get(url).json()

    return res['text']


@itchat.msg_register(TEXT, isFriendChat=True)
def auto_reply(msg):
    print('消息是:%s' % msg['Content'])
    auto_reply_ = get_response(msg['Content'])
    itchat.send_msg(auto_reply_ + '(send by python)',toUserName=msg['FromUserName'])
    print('auto_reply:{} (send by python)'.format(auto_reply_))


if __name__ == '__main__':

    jinshan_api = 'http://open.iciba.com/dsapi'

    itchat.auto_login(hotReload=True)

    itchat.run()
