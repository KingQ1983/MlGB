import requests
import os
import re
import json
import time
import random
import timeit
import urllib
from datetime import datetime
from dateutil import tz


djj_bark_cookie=''
djj_sever_jiang=''
djj_tele_cookie=''
   
   
result=''
osenviron={}
hd={}
urllist=[]
hdlist=[]
btlist=[]



def Av(i,hd,k,key=''):
   print(str(k)+'=🔔='*k)
   try:
     response =requests.get(i,headers=hd,data=key,timeout=10)
     response.encoding=response.apparent_encoding
     userRes=response.json()
     hand(userRes,k)
   except Exception as e:
      print(str(e))


def hand(userRes,k):
  try:
   msg=''
   if k==4:
       print(userRes)
       msg+='|sn:'+userRes['tixian_sign_day']
       print(msg)
       for data in userRes['tixian_html']:
         if (data['jine']=='50' and data['is_ok']==1):
           bd='tx=50&'
           Av(urllist[k],hd,k+1,bd)
         else:
           print('nono:55555500000:::::')
   if k==5:
       print('code:'+str(userRes['code']))
  except Exception as e:
      print(str(e))
     
     


def trump(b):
  try:
    b1=0
    b2=0
    b3=0
    zs=datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%H:%M:%S", )
    print(zs)
    b1=int(b.split(':')[0])
    b2=int(b.split(':')[1])
    b3=int(b.split(':')[2])
    zs=zs.split(':')
    if b1==0:
       b1=24
    if b2==0:
       b2=60
    if b3==0:
       b3=60
    firetm1=b2-int(zs[1])
    firetm2=b3-int(zs[2])
    print(str(firetm1)+':'+str(firetm2))
    if int(zs[0])>b1-2 and int(zs[0])<b1:
       print('H=====')
       if firetm1>9:
          print('fire_480')
          time.sleep(480)
       elif firetm1<=9 and firetm1>=2:
          print('fire_60')
          time.sleep(60)
       elif firetm1<2 and firetm1>=0:
          print('fire_1')
          time.sleep(1)
       trump(b)
    elif int(zs[0])==int(b.split(':')[0]) and int(zs[1])<(b2-60) :
      print('M----->>>>>>>')
      zs=datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%H:%M:%S", )
      print('go.....'+zs)
      ss=2
      if firetm1==1:
         ss=1
      print('ss_fireon'+str(ss))
      time.sleep(ss)
      trump(b)
    elif int(zs[0])==int(b.split(':')[0]) and int(zs[1])==(b2-60) and int(zs[2])<30:
      print('S----->>>>>>>')
      zs=datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%H:%M:%S", )
      print('.....'+zs)
      for j in range(len(hdlist)):
         print(f'''===={str(j+1)}''')
         Av(urllist[3],hd,4)
      print('loop========')
      time.sleep(1)
      trump(b)
    else:
       print('pass')
       exit()
  except Exception as e:
      print(str(e))

def watch(flag,list):
   vip=''
   global djj_bark_cookie
   global djj_sever_jiang
   global djj_tele_cookie
   if "DJJ_BARK_COOKIE" in os.environ:
      djj_bark_cookie = os.environ["DJJ_BARK_COOKIE"]
   if "DJJ_TELE_COOKIE" in os.environ:
      djj_tele_cookie = os.environ["DJJ_TELE_COOKIE"]
   if "DJJ_SEVER_JIANG" in os.environ:
      djj_sever_jiang = os.environ["DJJ_SEVER_JIANG"]
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


    

def clock(func):
    def clocked(*args, **kwargs):
        t0 = timeit.default_timer()
        result = func(*args, **kwargs)
        elapsed = timeit.default_timer() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[🔔运行完毕用时%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked
    
    
    
    
@clock
def start():
   global result,hd
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('dashabi_sub_url',urllist)
   watch('dashabi_hd',hdlist)
   hd=eval(hdlist[0])
   trump('00:00:00')
   print('🏆🏆🏆🏆运行完毕')
   
    
    
   
     
if __name__ == '__main__':
       start()
    
