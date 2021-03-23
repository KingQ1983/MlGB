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




Game_Name='摇京豆'
xmly_bark_cookie=''
djj_tele_cookie=''
   
result=''
osenviron={}
hd={}

cookiesArr=[]


JD_API_HOST = 'https://api.m.jd.com/client.action?functionId=liveDrawLotteryV842&body=%7B%22lotteryId%22%3A667624%2C%22liveId%22%3A3576206%7D&uuid=8888888&client=apple&clientVersion=9.4.1&st=1615456616059&sign=22d845d5daf2d049a4cdf697bede2194&sv=121&'
#手动输入地址


isLogin=True
nickName=''
UserName=''
cookie=''
index=0
coins=0
tasklist=[]









hd={"Accept": "application/json,text/plain, */*",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-cn",
        "Connection": "keep-alive",
        "Referer": "https://wqs.jd.com/my/jingdou/my.shtml?sceneval=2",
        "User-Agent":"jdapp;iPhone;9.2.2;14.2;%E4%BA%AC%E4%B8%9C/9.2.2 CFNetwork/1206 Darwin/20.1.0"
      }

def JdDlive():
   try:
     
     AllTask()
     
     
	
	
   except Exception as e:
      print(str(e))




      
        
        
      
        
    
  
    






def showMsg():
    global result,coins
    result += f'''本次运行获得{coins}枚'''
    pushmsg(Game_Name,f'''【京东账号{index}{nickName}\n{result}''')

def TotalBean():
   print('\n用户信息')
   global isLogin,nickName
   try:
        
        response = requests.get('https://wq.jd.com/user/info/QueryJDUserInfo?sceneval=2',headers=hd,timeout=10)
        
        userRes=json.loads(response.text)
        if userRes['retcode']==13:
           isLogin = False #cookie过期
           return
        nickName= userRes['base']['nickname']
        
        print(nickName)
   except Exception as e:
      print(str(e))
      
def browseTaskdo(taskid):
   print('\n 获取做任务')
   msg=''
   try:
     response = requests.get(f'https://api.m.jd.com/?t=1616462484171&appid=vip_h5&functionId=vvipclub_doTask&body=%7B%22taskName%22:%22browseTask%22,%22taskItemId%22:{taskid}%7D',headers=hd,timeout=10)
     userRes=json.loads(response.text)
     print(userRes)
   except Exception as e:
      print(str(e))
      

def AllTask():
   print('\n 任务菜单')
   msg=''
   try:
     response = requests.get('https://api.m.jd.com/?t=1616462484576&appid=vip_h5&functionId=vvipclub_lotteryTask&body=%7B%22info%22:%22browseTask%22,%22withItem%22:true%7D',headers=hd,timeout=10)
     userRes=json.loads(response.text)
    # print(userRes)
     data=userRes['data'][0]['taskItems']
     #print(data)
     for i in range(len(data)):
        print(f'''{i+1}【{data[i]['finish']}】{data[i]['title']}''')
        
        if not data[i]['finish']:
          browseTaskdo(data[i]['id'])
          time.sleep(2)
     if userRes['data'][0]['totalPrizeTimes']>0:
        lotteryTask()
       
   except Exception as e:
      print(str(e))
      
def lotteryTask():
   print('\n 摇一摇')
   msg=''
   global coins
   try:
     response = requests.get('https://api.m.jd.com/?appid=sharkBean&functionId=vvipclub_shaking_lottery&body=%7B%7D',headers=hd,timeout=10)
     userRes=json.loads(response.text)
     print(userRes)
     if json.dumps(userRes).find('rewardBeanAmount')>0:
        coins+=userRes['data']['rewardBeanAmount']
     if userRes['data']['remainLotteryTimes']>0:
         time.sleep(2)
         lotteryTask()
     
     	
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
       for line in vip.split('&'):
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
    

    
    
@clock
def start():
   global result,hd,index,isLogin,nickName,UserName,cookie
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('JD_COOKIE',cookiesArr)

   if not cookiesArr[0]:
       pushmsg(Game_Name,'【提示】请先获取京东cookie\n直接使用NobyDa的京东签到获取,https://bean.m.jd.com/')
       exit()
   for cc in range(len(cookiesArr)):
        
        cookie=cookiesArr[cc]
        hd['Cookie']=cookie
        
        UserName = urllib.parse.quote(re.compile('pt_pin=(.+?);').findall(cookie)[0])
        #print(UserName)
        index = cc + 1
        isLogin =True
        nickName = ''
        result = ''
        coins=0
        TotalBean()
        print(f'''\n******开始【京东账号{index}】{nickname[-4]:} || {UserName[-4:]}*********\n''')
        if not isLogin:
           pushmsg(Game_Name,f'''【提示】cookie已失效 ,京东账号{index} {nickName} || {UserName}\n请重新登录获取\nhttps://bean.m.jd.com/''')
           continue
        result+=f'''【京东账号{index}】{nickName}\n '''
        JdDlive()
        result+=f'''本次共计获得{coins}京豆\n'''
        #print(result)
        pushmsg(Game_Name+'\n',result)
    
    
   
     
if __name__ == '__main__':
       start()
    
