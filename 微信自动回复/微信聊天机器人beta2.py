# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     微信聊天机器人beta2
   Description :
   Author :       86138
   date：          2019/3/1
-------------------------------------------------
   Change Activity:
                   2019/3/1:
-------------------------------------------------
"""

import requests
import itchat
from itchat.content import *

def get_response(question):

    apikey = '9d19f2f79b0f43ec9406fc8ecdd91dab'
    url = 'http://www.tuling123.com/openapi/api?key=' + apikey + '&info=' + question

    res = requests.get(url).json()

    return res['text']

#个人聊天自动回复
@itchat.msg_register(TEXT,isFriendChat=True)
def auto_reply(msg):
    print('消息是:%s' % msg['Content'])
    itchat.send_msg(get_response(msg['Content']) + '(send by python)',toUserName=msg['FromUserName'])
    print('auto_reply:%s' % get_response(msg['Content']))

#群聊自动回复
@itchat.msg_register([TEXT,PICTURE],isGroupChat=True)
def reply(msg):
    if msg['Type'] == TEXT:
        return 'i received: %s' % (msg['Content'])


if __name__ == '__main__':

    itchat.auto_login(hotReload=True)
    itchat.run()




