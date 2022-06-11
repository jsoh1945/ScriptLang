#!/usr/bin/python
# coding=utf-8

import time
import sqlite3
import telepot
from pprint import pprint

from datetime import date, datetime

import noti

# 코로나 실시간 현황 정보 불러오기
def replyAptData(data_param, user):
    print(user)
    res_list = noti.getLiveInfo(data_param)

    msg = ''
    for r in res_list:
        print( str(datetime.now()).split('.')[0], r )
        if len(r+msg)+1>noti.MAX_MSG_LENGTH:
            noti.sendMessage( user, msg )
            msg = r+'\n'
        else:
            msg += r+'\n'
        if msg:
            noti.sendMessage( user, msg )

def save( user, loc_param ):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS \ users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    try:
        cursor.execute('INSERT INTO users(user, location) VALUES ("%s", "%s")' % (user, loc_param))
    except sqlite3.IntegrityError:
        noti.sendMessage( user, '이미 해당 정보가 저장되어 있습니다.' )
        return
    else:
        noti.sendMessage( user, '저장되었습니다.' )
        conn.commit()


def check( user ):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, locationTEXT, PRIMARY KEY(user, location) )')
    cursor.execute('SELECT * from users WHERE user="%s"' % user)
    for data in cursor.fetchall():
        row = 'id:' + str(data[0]) + ', location:' + data[1]
        noti.sendMessage( user, row )


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return
    data_param = msg['text']
    text = msg['text']
    args = text.split(' ')

    if data_param == '코로나 정보' or data_param == '일일 확진자' or data_param == '일일 신규입원자' or data_param == '일일 재원 위중증 발생자' or \
            data_param == '일일 사망자' or data_param == '인구 10만명당 사망률' or data_param == '재원 위중증 발생률':
        replyAptData(data_param, chat_id)

    else:
        noti.sendMessage(chat_id, '''모르는 명령어입니다. \n 다음과 같은 명령어를 입력해주세요! \n
        코로나 정보 : 코로나 정보와 관련한 통합적인 내용을 출력 \n
        일일 확진자 : 현재 일자 기준 일일 확진자 수 출력 \n
        일일 신규입원자 : 현재 일자 기준 신규 입원자 수 출력 \n
        일일 재원 위중증 발생자 : 일일 재원 위중증 발생자 수 출력 \n
        일일 사망자 : 현재 일자 기준 일일 사망자 수 출력 \n
        인구 10만명당 사망률 : 현재 인구 10만명당 사망률 출력 \n
        재원 위중증 발생률 : 재원 환자 중 위중증 발생률 출력 \n ''')


today = date.today()
current_month = today.strftime('%Y%m')

print('[', today, ']received token :', noti.TOKEN)

from noti import bot
pprint(bot.getMe())

bot.message_loop(handle)

print('Listening...')

while 1:
    time.sleep(10)
