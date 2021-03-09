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
acloop=10
pkg=''
tid=''
id=''
chesttid=''



hd={"Accept": "*/*","Accept-Encoding": "br, gzip, deflate","Accept-Language": "zh-cn","Content-Type": "application/x-www-form-urlencoded","Request-Tag": "Others","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 SP-engine/2.24.0 matrixstyle/0 info baiduboxapp/5.1.0.10 (Baidu; P2 12.4)"}





def kindapretty():
  global id,tid
  try:
   userinfo()
   task_sign()
   opennew()
   income()
   coinexchange()
   id=taskidlist[1]
   for data in tasklist:
      print('🔔任务======================')
      tid=data
      tasks_active()
      tasks_rewardad()
      print('...waiting20')
      time.sleep(20)
      tasks_complete()
      print('...waiting7')
      time.sleep(7)
      tasks_taskreward()
   print('🔔======================')
   id=taskidlist[2]
   print(id)
   chestDouble_active()
   chestDouble_rewardad()
   print('...waiting')
   time.sleep(20)
   chestDouble_complete()
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
        response = requests.get('https://haokan.baidu.com/activity/h5/income?productid=1&idfrom=selfrw&pd=selfrw&tag=guide&tab=guide&source=selfrw-0-0&ugChannel=381d&ugVersion=6.3.0.10',headers=hd,timeout=10)
        userRes=json.loads(prehtml(response.text))
        data=userRes['comps'][0]['data']
        #print(data)
        msg='|审核金币'+str(data['user_info']['check_coin'])+'|金币余额'+str(data['user_info']['available_coin'])+'|可兑换金币'+str(data['user_info']['enabled_coin'])+'|现金余额'+str(data['user_info']['enabled_money']/100)+'|累计现金'+str(data['user_info']['earned_money']/100)
        loger(msg)
   except Exception as e:
      print(str(e))
      
def coinexchange():
   print('\n金币兑换23800')
   try:
        response = requests.post('https://haokan.baidu.com/activity/api/coinexchange?coinnum=23800&autolock=1&productid=1&ugus=6372015161&_ugtk=&_ugvw=021171412370000000000000000000000000000000000000000000008401ff80037FA521A069A7FC7CBE092375EFD2C8D6D:FG%3D10000000000000&_ugto=20$1237161484562057033557121497161510270579759924b94d7ffbce8407600e31d4e69313d7df8bb8dffb784df3280b0630d34e659e63ae6481e1614845621478&_ugz=&ugChannel=381d&ugVersion=6.3.0.10',headers=hd,timeout=10)
        userRes=json.loads(response.text)
        print(userRes)
   except Exception as e:
      print(str(e))
      
      

def task_sign():
   print('\n视频签到')
   try:
      url='https://haokan.baidu.com/activity/acusercheckin/update'
      body='productid=1&ugus=9766888061'
      userRes = requests.post(url,headers=hd,data=body,timeout=10).json()
      print(userRes)
   except Exception as e:
      print(str(e))
      
def opennew():
   print('\n开宝箱')
   try:
        body='taskid=670&productid=1&ugus=6500584161&_ugtk=&_ugvw=021171412370000000000000000000000000000000000000000000008401ff80037FA521A069A7FC7CBE092375EFD2C8D6D:FG%3D10000000000000&_ugto=20$1237161484562057033557121497161484965951541534b94d7ffbce8407600e31d4e69313d7df8bb8dffb784df3280b0630d34e659e63ae6481e1614845621478&_ugz=kpIQDnzO0PGTjL4aQeq1kT2bpLYriI6FpvQXLNFNU14nVaHSzfncLjj3fRf020D46yxjrKbjR5rG1RMOtVOoNug&ugChannel=381d&ugVersion=6.3.0.10'
        response = requests.post('https://haokan.baidu.com/activity/acuserchest/opennew',headers=hd,data=body,timeout=10)
        userRes=json.loads(response.text)
        print(userRes)
   except Exception as e:
      print(str(e))
      
      
def tasks_active():
   print('\n任务激活')
   global tid
   try:
        hd['Referer']='https://eopa.baidu.com/page/pagekey-qWYNoPr0?productid=1&type=1&tid='+tid
        response = requests.get('https://haokan.baidu.com/activity/tasks/active?productid=1&id='+tid+'&qaenv=&_=1615103092797',headers=hd,timeout=10)
        userRes=json.loads(response.text)
        print(userRes['msg'])
   except Exception as e:
      print(str(e))
      
def tasks_rewardad():
   print('\n任务奖励')
   try:
        global pkg,tid

        hd['Referer']='https://eopa.baidu.com/page/pagekey-qWYNoPr0?productid=1&type=1&tid='+tid
        response = requests.get('https://haokan.baidu.com/activity/acad/rewardad?device=%7B%22imei_md5%22%3A%22%22%2C%22device_type%22%3A1%2C%22model%22%3A%22IPHONE%22%2C%22manufacturer%22%3A%22Apple%22%2C%22os_version%22%3A%2214.4%22%2C%22idfa%22%3A%22B38160D2-DC94-4414-905B-D15F395FD787%22%2C%22androidId%22%3A%22%22%2C%22screen_width%22%3A828%2C%22screen_height%22%3A1792%7D&network=%7B%22connect_type%22%3A1%2C%22carrier%22%3A0%7D&productid=1&tid='+tid+'&type=1&source=&qaenv=&_=',headers=hd,timeout=10)
        userRes=json.loads(response.text)
        print(userRes['msg'])
        if (userRes['errno'] == 0 and userRes['data']['isDone'] ==0):
         	
          pkg = userRes['data']['adInfo'][0]['material']['pkg']
          tid = userRes['data']['taskPf']['taskId']
          print(pkg)
          
   except Exception as e:
      print(str(e))
      
      
def tasks_complete():
   print('\n完成任务')
   global tid,pkg,id
   try:
        hd['Referer']='https://eopa.baidu.com/page/pagekey-qWYNoPr0?productid=1&type=1&tid='+tid
        response = requests.get('https://eopa.baidu.com/api/task/1/task/'+id+'/complete?rewardType=coin&rewardVideoPkg='+pkg+'&sys=ios&rewardVideoDrawKey=&source=0&appid=0&bid=0&chestTid=0&signAim=0&date=&_=1615122456808',headers=hd,timeout=10)
        userRes=json.loads(response.text)
        print(userRes)
   except Exception as e:
      print(str(e))

def tasks_taskreward():
   print('\n确定奖励任务')
   try:
        hd['Referer']='https://haokan.baidu.com/activity/h5/vault?productid=1&tab=guide&tag=guide&pd=selfrw&source=selfrw-0-0&idfrom=selfrw&idfa=B38160D2-DC94-4414-905B-D15F395FD787&package=com.baidu.haokan&os=ios&ut=iPhone11%252C8_14.4&time=1615122419'
        response = requests.get('https://haokan.baidu.com/activity/tasks/taskreward?productid=1&ugus=4642215161&_ugtk=&_ugvw=021171412370000000000000000000000000000000000000000000008401ff80037FA521A069A7FC7CBE092375EFD2C8D6D:FG%3D10000000000000&_ugto=20$1237161484562057033557121497161512242282161564b94d7ffbce8407600e31d4e69313d7df8bb8dffb784df3280b0630d34e659e63ae6481e1614845621478&_ugz=kpIQDnzO0PGTjL4aQeq1kT2bpLYriI6FpvQXLNFNU14kjNV857lYSVtQYVLat6jj8fJFSojZjIXooEOBEkPK29g&ugChannel=381d&ugVersion=6.3.0.10',headers=hd,timeout=10)
        userRes=json.loads(response.text)
        print(userRes['msg'])
   except Exception as e:
      print(str(e))
      
      
def chestDouble_active():
   print('\n翻倍任务激活')
   try:
        hd['Referer']='https://activity.baidu.com/mbox/4a81ae9967/videoTrade?type=1&tid='+tid+'&productid=1&chesttid='+chesttid+'&chestname=chestDouble'
        response = requests.get('https://haokan.baidu.com/activity/tasks/active?url=https%3A%2F%2Fhaokan.baidu.com%2Factivity%2Ftasks%2Factive&productid=1&id='+tid,headers=hd,timeout=10)
        userRes=json.loads(response.text)
        print(userRes['msg'])
   except Exception as e:
      print(str(e))
      
def chestDouble_rewardad():
   print('\n翻倍任务奖励')
   global pkg,tid
   try:
        hd['Referer']='https://activity.baidu.com/mbox/4a81ae9967/videoTrade?type=1&tid='+tid+'&productid=1&chesttid=670&chestname=chestDouble'
        
        response = requests.get('https://haokan.baidu.com/activity/acad/rewardad?url=https%3A%2F%2Fhaokan.baidu.com%2Factivity%2Facad%2Frewardad&device=%7B%22idfa%22%3A%22%22%2C%22imei_md5%22%3A%22%22%2C%22manufacturer%22%3A%22%22%2C%22device_type%22%3A1%2C%22model%22%3A%22%22%2C%22os_version%22%3A%22%22%7D&network=%7B%22carrier%22%3A3%2C%22connect_type%22%3A1%7D&productid=1&tid='+tid+'&type=1&source=&qaenv=',headers=hd,timeout=10)
        userRes=json.loads(response.text)
        
        print(userRes)
        if (userRes['errno'] == 0 and len(userRes['data']['adInfo'])>0):
         	
          pkg = userRes['data']['adInfo'][0]['material']['pkg']
          tid = userRes['data']['taskPf']['taskId']
          print(pkg)

      
   except Exception as e:
      print(str(e))
      
      
def chestDouble_complete():
   print('\n翻倍完成任务')
   try:
        hd['Referer']='https://activity.baidu.com/mbox/4a81ae9967/videoTrade?type=1&tid='+tid+'&productid=1&chesttid=670&chestname=chestDouble'
        response = requests.get('https://eopa.baidu.com/api/task/1/task/'+id+'/complete?url=https%3A%2F%2Feopa.baidu.com%2Fapi%2Ftask%2F1%2Ftask%2F893%2Fcomplete&rewardType=chestDouble&rewardVideoPkg=a8d4f9aa88fbc06571592b6fb5ee7fe51614850106&sys=ios&rewardVideoDrawKey=&source=0&appid=0&bid=0&chestTid=670&signAim=0&cuid=0a2Walusvfgk8SaUluS78YaxHtYg8vaNlP2NiYOSS80L82u9luHUa_80WPl0iWRdyHFmA&date=&productid=1',headers=hd,timeout=10)
        userRes=json.loads(response.text)
        print(userRes)
   except Exception as e:
      print(str(e))

def tasks_taskad():
   print('\n试玩领金币15个')
   try:
        global pkg,tid
        print(tid)
        tid='393'
        tasks_active()
        hd['Referer']='https://eopa.baidu.com/page/pagekey-l4t5CEae?productid=1&type=1&tid=393&rvid=379'
        response = requests.get('https://haokan.baidu.com/activity/acad/taskad?device=%7B%22imei_md5%22%3A%22%22%2C%22device_type%22%3A1%2C%22screen_width%22%3A828%2C%22screen_height%22%3A1792%2C%22model%22%3A%22IPHONE%22%2C%22manufacturer%22%3A%22Apple%22%2C%22os_version%22%3A%2214.4%22%2C%22idfa%22%3A%22B38160D2-DC94-4414-905B-D15F395FD787%22%2C%22androidId%22%3A%22%22%7D&network=%7B%22connect_type%22%3A1%2C%22carrier%22%3A0%7D&productid=1&tid=393&type=1&rvid=379&_=1615127761376',headers=hd,timeout=10)
        userRes=json.loads(response.text)
   
        print(userRes['msg'])
        if (userRes['errno'] == 0):
         for i in range(len(userRes['data']['adInfo'])):
            pkg = userRes['data']['adInfo'][i]['material']['pkg']
            time.sleep(30)
            tasks_rvidcomplete379()
            time.sleep(20)
            print('\n'+str(i+1),pkg)
          
   except Exception as e:
      print(str(e))
      

def tasks_rvidcomplete379():
   print('\n试玩完成奖励')
   global tid,pkg
   try:
        hd['Referer']='https://eopa.baidu.com/page/pagekey-l4t5CEae?productid=1&type=1&tid=393&rvid=379'
        response = requests.get('https://eopa.baidu.com/api/task/1/task/256/complete?pkg='+pkg+'&sys=ios&_=1615128599066',headers=hd,timeout=10)
        userRes=json.loads(response.text)
        print(userRes['msg'])
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
   global result,hd,btlist,urllist,hdlist,bdlist,taskidlist,id,tid,tasklist
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('bd_ck',btlist)
   watch('hk_task',taskidlist)
   tasklist=s(taskidlist[0])
   if not taskidlist[0]:
       exit()
   for ac in range(acloop):
      result=''
      for cc in range(len(btlist)):
        result+='【'+str(cc+1)+'】'
        hd['Cookie']=btlist[cc]
        kindapretty()
        print('【'+str(ac+1)+'】-'+'【'+str(cc+1)+'】-'+'🏆🏆🏆🏆运行完毕')
        result+='\n'
  # print(result)
   pushmsg('白菜_漂亮20210308',result)
    
    
   
     
if __name__ == '__main__':
       start()
    
