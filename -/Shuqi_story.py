import re
import requests
import json
import urllib
import time
import timeit
import math
import random
import sys
from datetime import datetime
from dateutil import tz
import gzip
import os

Gamename='ShiQi_Story'
osenviron={}
IDARY=[]


result=''
header = {}
sign_bd=''
video_bd=''
draw_bd=''
with_bd=''
tm_bd=''
yuan1_bd=''
bubble_bd=''

tmlong=1

sign_bdlist=[]
video_bdlist=[]
draw_bdlist=[]
with_bdlist=[]
tm_bdlist=[]
yuan1_bdlist=[]
bubble_bdlist=[]


djj_tele_cookie=''
header={"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Connection": "keep-alive","Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18D52 AliApp(shuqi/4.3.6.0) WindVane/8.6.1 Shuqi (iPhone11,8__shuqi__v4.3.6.0) 828x1792 Winding(WV_19) WK",}






def spring_earn():
   getsign()
   draw()
   lottery_10()
   with_()
   
   boxTask()
   Prisecenter()
 


def boxTask():
   print('\n boxTask')
   try:
     msg=''

     response = requests.get('https://ocean.shuqireader.com/api/activity/v1/activity/boxTask?activityId=309&appVer=4.3.6.0&placeId=111111&ver=210301&platform=1&userId='+userId,headers=header)
     Res=response.json()
     print(Res['message'])
     if Res['status']=='200':
        msg+=f'''|{Res['data']['readTime']}|'''
     loger(msg)
   except Exception as e:
      msg=str(e)
      print(msg)


      
def getsign():
   print('\n sign')
   try:
     msg=''
     if(sign_bd=='xxx'):
       return 
     response = requests.post('https://ocean.shuqireader.com/api/activity/xapi/signin/v5/signInAction',headers=header,data=sign_bd)
     Res=response.json()
     print(Res['message'])
     
   except Exception as e:
      msg=str(e)
      print(msg)

def draw():
   print('\n draw')
   try:
     msg=''

     response = requests.post('https://ocean.shuqireader.com/api/activity/activity/v1/lottery/draw?asac=2A20C07RJ9F51AOEFSNHDR',headers=header,data=draw_bd)
     Res=response.json()
     print(Res['message'])
     
   except Exception as e:
      msg=str(e)
      print(msg)
      
      
def lottery_10():
   print('\n lottery_10')
   try:
     msg=''

     response = requests.post('https://ocean.shuqireader.com/api/ad/v1/api/prize/lottery',headers=header,data=video_bd)
     Res=response.json()
     print(Res['message'])
     
   except Exception as e:
      msg=str(e)
      print(msg)
      
def with_():
   print('\n with_')
   try:
     msg=''

     response = requests.post('https://ocean.shuqireader.com/api/activity/xapi/gold/withdraw/info',headers=header,data=with_bd)
     Res=response.json()
     print(Res['message'])
     if Res['status']=='200':
        msg=f'''{Res['data']['withdrawableCash']}|{Res['data']['gold']}'''
     loger(msg)
   except Exception as e:
      msg=str(e)
      print(msg)
      
      
def bubble():
   print('\n bubble')
   try:
     msg=''

     response = requests.post('https://ocean.shuqireader.com/api/prizecenter/xapi/prize/bubble/info',headers=header,data=bubble_bd)
     Res=response.json()
     print(Res)
     if Res['status']=='200':
        msg=f'''|阅读金币{Res['data']['totalGold']}'''
        if Res['data']['totalGold']>0:
          response = requests.post('https://ocean.shuqireader.com/api/prizecenter/xapi/prize/manual/receive',headers=header,data=bubble_bd)
          Res=response.json()
          print(Res)
     loger(msg)
     
   except Exception as e:
      msg=str(e)
      print(msg)
      
def Prisecenter():
   print('\n Prisecenter')
   try:
     msg=''
     sbd=f'''&activityId=232&userId={userId}&sign=809011b55f94797d7ffd0482c48d1480&key=sq_h5_gateway&{with_bd[with_bd.find('_public='):len(with_bd)]}'''
     response = requests.get(f'''https://ocean.shuqireader.com/api/activity/xapi/gold/amount?{sbd}''',headers=header)
     Res=response.json()
     print(Res['message'])
     if Res['status']=='200':
        msg=f'''{Res['data']['todayCoin']}'''
        loger(msg)
     
   except Exception as e:
      msg=str(e)
      print(msg)
      
      
      
def watch(flag,list):
   vip=''
   global djj_tele_cookie

   if "DJJ_TELE_COOKIE" in os.environ:
      djj_tele_cookie = os.environ["DJJ_TELE_COOKIE"]
   if flag in os.environ:
      vip = os.environ[flag]
   if flag in osenviron:
      vip = osenviron[flag]
   if vip:
       for line in vip.split('\n'):
         if not line:
            continue 
         list.append(line.strip())
       return list
   else:
       print(f'''【{flag}】 is empty,DTask is over.''')
       exit()


   
def pushmsg(title,txt):
   try:
     txt=urllib.parse.quote(txt)
     title=urllib.parse.quote(title)
     if djj_tele_cookie.strip():
         print("\n【Telegram消息】")
         id=djj_tele_cookie[djj_tele_cookie.find('@')+1:len(djj_tele_cookie)]
         botid=djj_tele_cookie[0:djj_tele_cookie.find('@')]

         turl=f'''https://api.telegram.org/bot{botid}/sendMessage?chat_id={id}&text={title}\n{txt}'''

         response = requests.get(turl,timeout=5)
   except Exception as e:
      print(str(e))
   
def loger(m):
   #print(m)
   global result
   result +=m     

    
   
   
def clock(func):
    def clocked(*args, **kwargs):
        t0 = timeit.default_timer()
        result = func(*args, **kwargs)
        elapsed = timeit.default_timer() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[🔔speed time:%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked
def fun(h):
   aar=[]
   for i in h[1:len(h)-1].split(','):
     aar.append(i[1:len(i)-1])
   #print(aar)
   return aar
@clock
def start():
   global result,video_bd,sign_bd,draw_bd,with_bd,tm_bd,yuan1_bd,userId,bubble_bd
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('SHUQI_SIGN_BODY',sign_bdlist)
   watch('SHUQI_VIDEO_BODY',video_bdlist)
   watch('SHUQI_DRAW_BODY',draw_bdlist)
   watch('SHUQI_WITH_BODY',with_bdlist)
   watch('SHUQI_BUBBLE_BODY',bubble_bdlist)
   watch('SHUQI_USER',IDARY)
   print('=======')
   for i in range(len(video_bdlist)):
     print(f'【{i+1}】')
     result+='【'+str(i+1)+'】'+fun(IDARY[0])[i]+'|'
     sign_bd=sign_bdlist[i]
     video_bd=video_bdlist[i]
     draw_bd=draw_bdlist[i]
     with_bd=with_bdlist[i]
     bubble_bd=bubble_bdlist[i]
     userId=fun(IDARY[0])[i]
     spring_earn()
     result+='\n'
   #print(result)
     
   pushmsg(Gamename,result)

if __name__ == '__main__':
       start()
