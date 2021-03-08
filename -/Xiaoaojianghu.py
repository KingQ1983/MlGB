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
body1={}
body2={}
body3={}
body4={}
prosecutor={}
urllist=[]
hdlist=[]
bdlist=[]
alllist=[]
liveIdList=[]
tkbdlist=[]
tklist=[]
actId1=''
actId2=''
actId3=''
acount=10

liveflag=True

xmly_bark_cookie=''
djj_tele_cookie=''








def Av(i,hd,k,l,key=''):
   try:
      print(str(k)+'go====')
      userRes=''
      if k>1 and k<13 or k==15 or k==16:
        
        response = requests.get(i,headers=hd,timeout=10)
        response.raise_for_status()
        response.close()
        userRes=json.loads(response.text)
      if k==1 or k==13 or k==14 or k==17:
         response = requests.post(i,headers=hd,data=key,timeout=10)
     
         userRes=json.loads(response.text)
      
      hand(userRes,k,l)
   except Exception as e:
      print(str(e))


def hand(userRes,k,l):
   global actId1,liveIdList,actId2,actId3,hd,body4,prosecutor
   msg=''
   try:
    
    if k==1:
      #print(userRes)
      
      if(userRes['resultCode']==1):
        hd['token']=userRes['data']['accessToken']
    if k==11:
          #print(userRes)
          for data in userRes['data']['everyDayActivityList']:
           if data['actName'].find('直播')>0:
              actId2=data['actId']
           elif data['actName'].find('视频')>0:
             	actId1=data['actId']
           elif data['actName'].find('红包')>0:
             	actId3=data['actId']
    if k==12:
       if userRes['resultCode']==1:
          liveIdList= userRes['data']['liveIdList']
          print(liveIdList)
          
    if k==13:
       print(userRes)
       if userRes['resultCode']== 1:
         print(str(userRes['data']['goldCoinNumber']))
         if userRes['data']['goldCoinNumber']==0:
             prosecutor['v'+str(l)]=1
       else:
          if userRes['errorDesc'].find('上限')>0:
             prosecutor['v'+str(l)]=1
          print(userRes['errorCode']+userRes['errorDesc'])
       time.sleep(random.randint(30,60)/len(tkbdlist))
    if k==14:
      if userRes['resultCode']== 1:
         print(str(userRes['data']['goldCoinAmt']))
         time.sleep(random.randint(30,90))
      else:
          print(userRes['errorCode']+userRes['errorDesc'])
          if userRes['errorDesc'].find('台')>0:
            time.sleep(random.randint(15,30)/len(tkbdlist))
          if userRes['errorDesc'].find('已领')>0:
              prosecutor['l'+str(l)]+=1
          elif userRes['errorDesc'].find('上限')>0:
             prosecutor['l'+str(l)]=len(liveIdList)
          else:
              prosecutor['l'+str(l)]=0
    if(k==15):
       #print(userRes)
       if userRes['resultCode']== 1:
         msg=userRes['data']['customerInfo']['nickname'][0:2]+'|'+userRes['data']['customerInfo']['phone'][0:5]+'|'
         loger(msg)
       else:
          print(userRes['errorCode']+userRes['errorDesc'])
    if(k==16):
      #print(userRes)
      if userRes['resultCode']== 1:
        msg=str(userRes['data']['balanceSum']/100)+'|'+str(userRes['data']['coinSum'])
        loger(msg)
        if userRes['data']['balanceSum']/100>15:
          body4=json.loads(body4)
          body4['amount']=1500
          body4=json.dumps(body4)
        Av(urllist[k],hd,(k+1),l,body4)
      else:
          print(userRes['errorCode']+userRes['errorDesc'])
    if(k==17):
          print(userRes)
          print('wtok(1/2):::::'+str(userRes['data']['withdrawRes']))
       
   except Exception as e:
      #print(str(e))
      pass
      

def watch(flag,list):
   vip=''
   global xmly_bark_cookie
   global djj_sever_jiang
   global djj_tele_cookie
   if "XMLY_BARK_COOKIE" in os.environ:
      xmly_bark_cookie =os.environ["XMLY_BARK_COOKIE"]
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
  # print(m)
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
    
  
def tm13():
   Localtime=datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S.%f", )
   timeArray = datetime.strptime(Localtime, "%Y-%m-%d %H:%M:%S.%f")
   timeStamp = int(time.mktime(timeArray.timetuple())*1000+timeArray.microsecond/1000)
   return timeStamp   
  


def allinone(i):
   global alllist
   try:
     response = requests.get(i,timeout=10)
     response.raise_for_status()
     response.close()
     userRes=json.loads(response.text)
     if userRes['resultCode']==1:
      for l in userRes['data']['records']:
        alllist.append(l['videoPublishId'])
   except Exception as e:
      print(str(e))
      



def allinbd(alllist,liveId=0):
      global body1,body2,body3
      
      body1=json.loads(body1)
      body2=json.loads(body2)
      body3=json.loads(body3)
      tf=[1,1,2]
      body1['videoList'][0]['videoId']=random.choice(alllist)
      body1['videoList'][0]['type']=random.choice(tf)
      body1['videoList'][1]['videoId']=random.choice(alllist)
      body1['videoList'][1]['type']=body1['videoList'][0]['type']
      body1['actId']=str(actId1)
      
     # body2['liveId']=random.choice(liveIdList)
      body2['liveId']=liveId
      body2['actId']=str(actId2)
      body3['actId']=str(actId3)
      body1=json.dumps(body1)
      body2=json.dumps(body2)
     # print('找出错误❌')
      #print(body3)
      body3=json.dumps(body3,separators=(':',':'))
      #print(body3)
      print(str(actId1),str(actId2),str(actId3))
   




@clock
def start():
   global result,hd,body1,body2,body3,body4,prosecutor
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   try:
      watch('xb_main_url',urllist)
      watch('xb_main_hd',hdlist)
      watch('xb_main_bd',bdlist)
      watch('xb_tk_bd',tkbdlist)
      watch('xb_tk',tklist)
      allcode=[]
      
       
      for i in range(1,10):
        allcode.append(urllist[i])
      allinone(random.choice(allcode))
      print(prosecutor)
      for k in range(len(tklist)):
          prosecutor['l'+str(k)]=0
          prosecutor['v'+str(k)]=0
          
      print(prosecutor)
      for ac in range(acount):
        result=''
        for k in range(0,len(tklist)):
          body1=bdlist[0]
          body2=bdlist[1]
          body3=bdlist[2]
          body4=bdlist[3]
          
          
          hd=eval(hdlist[0])
          
          hd['token']=tklist[k].split('@')[0]
          st=tklist[k].split('@')[1]
          hd['traceid']=st.replace(st[20:33],str(tm13()))
          print(str(ac+1)+'_loop__【C】'+str(k+1))
          if k<len(tkbdlist):
             Av(urllist[0],hd,(1),k,tkbdlist[k])
          #Av(urllist[14],hd,(15),body3)
             print('let me try')
          Av(urllist[10],hd,(11),k)
          Av(urllist[11],hd,(12),k)
          allinbd(alllist)
          if prosecutor['v'+str(k)]==0:
              Av(urllist[12],hd,(13),k,body1)
          if len(alllist)>10:
             
             for ii in range(len(liveIdList)):
                 if prosecutor['l'+str(k)]>=len(liveIdList):
                     break
                
                 print(prosecutor)
                 print(str(ii+1)+'=go='+str(len(liveIdList)))
                 allinbd(alllist,liveIdList[ii])
                 Av(urllist[13],hd,(14),k,body2)
                 time.sleep(random.randint(15,30))
          
          
          
          
          if ac!=acount-1:
              del hd['signature']
              del hd['User-Agent']
              del hd["X-User-Agent"]
              del hd['random']
          
          if ac==acount-1:
              print('acount')
              Av(urllist[14],hd,(15),k)
              Av(urllist[15],hd,(16),k)
      
              time.sleep(1)
              result+='\n'
      

        print('<<<<<<<'+str(ac+1)+'>>>>>>>>>')
      #print(result)
      pushmsg('笑傲江湖',result)
      print('🏆🏆🏆🏆运行完毕')
   except Exception as e:
      print(str(e))
   print('🏆🏆🏆🏆运行完毕')
    
    
   
     
if __name__ == '__main__':
       start()
    
