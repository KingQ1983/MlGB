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
IDARY=['2028096967','2027555822']
result=''
header = {}
sign_bd=''
video_bd=''
draw_bd=''
with_bd=''
tm_bd=''
yuan1_bd=''

tmlong=30

sign_bdlist=[]
video_bdlist=[]
draw_bdlist=[]
with_bdlist=[]
tm_bdlist=[]
yuan1_bdlist=[]



djj_tele_cookie=''







header={"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Connection": "keep-alive","Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18D52 AliApp(shuqi/4.3.6.0) WindVane/8.6.1 Shuqi (iPhone11,8__shuqi__v4.3.6.0) 828x1792 Winding(WV_19) WK",}




#签到
def spring_earn():
   
   boxTask()
   tm()
   getsign()
   draw()
   lottery_10()
   with_()
   yuan1()
    

 


def boxTask():
   print('\n boxTask')
   try:
     msg=''

     response = requests.get('https://ocean.shuqireader.com/api/activity/v1/activity/boxTask?activityId=309&appVer=4.3.6.0&placeId=111111&ver=210301&platform=1&userId='+userId,headers=header)
     Res=response.json()
     print(Res)
     if Res['status']=='200':
        msg+=f'''{Res['data']['readTime']}|'''
     loger(msg)
   except Exception as e:
      msg=str(e)
      print(msg)

def yuan1():
   print('\n yuan1')
   try:
     msg=''
     if(yuan1_bd=='xxx'):
       return 
     response = requests.post('https://ocean.shuqireader.com/api/activity/xapi/gold/withdraw?asac=2A20806CUDY8L7BO8DZ1I7',headers=header,data=yuan1_bd)
     Res=response.json()
     print(Res)
     
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
     print(Res)
     
   except Exception as e:
      msg=str(e)
      print(msg)
def tm():
   print('\n tm')
   try:
     msg=''
     for i in range(tmlong):
       response = requests.post('https://jcollection.shuqireader.com/collection/iosapi/reading/upload',headers=header,data=tm_bd)
       Res=response.json()
       print(Res)
       time.sleep(30)
   except Exception as e:
      msg=str(e)
      print(msg)
      
def draw():
   print('\n draw')
   try:
     msg=''

     response = requests.post('https://ocean.shuqireader.com/api/activity/activity/v1/lottery/draw?asac=2A20C07RJ9F51AOEFSNHDR',headers=header,data=draw_bd)
     Res=response.json()
     print(Res)
     
   except Exception as e:
      msg=str(e)
      print(msg)
      
      
def lottery_10():
   print('\n lottery_10')
   try:
     msg=''

     response = requests.post('https://ocean.shuqireader.com/api/ad/v1/api/prize/lottery',headers=header,data=video_bd)
     Res=response.json()
     print(Res)
     
   except Exception as e:
      msg=str(e)
      print(msg)
      
def with_():
   print('\n with_')
   try:
     msg=''

     response = requests.post('https://ocean.shuqireader.com/api/activity/xapi/gold/withdraw/info',headers=header,data=with_bd)
     Res=response.json()
     print(Res)
     if Res['status']=='200':
        msg=f'''{Res['data']['withdrawableCash']}|{Res['data']['gold']}'''
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
    
@clock
def start():
   global result,video_bd,sign_bd,draw_bd,with_bd,tm_bd,yuan1_bd,userId
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('SHUQI_SIGN_BODY',sign_bdlist)
   watch('SHUQI_VIDEO_BODY',video_bdlist)
   watch('SHUQI_DRAW_BODY',draw_bdlist)
   watch('SHUQI_WITH_BODY',with_bdlist)
   watch('SHUQI_TM_BODY',tm_bdlist)
   watch('SHUQI_1YUAN_BODY',yuan1_bdlist)
   
   
   j=0
   for i in range(len(video_bdlist)):
     j+=1
     result+='【'+str(j)+'】'
     sign_bd=sign_bdlist[i]
     video_bd=video_bdlist[i]
     draw_bd=draw_bdlist[i]
     with_bd=with_bdlist[i]
     tm_bd=tm_bdlist[i]
     yuan1_bd=yuan1_bdlist[i]
     userId=IDARY[i]
     spring_earn()
     result+='\n'
     print(result)
   pushmsg(Gamename,result)

if __name__ == '__main__':
       start():
