import requests
import os
import json
import time
import random
import timeit
import urllib
from datetime import datetime
from dateutil import tz



result=''
osenviron={}
msg={}
hd={}
urllist=[]
hdlist=[]
keylist=[]
artlist=[]
osenviron['lucky_sub_hd']='''

{"Accept": "*/*","Accept-Encoding": "br, gzip, deflate","Accept-Language": "zh-cn","Connection": "keep-alive","Host": "script.baertt.com","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.20(0x1700142b) NetType/4G Language/zh_CN",}



'''


def Av(i,hd,k,key=''):
   print(str(k)+'=🔔='*k)
   try:
      userRes = requests.get(i,headers=hd,data=key,timeout=10)
      hand(userRes,k)
   except Exception as e:
      print(str(e))


def hand(userRes,k):
   try:
     print('success')

   except Exception as e:
      print(str(e))
def tm13():
   Localtime=datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S.%f", )
   timeArray = datetime.strptime(Localtime, "%Y-%m-%d %H:%M:%S.%f")
   timeStamp = int(time.mktime(timeArray.timetuple())*1000+timeArray.microsecond/1000)
   return timeStamp   
def getid(j):
  base_str = 'abcdefghigklmnopqrstuvwxyz0123456789'
  random_str=''
  length = len(base_str) - 1
  for i in range(j):
    random_str += base_str[random.randint(0, length)]
  return random_str
def addurl():
   url=getid(32)+'&_='+str(tm13())
   return url
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
def s(st):
   st=st[1:len(st)-1]
   l=[]
   for i in st.strip().split(','):
      l.append(i[1:len(i)-1])
   return l
@clock
def start():
   global result,hd,urllist,keylist,artlist
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('lucky_sub_url',urllist)
   watch('lucky_sub_hd',hdlist)
   watch('lucky_key_url',keylist)
   watch('lucky_art_md5',artlist)
  
   
   
   hd=eval(hdlist[0])
   for i in range(len(keylist)):
      md5=s(artlist[i])
      hd['Referer']=keylist[i].replace('xxx',random.choice(md5))
      
      Av(urllist[0]+addurl(),hd,i+1)
      time.sleep(10)
   print('🏆🏆🏆🏆运行完毕')
 
    
    
   
     
if __name__ == '__main__':
       start()
   
