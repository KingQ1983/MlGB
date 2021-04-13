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
hd={}
urllist=[]
hdlist=[]
btlist=[]
bdlist=[]
taskidlist=[]





def BD():
     B1('1','590')
     B1('1','730')




 
def B1(chanel,tid):
  try:
   print('\n获取=======B1任务:')
   url='https://haokan.baidu.com/activity/acad/rewardad?url=https%3A%2F%2Fhaokan.baidu.com%2Factivity%2Facad%2Frewardad&device=%7B%22imei_md5%22%3A%22%22%2C%22device_type%22%3A1%2C%22model%22%3A%22IPHONE%22%2C%22manufacturer%22%3A%22Apple%22%2C%22os_version%22%3A%2214.4.2%22%2C%22idfa%22%3A%22_a2S8_aq28_qa28q8i2At_a02ug_hSaaYuXtigagvIYIu2uPziv_iluPB80Ji2tD_0vyijODvilHOsiIguvJN_8iHaoIO2iTlC2Pi0uSHtYRaSaI_TqSC%22%2C%22androidId%22%3A%22%22%2C%22geo%22%3A%7B%22lat%22%3A%22%22%2C%22lon%22%3A%22%22%7D%2C%22screen_width%22%3A828%2C%22screen_height%22%3A1792%7D&network=%7B%22connect_type%22%3A1%2C%22carrier%22%3A0%7D&productid=2&tid='+tid+'&type=1&source=&qaenv=&'
   hd['Referer']='https://activity.baidu.com/mbox/4a81ae9967/videoTrade?productid=2&type=1&tid='+tid
   userRes = requests.get(url,headers=hd,timeout=10).json()
   print(userRes['msg'])
   if (userRes['errno'] == 0 and userRes['data']['isDone'] ==0):
         	
      Pkg = userRes['data']['adInfo'][0]['material']['pkg']
      taskid = userRes['data']['taskPf']['taskId']
      B2(tid)
      time.sleep(20)
      B3(chanel,taskid,Pkg,tid)
   elif (userRes['errno'] == 0 and userRes['data']['isDone'] ==1):
      print("已完成")

  except Exception as e:
      print('B1'+str(e))


def B2(tid):
  try:
   print('\n B2')
   url='https://haokan.baidu.com/activity/tasks/active?productid=2&qaenv=&_=&id='+tid
   hd['Referer']='https://activity.baidu.com/mbox/4a81ae9967/videoTrade?productid=2&type=1&tid='+tid
   userRes = requests.get(url,headers=hd,timeout=10).json()
   if userRes['errno']==0:
      print(userRes['msg'])
   else:
      print(userRes['errmsg'])
  except Exception as e:
      print('B2'+str(e))
 

def B3(chanel,taskid,rewardVideoPkg,tid):
  try:
   print('\n 金币rewardVideoPkg')
   url='https://eopa.baidu.com/api/task/'+chanel+'/task/'+taskid+'/complete?url=https%3A%2F%2Feopa.baidu.com%2Fapi%2Ftask%2F13%2Ftask%2F747%2Fcomplete&rewardType=coin&rewardVideoPkg='+rewardVideoPkg+'&sys=ios&rewardVideoDrawKey=&source=0&appid=0&bid=0&chestTid=0&signAim=0&cuid=0a2Walusvfgk8SaUluS78YaxHtYg8vaNlP2NiYOSS80L82u9luHUa_80WPl0iWRdyHFmA&date=&productid=&'
   hd['Referer']='https://activity.baidu.com/mbox/4a81ae9967/videoTrade?type=1&tid='+tid+'&entrance=y_treasure_goods'
   
   userRes = requests.get(url,headers=hd,timeout=10).json()
   if userRes['errno']==0:
      print(userRes['data']['coin'])
   else:
      print(userRes['errmsg'])
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

def s(st):
   st=st[0][1:len(st[0])-1]
   l=[]
   for i in st.split(','):
      l.append(i[1:4])
   return l
   
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
   print(m)
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
   global result,hd,btlist,urllist,hdlist,bdlist,taskidlist
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('bd_hd',hdlist)
   hd=eval(hdlist[0])
   watch('bd_ck',btlist)
   for j in range(len(btlist)):
       print(f'''===={str(j+1)}''')
       hd['Cookie']=btlist[j]
       BD()
   print('🏆🏆🏆🏆运行完毕')
   
    
   
     
if __name__ == '__main__':
       start()
    
