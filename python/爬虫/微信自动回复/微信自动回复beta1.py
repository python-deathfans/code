# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     itchat
   Description :
   Author :       86138
   date：          2019/1/13
-------------------------------------------------
   Change Activity:
                   2019/1/13:
-------------------------------------------------
"""

import itchat
from itchat.content import *
import requests
import datetime
import time
import random

def get_response(question):

    apikey = '9d19f2f79b0f43ec9406fc8ecdd91dab'
    url = 'http://www.tuling123.com/openapi/api?key=' + apikey + '&info=' + question

    res = requests.get(url).json()

    return res['text']

@itchat.msg_register(itchat.content.TEXT, isMpChat=True)
def reply_msg(msg):
    print("收到一条公众号信息：", msg['User']['NickName'], msg['Content'])
    itchat.send_msg( get_response(msg['Content'])+ '\nsend by 小机器人',toUserName=msg['FromUserName'])


@itchat.msg_register(TEXT,isFriendChat=True)
def auto_reply(msg):
    r_mess = get_response(msg['Content'])
    message = ['你好啊，扬扬','主人在忙，马上回你哈','虽然不在你身边，但是心还是和你一起哒',r_mess]
    
    users = itchat.search_friends("扬扬")    #找到用户
    userName = users[0]['UserName']

    if (msg['FromUserName'] == userName):

        print('消息内容:%s'% msg['Content'])
        itchat.send_msg( random.choice(message)+ '\nsend by 小机器人',toUserName=msg['FromUserName'])
        print("auto reply :%s"%(get_response(msg['Content'])))



if __name__ == '__main__':

    itchat.auto_login(hotReload=True)

    # itchat.send_msg('你好啊',toUserName='filehelper')

    itchat.run()


