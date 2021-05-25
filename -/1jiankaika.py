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




userNameList = []
cookiesList = []
pinNameList = []
jd_cookie=''
grouplist=[]
#=============


bean=0
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




def GetGrouplist():
    print('\n获取开卡信息')
    global result_all,grouplist
    grouplist=[]
    result=''
    url = 'https://jdjoy.jd.com/module/unioncard/getHomeInfo?activityCode=9c70cbc2575e44f29a3f028bc28f5c44&invitePin=&relatedCode=&_t='
    headers ={"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Connection": "keep-alive","Cookie": jd_cookie,"Host": "jdjoy.jd.com","Origin": "https://prodev.m.jd.com","User-Agent": "jdapp;iPhone;9.4.0;14.4.2;3c6b06b6a8d9cc763215d2db748273edc4e02512;network/4g;ADID/B38160D2-DC94-4414-905B-D15F395FD787;supportApplePay/0;hasUPPay/0;hasOCPay/0;model/iPhone11,8;addressid/2995956914;supportBestPay/0;appBuild/167541;jdSupportDarkMode/0;Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1"}
    
    resp = requests.get(url=url,headers=headers,timeout=60).json()
    #print(resp)
    if resp['success']:
       result=resp['data']['activityDetail']['activityName']+'-'+resp['data']['activityDetail']['mainTitle']+resp['data']['activityDetail']['activityStatus']
       print(result)
       result_all+=result
       grouplist=resp['data']['activityDetail']['groups']
       
    else:
        result='返回错误:'+resp['errorCode']

    
def submitBindCards(brandsIds,token):
    print('\n提交开卡信息')
    result=''
    url = 'https://crmsam.jd.com/union/submitBindCards'
    headers ={"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Connection": "keep-alive","Content-Type": "application/json","Cookie": jd_cookie,"Host": "crmsam.jd.com","Origin": "https://crmsam.jd.com","User-Agent": "jdapp;iPhone;9.4.0;14.4.2;3c6b06b6a8d9cc763215d2db748273edc4e02512;network/4g;ADID/B38160D2-DC94-4414-905B-D15F395FD787;supportApplePay/0;hasUPPay/0;hasOCPay/0;model/iPhone11,8;addressid/2995956914;supportBestPay/0;appBuild/167541;jdSupportDarkMode/0;Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1"}
    
    body={"phone":None,"smsCode":None,"brandsIds":brandsIds,"bindChannel":False,"activityId":"","token":token}
    resp = requests.post(url=url,headers=headers,data=json.dumps(body),timeout=60).json()
    #print(resp)
    if resp['message']=='SUCCESS':
       for data in resp['data']:
        print(data['brandsName']+'-开卡'+data['detail']+'\n')
    else:
        result='返回错误:'+resp['message']

def Yijiankaika():
   print('\n一键开卡')
   GetGrouplist()
   for i in range(len(grouplist)):
     brandsIds=[]
     token=''
     if grouplist[i]['joinStatus']=='not_member':
       cardConfigs=grouplist[i]['cardConfigs']
       bindCardUrl=grouplist[i]['bindCardUrl']
       token=re.compile('token=(.+)&url=').findall(bindCardUrl)[0]
       print(token)
       for j in range(len(cardConfigs)):
          brandsIds.append(cardConfigs[j]['cardId'])
       print('【第'+str(i+1)+'组】开卡:')
       submitBindCards(brandsIds,token)
       time.sleep(2)
     else:
        print('【第'+str(i+1)+'组】开卡:已经开过卡了')


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





def start():
       global jd_cookie
       scriptHeader = """
════════════════════════════════════════
║                                      ║
║     京东一键开卡-公众号iosrule          ║
║                                      ║
════════════════════════════════════════
"""
       print(scriptHeader)
       Readint()
       iscookie()
       for i in range(len(cookiesList)):
         if github==0:
         	print(f"【{i+1}】-【用户名:{pinNameList[i]}】-任务开始\n")
         else:
            print(f"【{i+1}】-任务开始\n")
         jd_cookie=cookiesList[i]
         #if i!=2:
             #continue
         Yijiankaika()

if __name__ == '__main__':
    print('Localtime', datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
    start()
