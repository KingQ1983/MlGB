

import requests
import os
import string
import json
import re
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
datalist=[]
bdlist=[]


#=================================
def Av(i,hd,k,key=''):
   print(str(k)+'=🔔='*k)
   try:
      response =requests.post(i,headers=hd,data=key,timeout=10)
      userRes=json.loads(response.text)
      hand(userRes,k)
   except Exception as e:
      print(str(e))


def hand(userRes,k):
  try:
     print(str(userRes['code']))
  except Exception as e:
      print(str(e))


      
      

def watch(flag,list):
   vip=''
   global djj_bark_cookie
   global djj_sever_jiang
   global djj_tele_cookie
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
def tn(n):
    if n>28:
       return ''.join(random.sample(string.ascii_lowercase + string.digits,n))
    else:
      return ''.join(random.sample(string.ascii_letters + string.digits,n))
def s(st,n):
   st=st[1:len(st)-1]
   l=[]
   for i in st.split(','):
      l.append(i.strip()[n:len(i)-2])
   return l
@clock
def start():
  global result,hd,bdlist,urllist,hdlist,datalist
  try:
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('dashabi_av_url',urllist)
   watch('dashabi_hd',hdlist)
   watch('dashabi_av_bd',bdlist)
   watch('dashabi_av_data',datalist)
   if len(urllist)==0 or len(hdlist)==0:
      print('data is null.......')
      exit()
   data1=s(datalist[0],1)
   data2=s(datalist[1],1)
   data3=s(datalist[2],1)
   data4=s(datalist[3],1)
   for loop in range(10):
    for c in range(len(data4)):
      for ii in range(len(hdlist)):
        hd=eval(hdlist[ii])
        print('【'+str(loop+1)+'】号:'+str(ii+1))
        num=random.randint(0,len(data1))
        md5='{'+bdlist[0]+'"'+data3[num]+'",'+bdlist[1]+'"'+data4[c]+'",'+bdlist[2]+'"'+data1[num]+'",'+bdlist[3]+'"'+data2[num]+'",'+bdlist[4]+bdlist[5]+bdlist[6]+'"'+tn(32)+'",'+bdlist[7]+'"'+tn(28)+'"}'
        for u in range(len(urllist)):
           Av(urllist[u],hd,u+1,md5)
        print('waiting.....')
        time.sleep(random.randint(5,30))
      time.sleep(random.randint(30,120))
  except Exception as e:
      print(str(e))
  print('🏆🏆🏆🏆运行完毕')
 
    
    
   
     
if __name__ == '__main__':
       start()
    
