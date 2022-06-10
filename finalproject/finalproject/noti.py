#!/usr/bin/python
# coding=utf-8

import sys
import telepot
from pprint import pprint # 데이터를 읽기 쉽게 출력
import traceback


from LiveCoronaInfoJson import *

# 봇정보 : 코로나실시간정보봇 , @covid_live_info_bot
TOKEN = '5531212925:AAGHzN7uQWvYXVNecQO72jvSyc-Hfo8JGYI'
MAX_MSG_LENGTH = 300

bot = telepot.Bot(TOKEN)


def getLiveInfo(data_param):
    global LiveCoronaInfo

    res_list = []
    row = str()
    basedate = "기준 일시: " + "2022.0" + LiveCoronaInfo['mmddhh']

    if data_param == '코로나 정보':
        datconfrim = "일일 확진자: " + LiveCoronaInfo['cnt_confirmations'] + "명"
        datenewinmate = "일일 신규입원자: " + LiveCoronaInfo['cnt_hospitalizations'] + "명"
        datcritical = "일일 재원 위중증 발생자: " + LiveCoronaInfo['cnt_severe_symptoms'] + "명"
        datdeath = "일일 사망자: " + LiveCoronaInfo['cnt_deaths'] + "명"
        dat10death = "인구10만명당 사망률: " + LiveCoronaInfo['rate_deaths'] + "%"
        dat10newinmate = '인구 10만명당 신규입원률: ' + LiveCoronaInfo['rate_hospitalizations'] + "%"
        datcriticalrat = '재원 위중증 발생률: ' + LiveCoronaInfo['rate_severe_symptoms'] + "%"
        row = basedate + '\n' + '\n' + datconfrim + '\n' + datenewinmate + '\n' + datcritical + '\n' + datdeath + '\n' + dat10death + '\n' + dat10newinmate + '\n' + datcriticalrat

    elif data_param == '일일 확진자':
        datconfrim = "일일 확진자: " + LiveCoronaInfo['cnt_confirmations'] + "명"
        row = basedate + '\n' + '\n' + datconfrim + '\n'

    elif data_param == '일일 신규입원자':
        datenewinmate = "일일 신규입원자: " + LiveCoronaInfo['cnt_hospitalizations'] + "명"
        row = basedate + '\n' + '\n' + datenewinmate + '\n'

    elif data_param == '일일 재원 위중증 발생자':
        datcritical = "일일 재원 위중증 발생자: " + LiveCoronaInfo['cnt_severe_symptoms'] + "명"
        row = basedate + '\n' + '\n' + datcritical + '\n'

    elif data_param == '일일 사망자':
        datdeath = "일일 사망자: " + LiveCoronaInfo['cnt_deaths'] + "명"
        row = basedate + '\n' + '\n' + datdeath + '\n'

    elif data_param == '인구 10만명당 사망률':
        dat10deathrat = "인구 10만명당 사망률: " + LiveCoronaInfo['rate_deaths'] + "%"
        row = basedate + '\n' + '\n' + dat10deathrat + '\n'

    elif data_param == '인구 10만명당 신규입원률':
        dat10newinmate = '인구 10만명당 신규입원률: ' + LiveCoronaInfo['rate_hospitalizations'] + "%"
        row = basedate + '\n' + '\n' + dat10newinmate + '\n'

    elif data_param == '재원 위중증 발생률':
        datcriticalrat = '재원 위중증 발생률: ' + LiveCoronaInfo['rate_severe_symptoms'] + "%"
        row = basedate + '\n' + '\n' + datcriticalrat + '\n'

    res_list.append(row)

    return res_list


def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except: # 예외 정보와 스택 트레이스 항목을 인쇄.
        traceback.print_exception(*sys.exc_info(), file=sys.stdout)





