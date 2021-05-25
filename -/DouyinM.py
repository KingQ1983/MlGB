import requests
import os
import json
import time
import random
from datetime import datetime
from dateutil import tz
import urllib

osenviron={}
urllist=[]
tokenlist=[]
tklist= []
funlist=[]
bdlist= []
moneylist=[]
hd={}
Card_telegram=''
telelist=[]




msg=''
hd={"Accept": "*/*","Accept-Encoding": "br, gzip, deflate","Accept-Language": "zh-Hans-CN;q=1, en-US;q=0.9, zh-Hant-CN;q=0.8","As-Version": "v1","Content-Type": "application/json","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 qapp","Version": "1211","Version-Name": ""}

def ludingji(i,j,k):
   print('=🔔='*k)
   try:
       response = requests.post(i,headers=hd,data=j)
       res=json.loads(response.text)
       if res['code']==0:
         msg=res['data']['task']['task_id']+'-'+res['data']['task']['title'][0:3]
         print(msg)
       else:
       	print('None')
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
       print(f'''【{flag}】 is empty,DTaskuset is over.''')
       exit()
       
def user(url,i,bd):
   try:
       global msg
       response = requests.post(url,headers=hd,data=bd)
       res=json.loads(response.text)
       if res['code']==0:
         msg+=f"【{i+1}】{res['data']['nickname'][0:3]}|"
       else:
         msg+=f"【{i+1}】None|"
   except Exception as e:
      print(str(e))

def earn(url,i,bd):
   try:
       global msg
       response = requests.post(url,headers=hd,data=bd)
       res=json.loads(response.text)
       if res['code']==0:
         msg+=res['data']['coin_daily']+'|'+res['data']['coin_value']+'|'+res['data']['coins']+'|'+str(res['data']['view_duration'])+'\n'
       else:
          msg+='None|'
   except Exception as e:
      print(str(e))


def pushmsg(title,txt):
   txt=urllib.parse.quote(txt)
   title=urllib.parse.quote(title)
   try:
     if Card_telegram.strip():
         print("\n【Telegram消息】")
         id=Card_telegram[Card_telegram.find('@')+1:len(Card_telegram)]
         botid=Card_telegram[0:Card_telegram.find('@')]

         turl=f'''https://api.telegram.org/bot{botid}/sendMessage?chat_id={id}&text={title}\n{txt}'''

         response = requests.get(turl,timeout=5)
   except Exception as e:
      print(str(e))


def start():
   global hd,Card_telegram
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('Card_telegram',telelist)
   watch('douyin_urlm',urllist)
   watch('douyin_tk',tklist)
   watch('douyin_token',tokenlist)
   watch('douyin_earn',moneylist)
   watch('douyin_funm',funlist)
   watch('douyin_body',bdlist)
   print('========begin=======')
   for jj in range(35):
     for k in range(len(tklist)):
       print('==='+str(k+1)+'======')
       hd['tk']=tklist[k]
       hd['token']=tokenlist[k]
       ludingji(urllist[0],random.choice(funlist),(k+1))
       time.sleep(random.randint(10,25))
   time.sleep(random.randint(5,15))
   print('=======end=======')
#===================
   for k in range(len(tklist)):
      hd['tk']=tklist[k]
      hd['token']=tokenlist[k]
      user(urllist[1],k,bdlist[k])
      earn(urllist[2],k,moneylist[k])
   Card_telegram=telelist[0]
   t =datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S",)
   pushmsg('Douyin2020'+t,msg)
#===========::::
if __name__ == '__main__':
       start()
    
