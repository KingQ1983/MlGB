import requests
import json
import time
import timeit
import os
import random
import re
import urllib
from datetime import datetime
from dateutil import tz

Card_telegram=''
result=''
osenviron={}
tx_com_cookie=''





tx_rd_cookie22=''
tx_rd_cookie12=''
tx_rd_cookie21=''
tx_rd_cookie11=''
tx_rd_cookie31=''
tx_rd_cookie32=''
tx_rd_cookie41=''
tx_rd_cookie42=''
   
tx_vd_cookie11=''
tx_vd_cookie12=''
tx_vd_cookie21=''
tx_vd_cookie22=''
tx_vd_cookie31=''



tx_vd_cookie32=''
tx_vd_cookie41=''
tx_vd_cookie42=''

vcookiesList1=[]
rcookiesList1=[]
vcookiesList2=[]
rcookiesList2=[]
rcookiesList3=[]
vcookiesList3=[]
rcookiesList4=[]
vcookiesList4=[]
cmcookiesList=[]


result=''

tx_vd_cookie11=''
tx_vd_cookie12=''





headers = {
        'User-Agent': 'QQNews/6.1.30 (iPhone; iOS 12.4; Scale/2.00)','Content-Type':'application/x-www-form-urlencoded'}

def tx_user():
    try:
        response = requests.post('https://r.inews.qq.com/i/getUserCheckInfo?',headers=headers)
        obj=response.json()
        msg=f"""用户名:{obj['data']['nick']}"""
    except Exception as e:
        msg=str(e)
    loger(msg)

def tx_signCash(rck):
    try:
        response = requests.post('https://api.inews.qq.com/task/v1/user/signin/add?mac=020000000000&'+rck,headers=headers,data='v=gh')
        obj=response.json()
        msg=f"""连续签到:{obj['data']['signin_days']}天"""
    except Exception as e:
        msg=str(e)
    loger(msg)
    
def tx_activityid(rck):
    print('\n   🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧')
    try:
        response = requests.get('https://api.inews.qq.com/activity/v1/activity/info/get?activity_id=stair_redpack_chajian&mac=020000000000&'+rck,headers=headers)
        print(response.json())
    except Exception as e:
        msg=str(e)
        loger(msg)
   
    
def tx_task(ck,rck,vck):
    try:
        response = requests.get('https://api.inews.qq.com/activity/v1/activity/info/get?activity_id=stair_redpack_chajian&'+rck,headers=headers)
        #print(response.json())
        obj=response.json()
        if obj['ret']==0:
          tx1 = obj['data']['award'][0]['openable']
          tx2 = obj['data']['award'][1]['openable']
          msg=f"""[阅读红包]{obj['data']['award'][0]['opened']}-{obj['data']['award'][0]['total']}-{obj['data']['award'][0]['openable']}[视频红包]{obj['data']['award'][1]['opened']}-{obj['data']['award'][1]['total']}-{obj['data']['award'][1]['openable']}[阅读任务]{obj['data']['award'][0]['title']}[视频任务]{obj['data']['award'][1]['title']};"""
        else:
         print('数据错误❌')
    except Exception as e:
          msg=str(e)
          tx1=0
          tx2=0
    print(msg)
    loger(msg)
    print('开包条件:',tx1,tx2)
    if tx1>0:
         print('阅读红包')
         tx_red_info(rck)
         tx_openred1(ck,rck)
         
    if tx2>0:
         print('视频红包')
         tx_red_info(rck)
         tx_openred2(ck,rck)
         
    try:
       if obj['data']['award'][0]['opened'] != obj['data']['award'][0]['total'] and obj['data']['award'][0]['opened'] <6:
       
         tx_read(rck)
         time.sleep(1)


       if obj['data']['award'][1]['opened'] != obj['data']['award'][1]['total'] and obj['data']['award'][1]['opened'] <6:
       
         tx_video(vck)
    except Exception as e:
        msg=str(e)
        #loger(msg)
        tx_read(rck)
        tx_video(rck)
        loger(msg)
    
def tx_read(rck):
    body ='event=article_read'
    response = requests.post('https://api.inews.qq.com/event/v1/user/event/report?mac=020000000000&'+rck,headers=headers,data=body)
    print(response.text)
    obj=response.json()
    msg='阅读:'+obj['info']+'✅'
    loger(msg)
   
      
def tx_video(vck):
    body ='event=video_read&extend=%7B%22video_id%22%3A%2220200622V0CGJH00%22%7D'
    
    response = requests.post('https://api.inews.qq.com/event/v1/user/event/report?mac=020000000000&'+vck,headers=headers,data=body)
    print(response.text)
    obj1=response.json()
    msg='视频:'+obj1['info']+'✅'
    loger(msg)

def tx_red_info(rck):
   print('\🔔🔔🔔🔔🔔🔔🔔🔔🔔🔔🔔')
   response = requests.get('https://api.inews.qq.com/activity/v1/user/activity/get?mac=020000000000&'+rck,headers=headers)
   print(response.text)
   time.sleep(2)
def tx_openred1(ck,rck):
    body ='redpack_type=article&activity_id=stair_redpack_chajian'
    header={
  "Accept-Encoding" : "gzip, deflate, br",
  "idfa" : "EB8686CB-8DC7-463A-95F4-93F8A9F3FD13",
  "Host" : "api.inews.qq.com",
  "qn-sig" : "90C751A56073716051E10600CE9C1981",
  "qqnetwork" : "wifi",
  "store" : "1",
  "deviceToken" : "e7d30dec49381a2293f7dc4a186c110a96764ee23e5313f92d1461807c2cf9eb",
  "Accept-Language" : "zh-Hans-CN;q=1",
  "RecentUserOperation" : "1_news_news_top,1_news_news_top,1_news_background",
  "Content-Type" : "application/x-www-form-urlencoded",
  "Referer" : "http://inews.qq.com/inews/iphone/",
  "User-Agent" : "QQNews/6.2.70 (iPhone; iOS 13.4.1; Scale/3.00)",
  "qn-rid" : "1005_1577260C-06FB-445A-8D16-9403CE5B3E81",
  "Accept" : "*/*",
  "devid" : "955e2c05-1622-453a-821b-8b7cbae7046c",
  "idft" : "C69F97F4-038F-44B2-823B-24A8677FEF2E",
  "appver" : "13.4.1_qqnews_6.2.70"
}
    header['Cookie']=ck
    response = requests.post('https://api.inews.qq.com/activity/v1/activity/redpack/get?mac=020000000000&'+rck,headers=header,data=body)
    print(response.text)
    obj2=response.json()
    msg='阅读红包'+obj2['info']+'✅'
    loger(msg)
    
def tx_openred2(ck,rck):
    body ='redpack_type=video&activity_id=stair_redpack_chajian'
    header={
  "Accept-Encoding" : "gzip, deflate, br",
  "idfa" : "EB8686CB-8DC7-463A-95F4-93F8A9F3FD13",
  "Host" : "api.inews.qq.com",
  "qn-sig" : "90C751A56073716051E10600CE9C1981",
  "qqnetwork" : "wifi",
  "store" : "1",
  "deviceToken" : "e7d30dec49381a2293f7dc4a186c110a96764ee23e5313f92d1461807c2cf9eb",
  "Accept-Language" : "zh-Hans-CN;q=1",
  "RecentUserOperation" : "1_news_news_top,1_news_news_top,1_news_background",
  "Content-Type" : "application/x-www-form-urlencoded",
  "Referer" : "http://inews.qq.com/inews/iphone/",
  "User-Agent" : "QQNews/6.2.70 (iPhone; iOS 13.4.1; Scale/3.00)",
  "qn-rid" : "1005_1577260C-06FB-445A-8D16-9403CE5B3E81",
  "Accept" : "*/*",
  "devid" : "955e2c05-1622-453a-821b-8b7cbae7046c",
  "idft" : "C69F97F4-038F-44B2-823B-24A8677FEF2E",
  "appver" : "13.4.1_qqnews_6.2.70"
}
    header['Cookie']=ck
    response = requests.post('https://api.inews.qq.com/activity/v1/activity/redpack/get?mac=020000000000&'+rck,headers=header,data=body)
    print(response.text)
    obj=response.json()
    msg='视频红包'+obj['info']+'✅'
    loger(msg)
    
def tx_wallet():
    try:
        response = requests.get('https://api.inews.qq.com/activity/v1/usercenter/activity/list?isJailbreak=0',headers=headers)
    #print(response.json())
        obj=response.json()
        msg=f"""金币:{obj['data']['wealth'][0]['title']}红包:{obj['data']['wealth'][1]['title']}"""
    except Exception as e:
        msg=str(e)
    loger(msg)
    
    

   
def loger(m):
   print(m)
   global result
   result +=m+'\n'
    
def check():
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))

   global tx_com_cookie
   global Card_telegram
   global tx_rd_cookie11
   global tx_rd_cookie12
   global tx_rd_cookie21
   global tx_rd_cookie22
   global tx_rd_cookie31
   global tx_rd_cookie32
   global tx_rd_cookie41
   global tx_rd_cookie42
   
   global tx_vd_cookie11
   global tx_vd_cookie12
   global tx_vd_cookie21
   global tx_vd_cookie22
   global tx_vd_cookie31
   global tx_vd_cookie32
   global tx_vd_cookie41
   global tx_vd_cookie42

   
   
   if "TX_COM_COOKIE" in os.environ:
       tx_com_cookie = os.environ["TX_COM_COOKIE"]
     
     
   if "TX_RD_COOKIE11" in os.environ:
      tx_rd_cookie11 = os.environ["TX_RD_COOKIE11"]
   if "TX_RD_COOKIE12" in os.environ:
      tx_rd_cookie12 = os.environ["TX_RD_COOKIE12"]
   if "TX_RD_COOKIE21" in os.environ:
      tx_rd_cookie21 = os.environ["TX_RD_COOKIE21"]
   if "TX_RD_COOKIE22" in os.environ:
      tx_rd_cookie22 = os.environ["TX_RD_COOKIE22"]
   if "TX_RD_COOKIE31" in os.environ:
      tx_rd_cookie31 = os.environ["TX_RD_COOKIE31"]
   if "TX_RD_COOKIE32" in os.environ:
      tx_rd_cookie32 = os.environ["TX_RD_COOKIE32"]
   if "TX_RD_COOKIE41" in os.environ:
      tx_rd_cookie41 = os.environ["TX_RD_COOKIE41"]
   if "TX_RD_COOKIE42" in os.environ:
      tx_rd_cookie42 = os.environ["TX_RD_COOKIE42"]
      
   if "TX_VD_COOKIE11" in os.environ:
      tx_vd_cookie11 = os.environ["TX_VD_COOKIE11"]
   if "TX_VD_COOKIE12" in os.environ:
      tx_vd_cookie12 = os.environ["TX_VD_COOKIE12"]
   if "TX_VD_COOKIE21" in os.environ:
      tx_vd_cookie21 = os.environ["TX_VD_COOKIE21"]
   if "TX_VD_COOKIE22" in os.environ:
      tx_vd_cookie22 = os.environ["TX_VD_COOKIE22"]
   if "TX_VD_COOKIE31" in os.environ:
      tx_vd_cookie31 = os.environ["TX_VD_COOKIE31"]
   if "TX_VD_COOKIE32" in os.environ:
      tx_vd_cookie32 = os.environ["TX_VD_COOKIE32"]
   if "TX_VD_COOKIE41" in os.environ:
      tx_vd_cookie41 = os.environ["TX_VD_COOKIE41"]
   if "TX_VD_COOKIE42" in os.environ:
      tx_vd_cookie42 = os.environ["TX_VD_COOKIE42"]
      

      
      
      
   if tx_com_cookie:
      for line in tx_com_cookie.split('\n'):
         if not line:
            continue 
         cmcookiesList.append(line.strip())
   else:
     print('DTask is over.')
     exit()

   if tx_rd_cookie11 and tx_rd_cookie12:
      for line in tx_rd_cookie11.split('\n'):
         if not line:
            continue 
         rcookiesList1.append(line.strip())
      for line in tx_rd_cookie12.split('\n'):
         if not line:
            continue 
         rcookiesList1.append(line.strip())
   if tx_rd_cookie21 or tx_rd_cookie22:
      for line in tx_rd_cookie21.split('\n'):
         if not line:
            continue 
         rcookiesList2.append(line.strip())
      for line in tx_rd_cookie22.split('\n'):
         if not line:
            continue 
         rcookiesList2.append(line.strip())
         
   if tx_rd_cookie31 or tx_rd_cookie32:
      for line in tx_rd_cookie31.split('\n'):
         if not line:
            continue 
         rcookiesList3.append(line.strip())
      for line in tx_rd_cookie32.split('\n'):
         if not line:
            continue 
         rcookiesList3.append(line.strip())
   if tx_rd_cookie41 and tx_rd_cookie42:
      for line in tx_rd_cookie41.split('\n'):
         if not line:
            continue 
         rcookiesList4.append(line.strip())
      for line in tx_rd_cookie42.split('\n'):
         if not line:
            continue 
         rcookiesList4.append(line.strip())
         
   if tx_vd_cookie11 and tx_vd_cookie12:
      for line in tx_vd_cookie11.split('\n'):
         if not line:
            continue 
         vcookiesList1.append(line.strip())
      for line in tx_vd_cookie12.split('\n'):
         if not line:
            continue 
         vcookiesList1.append(line.strip())
   if tx_vd_cookie21 or tx_vd_cookie22:
      for line in tx_vd_cookie21.split('\n'):
         if not line:
            continue 
         vcookiesList2.append(line.strip())
      for line in tx_vd_cookie22.split('\n'):
         if not line:
            continue 
         vcookiesList2.append(line.strip())
         
   if tx_vd_cookie31 or tx_vd_cookie32:
      for line in tx_vd_cookie31.split('\n'):
         if not line:
            continue 
         vcookiesList3.append(line.strip())
      for line in tx_vd_cookie32.split('\n'):
         if not line:
            continue 
         vcookiesList3.append(line.strip())
   if tx_vd_cookie41 and tx_vd_cookie42:
      for line in tx_vd_cookie41.split('\n'):
         if not line:
            continue 
         vcookiesList4.append(line.strip())
      for line in tx_vd_cookie42.split('\n'):
         if not line:
            continue 
         vcookiesList4.append(line.strip())

   if "Card_telegram" in os.environ:
      Card_telegram = os.environ["Card_telegram"]
   if "Card_telegram" in osenviron:
      Card_telegram = osenviron["Card_telegram"]
   if not Card_telegram:
       print(f'''【通知参数】 is empty,DTask is over.''')
         
def getRD_ck(index):
   #print(index)
   
   tx_ck1=''
   if index==1 and len(rcookiesList1)>0:
      tx_ck1=fomat(random.choice(rcookiesList1))
   elif index==2 and len(rcookiesList2)>0:
      tx_ck1=fomat(random.choice(rcookiesList2))
   elif index==3 and len(rcookiesList3)>0:
      tx_ck1=fomat(random.choice(rcookiesList3))
   elif index==4 and len(rcookiesList4)>0:
      tx_ck1=fomat(random.choice(rcookiesList4))
   return tx_ck1
def getVD_ck(index):
   tx_ck2=''
   if index==1 and len(vcookiesList1)>0:
      tx_ck2=fomat(random.choice(vcookiesList1))
   elif index==2 and len(vcookiesList2)>0:
      tx_ck2=fomat(random.choice(vcookiesList2))
   elif index==3 and len(vcookiesList3)>0:
      tx_ck2=fomat(random.choice(vcookiesList3))
   elif index==4 and len(vcookiesList4)>0:
      tx_ck2=fomat(random.choice(vcookiesList4))
   return tx_ck2

def fomat(k):
   
   S='isJailbreak'+re.compile('isJailbreak(.+)').findall(k)[0]
   return S

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
   global result
   check()
   n=30
   for max in range(n):
     index=0
     print(f"【{n}--{max}】")
     for count in cmcookiesList:
       index+=1
       result=''
       print(f'''>>>>>>>>>【账号{str(index)}开始''')
       headers['Cookie']=count
       tx_user()
       tx_signCash(getRD_ck(index))
       tx_activityid(getRD_ck(index))
       tx_task(count,getRD_ck(index),getVD_ck(index))
       tx_wallet()
       time.sleep(2)
       if max==n-1:
          pushmsg('腾讯新闻',result)
          #result=''
     if max<n-1:
       time.sleep(60)
     
def main_handler(event, context):
    return start()

if __name__ == '__main__':
       start()
  
