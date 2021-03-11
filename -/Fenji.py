#浏览器注册http://freeperson.xyz/auth/register?code=b3aC
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
sign=''
osenviron={}
hd={}
urllist=[]
hdlist=[]
btlist=[]
bdlist=[]


xmly_bark_cookie=''

djj_tele_cookie=''



def Av(i,hd,k,o,key=''):
   
   print(str(k)+'=🔔='*k)
   try:
     if o==1:
       response =requests.post(i,headers=hd,data=key,timeout=10)
     if o==0:
       response =requests.get(i,headers=hd,timeout=10)
     	
     	
     
     
     hand(response.text,k)

   except Exception as e:
      print(str(e))


def hand(userRes,k):
  global sign
  try:
   msg=''
   if k==2:
      #print(userRes)
      us=re.compile('<div class="font-size-h6 text-dark-75 font-weight-bolder">(.*)</div>').findall(userRes)
      log=re.compile('<p class="text-dark-50">(.*)</p>').findall(userRes)
      
      nm=re.compile('<strong>(.*)</strong></div>').findall(userRes)
      msg='【用户名】'+nm[0]+'\n【时长】'+re.compile('counter">(.*)</span>').findall(nm[1])[0]+'\n【总流量】'+nm[2]+'\n【已使用】'+us[1]+sign+'\n【登录时间】'+log[3]
      
      
      loger(msg)
      
      
      
      adress=re.compile('data-clipboard-text="(.*)</button>').findall(userRes)
      msg='\n【订阅地址】\n'
      for dt in adress:
         dt=dt.replace('">','')
         dt=dt.replace('<i class="metron-quantumultx text-white</i>&nbsp;&nbsp;','')
         dt=dt.replace('<i class="metron-v2rayng text-white</i>&nbsp;&nbsp;','')
         dt=dt.replace('<i class="metron-surfboard text-white</i>&nbsp;&nbsp;','')
         dt=dt.replace('<i class="metron-kitsunebi text-white</i>&nbsp;&nbsp;','')
         dt=dt.replace('&nbsp;&nbsp;','')
         msg+=dt+'\n'
      loger(msg)
   elif k==1:
      
      userRes=json.loads(userRes)
      print(userRes)
      if(userRes['ret']==1):
       sign='\n【签到】'+userRes['msg']
      elif(userRes['ret']==0):
        sign='\n【签到】'+'重复签到'
      
  except Exception as e:
      print(str(e))



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
      # exit()


       
       
       

  

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
        print('[🔔运行完毕用时%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked
    


@clock
def start():
  global result,hd,bdlist,urllist,hdlist
  try:
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('airplay_data',urllist)
   
   if len(urllist)==0:
      print('data is null.......')
      exit()
   hd=eval(urllist[1])
   Av(urllist[0]+'/checkin',hd,1,1)
   Av(urllist[0],hd,2,0)
   result+='\n'
   #print(result)
   pushmsg('机场签到',result,0,0,1)
   result=result[0:result.find('【订阅')]
   pushmsg('机场签到',result,1,0,0)
   
   
  except Exception as e:
      print(str(e))
  print('🏆🏆🏆🏆运行完毕')
  
    
    
   
     
if __name__ == '__main__':
       start()
    
