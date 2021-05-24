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
Card_num=0
github=1#判断是否在远程运行

#618入口https://carnivalcity.m.jd.com/#/home
#通知telegram格式,机器人id@自己的id




userNameList = []
cookiesList = []
pinNameList = []
shareIdlist=[]#互助码

#=============
questionTask={}
meetingTask= []
shopTask= []
skuTask= []
brandList=[]


      
shareId=''
result=''
bean=0
jifen=0
ispartin=False
result_all=''

def getUserInfo(ck, pinName):
    url = 'https://me-api.jd.com/user_new/info/GetJDUserInfoUnion?orgFlag=JD_PinGou_New&callSource=mainorder&channel=4&isHomewhite=0&sceneval=2&sceneval=2&callback=GetJDUserInfoUnion'
    headers = {
        'Cookie': ck,
        'Accept': '*/*',
        'Connection': 'close',
        'Referer': 'https://home.m.jd.com/myJd/home.action',
        'Accept-Encoding': 'gzip, deflate, br',
        'Host': 'me-api.jd.com',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Mobile/15E148 Safari/604.1',
        'Accept-Language': 'zh-cn'
    }
    try:
        resp = requests.get(url=url, headers=headers, timeout=60).text
        r = re.compile(r'GetJDUserInfoUnion.*?\((.*?)\)')
        result = r.findall(resp)
        userInfo = json.loads(result[0])
        nickname = userInfo['data']['userInfo']['baseInfo']['nickname']
        return ck, nickname
    except Exception:
        pushmsg(f"用户【{pinName}】Cookie 已失效！",'请重新获取。')
        
        return ck, False


def iscookie():
    
    cookies = djj_djj_cookie
    
    if 'pt_key=' in cookies and 'pt_pin=' in cookies:
        r = re.compile(r"pt_key=.*?pt_pin=.*?;", re.M | re.S | re.I)
        result = r.findall(cookies)
        if len(result) >= 1:
            print("您已配置{}个账号".format(len(result)))
            for i in result:
                r = re.compile(r"pt_pin=(.*?);")
                pinName = r.findall(i)
                pinName = urllib.parse.unquote(pinName[0])
                
                # 获取用户名
                ck, nickname = getUserInfo(i, pinName)
                if nickname != False:
                    cookiesList.append(ck)
                    userNameList.append(nickname)
                    pinNameList.append(pinName)
                else:
                    continue
                
            if len(cookiesList) > 0 and len(userNameList) > 0:
                return cookiesList, userNameList, pinNameList
            else:
                print("没有可用Cookie，已退出")
                exit()
        else:
            print("cookie 格式错误！...本次操作已退出")
            exit()
    else:
        print("cookie 格式错误！...本次操作已退出")
        exit()


def task_mult(count):
     #skuTask,shopTask,meetingTask,questionTask,brandList
     
   for k in range(len(brandList)):
     brandId=brandList[k]['brandId']
     print(f"\n【{k+1}】【{brandId}品牌任务开始】\n")
     brandTaskInfo(count,brandId)
     browseId=''
     if len(skuTask)==0:
        print('账号黑了')
        break
     print('任务1═══════════════════════════════════')
     
     for i in range(len(skuTask)):
       print(f"开始浏览任务【{i+1}】-{skuTask[i]['name']}")
       body='brandId='+brandId+'&id='+skuTask[i]['id']+'&taskMark=brand&type=presell&logMark=browseSku'
       browseId=task_doBrowse(count,skuTask[i]['id'],body)
       time.sleep(5)
       print(f"任务【{i+1}】-{skuTask[i]['name']}奖励")
       task_getBrowsePrize(count,browseId,brandId)
       
     print('任务2═══════════════════════════════════')
     for i in range(len(meetingTask)):
       print(f"开始浏览任务任务【{i+1}】-{meetingTask[i]['name']}")
       body='brandId='+brandId+'&id='+meetingTask[i]['id']+'&taskMark=brand&type=meeting&logMark=browseVenue'
       browseId=task_doBrowse(count,meetingTask[i]['id'],body)
       time.sleep(5)
       print(f"任务【{i+1}】-{meetingTask[i]['name']}奖励")
       task_getBrowsePrize(count,browseId,brandId)
       time.sleep(1)
       print(f"【{brandId}品牌任务结束】")
       

def brandTaskInfo(count,brandId):
    global result,meetingTask,shopTask,skuTask,questionTask
    result=''
    url = 'https://carnivalcity.m.jd.com/khc/index/brandTaskInfo?brandId='+brandId+'&t=1621815248440'
    headers = {"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Connection": "keep-alive","Cookie":count,"Host": "carnivalcity.m.jd.com","Referer": "https://carnivalcity.m.jd.com/","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"}
    
    resp = requests.get(url=url,headers=headers,timeout=60).json()
    #print(resp)
    if resp['code']==200:
       skuTask=resp['data']['skuTask']
       shopTask=resp['data']['shopTask']
       meetingTask=resp['data']['meetingTask']
       questionTask=resp['data']['questionTask']
       return skuTask,shopTask,meetingTask,questionTask
    else:
        result='🍵'+resp['msg']

    
    #result=f"现有积分{resp['data']['integralCount']}排名{resp['data']['rank']}"
    #print(result)
def task_doBrowse(count,id,body):
    global result
    url = 'https://carnivalcity.m.jd.com/khc/task/doBrowse'
    headers = {"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Connection": "keep-alive",'Content-Type': 'application/x-www-form-urlencoded',"Cookie":count,"Host": "carnivalcity.m.jd.com","Referer": "https://carnivalcity.m.jd.com/","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"}
    
    
    resp = requests.post(url=url,headers=headers,data=body,timeout=60).json()
    if resp['code']==200:
      browseId=resp['data']['browseId']
      return browseId
    else:
      result='任务'+resp['msg']
      print(result)
    

def task_getBrowsePrize(count,browseId,brandId):
    result=''
    global bean,jifen
    url = 'https://carnivalcity.m.jd.com/khc/task/getBrowsePrize'
    headers = {"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Connection": "keep-alive",'Content-Type': 'application/x-www-form-urlencoded',"Cookie":count,"Host": "carnivalcity.m.jd.com","Referer": "https://carnivalcity.m.jd.com/","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"}
    body='brandId='+brandId+'&browseId='+browseId
    resp = requests.post(url=url,headers=headers,data=body,timeout=60).json()
    #print(resp)
    if resp['code']==200:
      result=f"任务:{resp['data']['jingBean']}京东豆-{resp['data']['integral']}积分"
      bean+=resp['data']['jingBean']
      jifen+=resp['data']['integral']
    else:
      result='任务'+resp['msg']
    print(result)
    



#积分排名
def carnivalcity(count):
    global result,brandList
    result=''
    url = 'https://carnivalcity.m.jd.com/khc/index/indexInfo?t=1621812633262'
    headers = {"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Connection": "keep-alive","Cookie":count,"Host": "carnivalcity.m.jd.com","Referer": "https://carnivalcity.m.jd.com/","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"}
    
    resp = requests.get(url=url,headers=headers,timeout=60).json()
    #print(resp)
    result=f"现有积分{resp['data']['integralCount']}排名{resp['data']['rank']}"
    #print(result)
    
    brandList=resp['data']['brandList']
    return brandList,result
    
def getBean(count):
    print('\n京东豆记录')
    url = 'https://carnivalcity.m.jd.com/khc/record/jingBeanRecord?pageNum=1'
    headers = {"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Connection": "keep-alive","Cookie":count,"Host": "carnivalcity.m.jd.com","Referer": "https://carnivalcity.m.jd.com/","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"}
    jingBeanNum=0
    resp = requests.get(url=url,headers=headers,timeout=60).json()
    #print(resp)
    if resp['code']==200:
      jingBeanNum=resp['data']['jingBeanNum']
    else:
      result='获取京豆记录失败:'+resp['msg']
      print(result)
    return jingBeanNum
    
    
#邀请码
def getshareId(count):
    global ispartin,shareId
    ispartin=False
    shareId=''
    url = 'https://carnivalcity.m.jd.com/khc/task/getSupport'
    headers = {"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Connection": "keep-alive","Cookie":count,"Host": "carnivalcity.m.jd.com","Referer": "https://carnivalcity.m.jd.com/","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"}
    
    resp = requests.get(url=url,headers=headers,timeout=60).json()
    if resp['code']==200:
      shareId=resp['data']['shareId']
      ispartin=True
    #else:
     # print('获取邀请码失败:'+resp['msg'])
      #ispartin=False
#助力
def doSupport(count,shareId):
    print('\n助力结果')
    global ispartin
    url = 'https://carnivalcity.m.jd.com/khc/task/doSupport'
    headers = {"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Connection": "keep-alive",'Content-Type': 'application/x-www-form-urlencoded',"Cookie":count,"Host": "carnivalcity.m.jd.com","Referer": "https://carnivalcity.m.jd.com/?","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"}
    body="shareId="+shareId
    resp = requests.post(url=url,headers=headers,data=body,timeout=60).json()
    print(resp)
    if resp['code']==200:
      if resp['data']['status']==3:
         print('你已经助力过了，不要重复助力')
      elif resp['data']['status']==6:
         print('助力成功')
      ispartin=True
    else:
      result='助力失败:'+resp['msg']
      ispartin=False
      print(result)

def Start_Support(count):
   print('\n开始助力')
   if len(shareIdlist)>0:
     for code in shareIdlist:
       if code!=shareId:
         doSupport(count,code)
         time.sleep(2)
       else:
           print('跳过自己的朱丽娜')
   else:
     print('本地朱丽娜为空，本次不助力')
     
def Get_shareIdlist():
   try:
     for ck in range(len(cookiesList)):
        getshareId(cookiesList[ck])
        if github==0:
            print(f"【{ck+1}】用户名:{pinNameList[ck]},邀请码:{shareId}\n")
        else:
            print(f"【{ck+1}】邀请码:{shareId}\n")
        if not shareId:
          continue
        if not ck in shareIdlist:
          shareIdlist.append(shareId)
        time.sleep(1)
   except Exception as e:
      print(str(e))
   print(f"本地邀请码共计{len(shareIdlist)}个:\n{shareIdlist}\n")
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
    
#def logtxt(user,tm):
  #if os.path.exists(f"/log/入会{user}_{tm}.txt"):
	#1000331552

def Readint():
   global Card_telegram,djj_djj_cookie

   if "Card_telegram" in os.environ:
      Card_telegram = os.environ["Card_telegram"]
   if "Card_telegram" in osenviron:
      Card_telegram = osenviron["Card_telegram"]
   if not Card_telegram:
       print(f'''【通知参数】 is empty,DTask is over.''')
   if "JD_COOKIE" in os.environ:
      djj_djj_cookie = os.environ["JD_COOKIE"]
   if "JD_COOKIE" in osenviron:
      djj_djj_cookie = osenviron["JD_COOKIE"]
   if not djj_djj_cookie:
       print(f'''【djj_djj_cookie】 is empty,DTask is over.''')
       exit()


def count_int():
   global bean,jifen,ispartin,shareId
   bean=0
   jifen=0
   questionTask={}
   meetingTask= []
   shopTask= []
   skuTask= []
   brandList=[]
   shareId=""

def show_result(i,count,username):
   print('\n任务统计')
   global result_all
   jingBeanNum=getBean(count)
   brandList,jinfen_rank=carnivalcity(count)
   result_all+=f"【{i+1}】-【{username}】,本次任务获得{bean}个京东豆,{jifen}积分,活动总京豆{jingBeanNum}个,{jinfen_rank}\n"
   if github==0:
     print(f"【{i+1}】-【{username}】,本次任务获得{bean}个京东豆,{jifen}积分,活动总京豆{jingBeanNum}个,{jinfen_rank}\n")
   else:
      print(f"【{i+1}】本次任务获得{bean}个京东豆,{jifen}积分,活动总京豆{jingBeanNum}个,{jinfen_rank}\n")
def start():
       scriptHeader = """
════════════════════════════════════════
║                                      ║
║     京东618 活动-助力助力助力           ║
║                                      ║
════════════════════════════════════════
"""
       print(scriptHeader)
       Readint()
       iscookie()
       Get_shareIdlist()
       for ck in range(len(cookiesList)):
         if github==0:
         	print(f"【{ck+1}】-【用户名:{pinNameList[ck]}】-任务开始\n")
         else:
            print(f"【{ck+1}】-任务开始\n")
         if ck==0:
             continue
         count_int()
         Start_Support(cookiesList[ck])
         #continue
         if not ispartin:
            print('号码黑了，无法参加活动')
            show_result(ck,cookiesList[ck],pinNameList[ck])
            continue
         carnivalcity(cookiesList[ck])
         task_mult(cookiesList[ck])
         show_result(ck,cookiesList[ck],pinNameList[ck])
       if github==0:
         print(result_all)
       pushmsg('京东618活动',result_all)
if __name__ == '__main__':
    print('Localtime', datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
    start()
