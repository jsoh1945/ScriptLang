#!/usr/bin/python
# coding=utf-8

import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
import re
from datetime import date, datetime

import noti


# date_param: 날짜, user: 사용자ID, loc_param:지역코드
def replyAptData(date_param, user, loc_param='11710'):
    print(user, date_param, loc_param)
    res_list = noti.getData( loc_param, date_param )

    # 하나씩 보내면 메세지 개수가 너무 많아지므로
    # 300자까지는 하나의 메세지로 묶어서 보내기.
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
        else:
            noti.sendMessage( user, '%s 기간에 해당하는 데이터가 없습니다.'%date_param)


# date_param: 날짜, user: 사용자ID, loc_param:지역코드
def replyAptData(data_param, user):
    print(user)
    res_list = noti.getLiveInfo(data_param)

    # 하나씩 보내면 메세지 개수가 너무 많아지므로
    # 300자까지는 하나의 메세지로 묶어서 보내기.
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

    # if data_param == '코로나 정보':
    #     #replyAptData(args[1], chat_id, args[2])
    #     replyAptData(data_param, chat_id)
    else:
        noti.sendMessage(chat_id, '''모르는 명령어입니다.''')

# def handle(msg):
#     content_type, chat_type, chat_id = telepot.glance(msg)
#     if content_type != 'text':
#         noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
#         return
#     text = msg['text']
#     args = text.split(' ')
#
#     if text.startswith('거래') and len(args) > 1:
#         print('try to 거래', args[1])
#         replyAptData(args[1], chat_id, args[2])
#     elif text.startswith('지역') and len(args) > 1:
#         print('try to 지역', args[1])
#         replyAptData('202205', chat_id, args[1])
#     elif text.startswith('저장') and len(args) > 1:
#         print('try to 저장', args[1])
#         save(chat_id, args[1])
#     elif text.startswith('확인'):
#         print('try to 확인')
#         check(chat_id)
#     else:
#         noti.sendMessage(chat_id, '''모르는 명령어입니다.''')



today = date.today()
current_month = today.strftime('%Y%m')

print('[', today, ']received token :', noti.TOKEN)

from noti import bot
pprint(bot.getMe())

bot.message_loop(handle)

print('Listening...')

while 1:
    time.sleep(10)
