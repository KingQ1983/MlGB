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


   
   
result=''
osenviron={}
hd={}
urllist=[]
hdlist=[]
btlist=[]
bdlist=[]
SB=''
SP=0

djj_bark_cookie=''
djj_sever_jiang=''
djj_tele_cookie=''




def Av(i,hd,k,key=''):
   print(str(k)+'=🔔='*k)
   try:
     response =requests.post(i,headers=hd,data=key,timeout=10)
     userRes=json.loads(response.text)
     #print(userRes)
     hand(userRes,k)
   except Exception as e:
      print(str(e))


def hand(userRes,k):
  try:
   global SB
   if k==1:
     print(userRes['jinbi'])
     if userRes['code']==-1:
        print(userRes['msg']+'hp......')
     elif userRes['code']==1:
          Av(urllist[1],hd,2,bdlist[0])
   if k==2:
     if userRes['code']==-1:
        print(userRes['msg']+'hp......')
     elif userRes['code']==1:
       print('hp:'+userRes['nonce_str'])
       SB=bdlist[1]+userRes['nonce_str']
       Av(urllist[2],hd,3,'nonce_str='+userRes['nonce_str']+'&')
   if k==3:
     if userRes['code']==-1:
        print(userRes['msg']+'HPJB1,completed......')
     elif userRes['code']==1:
       print('HPJB1:'+str(userRes['jinbi'])+','+userRes['msg'])
     Av(urllist[3],hd,4,SB)
   if k==4:
       if not userRes['msg']:
         print('fb:succes......')
         print('waiting......')
       else:
         print('fb:failure......')
       
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
      # exit()

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
  global result,hd,bdlist,urllist,hdlist
  try:
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('dashabi_666_url',urllist)
   watch('dashabi_hd',hdlist)
   watch('dashabi_666_bd',bdlist)
   if len(urllist)==0 or len(hdlist)==0:
      print('data is null.......')
      exit()
   
   for loop in range(1):
    for c in range(len(hdlist)):
      hd=eval(hdlist[c])
      print('【'+str(loop+1)+'】C:'+str(c+1))
      for u in range(len(urllist)):
        if u==0:
          Av(urllist[u],hd,u+1)
        else:
          continue
      time.sleep(random.randint(15,60))
  except Exception as e:
      print(str(e))
  print('🏆🏆🏆🏆运行完毕')
  
    
    
   
     
if __name__ == '__main__':
       start()
    
