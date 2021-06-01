#!/bin/env python3
# -*- coding: utf-8 -*
'''
转载

'''
import time, os, sys
import requests
import random, string
import re, json,base64
from urllib.parse import unquote
from threading import Thread
from configparser import RawConfigParser
from dateutil import tz
import urllib
from datetime import datetime

# 定义一些要用到参数
requests.packages.urllib3.disable_warnings()

timestamp = int(round(time.time() * 1000))
shopidlist=[]
Card_telegram=''
beanshop=[]
osenviron={}
djj_djj_cookie=''
midNum=0
log=0


UA=["Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1","Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1","Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Mobile Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15"]








cookies = ''
userNameList = []
cookiesList = []
pinNameList = []



################################### Function ################################

def nowtime():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def exitCodeFun(code):
    try:
        exitCode = input()
        print(exitCode)
        exit(code)
    except:
        time.sleep(3)
        exit(code)


# 检测cookie格式是否正确
def iscookie():
    """
    :return: cookiesList,userNameList,pinNameList
    """
    cookiesList = []
    userNameList = []
    pinNameList = []
    if 'pt_key=' in djj_djj_cookie and 'pt_pin=' in djj_djj_cookie:
        r = re.compile(r"pt_key=.*?pt_pin=.*?;", re.M | re.S | re.I)
        result = r.findall(djj_djj_cookie)
        if len(result) >= 1:
            print("您已配置{}个账号".format(len(result)))
            for i in result:
                r = re.compile(r"pt_pin=(.*?);")
                pinName = r.findall(i)
                pinName = unquote(pinName[0])
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
                exitCodeFun(3)
        else:
            print("cookie 格式错误！...本次操作已退出")
            exitCodeFun(4)
    else:
        print("cookie 格式错误！...本次操作已退出")
        exitCodeFun(4)



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
        resp = requests.get(url=url, verify=False, headers=headers, timeout=60).text
        r = re.compile(r'GetJDUserInfoUnion.*?\((.*?)\)')
        result = r.findall(resp)
        userInfo = json.loads(result[0])
        nickname = userInfo['data']['userInfo']['baseInfo']['nickname']
        return ck, nickname
    except Exception:
        #print(f"用户【{pinName}】Cookie 已失效！请重新获取。")
        msg=f"用户【{pinName}】Cookie 已失效！请重新获取。"
        pushmsg('ck失效',msg)
        return ck, False
def getShopMemberCardDetail(shopId,VenderId,shopName):
    global shopidlist
    print(shopId,VenderId,shopName)
    url = f"https://api.m.jd.com/client.action?appid=jd_shop_member&functionId=getShopMemberCardDetail&body=%7B%22venderId%22%3A%22{VenderId}%22%2C%22channel%22%3A406%7D&client=H5&clientVersion=9.2.0&uuid=88888&"
    
    headers={"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Connection": "keep-alive","Cookie":djj_djj_cookie,"Host": "api.m.jd.com","User-Agent": random.choice(UA)}
    headers['Referer']=f"https://shopmember.m.jd.com/shopcard/?venderId={VenderId}&shopId={shopId}&venderType=0&channel=406&sceneval=2&jxsid=16225098685377580567"
    resp = requests.get(url=url,headers=headers,timeout=60).json()
    if resp['code']=='0':
       bean=0
       huiyuan=0
       cardRightsList=resp['result']['cardRightsList']
       if len(cardRightsList)>0:
           huiyuan=1
       if json.dumps(resp).find('newGiftList')>0:
          newGiftList=resp['result']['newGiftList']
          for data in newGiftList:
            if data['prizeTypeName']=='京豆':
               bean=data['discount']
       if huiyuan==1:
         shopidlist.append(str(shopId)+'-'+str(VenderId)+'-'+shopName+'-'+str(huiyuan)+'-'+str(bean))
       



def getVenderId(shopId):
    url = f"https://shop.m.jd.com/?shopId={shopId}"
    netisok=False
    venderId=0
    shopName=''
    headers={"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Connection": "keep-alive","Cookie":djj_djj_cookie,"User-Agent": random.choice(UA)}
    resp = requests.get(url=url,headers=headers,timeout=60)
    #print(resp.text)
    if str(resp).find('200')>0 and resp.text.find('venderId')>0:
      
      r = re.compile(r'venderId: \'(\d+)\'')
      venderId = r.findall(resp.text)[0]
      r = re.compile('shopName: \(\'(.+)\'\)')
      if len(r.findall(resp.text))>0:
         netisok=True
         shopName=r.findall(resp.text)[0]
         if shopName.find('类目运营test')>=0:
           netisok=False
           p(str(shopId)+shopName+'店铺不存在❌\ n')
         r = re.compile('shopTotalNum: Number\(\'(.+)\'\)')
         shopTotalNum = r.findall(resp.text)[0]
      
         p('shopTotalNum:'+shopTotalNum)
         if shopTotalNum=='0':
           netisok=False
           p(str(shopId)+'shopTotalNum'+'店铺不存在❌')
      else:
           p(str(shopId)+'店铺名字不存在❌')
    else:
         p(str(shopId)+'数据为空❌,跳过.....')
    return netisok,venderId,shopName




        
def getRemoteShopid(start,end,threadNum):
    #try:
        netisok=False
        venderId=0
        shopName=''
        i=0
        for shopId in range(start,end):
           
           i+=1
           p('\n'+str(i)+'获取会员详情:'+str(shopId)+'线程:'+str(threadNum)+'\n')
           if i % 10 == 0 and i != 0:
                progress_bar(i, end-start, threadNum)
           netisok,venderId,shopName=getVenderId(shopId)
           if netisok==True:
              getShopMemberCardDetail(shopId,venderId,shopName)
              
           time.sleep(5)
        time.sleep(5)
  


def progress_bar(start, end, threadNum):
    print("\r", end="")
    if threadNum == 2:
        
        print("\n###[{1}]:线程{2}【当前进度: {0}%】\n".format(round(start / end * 100, 2), nowtime(), threadNum))
        print(str(start)+'-'+str(end))
    elif threadNum == 1:
        print("\n###[{1}]:线程{2}【当前进度: {0}%】\n".format(round(start / end * 100, 2), nowtime(), threadNum))
        
    sys.stdout.flush()
    
    
def multrun(start,end):
    global midNum
    midNum = start+int((end-start) / 2)
    p('开始数:'+str(start)+'中间值'+str(midNum)+'结束数字'+str(end))
    #return 
    
    if end-start > 1:
        threads = []
        t1 = Thread(target=getRemoteShopid, args=(start, midNum,1))
        threads.append(t1)
        t2 = Thread(target=getRemoteShopid, args=(midNum, end,2))

        threads.append(t2)
        #t1.setDaemon(True)
        #t2.setDaemon(True)
        #t1.start()
        #t2.start()
        
        try:
            for t in threads:
                t.setDaemon(True)
                t.start()
            for t in threads:
                t.join()
            isSuccess = True
        except:
            isSuccess = False

        
        
    elif end == 1:
        isSuccess = True
    



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
def Readint():
   global Card_telegram,djj_djj_cookie

   if "Card_telegram" in os.environ:
      Card_telegram = os.environ["Card_telegram"]
   if "Card_telegram" in osenviron:
      Card_telegram = osenviron["Card_telegram"]
   if not Card_telegram:
       print(f'''【通知参数】 is empty,DTask is over.''')
   if "MM_COOKIE" in os.environ:
      djj_djj_cookie = os.environ["MM_COOKIE"]
   if "MM_COOKIE" in osenviron:
      djj_djj_cookie = osenviron["MM_COOKIE"]
   if not djj_djj_cookie:
       print(f'''【MM_COOKIE】 is empty,DTask is over.''')
       exit()
def p(msg):
   if log==1:
      print(msg)
      
def logmember(shopidlist):
   global beanshop
   print('\n统计会员商店ID共计'+str(len(shopidlist))+'个:\n')
   if len(shopidlist)==0:
       return
   print(shopidlist)
   for i in range(len(shopidlist)):
     Arry=shopidlist[i].split('-')
     shopId=Arry[0]
     VenderId=Arry[1]
     shopName=Arry[2]
     huiyuan=Arry[3]
     bean=Arry[4]
     i+=1
     if int(bean)>0:
       print(f"【{i}】入会{bean}京东豆:")
       print(f"加入店铺{shopName}会员:https://shop.m.jd.com/?shopId={shopId}")
       print(f"取消店铺{shopName}会员:https://shopmember.m.jd.com/member/memberCloseAccount?venderId={VenderId}\n")
       beanshop.append(shopId)
   if len(beanshop)==0:
       return
   print('\n统计京豆商店ID共计'+str(len(beanshop))+'个:\n')
   print(beanshop)
# start
def start():
    global  djj_djj_cookie
    starttime = time.perf_counter()  # 记录时间开始
    Readint()
    cookiesList, userNameList, pinNameList = iscookie()
    djj_djj_cookie=cookiesList[0]
    b=7000
    e=10000
    print('开启任务')
    #multrun(10352080,10352090)
    multrun(b,e)
    
    
    logmember(shopidlist)
    endtime = time.perf_counter()  # 记录时间结束
    print("--- 获取店铺id总耗时 : %.03f 秒 seconds ---" % (endtime - starttime))
    
    t=datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", )
    
    pushmsg('('+str(b)+'-'+str(e)+')'+t,'统计'+str(len(beanshop))+'/'+str(len(shopidlist))+'\n-- 获取店铺id总耗时 : '+str(endtime - starttime)+'秒---')
    
    exit()

if __name__ == '__main__':
    start()


