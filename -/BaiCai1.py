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






def geturl(u,tid):
   u=u[0:u.find('&tid=')+5]+tid+u[u.find('&type'):len(u)]
   return u

def geturl2(u,taskid,Pkg):
   u=u[0:u.find('1/task/')+7]+taskid+u[u.find('/complete'):u.find('Pkg=')+4]+Pkg+u[u.find('&sys'):len(u)]
   return u
def geturl3(u,cmd):
   u=u[0:u.find('cmd=')+4]+cmd+u[u.find('&imgtype'):len(u)]
   return u

def BD():

   for index in range(len(taskidlist)):
     if index==0:
       X4()
       B1(taskidlist[0])
     else:
       B1(taskidlist[index])
     time.sleep(1)
   AV()
   X5()
   Z()

def prehtml(Sg):
   tmd=Sg[Sg.find('window.PAGE_DATA =')+19:Sg.find('window.securityData =')-2]
   return tmd


def Z():
   try:
      userRes = requests.get(urllist[len(urllist)-1],headers=hd,timeout=10).text
      data=json.loads(prehtml(userRes))
      data=data['comps'][0]['data']
      #print(data)
      msg=data['user_name']+'|'+str(data['user_info']['earned_coin'])+'|'+str(data['user_info']['check_coin'])+'|'+str(data['user_info']['enabled_money']/100)+'|'
      loger(msg)
   except Exception as e:
      print(str(e))

def X1():
   try:
     print('\n X1')
     userRes = requests.post(urllist[5],headers=hd,data=bdlist[3],timeout=10).json()
   except Exception as e:
     print(str(e))



def X2():
   try:
     print('\n X2')
     userRes = requests.post(urllist[4],headers=hd,data=bdlist[2],timeout=10).json()
   except Exception as e:
      print(str(e))

def X3():
  try:
   print('\n X3')
   userRes = requests.get(urllist[3],headers=hd,timeout=10).text
  except Exception as e:
      print(str(e))


def X4():
  try:
   print('\n X4')
   userRes = requests.post(urllist[2],headers=hd,data=bdlist[1],timeout=10).json()
   if userRes['err_no']==0:
      print(userRes['err_msg'])
   else:
      print(userRes['err_msg'])
   B4()
  except Exception as e:
      print(str(e))
def X5():
  try:
   print('\n X5')
   url=urllist[1]
   body=bdlist[0]
   userRes = requests.post(url,headers=hd,data=body,timeout=10).json()
   print(userRes['msg'])
   B4()
  except Exception as e:
      print(str(e))
   

def C2(taskid,Pkg):
  try:
   print('\n C2')
   url=geturl2(urllist[6],taskid,Pkg)
   hd['Referer']=urllist[7]
   userRes= requests.get(url,headers=hd,timeout=10).json()
   #print(userRes)
   if userRes['errno']==0:
      print(userRes['msg'])
   else:
      print(userRes['errmsg'])
  except Exception as e:
      print(str(e))
   

def AV():
  try:
   print('\n AV')
   response = requests.get(urllist[0],headers=hd,timeout=10).text
   
   userRes=json.loads(response)
   for im in userRes['data']['comps']:
     if im['id']=='1068':
       time.sleep(1)
       for l in im['data']['gameheader']['progressList']:
         if l['status']==1:
            X3()
       time.sleep(1)
       x=im['data']['jingang']['countDown']
       top='587:'+str(x['587']['countDown'])+'-'+str(x['587']['finishTimes'])+'\n'+'590:'+str(x['590']['countDown'])+'-'+str(x['590']['finishTimes'])
       if x['587']['countDown']==0:
          B1('587')
       if x['590']['countDown']==0:
          B1('590')
     if im['id']=='52':
       time.sleep(1)
       for l in im['data']['checkin_list']:
         top=str(l['is_checkin'])+'-'+l['date']
         if l['date']==im['data']['current_date']:
            if l['is_checkin']==0:
              X2()
       
       
       
     if im['id']=='33':
       time.sleep(1)
       for l in im['data']['tasklist']:
         if l['taskStatus']==0:
           X1()
       
       

     if im['id']=='277':
       time.sleep(1)
       for l in im['data']['tasklist']:
          if l['id']=='4':
            if l['current_count']<200:
               D1('100',4,l['current_count'])
          elif l['id']=='5':
            if l['current_count']<200:
               D1('100',5,l['current_count'])
          elif l['id']=='3':
            if l['current_count']<200:
               D1('100',3,l['current_count'])
  except Exception as e:
      print('AV'+str(e))
 
def B1(tid):
  try:
   print('\n获取=======B1任务:')
   url=geturl(urllist[8],tid)
   hd['Referer']=urllist[9]+tid
   userRes = requests.get(url,headers=hd,timeout=10).json()
   print(userRes['msg'])
   if (userRes['errno'] == 0 and userRes['data']['isDone'] ==0):
         	
      Pkg = userRes['data']['adInfo'][0]['material']['pkg']
      taskid = userRes['data']['taskPf']['taskId']
      B2(tid)
      time.sleep(20)
      if tid=='693':
         C2(taskid,Pkg)
      elif tid=='695':
         C1(taskid,Pkg)
      else:
         B3(taskid,Pkg)
      B4()
   elif (userRes['errno'] == 0 and userRes['data']['isDone'] ==1):
      print("已完成")

  except Exception as e:
      print('B1'+str(e))


def B2(tid):
  try:
   print('\n B2')
   url=urllist[10]+tid
   hd['Referer']=urllist[9]+tid
   userRes = requests.get(url,headers=hd,timeout=10).json()
   if userRes['errno']==0:
      print(userRes['msg'])
   else:
      print(userRes['errmsg'])
  except Exception as e:
      print('B2'+str(e))
 

def B3(taskid,Pkg):
  try:
   print('\n B3')
   url=geturl2(urllist[len(urllist)-6],taskid,Pkg)
   userRes = requests.get(url,headers=hd,timeout=10).json()
   if userRes['errno']==0:
      print(userRes['data']['coin'])
   else:
      print(userRes['errmsg'])
  except Exception as e:
      print(str(e))
def C1(taskid,Pkg):
  try:
   print('\n C1')
   url=geturl2(urllist[len(urllist)-5],taskid,Pkg)
   userRes = requests.get(url,headers=hd,timeout=10).json()
   if userRes['errno']==0:
      print(userRes['msg'])
   else:
      print(userRes['errmsg'])
  except Exception as e:
      print(str(e))

def B4():
  try:
    print('\n B4')
    userRes = requests.get(urllist[len(urllist)-4],headers=hd,timeout=10).json()
    if userRes['errno']==0:
      print(userRes['data']['coin'])
    else:
      print(userRes['data']['errmsg'])
  except Exception as e:
      print('B4'+str(e))

    


def D1(cmd,taskid,num):
  try:
   print('+++D1++'+str(num+1))
   url=geturl3(urllist[len(urllist)-3],cmd)
   userRes = requests.post(url,headers=hd,timeout=10).json()
   m=num
   if userRes['errno']=='0':
     for item in userRes['data'][cmd]['itemlist']['items']:
        #print(item)
        id = item['id']
        if id.find('ad')>=0:
            continue
        m+=1
        D2(id,taskid,m)
        time.sleep(30)
  except Exception as e:
      print(str(e))
   
   
   

def D2(id,taskid,num):
  try:
   print('\n D2任务请求'+str(num+1))
   url=urllist[len(urllist)-2]
   body='data='+urllib.parse.quote(json.dumps({"origin_nid":id,"taskid":taskid}))
   hd['Content-Type']= 'application/x-www-form-urlencoded'
   
   userRes = requests.post(url,headers=hd,data=body,timeout=10).json()
   #print(userRes)
   if userRes['errno'] == 0 and userRes['data']['197']['istip'] == 1:
       print(userRes['data']['197']['tips'])
   else:
       print('no result')
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
   for j in range(1):
       print(f'''===={str(j+1)}''')
       urllist=[]
       btlist=[]
       watch('bd_url',urllist)
       watch('bd_ck',btlist)
       watch('bd_bd',bdlist)
       watch('bd_task',taskidlist)
       taskidlist=s(taskidlist)
       hd['Cookie']=btlist[j]
       BD()
   print('🏆🏆🏆🏆运行完毕')
   print(result)
   pushmsg('一颗好白菜1',result)
    
    
   
     
if __name__ == '__main__':
       start()
    
