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
SB=''
SP=0
JD=0


def Av(i,hd,k,key=''):
   print(str(k)+'=🔔='*k)
   try:
     if k==1:
       key=bdlist[0]
     if k==8:
       key=bdlist[2]
     if k==18:
       key=bdlist[4]
     if k==19:
       key=bdlist[5]
     if k==20:
       key=bdlist[7]
     if k==24:
       key=bdlist[8]
     response =requests.post(i,headers=hd,data=key,timeout=10)
     userRes=json.loads(response.text)
     hand(userRes,k)

   except Exception as e:
      print(str(e))


def hand(userRes,k):
  global SB,SP,JD
  try:
   if k==1:
     for mm in userRes:
      if mm['is_ok']==0:
         Av(urllist[k],hd,k+1,'mini_id='+mm['mini_id']+'&')
      else:
        print('completed......')
   if k==2:
     SB='taskid='+str(userRes['taskid'])+'&nonce_str='+userRes['nonce_str']+'&'
     print(userRes['nonce_str'])
     time.sleep(30)
     Av(urllist[k],hd,k+1,SB)
   if k==3:
     #print(userRes['msg'])
     if userRes['code']==1:
       print(f'''rd2:{userRes['jinbi']}''')
       bd=bdlist[1]+userRes['fb_str']
       Av(urllist[k],hd,k+1,bd)
     else:
        #print(userRes['msg'])
        if json.dumps(userRes).find('u8fc7')>0:
          time.sleep(10) 
          Av(urllist[k-1],hd,k,SB)
   if k==4:
       print(userRes)
       if not userRes['msg']:
          print('fbs.....')
       else:
          print('fbf..')
   if k==5:
        print('card:'+str(userRes['ka']))
        if userRes['ka']==0:
          return 
        for p in userRes['list']:
          if p['is_ad']=='0':
            bd='gid='+p['id']+'&'
            print(bd)
            Av(urllist[k],hd,k+1,bd)
            time.sleep(5)
   if k==6:
         bd='sign='+userRes['sign']+'&gid='+userRes['id']+'&glid='+str(userRes['glid'])+'&'
         Av(urllist[k],hd,k+1,bd)
   if k==7:
        print(f'''jf:{userRes['jf']}-{userRes['up']}''')
        time.sleep(15)
        Av(urllist[3],hd,4,bdlist[1]+userRes['nonce_str'])
   if k==8:
       
       if userRes['code']==1:
         print(f'''rd:{userRes['jinbi']}''')
         time.sleep(15)
         Av(urllist[k],hd,k+1,'nonce_str='+userRes['nonce_str']+'&')
   if k==9:
      if userRes['code']==-1:
          print(userRes['msg'])
      elif userRes['code']==1:
        print(f'''JB:{userRes['day_jinbi']}_{userRes['jinbi']}''')
        SP+=1
        print('SP:'+str(SP))
        if SP<random.randint(10,20):
          Av(urllist[k-2],hd,k-1)
   if k==10:
     if userRes['code']==1:
       print(str(userRes['lucky_num']))
       Av(urllist[3],hd,4,bdlist[1]+userRes['nonce_str'])
       if userRes['lucky_num']>0:
          time.sleep(10)
          Av(urllist[k-1],hd,k)
     else:
           print(userRes['msg'])
           for x in range(1,5):
             Av(urllist[k],hd,k+1,'box='+str(x)+'&')
             time.sleep(1)
   if k==11:
      if userRes['code']==-1:
       print(userRes['msg'])
      elif userRes['code']==1:
        Av(urllist[3],hd,4,bdlist[1]+userRes['nonce_str'])
   if k==12:
      print(userRes)
      if userRes['steps_btn']!="明天再领":
        Av(urllist[14],hd,15)
      if userRes['jindan_show']==0:
          Av(urllist[12],hd,13)
      
      if userRes['hb_jinbi']!=0:
         Av(urllist[15],hd,16,bdlist[3])
         time.sleep(2)
         Av(urllist[15],hd,16,bdlist[6])
         
      if 'right_text' in userRes.keys():
        if userRes['right_text']!='明天再领':
            Av(urllist[16],hd,17)
      else:
             Av(urllist[16],hd,17)
      if userRes['jinbi']!=0:
         Av(urllist[17],hd,18)
         time.sleep(2)
         Av(urllist[18],hd,19)
   if k==13:
     if userRes['code']==-1:
       print(userRes['msg'])
     elif userRes['code']==1:
      print('JDDD:返回')
      bd='taskid='+str(userRes['taskid'])+'&clicktime=1611232580&donetime=1611232583&nonce_str='+userRes['nonce_str']+'&'
      Av(urllist[k],hd,k+1,bd)
   if k==14:
     if userRes['code']==-1:
       print(userRes)
     elif userRes['code']==1:
       print('JDDD_'+str(userRes['jinbi']))
       time.sleep(5)
       Av(urllist[3],hd,4,bdlist[1]+userRes['nonce_str'])
     JD+=1
     print('JD:'+str(JD))
     if JD<random.randint(10,20):
        Av(urllist[12],hd,13)
   
   
   if k==15:
     if userRes['code']==-1:
       print(userRes['msg']+',HB,completed......')
       time.sleep(5)
       Av(urllist[19],hd,20)
     elif userRes['code']==1:
       print(f'''{userRes['msg']},DH_JB:{userRes['jinbi']}''')
       Av(urllist[3],hd,4,bdlist[1]+userRes['nonce_str'])
   if k==16:
     if userRes['code']==-1:
        print(userRes['msg']+'RED:,completed......')
     elif userRes['code']==1:
       print('red:'+userRes['nonce_str'])
       time.sleep(5)
       Av(urllist[3],hd,4,bdlist[1]+userRes['nonce_str'])
   if k==17:
     if userRes['code']==-1:
        print(userRes['msg']+'homeJB1,completed......')
     elif userRes['code']==1:
       print('homeJB1:'+str(userRes['jinbi'])+','+userRes['msg'])
       Av(urllist[3],hd,4,bdlist[1]+userRes['nonce_str'])
   if k==18:
      if userRes['code']==-1:
        print('failure......')
      elif userRes['code']==1:
         print('success......')
   if k==19:
     if userRes['code']==-1:
        print(userRes['msg']+'homeJB2,completed......')
     elif userRes['code']==1:
       print('homeJB2:'+str(userRes['jinbi'])+','+userRes['msg'])
   if k==20:
      print(userRes)
   if k==21:
      print('ad_____')
      Av(urllist[k],hd,k+1,'ad_id='+str(userRes['ad_id'])+'&')
   if k==22:
      time.sleep(5)
      Av(urllist[k],hd,k+1,'nonce_str='+userRes['nonce_str']+'&ad_id='+str(userRes['ad_id'])+'&')
   if k==23:
     if userRes['code']==-1:
        print(userRes['msg']+'adjb..')
     elif userRes['code']==1:
        print('ad_jb:'+userRes['jinbi'])
   if k==24:
     if userRes['is_show']==1:
        Av(urllist[k],hd,k+1)
     else:
       print('no cas')
   if k==25:
     print(userRes['msg'])
     
  except Exception as e:
      print(str(e))



def watch(flag,list):
   vip=''
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
   watch('dashabi_main_url',urllist)
   watch('dashabi_hd',hdlist)
   watch('dashabi_bd',bdlist)
   if len(urllist)==0 or len(hdlist)==0:
      print('data is null.......')
      exit()
   
   for loop in range(5):
    for c in range(len(hdlist)):
      hd=eval(hdlist[c])
      print('【'+str(loop+1)+'】C:'+str(c+1))
      for u in range(len(urllist)):
        if u==0 or u==4 or u==7 or u==9 or u==11 or u==20 or u==23:
          Av(urllist[u],hd,u+1)
        else:
          continue
    time.sleep(30)
  except Exception as e:
      print(str(e))
  print('🏆🏆🏆🏆运行完毕')
  
    
    
   
     
if __name__ == '__main__':
       start()
    
