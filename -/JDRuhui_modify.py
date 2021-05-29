#!/bin/env python3
# -*- coding: utf-8 -*
'''
修改自https://github.com/curtinlv/JD-Script

'''
import time, os, sys, datetime
import requests
import random, string
import re, json,base64
from urllib.parse import unquote
from threading import Thread
from configparser import RawConfigParser
from dateutil import tz
import urllib
# 定义一些要用到参数
requests.packages.urllib3.disable_warnings()

timestamp = int(round(time.time() * 1000))

Card_telegram=''

osenviron={}
djj_djj_cookie=''




cookies = ''
openCardBean = 1
sleepNum = 0.5
isRemoteSid = True
allShopid=[]
userNameList = []
cookiesList = []
pinNameList = []
bean=[]


################################### Function ################################

def nowtime():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')




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
        pushmsg('一键入会',msg)
        return ck, False


# 设置Headers
def setHeaders(cookie, intype):
    if intype == 'mall':
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Host": "shop.m.jd.com",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
            "Accept-Language": "zh-cn",
            "Accept-Encoding": "gzip, deflate, br",
            # "Connection": "keep-alive"
            "Connection": "close"
        }
        return headers
    elif intype == 'JDApp':
        headers = {
            'Cookie': cookie,
            'Accept': "*/*",
            'Connection': "close",
            'Referer': "https://shopmember.m.jd.com/shopcard/?",
            'Accept-Encoding': "gzip, deflate, br",
            'Host': "api.m.jd.com",
            'User-Agent': "jdapp;iPhone;9.4.8;14.3;809409cbd5bb8a0fa8fff41378c1afe91b8075ad;network/wifi;ADID/201EDE7F-5111-49E8-9F0D-CCF9677CD6FE;supportApplePay/0;hasUPPay/0;hasOCPay/0;model/iPhone13,4;addressid/;supportBestPay/0;appBuild/167629;jdSupportDarkMode/0;Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
            'Accept-Language': "zh-cn"
        }
        return headers
    elif intype == 'mh5':
        headers = {
            'Cookie': cookie,
            'Accept': "*/*",
            'Connection': "close",
            'Referer': "https://shopmember.m.jd.com/shopcard/?",
            'Accept-Encoding': "gzip, deflate, br",
            'Host': "api.m.jd.com",
            'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
            'Accept-Language': "zh-cn"

        }
        return headers









# 获取VenderId
def getVenderId(shopId, headers):
    """
    :param shopId:
    :param headers
    :return: venderId
    """
    url = 'https://shop.m.jd.com/?shopId={0}'.format(shopId)
    resp = requests.get(url=url, verify=False, headers=headers, timeout=60)
    resulttext = resp.text
    r = re.compile(r'venderId: \'(\d+)\'')
    venderId = r.findall(resulttext)
    return venderId[0]


# 查询礼包
def getShopOpenCardInfo(venderId, headers, shopid, userName):
    """
    :param venderId:
    :param headers:
    :return: activityId,getBean 或 返回 0:没豆 1:有豆已是会员 2:记录模式（不入会）
    """
    num1 = string.digits
    v_num1 = ''.join(random.sample(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 1)) + ''.join(
        random.sample(num1, 4))  # 随机生成一窜4位数字
    url = 'https://api.m.jd.com/client.action?appid=jd_shop_member&functionId=getShopOpenCardInfo&body=%7B%22venderId%22%3A%22{2}%22%2C%22channel%22%3A406%7D&client=H5&clientVersion=9.2.0&uuid=&jsonp=jsonp_{0}_{1}'.format(
        timestamp, v_num1, venderId)
    resp = requests.get(url=url, verify=False, headers=headers, timeout=60)
    time.sleep(sleepNum)
    resulttxt = resp.text
    r = re.compile(r'jsonp_.*?\((.*?)\)\;', re.M | re.S | re.I)
    result = r.findall(resulttxt)
    cardInfo = json.loads(result[0])
    venderCardName = cardInfo['result']['shopMemberCardInfo']['venderCardName']  # 店铺名称
    print(f"\t╰查询入会礼包【{venderCardName}】{shopid}")
    openCardStatus = cardInfo['result']['userInfo']['openCardStatus']  # 是否会员
    interestsRuleList = cardInfo['result']['interestsRuleList']
    if interestsRuleList == None:
        print("\t\t╰Oh,该店礼包已被领光了~")
        return 0, 0
    try:
        if len(interestsRuleList) > 0:
            for i in interestsRuleList:
                if "京豆" in i['prizeName']:
                    getBean = int(i['discountString'])
                    activityId = i['interestsInfo']['activityId']
                    in_url='https://shop.m.jd.com/?shopId={}'.format(shopid)
                    url = 'https://shopmember.m.jd.com/member/memberCloseAccount?venderId={}'.format(venderId)
                    context = "[{0}]:入会{2}豆店铺【{1}】\n\t加入会员:{4}\n\t解绑会员:{3}".format(nowtime(), venderCardName, getBean, url,in_url)  # 记录
   
                    if getBean >= openCardBean:  # 判断豆是否符合您的需求
                        print(f"\t╰{venderCardName}:入会赠送【{getBean}豆】，可入会")
                        context = "{0}".format(shopid)
                        
          
                            
                        if openCardStatus == 1:
                            url = 'https://shopmember.m.jd.com/member/memberCloseAccount?venderId={}'.format(venderId)
                            print("\t\t╰[账号：{0}]:您已经是本店会员，请注销会员卡24小时后再来~\n注销链接:{1}".format(userName, url))
                            pushmsg('注销卡',f"\t╰{venderCardName}:入会赠送【{getBean}豆】，可入会\n"+"\t\t╰[账号：{0}]:您已经是本店会员，请注销会员卡24小时后再来~\n注销链接:{1}".format(userName, url))
                            context = "[{3}]:入会{1}豆，{0}销卡：{2}".format(venderCardName, getBean, url, nowtime())
                            return 1, 1
                        return activityId, getBean
                    else:
                        print(f'\t\t╰{venderCardName}:入会送【{getBean}】豆少于【{openCardBean}豆】,不入...')
                    
                        return 0, openCardStatus

                else:
                    pass
            print("\t\t╰Oh~ 该店入会京豆已被领光了")
            return 0, 0
        else:
            return 0, 0
    except Exception as e:
        print(e)


# 开卡
def bindWithVender(venderId, shopId, activityId, channel, headers):
    """
    :param venderId:
    :param shopId:
    :param activityId:
    :param channel:
    :param headers:
    :return: result : 开卡结果
    """
    num = string.ascii_letters + string.digits
    v_name = ''.join(random.sample(num, 10))
    num1 = string.digits
    v_num1 = ''.join(random.sample(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 1)) + ''.join(random.sample(num1, 4))
    qq_num = ''.join(random.sample(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 1)) + ''.join(
        random.sample(num1, 8)) + "@qq.com"
    url = 'https://api.m.jd.com/client.action?appid=jd_shop_member&functionId=bindWithVender&body=%7B%22venderId%22%3A%22{4}%22%2C%22shopId%22%3A%22{7}%22%2C%22bindByVerifyCodeFlag%22%3A1%2C%22registerExtend%22%3A%7B%22v_sex%22%3A%22%E6%9C%AA%E7%9F%A5%22%2C%22v_name%22%3A%22{0}%22%2C%22v_birthday%22%3A%221990-03-18%22%2C%22v_email%22%3A%22{6}%22%7D%2C%22writeChildFlag%22%3A0%2C%22activityId%22%3A{5}%2C%22channel%22%3A{3}%7D&client=H5&clientVersion=9.2.0&uuid=&jsonp=jsonp_{1}_{2}'.format(
        v_name, timestamp, v_num1, channel, venderId, activityId, qq_num, shopId)
    try:
        respon = requests.get(url=url, verify=False, headers=headers, timeout=60)
        result = respon.text
        return result
    except Exception as e:
        print(e)


# 获取开卡结果
def getResult(resulttxt, userName, user_num):
    global bean
    r = re.compile(r'jsonp_.*?\((.*?)\)\;', re.M | re.S | re.I)
    result = r.findall(resulttxt)
    for i in result:
        result_data = json.loads(i)
        busiCode = result_data['busiCode']
        if busiCode == '0':
            message = result_data['message']
            try:
                result = result_data['result']['giftInfo']['giftList']
                #print(f"\t\t╰用户{user_num}【{userName}】:{message}")
                print(f"\t\t╰用户【{user_num}】:{message}")
                for i in result:
                    print("\t\t\t╰{0}:{1} ".format(i['prizeTypeName'], i['discount']))
                    if i['prizeTypeName']=='京豆':
                      bean[user_num-1]+=result[0]['discount']
            except:
                print(f'\t\t╰用户【{user_num}】:{message}')
            return busiCode
        else:
            print("\t\t╰用户【{0}】:{2}".format(user_num, result_data['message']))
            return busiCode

def gettext(url):
    try:
        resp = requests.get(url,timeout=60).text
        if '该内容无法显示' in resp:
            gettext(url)
        return resp
    except Exception as e:
        print(e)
        
def getRemoteShopid():
    url = base64.decodebytes(
        b"aHR0cHM6Ly9naXRlZS5jb20vY3VydGlubHYvUHVibGljL3Jhdy9tYXN0ZXIvT3BlbkNyYWQvc2hvcGlkLnR4dA==")
    try:
        rShopid= gettext(url)
        rShopid=rShopid.split("\n")
        return rShopid
    except:
        print("无法从远程获取shopid")
        exitCodeFun(999)


# 进度条
def progress_bar(start, end, threadNum):
    print("\r", end="")
    if threadNum == 2:
        start2 = start - midNum
        end2 = end - midNum
        print("\n###[{1}]:线程{2}【当前进度: {0}%】\n".format(round(start2 / end2 * 100, 2), nowtime(), threadNum))
    elif threadNum == 1:
        print("\n###[{1}]:线程{2}【当前进度: {0}%】\n".format(round(start / end * 100, 2), nowtime(), threadNum))
    sys.stdout.flush()


# 为多线程准备
def OpenVipCrad(startNum: int, endNum: int, shopids, cookies, userNames, pinNameList, threadNum):

    
    for i in range(startNum, endNum):
        user_num = 1
        
        activityIdLabel = 0
        for ck, userName, pinName in zip(cookies, userNames, pinNameList):
            
            if i % 10 == 0 and i != 0:
                progress_bar(i, endNum, threadNum)
            try:
                if len(shopids[i]) > 0:
                    print('【用户'+str(user_num)+'】任务运行结果:')
                    headers_b = setHeaders(ck, "mall")  # 获取请求头
                    venderId = getVenderId(shopids[i], headers_b)  # 获取venderId
                    time.sleep(sleepNum)  # 根据用户需求是否限制请求速度
                    # 新增记忆功能
                    
                    if activityIdLabel == 0:
                        headers_a = setHeaders(ck, "mh5")
                        activityId, getBean = getShopOpenCardInfo(venderId, headers_a, shopids[i], userName)  # 获取入会礼包结果
                    #  activityId,getBean 或 返回 0:没豆 1:有豆已是会员 2:记录模式（不入会）
                    time.sleep(sleepNum)  # 根据用户需求是否限制请求速度
                    if activityId == 0 or activityId == 2:
                        break
                    elif activityId == 1:
                        user_num += 1
                        continue
                    elif activityId > 10:
                        activityIdLabel = 1
                        headers = setHeaders(ck, "JDApp")
                        result = bindWithVender(venderId, shopids[i], activityId, 208, headers)
                        busiCode = getResult(result, userName, user_num)
                        if busiCode == '0':
                            print(f"用户【{user_num}:】累计获得：{bean[user_num-1]} 京豆")
                            #print(f"用户{user_num}:【{userName}】累计获得：{bean[user_num-1]} 京豆")
                            time.sleep(sleepNum)
                    else:
                        break
            except Exception as e:
                user_num += 1
                print(e)
                continue
            user_num += 1
            
    time.sleep(1)
    progress_bar(endNum, endNum, threadNum)


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
   if "JD_COOKIE" in os.environ:
      djj_djj_cookie = os.environ["JD_COOKIE"]
   if "JD_COOKIE" in osenviron:
      djj_djj_cookie = osenviron["JD_COOKIE"]
   if not djj_djj_cookie:
       print(f'''【djj_djj_cookie】 is empty,DTask is over.''')
       exit()



# start
def start():
    global endShopidNum, midNum, allUserCount,bean
    Readint()
    print("获取用户...")
    cookiesList, userNameList, pinNameList = iscookie()
    
    allUserCount = len(cookiesList)
    for i in range(allUserCount):
           bean.append(0)
    print(bean)
    if isRemoteSid:
        print("已启用远程获取shopid")
        allShopid = getRemoteShopid()
 
    allShopid = list(set(allShopid))
    endShopidNum = len(allShopid)
    print('endShopidNum='+str(endShopidNum))
    midNum = int(endShopidNum / 2)
    print("获取到店铺数量:", endShopidNum)
    print(f"您已设置入会条件：{openCardBean} 京豆")
    
    memorylabel = 0
    startNum1 = 0
    startNum2 = midNum
    starttime = time.perf_counter()  # 记录时间开始
    if endShopidNum > 1:
        # 如果启用记忆功能，则获取上一次记忆位置
        #startNum1, startNum2, memorylabel = isMemory(memorylabel, startNum1, startNum2, midNum, endShopidNum,pinNameList)
        # 多线程部分
        threads = []
        t1 = Thread(target=OpenVipCrad, args=(startNum1, startNum2, allShopid, cookiesList, userNameList, pinNameList, 1))
        threads.append(t1)
        t2 = Thread(target=OpenVipCrad, args=(startNum2, endShopidNum, allShopid, cookiesList, userNameList, pinNameList, 2))
        threads.append(t2)
        try:
            for t in threads:
                t.setDaemon(True)
                t.start()
            for t in threads:
                t.join()
            isSuccess = True
        except:
            isSuccess = False
    elif endShopidNum == 1:
        isSuccess = True
    else:
        print("获取到shopid数量为0")
        exitCodeFun(9)
    endtime = time.perf_counter()  # 记录时间结束
    n = 1
    result=''
    for name,pinname in zip(userNameList,pinNameList):
          try:
              result+=f"用户{n}:【{name}】:本次累计获得：{bean[n-1]}豆\n"
              #print(f"用户{n}:【{name}】:本次累计获得：{bean[n-1]}豆")
          except:
              print('统计结果错误')
          n += 1
     
    time.sleep(1)
    t=datetime.datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", )
    pushmsg('开卡入会'+t,result)
    print("--- 入会总耗时 : %.03f 秒 seconds ---" % (endtime - starttime))
    exitCodeFun(0)

if __name__ == '__main__':
    start()
