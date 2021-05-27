import requests
import os
import json
import time
import random
from datetime import datetime
from dateutil import tz
import urllib

osenviron={}
urllist=[]
hdlist=[]
bdlist= []
moneylist=[]
hd={}
Card_telegram=''
telelist=[]






msg=''


def watch(flag,list):
   vip=''
   if flag in osenviron:
      vip = osenviron[flag]
   if flag in os.environ:
      vip = os.environ[flag]
   if vip:
       for line in vip.split('\n'):
         if not line:
            continue 
         list.append(line.strip())
       return list
   else:
       print(f'''【{flag}】 is empty,DTaskuset is over.''')
       exit()
       
def zhuanpan():
   print('\n【13-14】')
   try:
       bd=f'''------WebKitFormBoundaryf0SB8zu6PSyjeMyM--'''
       msg=''
       hd_={"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Connection": "keep-alive","Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryf0SB8zu6PSyjeMyM","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148/zealer/3.1.1","accessToken": hd['accesstoken'],"vesioncode": "3.0.0"}
       response = requests.post(urllist[13],headers=hd_,data=bd)
       res=json.loads(response.text)
       if res['status']==200:
          print(f"【free_num={res['data']['free_num']}】,【surplus_num={res['data']['surplus_num']}】)")
          if res['data']['surplus_num']>0:
              response = requests.post(urllist[14],headers=hd_,data=bd)
              res=json.loads(response.text)
              
              if res['status']==200:
                print(f"【{res['data']['describe']}{res['data']['prize_desc']}】")
              else:
                 print(res['msg'])
       else:
              print(res['msg'])
   except Exception as e:
      print(str(e))
def mypize(type):
   print('\n【15】type=1+4')
   global msg
   them=''
   try:
       response = requests.get(urllist[15]+'type='+str(type),headers=hd)
       res=json.loads(response.text)
       if res['status']==200:
         n=1
         for data in res['data']:
           if type==1:
             them='(礼品)'
           print(f"{them}【{n}/{len(res['data'])}】<{data['price_desc']}>{data['id']}-{data['activity_title']}")
           msg+=f"【{n}/{len(res['data'])}】<{data['price_desc']}>{data['id']}-{data['activity_title']}\n"
           n+=1
       else:
          print(res['msg'])
   except Exception as e:
      print(str(e))
      

#myPrize

def mynewproduct():
   print('\n【16】')
   try:
       global msg
       bd=f"pageNum=1&pageSize=20&type=1&verifyStr=dc614521a63b229af781471952658ef8&verifyTime=1622074776"
       response = requests.post(urllist[16],headers=hd,data=bd)
       res=json.loads(response.text)
       #print(res)
       if res['status']==200:
         n=1
         for data in res['data']:
             msg+=f"【{n}/{len(res['data'])}】<{data['type']}>{data['id']}-{data['title']}\n"
             n+=1
       else:
          print(res['msg'])
   except Exception as e:
      print(str(e))
      
      


def huodongzhongxin(type):
   print('\n【9】')
   try:
       bd=f"pageNum=1&pageSize=10&type={type}&verifyStr=4d82100655be7e57bdb3c1b162c4b13a&verifyTime=1622029943"
       response = requests.post(urllist[9],headers=hd,data=bd)
       res=json.loads(response.text)
       #print(res)
       if res['status']==200:
         n=1
         for data in res['data']:
              if not 'id' in data:
                continue
              print(f"参加活动:【{n}/{len(res['data'])}】<{data['type']}>{data['id']}-{data['title']}")
              if type==0 or type==1 or type==3:
                 HDZC_jojo(urllist[10],data['id'])
                 time.sleep(2)
                 zanid(data['id'])
              if type==2:
                 HDZC_jojo(urllist[11],data['id'])
                 HDZC_jojo(urllist[12],data['id'])
                 time.sleep(2)
              n+=1
       else:
          print(res['msg'])
   except Exception as e:
      print(str(e))

      
def HDZC_jojo(url,aid):
   print('\n【10-11-12】')
   try:
       bd=f"aid={aid}&verifyStr=0ff795bee7ebdb66a267622af605c728&verifyTime=1622029597"
       response = requests.post(url,headers=hd,data=bd)
       res=json.loads(response.text)
       if res['status']==200:
            print(f"参与活动结果:【{res['data']['score']}score,{res['data']['energy']}】")
       else:
                 print(res['msg'])
   except Exception as e:
      print(str(e))
      
def newproduct(i):
   try:
       global msg
       print('\n【0】')
       bd='verifyStr=4bfb81b8c7810652f38719d6d1500ffe&verifyTime=1621987398'
       response = requests.post(urllist[0],headers=hd,data=bd)
       res=json.loads(response.text)
       if res['status']==200:
         n=0
         for data in res['data']:
           aid=data['id']
           if data['act_info']['user_lottery_status']==2:
              print('开始第'+str(n+1)+'任务')
              msg+='【'+str(n+1)+'】'+data['product_title']+'-('+data['market_price']+')'+data['active_desc']+','+data['act_info']['lottery_button_desc']+','+data['desc']+'\n'
              letsgo(aid)
              time.sleep(2)
           else:
           	  print('第'+str(n+1)+'任务完成')
           	  msg+='【'+str(n+1)+'】'+data['product_title']+'-('+data['market_price']+')'+data['active_desc']+','+data['act_info']['lottery_button_desc']+','+data['desc']+'\n'
           n+=1
       else:
         msg+=f"【{i+1}】None|"
       print(msg)
   except Exception as e:
      print(str(e))

def letsgo(aid):
   try:
       global msg
       print('\n【1】')
       bd='aid='+aid+'&product_id='+str(random.randint(1400,1700))+'&verifyStr=e916ef0daa80e77a6a9c60cb7db79482&verifyTime=1621991742'
       response = requests.post(urllist[1],headers=hd,data=bd)
       res=json.loads(response.text)
       #print(res)
       if res['status']==200:
         print('抽奖结果:'+res['msg']+'-'+res['data']['lotteryCode'])
       else:
          print('抽奖结果:'+res['msg'])
   except Exception as e:
      print(str(e))


def inlog(num):
   print('\n【4】')
   try:
       bd=f"action_type={num}&verifyStr=bfbb84d1483048d22e373a7cc5de2cb3&verifyTime=1622004689"
       response = requests.post(urllist[4],headers=hd,data=bd)
       res=json.loads(response.text)
       print(res['msg'])
   except Exception as e:
      print(str(e))

def zanid(content_id):
   print('\n【5】')
   try:
       bd=f"content_id={content_id}&type=0&verifyStr=0a728a8e622ee3ef70513d9924ed04bd&verifyTime=1622004684"
       response = requests.post(urllist[5],headers=hd,data=bd)
       res=json.loads(response.text)
       print(res['msg'])
   except Exception as e:
      print(str(e))
def getid():
   print('\n【7】')
   try:
       bd='lastId=0&pageNum=1&verifyStr=2960d3d7dae581b71f756abaa9865bb2&verifyTime=1622015941'
       response = requests.post(urllist[7],headers=hd,data=bd)
       res=json.loads(response.text)
       #print(res)
       if res['status']==200:
         n=1
         for data in res['data']:
           if 'id' in data:
              print(f"【{n}/{len(res['data'])}】{data['id']}")
              zanid(data['id'])
              time.sleep(3)
           n+=1
         
       
   except Exception as e:
      print(str(e))
      
      

def tasklist():
   print('\n【6】')
   try:
       bd=f'''------WebKitFormBoundaryf0SB8zu6PSyjeMyM--'''
       msg=''
       hd_={"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Connection": "keep-alive","Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryf0SB8zu6PSyjeMyM","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148/zealer/3.1.1","accessToken": hd['accesstoken'],"vesioncode": "3.0.0"}
       response = requests.post(urllist[6],headers=hd_,data=bd)
       res=json.loads(response.text)
       
       if res['status']==200:
         for data in res['data']['daily_tasks']:
            print(f"【{data['type']}】{data['desc']}-({data['score']}/{data['count_score']})")
            if data['type']==6 and int(data['score'])<5:
              print('zan=======')
              getid()
            else:
              print('''that's all''')
         
   except Exception as e:
      print(str(e))
      
def havingenergy(energyId):
   try:
       print('\n【2】')
       Isget=False
       bd=f'''------WebKitFormBoundaryf0SB8zu6PSyjeMyM
Content-Disposition: form-data; name="energyId"

{energyId}
------WebKitFormBoundaryf0SB8zu6PSyjeMyM--'''
       
       hd_={"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Connection": "keep-alive","Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryf0SB8zu6PSyjeMyM","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148/zealer/3.1.1","accessToken": hd['accesstoken'],"vesioncode": "3.0.0"}
       response = requests.post(urllist[2],headers=hd_,data=bd)
       res=json.loads(response.text)
       #print(res)
       if res['status']==200:
         Isget=True
       else:
          Isget=False
          print(res['msg'])
       return Isget
       
   except Exception as e:
      print(str(e))
def openbox():
   print('\n【8】')
   try:
       bd=f'''------WebKitFormBoundaryf0SB8zu6PSyjeMyM--'''
       msg=''
       hd_={"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Connection": "keep-alive","Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryf0SB8zu6PSyjeMyM","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148/zealer/3.1.1","accessToken": hd['accesstoken'],"vesioncode": "3.0.0"}
       response = requests.post(urllist[8],headers=hd_,data=bd)
       res=json.loads(response.text)
       
       if res['status']==200:
         print(f"get【{res['data']['energy']}】energy")
       else:
          print(res['msg'])
         
   except Exception as e:
      print(str(e))
      
      
      
def home(s):
   try:
       global msg
       print('\n【3】')
       bd=f'''------WebKitFormBoundaryf0SB8zu6PSyjeMyM
Content-Disposition: form-data; name="pageSize"

4
------WebKitFormBoundaryf0SB8zu6PSyjeMyM--'''
       
       hd_={"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Connection": "keep-alive","Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryf0SB8zu6PSyjeMyM","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148/zealer/3.1.1","accessToken": hd['accesstoken'],"vesioncode": "3.0.0"}
       response = requests.post(urllist[3],headers=hd_,data=bd)
       res=json.loads(response.text)
       #print(res)
       if res['status']==200:
         if s==2:
           print('\n统计结果')
           msg+=f"{res['data']['userInfo']['nickname']}|{res['data']['userInfo']['energy']}|{res['data']['userInfo']['score']}\n"
           
         else:
            print('\n我的主页')
            print(f"{res['data']['userInfo']['nickname']}|{res['data']['userInfo']['energy']}|{res['data']['userInfo']['score']}")
            if res['data']['boxWaitingOpen']==1:
             openbox()
            for data in res['data']['energyList']:
             if data['id']!=-1:
               if(havingenergy(data['id'])):
                   print('收取'+data['name']+data['energy']+'点')
       
       else:
          print(res['msg'])
       
   except Exception as e:
      print(str(e))
      
      
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


def start():
   global hd,Card_telegram
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('Card_telegram',telelist)
   watch('choujiang_url',urllist)
   watch('choujiang_hd',hdlist)
   print('========begin=======')
   
   for k in range(len(hdlist)):
     print('===【用户'+str(k+1)+'】======')
     hd=eval(hdlist[k])
     zhuanpan()
     home(1)
     huodongzhongxin(0)
     huodongzhongxin(1)
     huodongzhongxin(2)
     huodongzhongxin(3)
     tasklist()
     home(2)
     mypize(4)
     mypize(1)
     newproduct(k)
   print('=======end=======')
#===================

   print(msg)
   Card_telegram=telelist[0]
   t =datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S",)
   pushmsg('超级大乐透'+t,msg)
#===========::::
if __name__ == '__main__':
       start()
    
