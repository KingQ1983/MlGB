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
     userRes=response.text
     hand(userRes,k)
   except Exception as e:
      print(str(e))


def hand(userRes,k):
  try:
   msg=''
   if k==1:
      data=info(userRes)['available_money']
      if float(data)<30:
         print('hold on +++++++++++')
      elif float(data)>=30:
        print('fire on........')
        Av(urllist[k],hd,k+1)
   if k==2:
      print(userRes)
  except Exception as e:
      print(str(e))
     
     
def info(userRes):
  try:
   res=''
   res=re.compile('data = (.*)}}}').findall(userRes)[0]+'}}}'
   res=json.loads(res)
   return res
  except Exception as e:
      print(str(e))

def trump(b):
  try:
    zs=datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%H:%M:%S", )
    print(zs)
    
    zs=zs.split(':')
    firetm1=60-int(zs[1])
    firetm2=60-int(zs[2])
    print(str(firetm1)+':'+str(firetm2))
    if int(zs[0])>b-2 and int(zs[0])<b:
       if firetm1>9:
          print('fire_480')
          time.sleep(480)
       elif firetm1<=9 and firetm1>=2:
          print('fire_60')
          time.sleep(60)
       elif firetm1<2 and firetm1>=0:
          print('fire_10')
          time.sleep(10)
       trump(b)
    elif int(zs[0])==b and int(zs[1])==0 and int(zs[2])<50:
      zs=datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%H:%M:%S", )
      print('go.....'+zs)
      for j in range(len(btlist)):
          print(f'''===={str(j+1)}''')
          hd['Cookie']=btlist[j]
          for u in range(len(urllist)-1):
             Av(urllist[u],hd,u+1)
             time.sleep(2)
      print('fire5========')
      time.sleep(5)
      trump(b)
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
   global result,hd,btlist,urllist,hdlist,bdlist
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('bd_fire_url',urllist)
   watch('bd_ck',btlist)
   watch('bd_hd',hdlist)
   hd=eval(hdlist[0])
   trump(6)
   print('🏆🏆🏆🏆运行完毕')
''''''
   
    
    
   
     
if __name__ == '__main__':
       start()
    
