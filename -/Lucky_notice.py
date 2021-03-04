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
body=''
tmbody=''
wtbody=''
osenviron={}
msg={}
hd={}
urllist=[]
hdlist=[]
btlist=[]
tmbdlist=[]
rflist=[]
uslist=[]
datalist=[]
redlist=[]
wtlist=[]
zero=0
osenviron['lucky_com_hd']='''
{"Accept": "*/*","Accept-Encoding": "br, gzip, deflate","Accept-Language": "zh-Hans-CN;q=1, en-US;q=0.9, zh-Hant-CN;q=0.8","Content-Type":"application/x-www-form-urlencoded","User-Agent": "KDApp/1.8.2 (iPhone; iOS 12.4; Scale/2.00)",}
'''
osenviron['lucky_us_ck']='''
["E王德","IQ哥",K逆光yindpai"]
'''




def Av(i,hd,k,key=''):
   print(str(k)+'=🔔='*k)
   try:
     if(k>0 and k<5) or (k>5 and k<20) or k==22:
         response = requests.post(i,headers=hd,data=key,timeout=10)
         userRes=json.loads(response.text)
         #print(userRes)
         hand(userRes,k)
     else:
         userRes = requests.get(i,headers=hd,timeout=10)
         if k!=20:
            userRes=json.loads(userRes.text)
            #print(userRes)
         hand(userRes,k)
   except Exception as e:
      print(str(e))


def hand(userRes,k):
   msg=''
   global zero
   try:
     if k==1:
        if userRes['status']==0:
           print(userRes['msg'])
        elif userRes['status']==1:
           print(str(userRes['score']))
     elif k==2:
        print(str(userRes['time']/60))
        zero+=1
        if int(userRes['time']/60)<156 and zero<3:
          Av(urllist[k-1],hd,(k),tmbody)
        else:
          zero=0
          loger('|'+str(int(userRes['time']/60))+'|')
     elif k==3:
        if userRes['code']==0:
           print(userRes['msg'])
        elif userRes['code']==1:
           print(str(userRes['data']['score']))
     elif k==4:
        if userRes['code']==0:
           print(userRes['msg'])
        elif userRes['code']==1:
           print(str(userRes['data']['score']))
     elif k==5:
      if userRes['code']==1:
        print('continue_card_days:'+str(userRes['data']['luck']['continue_card_days'])+"-luckdraw_num:"+str(userRes['data']['luck']['luckdraw_num']))
        msg+='C:'+str(userRes['data']['luck']['continue_card_days'])+"-D:"+str(userRes['data']['luck']['luckdraw_num'])+'|'
        loger(msg)
        if userRes['data']['user']['status']==0:
           Av(urllist[k],hd,(k+1))
        else:
           today=datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%H:%M", )
           print('today:',today)
           if(int(today[0:2])>4 and int(today[0:2])<9):
              Av(urllist[k+1],hd,(k+2))
        if userRes['data']['user']['is_get_share_reward']==0:
           	Av(urllist[k+2],hd,(k+3))
           	time.sleep(10)
           	Av(urllist[k+3],hd,(k+4))
        if userRes['data']['luck']['luckdraw_num']=='1':
           	Av(urllist[k+4],hd,(k+5))
     elif k==6:
        if userRes['code']==0:
           print(userRes['msg'])
        else:
           print(userRes['data']['jackpot_money'])
     elif k==7:
        if userRes['code']==0:
           print(userRes['msg'])
     elif k==8:
        if userRes['code']==1:
           print(userRes['msg'])
     elif k==9:
        if userRes['code']==0:
           print(userRes['msg'])
     elif k==10:
      if userRes['code']==1:
           print(userRes['data']['score'])
     elif k==11:
        if userRes['status']==1:
          print(f'''score:{userRes['data']['score']}-remainTurn:{userRes['data']['remainTurn']}''')
          if userRes['data']['doubleNum']>0:
            Av(urllist[k]+str(tm13()),hd,(k+1),body)
          if userRes['data']['remainTurn']>0:
            print('继续++++status:'+str(userRes['status']))
            time.sleep(2)
            Av(urllist[k-1]+str(tm13()),hd,(k),body)
            
        elif userRes['status']==0:
            print(userRes['msg'])
     elif k==12:
        print('doubleNum......')
        if userRes['status']==1:
          print(f'''score:{userRes['data']['score']}-doubleNum:{userRes['data']['doubleNum']}''')
        elif userRes['status']==0:
           print(userRes['msg'])
        time.sleep(5)
        Av(urllist[k-2]+str(tm13()),hd,(k-1),body)
     elif k==13:
        if userRes['status']==0:
           print(userRes['msg'])
        elif userRes['status']==1:
           print(f'''num:{userRes['num']}-score:{userRes['score']}''')
        else:
           print('status...')
     elif k==14:
       if userRes['success']==True:
          temp1=userRes['data']['list']['sign']
          if len(temp1)==0:
            print('null.')
          elif len(temp1)>0:
            for i in temp1:
              if i['receive_status']==0:
                data='friend_uid='+str(i['friend_id'])
                Av(urllist[k],hd,(k+1),data)
                time.sleep(5)
              else:
                 print('complete.')
          temp2=userRes['data']['list']['unsign']
          if len(temp2)==0:
            print('Null..')
          elif len(temp2)>0:
             for i in temp2:
               if i['receive_status']==0:
                data='friend_uid='+str(i['friend_id'])
                Av(urllist[k],hd,(k+1),data)
                time.sleep(5)
               else:
                  print('complete.')
     elif k==15:
       if userRes['success']==True:
          print(f'''{userRes['data'][0]['money']}''')
       else:
           print('no red')
     elif k==16:
       if userRes['success']==True:
          print(f'''{userRes['items']['score']}''')
     elif k==17:
       if userRes['status']==1:
         print(str(userRes['data']['opened'])+'/'+str(userRes['data']['remainTurn']))
         kkk=0
         for jjj in userRes['data']['chestOpen']:
           kkk+=1
           if jjj['received']==0:
             Av(urllist[k]+str(tm13()),hd,(k+1),'num='+str(kkk))
     elif k==18:
        if userRes['status']==1:
          print(userRes['data']['score'])
     elif k==19:
        print('video')
        if userRes['success']==True:
           print(str(userRes['items']['score'][0:3]))
        elif userRes['success']==False:
           print(userRes['message'])
     elif k==20:
       print('success')
     elif k==21:
      msg=str(int(userRes['user']['score'])/10000)+'|'+str(int(int(userRes['user']['total_score'])/10000))+'|'+str(userRes['history'][0]['score']/10000)+'\n'
      wt=int(userRes['user']['score'])/10000
      print('wt:'+str(wt))
      if wt>30:
        if wtbody!='xx':
          Av(urllist[k],hd,(k+1),wtbody)
        else:
           print('无数据')
      l=0
      for s in userRes['history']:
        l+=1
        if l==3:
          break
        msg+=s['idx'][6:10]+'|'
        for ss in s['group']:
          if ss['id']==5:
             continue
          msg+=ss['money']+'|'
        msg+='\n'
      loger(msg)
     elif k==22:
       print(userRes['message'])
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
    
def s(st):
   st=st[0][1:len(st[0])-1]
   l=[]
   for i in st.split(','):
      l.append(i[1:4])
   return l
def tm13():
   Localtime=datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S.%f", )
   timeArray = datetime.strptime(Localtime, "%Y-%m-%d %H:%M:%S.%f")
   timeStamp = int(time.mktime(timeArray.timetuple())*1000+timeArray.microsecond/1000)
   return timeStamp   
    
@clock
def start():
  global result,hd,body,tmbody,wtbody,btlist,urllist,uslist,hdlist,tmbdlist,rflist,datalist,redlist,wtlist
  try:
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('lucky_com_url',urllist)
   watch('lucky_com_hd',hdlist)
   watch('lucky_us_ck',uslist)
   watch('lucky_tm_bd',tmbdlist)
   watch('lucky_red_bd',redlist)
   watch('lucky_sg_rf',rflist)
   watch('lucky_data_bd',datalist)
   watch('lucky_wt_bd',wtlist)
   if len(uslist)==0 or len(hdlist)==0:
      print('data is null.......')
      exit()
   hd=eval(hdlist[0])
   uslist=s(uslist)
   for loop in range(2):
    result=''
    for cc in range(len(rflist)):
      hd['Referer']=rflist[cc]
      tmbody=tmbdlist[cc]
      wtbody=wtlist[cc]
      print('账号'+str(cc+1))
      result+=str(cc+1)+'.'+uslist[cc]
      for k in range(len(urllist)):
        if (k>4 and k<10) or k==13 or k==17 or k==21:
         continue
        if k==0:
          Av(urllist[k],hd,(k+1))
        if k==1:
          Av(urllist[k],hd,(k+1),tmbody)
        if k==2 or k==3:
          Av(urllist[k],hd,(k+1))
        if k==10:
          body=rflist[cc].split('&')[15]+rflist[cc].split('&')[8]
          Av(urllist[k]+str(tm13()),hd,(k+1),body)
        if k==12:
          Av(urllist[k],hd,(k+1),'type=taskCenter')
        if k==15:
          Av(urllist[k],hd,(k+1),redlist[cc])
        if k==16:
          Av(urllist[k]+str(tm13()),hd,(k+1))
        if k==18:
          Av(urllist[k],hd,(k+1),datalist[cc])
        if k==4 or k==20:
          Av(urllist[k]+rflist[cc],hd,(k+1))
      time.sleep(10)
    time.sleep(10)
  except Exception as e:
      print(str(e))
  print('🏆🏆🏆🏆运行完毕')
  #print(result)
  pushmsg('中国好同志',result)
    
    
   
     
if __name__ == '__main__':
       start()
    
