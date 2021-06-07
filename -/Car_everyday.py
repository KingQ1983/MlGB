import requests
import re
import json
import urllib
import time
import timeit
import math
import sys
from datetime import datetime
from dateutil import tz
import os
import dateutil.parser
osenviron={}
djj_djj_cookie=''
Card_telegram=''
inviteid=''
versions='V0.1-2021-5-31'
cookiesList=[]
Chosecount=1#选择账号组的第x个，0位全部账号运行，1代表只运行第1个，2代表第2个
fun_task=1#开启任务模式

telelist=[]
Carheader={}
result=''

osenviron["Card_telegram"]=''#机器人的长长id@自己tg的id

osenviron["Car_cookies"]=''#你的heafder带大括号的那个，thor导出json格式的header
def autochina_getList():
    print('\n 获取任务菜单')
    global result
    try:
      url = 'https://assignment.api.autohome.com.cn/api/assignment/autochina/getList?platform=1&category=8ea8'
    
      resp = requests.get(url=url,headers=Carheader,timeout=60).json()
      #print(resp)
      if resp['returncode']==0:
         n=0
         for data in resp['result']:
           n+=1
           code=data['code']
           
           if data['completed']==1:
              print(str(n)+data['mainTitle']+'-'+data['subtitle']+'已完成.\n')
           else:
             name=data['mainTitle']+'-'+data['subtitle']
             print(str(n)+name+'开始执行任务.')
             for i in range(data['times']):
               finishWithCode(name,code)
               time.sleep(3)
           time.sleep(2)
    except Exception as e:
      msg=str(e)
      print(msg)
def sign():
    print('\n 查询{}任务'.format('签到'))
    global result
    try:
      url = 'https://assignment.api.autohome.com.cn/api/assignment/autochina/getSign?platform=1&code=ee1a6d0434dd4beca4623cb1c45f2f45'
    
      resp = requests.get(url=url,headers=Carheader,timeout=60).json()
      print(resp)
      dosign()
    except Exception as e:
      msg=str(e)
      print(msg)
      
      
def dosign():
    print('\n 开始{}任务'.format('签到'))
    global result
    try:
      url = 'https://assignment.api.autohome.com.cn/api/assignment/autochina/sign?code=ee1a6d0434dd4beca4623cb1c45f2f45'
    
      resp = requests.post(url=url,headers=Carheader,timeout=60).json()
      print(resp)
    except Exception as e:
      msg=str(e)
      print(msg)
      
def finishWithCode(name,code):
    print('\n {}任务'.format(name))
    try:
      url = 'https://assignment.api.autohome.com.cn/api/assignment/autochina/finishWithCode?code={}'.format(code)
      resp = requests.post(url=url,headers=Carheader,timeout=60).json()
      print(resp)
    except Exception as e:
      msg=str(e)
      print(msg)
def acceptOil():
    print('\n 每天10点抢油')
    try:
      url = 'https://fbp.api.autohome.com.cn/oil/acceptOil'
      
      resp = requests.post(url=url,headers=Carheader,data=json.dumps({}) ,timeout=60).json()
      print(resp)
    except Exception as e:
      msg=str(e)
      print(msg)
      
def landmarkList():
  print('\n 地图')
  try:
    url = 'https://fbp.api.autohome.com.cn/oil/landmarkList?appId=100010'
    resp = requests.get(url=url,headers=Carheader,timeout=60).json()
    
    if resp['returncode']==0:
       for ac in resp['result']:
         print(ac['cityName'])
         for da in ac['landmarkList']:
           completed='未完成'
           if da['completed']==True:
              completed='完成'
           print(f"{da['landmarkName']}{da['prizeDesc']}--{completed}")
  except Exception as e:
      msg=str(e)
      print(msg)

def landmarkList():
  print('\n 地图')
  try:
    url = 'https://fbp.api.autohome.com.cn/oil/landmarkList?appId=100010'
    resp = requests.get(url=url,headers=Carheader,timeout=60).json()
    
    if resp['returncode']==0:
       for ac in resp['result']:
         print(ac['cityName'])
         for da in ac['landmarkList']:
           completed='未完成'
           if da['completed']==True:
              completed='完成'
           print(f"{da['landmarkName']}{da['prizeDesc']}--{completed}")
  except Exception as e:
      msg=str(e)
      print(msg)


def startdriving():
  print('\n 开车')
  try:
    url = 'https://fbp.api.autohome.com.cn/oil/startdriving'
    resp = requests.post(url=url,headers=Carheader,data={"loading":False},timeout=60).json()
    print(resp)
  except Exception as e:
      msg=str(e)
      print(msg)
    
def raffle():
  print('\n 解锁景点')
  try:
    url = 'https://fbp.api.autohome.com.cn/oil/raffle?platform=APP-IOS&appversion=10.20.5'
    resp = requests.post(url=url,headers=Carheader,timeout=60).json()
    print(resp)
  except Exception as e:
      msg=str(e)
      print(msg)
      
      
def bigprize():
  print('\n 抽奖')
  try:
    url = 'https://fbp.api.autohome.com.cn/oil/bigprize?platform=APP-IOS&appversion=10.20.5'
    resp = requests.post(url=url,headers=Carheader,timeout=60).json()
    print(resp)
  except Exception as e:
      msg=str(e)
      print(msg)
      
      
def receiveredpack():
  print('\n 收红包')
  try:
    url = 'https://fbp.api.autohome.com.cn/oil/receiveredpack?platform=APP-IOS&appversion=10.20.5&m=1'
    resp = requests.post(url=url,headers=Carheader,timeout=60).json()
    print(resp)
  except Exception as e:
      msg=str(e)
      print(msg)

def userInit():
  print('\n 钱包')
  try:
    global result
    url = 'https://fbp.api.autohome.com.cn/oil/userInit'
    resp = requests.get(url=url,headers=Carheader,timeout=60).json()
    #print(resp)
    if resp['returncode']==0:
       result+=f"我的现金:{resp['result']['validBalance']}(满2元即可提现,{resp['result']['withdrawalDeadline']}清零)\n"
  except Exception as e:
      msg=str(e)
      print(msg)

def olduser():
  print('\n 主页')
  try:
    global result
    url = 'https://fbp.api.autohome.com.cn/oil/init?olduser=true'
    resp = requests.get(url=url,headers=Carheader,timeout=60).json()
    #print(resp)
    if resp['returncode']==0:
       drivingStatus='状态:停止中'
       if resp['result']['drivingStatus']==True:
         drivingStatus='状态:行驶中'
       result+=f"剩余汽油{resp['result']['lastOilAmount']}升,{drivingStatus}.解锁景点({resp['result']['finishLandmarkCount']}/{resp['result']['totalLandmarkCount']})\n"
  except Exception as e:
      msg=str(e)
      print(msg)

def Car():
   print('\n开始做任务.........')
   if fun_task==1:
     autochina_getList()
   sign()
   receiveredpack()
   acceptOil()
   startdriving()
   raffle()
   bigprize()
   landmarkList()
   olduser()
   userInit()
#=============================
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
     else:
       print('\n 获取通知数据错误❌')
   except Exception as e:
      print(str(e))
    


def watch(flag,list):
   vip=''
   if flag in osenviron:
      vip = osenviron[flag]
   if flag in os.environ:
      vip = os.environ[flag]
   if vip:
       for line in vip.split('&'):
         if not line:
            continue 
         list.append(line.strip())
       return list
   else:
       print(f'''【{flag}】 is empty,DTaskuset is over.''')
       #exit()
       


def loger(m):
   global result
   result +=m+'\n'
    
def start():
       global cookiesList,Carheader,result,Card_telegram
       scriptHeader = """
════════════════════════════════════════
║                                      ║
║     汽车人活动---公众号iosrule          ║
║                                      ║
════════════════════════════════════════
"""+f"【versions:{versions}】\n\n"
       print(scriptHeader)
       watch('Card_telegram',telelist)
       if len(telelist)==0:
            print('\n Card_telegram对应的数据为空,程序无法使用tg通知功能。.')
       else:
             Card_telegram=telelist[0]
       watch('Car_cookies',cookiesList)
       if len(cookiesList)==0:
            print('\n 退出中,Car_cookies对应的数据为空,请填写完整。.')
       if Chosecount==0:
          print(f"\n你配置的是{len(cookiesList)}个账号执行任务\n")
       else:
           print(f"\n你配置的是第{Chosecount}个账号执行任务\n")
       
       n=0
       for count in cookiesList:
         n+=1
         if Chosecount>0 and n!=Chosecount:
            continue
         result+='【'+str(n)+'】-'
         Carheader=eval(count)
         Carheader.pop('Host',None)
         Carheader.pop('Origin',None)
         Carheader['Content-Type']: 'application/x-www-form-urlencoded;charset=utf-8'
         Car()
         result+='\n'
       print('════════════════════════通知═══════════════')
       print(result)
       pushmsg('汽车之家',result)

if __name__ == '__main__':
    print('Localtime', datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
    start()
