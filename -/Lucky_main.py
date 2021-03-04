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
body=''
osenviron={}
msg={}
hd={}
urllist=[]
hdlist=[]
datalist=[]
looplist=[]
numlist=[]
md5list=[]
count={}
osenviron['lucky_com_hd']='''
{"Accept": "*/*","Accept-Encoding": "br, gzip, deflate","Accept-Language": "zh-Hans-CN;q=1, en-US;q=0.9, zh-Hant-CN;q=0.8","Content-Type":"application/x-www-form-urlencoded","User-Agent": "KDApp/1.8.2 (iPhone; iOS 12.4; Scale/2.00)",}
'''
osenviron['lucky_main_num']='''
10
'''
def Av(i,hd,k,key=''):
   global count
   try:
      response = requests.post(i,headers=hd,data=key,timeout=10)
      userRes=json.loads(response.text)
      hand(userRes,k)
   except Exception as e:
      print(str(e))


def hand(userRes,k):
   global count
   try:
     st=json.dumps(userRes)
     if userRes['success']==True:
       if st.find('max_notice')>0 or st.find('read_score')>0:
        count[str(k-1)]+=1
        print('【'+str(k)+'】-p'+str(count[str(k-1)])+'-'+str(userRes['items']['read_score']))
       else:
         count[str(k-1)]+=1
         print('waiting..........')
     else:
       count[str(k-1)]+=1
       print('【'+str(k)+'】-p'+str(count[str(k-1)])+'-'+userRes['message'])
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
       pass
def readdata(id):
   enddata=[]
   try:
     with open('./Lucky/Data'+str(id)+".txt", "r") as f:
       i=0
       for line in f.readlines():
        line = line.strip('\n')
        if not line:
            continue 
        enddata.append(line+md5list[id-1][i])
        i+=1
   except Exception as e:
      print('Data'+str(id)+'读取错误')
      enddata=['']
   return enddata

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
    
def myloop():
   global count
   h1=0
   h2=0
   for cc in range(int(numlist[0])):
     cc+=1
     if cc>len(looplist):
        break
     if len(looplist[cc-1])<2:
       continue
     if count['is'+str(cc-1)]==1:
       h2+=1
     if count[str(cc-1)]<len(looplist[cc-1]):
        data=looplist[cc-1][count[str(cc-1)]]
        Av(urllist[0],hd,cc,data)
     else:
       count['done'+str(cc-1)]=2
     if count['done'+str(cc-1)]==2:
       h1+=1
     if h2-h1>0:
         print('large+++++++'+str(h2-h1))
         print('waiting.....'+str(36/(h2-h1)))
         time.sleep(36/(h2-h1))
   if h1<h2:
      myloop()
def tm13():
   Localtime=datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S.%f", )
   timeArray = datetime.strptime(Localtime, "%Y-%m-%d %H:%M:%S.%f")
   timeStamp = int(time.mktime(timeArray.timetuple())*1000+timeArray.microsecond/1000)
   return timeStamp   
    
@clock
def start():
   global result,hd,urllist,datalist,looplist,count,done,numlist,md5list
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('lucky_main_url',urllist)
   watch('lucky_com_hd',hdlist)
   watch('lucky_main_num',numlist)
   if len(numlist)<1:
      exit()
   for md in range(1,int(numlist[0])+1):
     tmplist=[]
     watch('lucky_md5_data'+str(md),tmplist)
     print('L【'+str(md)+'】'+str(len(tmplist)))
     md5list.append(tmplist)
   if len(hdlist)<1:
      exit()
   hd=eval(hdlist[0])
   for i in range(1,int(numlist[0])+1):
     datalist=[]
     count[str(i-1)]=0
     datalist=readdata(i)
     count['done'+str(i-1)]=0
     if len(datalist)<2:
        count['is'+str(i-1)]=0
     count['is'+str(i-1)]=1
     print('H【'+str(i)+'】'+str(len(datalist)))
     looplist.append(datalist)
   myloop()
   print('🏆🏆🏆🏆运行完毕')
 
    
    
   
     
if __name__ == '__main__':
       start()
   
