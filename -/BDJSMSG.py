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
osenviron={}
msg=''

urllist=[]
hdlist=[]
btlist=[]
bdlist=[]
taskidlist=[]
tasklist=[]
acloop=1
pkg=''
tid=''
id=''
chesttid=''



hd={"Accept": "*/*","Accept-Encoding": "br, gzip, deflate","Accept-Language": "zh-cn","Content-Type": "application/x-www-form-urlencoded","Request-Tag": "Others","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 SP-engine/2.24.0 matrixstyle/0 info baiduboxapp/5.1.0.10 (Baidu; P2 12.4)"}





def BDwithdraw():
  global id,tid
  try:
   userinfo()
   income()
   coinexchange()
  except Exception as e:
      print(str(e))
def userinfo():
   print('\n用户信息')
   try:
        response = requests.get('https://mbd.baidu.com/userx/v1/info/get?fields=%5B%22gender%22%2C%22username%22%2C%22displayname%22%2C%22nickname%22%2C%22avatar%22%5D&cfrom=1099a&from=1099a&osbranch=i0&osname=baiduboxapp&service=bdbox&ua=828_1792_iphone_6.3.0.10_0&ut=iPhone11%2C8_14.4&appname=baiduboxapp',headers=hd,timeout=10)
        userRes=json.loads(response.text)
        #print(userRes)
        msg=userRes['data']['fields']['username']
        if not msg:
          msg=userRes['data']['fields']['nickname']+'|'
        msg+='|'+userRes['data']['fields']['displayname']
        loger(msg)
   except Exception as e:
      print(str(e))

def prehtml(Sg):
   tmd=Sg[Sg.find('window.PAGE_DATA =')+19:Sg.find('window.securityData =')-2]
   return tmd
def s(st):
   st=st[1:len(st)-1].split(',')
   l=[]
   for i in st:
      l.append(i[1:4])
   return l
def income():
   print('\n收入')
   try:
        response = requests.get('https://haokan.baidu.com/activity/h5/income?productid=9&_format=json&matrixstyle=0&channel=&taskclosedloop=0&ugus=9507007161&_ugtk=&_ugvw=&_ugto=&_ugz=&ugChannel=undefined&ugVersion=12.10.0.17',headers=hd,timeout=10)
        userRes=json.loads(response.text)
        data=userRes['data']['comps'][1]['data']
        #print(data)
        msg='|审核金币'+str(data['user_info']['check_coin'])+'|金币余额'+str(data['user_info']['available_coin'])+'|可兑换金币'+str(data['user_info']['enabled_coin'])+'|现金余额'+str(data['user_info']['enabled_money']/100)+'|累计现金'+str(data['user_info']['earned_money']/100)
        loger(msg)
   except Exception as e:
      print(str(e))
      
def coinexchange():
   print('\n金币兑换10000')
   try:
        response = requests.get('https://haokan.baidu.com/activity/api/coinexchange?coinnum=10000&autolock=1&productid=9&ugus=6507007161&_ugtk=&_ugvw=&_ugto=&_ugz=&ugChannel=undefined&ugVersion=12.10.0.17',headers=hd,timeout=10)
        userRes=json.loads(response.text)
        print(userRes)
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
       exit()


   
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
   global result,hd,btlist,urllist,hdlist,bdlist,taskidlist,id,tid,tasklist
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('bd_ck',btlist)
   result=''
   for cc in range(len(btlist)):
        result+='【'+str(cc+1)+'】'
        hd['Cookie']=btlist[cc]
        BDwithdraw()
        print('【'+str(cc+1)+'】-'+'🏆🏆🏆🏆运行完毕')
        result+='\n'
   #print(result)
   pushmsg('BJSDMSG',result)
    
    
   
     
if __name__ == '__main__':
       start()
    
