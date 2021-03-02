import requests
import os
import json
import time
import random
from datetime import datetime
from dateutil import tz

osenviron={}
urllist=[]
tokenlist=[]
tklist= []
funlist=[]
hd={}



hd={"Accept": "*/*","Accept-Encoding": "br, gzip, deflate","Accept-Language": "zh-Hans-CN;q=1, en-US;q=0.9, zh-Hant-CN;q=0.8","As-Version": "v1","Content-Type": "application/json","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 qapp","Version": "1211","Version-Name": ""}

def ludingji(i,j,k):
   print('=🔔='*k)
   try:
       response = requests.post(i,headers=hd,data=j)
       res=json.loads(response.text)
       msg=res['data']['task']['task_id']+'-'+res['data']['task']['title'][0:3]
       print(msg)
   except Exception as e:
      print(str(e))

def watch(flag,list):
   vip=''
   if flag in osenviron:
      vip = osenviron[flag]
   if flag in os.environ:
      vip = os.environ[flag]
   if vip:
       for line in vip.split('\n'):
         if not line:
            continue 
         list.append(line.strip())
       return list
   else:
       print(f'''【{flag}】 is empty,DTask is over.''')
       exit()
       




def start():
   global hd
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('douyin_urlm',urllist)
   watch('douyin_tk',tklist)
   watch('douyin_token',tokenlist)
   watch('douyin_funm',funlist)
   print(str(len(funlist)))
   for jj in range(35):
     for k in range(len(tklist)):
       print('==cccc='+str(k+1)+'===ccc=')
       hd['tk']=tklist[k]
       hd['token']=tokenlist[k]
       ludingji(urllist[0],random.choice(funlist),(k+1))
       time.sleep(random.randint(10,25))
     time.sleep(random.randint(5,15))
     print('💎'+str(jj+1)+'🔔🔔🔔🔔')
if __name__ == '__main__':
       start()
    
