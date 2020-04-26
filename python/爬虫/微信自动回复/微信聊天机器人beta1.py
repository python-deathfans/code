import requests
import itchat
from itchat.content import *
import datetime
import time

def get_sentence(api):

    sentence = requests.get(api)

    return sentence.json()

def get_weather_forcast():

    apikey = 'ffa2e199264d8575ebb6a165a272852c'
    url = 'http://v.juhe.cn/weather/index?format=2&cityname=济南&key=' + apikey
    weather_forcast = requests.get(url).json()

    return weather_forcast

def get_response(question):

    apikey = '9d19f2f79b0f43ec9406fc8ecdd91dab'
    url = 'http://www.tuling123.com/openapi/api?key=' + apikey + '&info=' + question

    res = requests.get(url).json()

    return res['text']

@itchat.msg_register(TEXT,isFriendChat=True)
def auto_reply(msg):
    print('消息是:%s' % msg['Content'])
    itchat.send_msg(get_response(msg['Content']) + '(send by python)',toUserName=msg['FromUserName'])
    print('auto_reply:%s' % get_response(msg['Content']))


if __name__ == '__main__':

    jinshanapi = 'http://open.iciba.com/dsapi'
    itchat.auto_login(hotReload=True)

    sentence = get_sentence(jinshanapi)
    content = sentence['content']   #抓取的英文句子
    translation = sentence['note']  #抓取的中文句子


    weather_forcast = get_weather_forcast()
    today_weather = weather_forcast['result']['today']
    temperature = today_weather['temperature']
    weather = today_weather['weather']
    wind = today_weather['wind']
    dressing_index = today_weather['dressing_index']
    dressing_advice = today_weather['dressing_advice']

    users = itchat.search_friends("秦空")    #找到用户
    userName = users[0]['UserName']

    while 1:
        t = datetime.datetime.now()
        hour = t.hour
        minute = t.minute

        if hour == 21 and minute == 46:
            itchat.send_msg('现在是北京时间：%s' % t,toUserName=userName)
            itchat.send_msg('%s:%s' % (content,translation),toUserName=userName)
            itchat.send_msg('天气:%s\n温度:%s\n风:%s穿衣指数:%s\n穿衣建议:%s' % (weather,temperature,wind,dressing_index,dressing_advice),toUserName=userName)

            break
        else:
            time.sleep(5)
            break

    itchat.run()
    time.sleep(86400)

