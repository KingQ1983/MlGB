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


djj_bark_cookie=''
djj_sever_jiang=''
djj_tele_cookie=''




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
   msg=''
   if k==1:
      print(f'''is_sign_day:{userRes['is_sign_day']}_sign_day:{userRes['sign_day']}''')
   if k==2:
      print('code:'+str(userRes['code']))
   if k==3:
     msg=f'''{userRes['username'][0:2]}|KP:{userRes['keep_day']}|{userRes['money']}|JB:{userRes['day_jinbi']}'''
     
     loger(msg)
   if k==4:
       msg+='|sn:'+userRes['tixian_sign_day']
       loger(msg)
       bd='tx=0.3&'
       for data in userRes['tixian_html']:
         if (data['jine']=='50' and data['is_ok']==1):
           bd='tx=50&'
           Av(urllist[k],hd,k+1,bd)
         if (data['jine']=='1' and data['is_ok']==1):
           bd='tx=1&'
           print('77777777')
           Av(urllist[k],hd,k+1,bd)
       Av(urllist[k],hd,k+1,bd)
   if k==5:
       print('code:'+str(userRes['code']))
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


       
       
       

  

def pushmsg(title,txt,bflag=1,wflag=1,tflag=1):
   try:
     txt=urllib.parse.quote(txt)
     title=urllib.parse.quote(title)
     if bflag==1 and djj_bark_cookie.strip():
         print("\n【Bark通知】")
         purl = f'''https://api.day.app/{djj_bark_cookie}/{title}/{txt}'''
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
   try:
     if wflag==1 and djj_sever_jiang.strip():
        print("\n【微信消息】")
        purl = f'''http://sc.ftqq.com/{djj_sever_jiang}.send'''
        headers={'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
        body=f'''text={txt})&desp={title}'''
        response = requests.post(purl,headers=headers,data=body)
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
   watch('dashabi_sub_url',urllist)
   watch('dashabi_hd',hdlist)
   
   if len(urllist)==0 or len(hdlist)==0:
      print('data is null.......')
      exit()
   for c in range(len(hdlist)):
      hd=eval(hdlist[c])
      result+=str(c+1)+'.'
      print('【C'+str(c+1)+'】')
      for u in range(len(urllist)-1):
            Av(urllist[u],hd,u+1)
      time.sleep(5)
      result+='\n'
   #print(result)
   pushmsg('步步高学习机',result)
  except Exception as e:
      print(str(e))
  print('🏆🏆🏆🏆运行完毕')
  
    
    
   
     
if __name__ == '__main__':
       start()
    
