import requests
import os
import json
import time
import random
from datetime import datetime
from dateutil import tz
import urllib
import hashlib
osenviron={}
urllist=[]
hdlist=[]
bdlist= []

hd={}
Card_telegram=''
telelist=[]



msg=''
rid=''
uuid=''
cash=0
jjj=0
st='@123hb#*^&xiMEI99'

times=int(round(time.time() * 1000))

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

def video_uiid():
   print('\n video_uuid')
   try:
       global uuid
       response = requests.get('https://app.hubonews.com/v1/activity/tasks',headers=hd)
       res=json.loads(response.text)
       uuid = res['data']['user_id']
   except Exception as e:
      print(str(e))
      
      
def video_point():
   print('\n video_point')
   try:
       time.sleep(2)
       bd={"positionId":"1391594488677285923","reward":True,"userKey":uuid}

       response = requests.post('http://app.qubiankeji.com:8084/callbacks/v1/reward',headers=hd,data=json.dumps(bd))
       res=response
       print(res)
       
   except Exception as e:
      print(str(e))

def read_id():
   print('\n read_id')
   global rid
   try:
       bd={"limit": 20,"page": 1}
       response = requests.post('https://app.hubonews.com/v3/articles/list',headers=hd,data=json.dumps(bd))
       res=json.loads(response.text)
       if res['code'] == 0:
         rid = res['data'][0]['data']['articleId']
         name = res['data'][0]['data']['translatedTitle']
         print(f"\nID:{rid}\n title:{name}\n") 
         read_points()
   except Exception as e:
      print(str(e))


def read_points():
   print('\n read_points')
   try:
       global jjj
       time.sleep(2)
       bd=''
       md5 =hashlib.md5()
      
       SN=f"action_time={times}&action_type=101&business_id={rid}&secret={st}"
       
       md5.update(SN.encode('utf-8'))
       
       
       bd={"sign":md5.hexdigest(),"action_time":times,"business_id":str(rid),"action_type":101}
       response = requests.post('https://app.hubonews.com/v1/activity/points/update',headers=hd,data=json.dumps(bd))
       res=json.loads(response.text)
       
       if res['code'] == 0:
         print(f"【{jjj+1}】->【{res['data']['point']}point】")
         
         time.sleep(2)
         read_id()
         
       else:
           print(res['msg'])
           
   except Exception as e:
      print(str(e))
      
     
def income(s):
   print('\n income')
   try:
       global cash,msg
       cash=0
       response = requests.get('https://app.hubonews.com/v1/activity/tasks',headers=hd)
       res=json.loads(response.text)
       
       if res['code'] == 0:
         if s==1:
           print(f"{res['data']['point']}-{res['data']['coin']}")
           cash=res['data']['point']
         else:
            msg+=f"{res['data']['point']}-{res['data']['coin']}\n"
         
         
   except Exception as e:
      print(str(e))
      
def withdraw():
   print('\n withdraw')
   try:
       if cash<100:
         print('继续努力！')
         return 
       time.sleep(1)
       bd={"cashout_credits":100,"assets_type":0}
       response = requests.post('https://app.hubonews.com/v1/credit/cashout/apply',headers=hd,data=json.dumps(bd))
       res=json.loads(response.text)
       
       if res['code'] == 0:
         print(f"{result['data']['order_status']}")
       else:
           print(res['msg'])
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
   global hd,Card_telegram,msg
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('Card_telegram',telelist)
   watch('XIMEIHD',hdlist)
   Card_telegram=telelist[0]
   print('========begin=======')
   for k in range(len(hdlist)):
     print('===【用户'+str(k+1)+'】======')
     hd=eval(hdlist[k])
     msg+=f"【{k+1}】"
     video_uiid()
     for i in range(20):
       video_point()
       print(f"【{i+1}】")
     read_id()
     income(1)
     withdraw()
     income(2)
     
   print('=======end=======')
#===================

   #print(msg)
   t =datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S",)
   pushmsg('梅赛德斯奔驰'+t,msg)
#===========::::
if __name__ == '__main__':
       start()
    
