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

osenviron={}
bdlist=[]
result=''

bd = {}


xmly_bark_cookie=''
djj_sever_jiang=''
djj_tele_cookie=''



header={"Accept": "*/*","Accept-Encoding": "br, gzip, deflate","Accept-Language": "zh-cn","Content-Type": "application/json","Host": "www.dawang-goon.cn","Referer": "https://servicewechat.com/wxd9e27d81d505e3b4/49/page-frame.html","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.14(0x17000e2e) NetType/WIFI Language/zh_CN",}
Mit = 'https://www.dawang-goon.cn/api/jbs/'

def Wx_dawang():
   getSign()
   sign()
   getinfos()
   
def getSign():
   print('\n getSign')
   try:
     msg=''
     
     response = requests.post(Mit+sys._getframe().f_code.co_name,headers=header,data=json.dumps(bd))
     Res=response.json()
     print(Res)
     if(Res['error']==0):
       if(len(Res['question'])>0):
         bd['answer']=random.choice(Res['question'])
       msg='签到成功✌🏻️.'
     else:
        if Res['signNow']=='1':
           msg='签到成功✌🏻️.'
   except Exception as e:
      msg=str(e)
   loger(msg)
def sign():
   print('\n sign')
   try:
     msg=''
     
     if json.dumps(bd).find('answer')<0:
        return 
     response = requests.post(Mit+sys._getframe().f_code.co_name,headers=header,data=json.dumps(bd))
     Res=response.json()
     print(Res)
   except Exception as e:
      msg=str(e)
      print(msg)

def getinfos():
   print('\n score')
   try:
     msg='积分'
     response = requests.post(Mit+sys._getframe().f_code.co_name,headers=header,data=json.dumps(bd))
     Res=response.json()
     
     if(Res['error']==0):
       msg+=Res['score']
     else:
     	msg+='cookies need update❌'
   except Exception as e:
      msg+=str(e)
   loger(msg)
    


      


def watch(flag,list):
   vip=''
   global xmly_bark_cookie
   global djj_sever_jiang
   global djj_tele_cookie
   if "XMLY_BARK_COOKIE" in os.environ:
      xmly_bark_cookie = os.environ["XMLY_BARK_COOKIE"]
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
        print('[🔔speed time:%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked
    
@clock
def start():
   global result,bd
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('wx_dawang_body',bdlist)
   j=0
   for count in bdlist:
     j+=1
     result+='【'+str(j)+'】'
     bd['id']=count
     Wx_dawang()
     result+='\n'
   #print(result)
   pushmsg('大王叫我来巡山',result)

if __name__ == '__main__':
       start()
