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
import os


Gamename='吹风吹又生阅读'
osenviron={}
cklist=[]
readidlist=[]
result=''
header = {}
issign=0
isdoubsign=0
isnooncoin=0
xmly_bark_cookie=''
djj_tele_cookie=''






header={"Accept": "*/*","Accept-Encoding": "gzip, deflate","Accept-Language": "zh-Hans-CN;q=1, en-US;q=0.9, zh-Hant-CN;q=0.8","Connection": "close","Content-Type": "application/x-www-form-urlencoded","Host": "cf-api.douzhuanapi.cn:10002","User-Agent": "NormalDemo/1 (iPhone; iOS 14.4; Scale/2.00)","X-V": "1","osType": "iOS","phoneModel": "","platform": "iOS","versioncode": "1",}
phoneModel=['iPhone XR','iPhone 7 Plus','iPhone 6s Plus','iPhone SE','iPad mini (WiFi)','iPhone 6 Plus','iPhone 5S','iPhone 8 Plus','iPhone 6','iPhone 6s Plus']


def spring_earn():
   getuser()
   self_task_info()
   getnooncoin()
   getsigninfo()
   getsign()
   treasure_box_gain()
   self_readlist()
   self_read()
   getsigninfo(1)
def getuser():
   print('\n getuser')
   try:
     msg=''
     
     response = requests.get('http://cf-api.douzhuanapi.cn:10002/api/user',headers=header)
     Res=response.json()
     print(Res['message'])
     if Res['code']==200:
       msg+=Res['data']['nick_name']+'|累收'+Res['data']['total_gain']+'|今收'+Res['data']['today_gain']+'|转收'+Res['data']['forward_gain']+'|现金余额'+Res['data']['balance']+'|'
   except Exception as e:
      print(str(e))
   loger(msg)



def self_task_info():
   print('\n self_task_info')
   try:
     msg=''
     response = requests.get('http://cf-api.douzhuanapi.cn:10002/api/gold_red_task_info?osType=iOS',headers=header)
     Res=response.json()
     
     if Res['code']==200:
         msg+='【'+Res['data']['new_user_task']['title']+'】\n'
         for da in Res['data']['new_user_task']['list']:
           msg+=da['title']+'-'+da['state_desc']+'\n'
        
         msg+='【'+Res['data']['common_task']['title']+'】\n'
         for da in Res['data']['common_task']['list']:
           msg+=da['title']+'-'+da['state_desc']+'\n'
           
         msg+='【'+Res['data']['advance_task']['title']+'】\n'
         for da in Res['data']['advance_task']['list']:
           msg+=da['title']+'-'+da['state_desc']+'\n'
         
         
           
       
   except Exception as e:
      msg=str(e)
   print(msg)
      



def getsigninfo(flag=0):
   print('\n getsigninfo')
   try:
     global issign,isdoubsign
     msg=''
     response = requests.get('http://cf-api.douzhuanapi.cn:10002/api/gold_sign_info',headers=header)
     Res=response.json()
     print(Res)
     if Res['code']==200:
        if  Res['data']['today_sign_status']==1:
           issign=1 
        if  Res['data']['double_sign_status']==1:
           isdoubsign=1
        if flag==0:
          return 
        msg+='|连续签到天数'+str(Res['data']['sign_days'])+'|'
        msg+='金币余额'+str(Res['data']['gold_balance'])+'|'
        msg+='今日金币'+str(Res['data']['today_gold_gain'])
   except Exception as e:
      print(str(e))
   loger(msg)


def getnooncoin():
   print('\n getnooncoin')
   try:
     msg=''
     response = requests.get('http://cf-api.douzhuanapi.cn:10002/api/get_red_task_gold?id=16',headers=header)
     Res=response.json()
     print(Res)
     response = requests.get('http://cf-api.douzhuanapi.cn:10002/api/get_red_task_gold?id=17',headers=header)
     Res=response.json()
     print(Res)
     response = requests.get('http://cf-api.douzhuanapi.cn:10002/api/get_red_task_gold?id=18',headers=header)
     Res=response.json()
     print(Res)
   except Exception as e:
      print(str(e))
      
      
      
def treasure_box_gain():
   print('\n treasure_box_gain')
   try:
     msg=''
     response = requests.get('http://cf-api.douzhuanapi.cn:10002/api/treasure_box_gain?treasure_box_id=425924&type=1',headers=header)
     Res=response.json()
     print(Res)
     response = requests.get('http://cf-api.douzhuanapi.cn:10002/api/treasure_box_gain?gold_gain_id=12284065&treasure_box_id=425924&type=2',headers=header)
     Res=response.json()
     print(Res)
   except Exception as e:
      print(str(e))
      
      
      
      
def getsign():
   print('\n sign')
   try:
     msg=''
     if issign==1:
   	   return 
     response = requests.get('http://cf-api.douzhuanapi.cn:10002/api/gold_sign?type=1',headers=header)
     Res=response.json()
     print(Res)
     if isdoubsign==1:
   	   return 
     msg=''
     response = requests.get('http://cf-api.douzhuanapi.cn:10002/api/gold_sign?gold_gain_id=12269873&type=2',headers=header)
     Res=response.json()
     print(Res)
   except Exception as e:
      print(str(e))
      



def self_readlist():
   print('\n self_readlist')
   try:
     global readidlist
     msg=''
     for i in range(19):
       response = requests.get('http://cf-api.douzhuanapi.cn:10002/api/article/list?city_type=1&page=4&slide=1&tag_id='+str(i)+'&type=1',headers=header)
       Res=response.json()
     #print(Res)
       if Res['code']==200:
          for id in Res['data']['top_list']:
            readidlist.append(id['id'])
          for id in Res['data']['list']:
            readidlist.append(id['id'])
     #print(readidlist)
   except Exception as e:
      print(str(e))
   print(msg)
      
      
def self_read():
   print('\n self_read')
   try:
     msg='|'
     randlist=[]
     if len(readidlist)==0:
        return
     for i in range(5):
        randlist.append(random.choice(readidlist))
     print(randlist)
     ii=0
     for readid in randlist:
       ii+=1
       
       response = requests.get('http://cf-api.douzhuanapi.cn:10002/h5/article/article_detail?article_id='+str(readid),headers=header)
       Res=response.json()
       if Res['code']==200:
         print(f'''【{ii}】loading.....\n''')
       else:
         print(f'''【{ii}】loading.....❌\n''')
         
       bd='ad_source=1&location=3&position=5&report_type=1'
       response = requests.post('http://cf-api.douzhuanapi.cn:10002/api/ad_sense/report',headers=header,data=bd)
       Res=response.json()
       print(Res)
       if Res['code']==200:
         print(f'''【{ii}】upload.....{Res['data']}\n''')
       else:
         print(f'''【{ii}】upload.....❌|n''')
         
         
       rm=30
       print('waiting........'+str(rm)+'s')
       time.sleep(rm)
       
       response = requests.get('http://cf-api.douzhuanapi.cn:10002/api/self_read_report?item_id='+str(readid),headers=header)
       Res=response.json()
       print(Res)
       if Res['code']==200:
         print(f'''【{ii}】awarding.....\n''')
       if Res['code']==422:
         print(f'''【{ii}】awarding.....{Res['message']}\n''')
         if Res['message'].find('系统')>=0:
           msg+='号码变黑，明天再来'
           break
      
       response = requests.get('http://cf-api.douzhuanapi.cn:10002/api/self_read_init?item_id='+str(readid),headers=header)
       Res=response.json()
       print(Res)
       if Res['code']==200:
         print(f'''【{ii}】complete.....\n''')
       else:
         print(f'''【{ii}】complete.....{Res['message']}\n''')
       if ii==5:
         msg+='本次完成阅读5篇'
         print('\n task competed=======')
         break
       rm=random.randint(60,180)
       print(f'''【{ii}】waiting.....{rm}s\n''')
       time.sleep(rm)
   except Exception as e:
      print(str(e))
   loger(msg)
    

      


def watch(flag,list):
   vip=''
   global xmly_bark_cookie
   global djj_tele_cookie
   if "XMLY_BARK_COOKIE" in os.environ:
      xmly_bark_cookie = os.environ["XMLY_BARK_COOKIE"]
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


   
def pushmsg(title,txt,bflag=1,wflag=1,tflag=1):
   try:
     txt=urllib.parse.quote(txt)
     title=urllib.parse.quote(title)
     if bflag==1 and xmly_bark_cookie.strip():
         print("\n【Bark通知】")
         purl = f'''https://api.day.app/{xmly_bark_cookie}/{title}/{txt}'''
         response = requests.post(purl)
   except Exception as e:
      print(str(e))
   try:
     if tflag==1 and djj_tele_cookie.strip():
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
   global result,bd
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('SPRING_EARN_BODY',cklist)
   j=0
   for count in cklist:
     j+=1
     result+='【'+str(j)+'】'
     header['Authorization']=count
     header['phoneModel']=phoneModel[j-1]
     spring_earn()
     result+='\n'
     #print(result)
     time.sleep(300)
   pushmsg(Gamename,result)

if __name__ == '__main__':
       start()
