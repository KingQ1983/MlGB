import requests
import json
import rsa
import base64
import time
import timeit
from itertools import groupby
from functools import reduce
from random import choice
import hashlib
from datetime import datetime
from dateutil import tz
import os

# github 作者 https://github.com/Zero-S1/xmly_speed


cookies1 = ""  # 字符串形式 都可以识别
cookies2 = {
}  # 字典形式




cookiesList = []
xmly_speed_cookie =''
xmly_bark_cookie=''
djj_tele_cookie=''
iosrule=''
def str2dict(str_cookie):
    if type(str_cookie) == dict:
        return str_cookie

    tmp = str_cookie.split(";")
    dict_cookie = {}
    for i in tmp:
        j = i.split("=")
        if not j[0]:
            continue
        dict_cookie[j[0].strip()] = j[1].strip()
    return dict_cookie

UserAgent = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 iting/1.0.12 kdtunion_iting/1.0 iting(main)/1.0.12/ios_1"



def check():


   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))


   global xmly_speed_cookie
   global xmly_bark_cookie
   global djj_tele_cookie
 
   if "DJJ_TELE_COOKIE" in os.environ:
      djj_tele_cookie = os.environ["DJJ_TELE_COOKIE"]
   if "XMLY_BARK_COOKIE" in os.environ:
     xmly_bark_cookie = os.environ["XMLY_BARK_COOKIE"]
   if "XMLY_SPEED_COOKIE" in os.environ:
      xmly_speed_cookie = os.environ["XMLY_SPEED_COOKIE"]
      for line in xmly_speed_cookie.split('\n'):
        if not line:
          continue
        cookiesList.append(line.strip())
   elif xmly_speed_cookie:
       for line in xmly_speed_cookie.split('\n'):
         if not line:
            continue
         cookiesList.append(line.strip())
   else:
     print('Task is over.')
     exit()


def listenData(cookies,uid):
    headers = {
        'User-Agent': UserAgent,
        'Host': 'm.ximalaya.com',
        'Content-Type': 'application/json',
    }
    mins = int(time.time())
    date_stamp = (mins-57600) % 86400
    _datatime = datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y%m%d", )
    listentime = date_stamp
    print(listentime//60)
    currentTimeMillis = int(time.time()*1000)-2
    sign = hashlib.md5(
        f'currenttimemillis={currentTimeMillis}&listentime={listentime}&uid={uid}&23627d1451047b8d257a96af5db359538f081d651df75b4aa169508547208159'.encode()).hexdigest()
    data = {
        # 'activtyId': 'listenAward',
        'currentTimeMillis': currentTimeMillis,
        'listenTime': str(listentime),
        # 'nativeListenTime': str(listentime),
        'signature': sign,
        'uid': uid
    }
    try:
       response = requests.post('http://m.ximalaya.com/speed/web-earn/listen/client/data',
                             headers=headers, cookies=cookies, data=json.dumps(data))
       print(response.text)
    except:
        pass

def ans_receive(cookies, paperId, lastTopicId, receiveType):

    headers = {
        'User-Agent': UserAgent,
        'Content-Type': 'application/json;charset=utf-8',
        'Host': 'm.ximalaya.com',
        'Origin': 'https://m.ximalaya.com',
        'Referer': 'https://m.ximalaya.com/growth-ssr-speed-welfare-center/page/quiz',
    }
    _checkData = f"""lastTopicId={lastTopicId}&numOfAnswers=3&receiveType={receiveType}"""
    checkData = rsa_encrypt(str(_checkData), pubkey_str)

    data = {
        "paperId": paperId,
        "checkData": checkData,
        "lastTopicId": lastTopicId,
        "numOfAnswers": 3,
        "receiveType": receiveType
    }
    try:
        response = requests.post('https://m.ximalaya.com/speed/web-earn/topic/receive',
                             headers=headers, cookies=cookies, data=json.dumps(data))
        print(response.text)
    except Exception as e:
        msg=str(e)
        print(msg)


def ans_restore(cookies):
    """
    看视频回复体力，type=2
    """
    headers = {
        'User-Agent': UserAgent,
        'Content-Type': 'application/json;charset=utf-8',
        'Host': 'm.ximalaya.com',
        'Origin': 'https://m.ximalaya.com',
        'Referer': 'https://m.ximalaya.com/growth-ssr-speed-welfare-center/page/quiz',
    }
    checkData = rsa_encrypt("restoreType=2", pubkey_str)

    data = {
        "restoreType": 2,
        "checkData": checkData,
    }
    try:
        response = requests.post('https://m.ximalaya.com/speed/web-earn/topic/restore',
                             headers=headers, cookies=cookies, data=json.dumps(data))
        print(response.text)
    except Exception as e:
        msg=str(e)
        print(msg)


def ans_getTimes(cookies):

    headers = {
        'Host': 'm.ximalaya.com',
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'User-Agent': UserAgent,
        'Accept-Language': 'zh-cn',
        'Referer': 'https://m.ximalaya.com/growth-ssr-speed-welfare-center/page/quiz',
        'Accept-Encoding': 'gzip, deflate, br',
    }

    try:
       response = requests.get(
        'https://m.ximalaya.com/speed/web-earn/topic/user', headers=headers, cookies=cookies)
       result = json.loads(response.text)
       stamina = result["data"]["stamina"]  # 答题次数
       remainingTimes = result["data"]["remainingTimes"]  # 可回复次数
       print(f"answer_stamina答题次数: {stamina}")
       print(f"answer_remainingTimes可回复次数: {remainingTimes}\n")
       return {"stamina": stamina,
            "remainingTimes": remainingTimes}
    except Exception as e:
         msg=str(e)
         print(msg)

def ans_start(cookies):
    headers = {
        'Host': 'm.ximalaya.com',
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'User-Agent': UserAgent,
        'Accept-Language': 'zh-cn',
        'Referer': 'https://m.ximalaya.com/growth-ssr-speed-welfare-center/page/quiz',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    try:
       response = requests.get(
        'https://m.ximalaya.com/speed/web-earn/topic/start', headers=headers, cookies=cookies)
       result = json.loads(response.text)
       paperId = result["data"]["paperId"]
       dateStr = result["data"]["dateStr"]
       lastTopicId = result["data"]["topics"][2]["topicId"]
       print(paperId, dateStr, lastTopicId)
       return paperId, dateStr, lastTopicId
    except Exception as e:
        msg=str(e)
        print(msg)

def ans_main(cookies):
   print("\n【答题】")
   ans_times = ans_getTimes(cookies)
   try:
    for i in range(ans_times["stamina"]):
        paperId, dateStr, lastTopicId = ans_start(cookies)
        ans_receive(cookies, paperId, lastTopicId, 1)
        time.sleep(2)
        ans_receive(cookies, paperId, lastTopicId, 2)
        time.sleep(2)

    if ans_times["remainingTimes"] > 0:
        print("[看视频回复体力]")
        ans_restore(cookies)
        for i in range(5):
            paperId, dateStr, lastTopicId = ans_start(cookies)
            ans_receive(cookies, paperId, lastTopicId, 1)
            time.sleep(1)
            ans_receive(cookies, paperId, lastTopicId, 2)
            time.sleep(1)
   except Exception as e:
        msg=str(e)
        print(msg)

def _str2key(s):
    b_str = base64.b64decode(s)
    if len(b_str) < 162:
        return False
    hex_str = ''
    for x in b_str:
        h = hex(x)[2:]
        h = h.rjust(2, '0')
        hex_str += h
    m_start = 29 * 2
    e_start = 159 * 2
    m_len = 128 * 2
    e_len = 3 * 2
    modulus = hex_str[m_start:m_start + m_len]
    exponent = hex_str[e_start:e_start + e_len]
    return modulus, exponent


def rsa_encrypt(s, pubkey_str):
    key = _str2key(pubkey_str)
    modulus = int(key[0], 16)
    exponent = int(key[1], 16)
    pubkey = rsa.PublicKey(modulus, exponent)
    return base64.b64encode(rsa.encrypt(s.encode(), pubkey)).decode()


pubkey_str = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCVhaR3Or7suUlwHUl2Ly36uVmboZ3+HhovogDjLgRE9CbaUokS2eqGaVFfbxAUxFThNDuXq/fBD+SdUgppmcZrIw4HMMP4AtE2qJJQH/KxPWmbXH7Lv+9CisNtPYOlvWJ/GHRqf9x3TBKjjeJ2CjuVxlPBDX63+Ecil2JR9klVawIDAQAB"

def lottery_info(cookies,uid):
  print("\n【幸运大转盘】")
  headers = {
        'Host': 'm.ximalaya.com',
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'User-Agent': UserAgent,
        'Accept-Language': 'zh-cn',
        'Referer': 'https://m.ximalaya.com/xmds-node-spa/apps/speed-ad-sweepstake-h5/home',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    # 查询信息
  try:
    response = requests.get(
        'https://m.ximalaya.com/speed/web-earn/inspire/lottery/info', headers=headers, cookies=cookies)

    result = json.loads(response.text)
    print(result)

    remainingTimes = result["data"]["remainingTimes"]
    print(f'lottery_remainingTimes转盘剩余次数: {remainingTimes}\n')
    if result["data"]["chanceId"] == 0 and result["data"]["remainingTimes"] == 0:
        print("免费抽奖次数用完")
        return
    print('继续抽奖')
    data = {
            "sign": rsa_encrypt(str(result["data"]["chanceId"]), pubkey_str),
        }
    response = requests.post('https://m.ximalaya.com/speed/web-earn/inspire/lottery/action',
                                 headers=headers, cookies=cookies, data=json.dumps(data))
    print(response.text)
    if result["data"]["remainingTimes"] in [0, 1]:
        return
    data = {
        "sign": rsa_encrypt(str(result["data"]["chanceId"]), pubkey_str),
    }
    response = requests.post('https://m.ximalaya.com/speed/web-earn/inspire/lottery/action',
                             headers=headers, cookies=cookies, data=json.dumps(data))
    print(response.text)
    # for i in range(3):
    # 获取token
    # exit()
    if remainingTimes > 0:
        headers = {
            'Host': 'm.ximalaya.com',
            'Accept': 'application/json, text/plain, */*',
            'Connection': 'keep-alive',
            'User-Agent': UserAgent,
            'Accept-Language': 'zh-cn',
            'Referer': 'https://m.ximalaya.com/xmds-node-spa/apps/speed-ad-sweepstake-h5/home',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        response = requests.get(
            'https://m.ximalaya.com/speed/web-earn/inspire/lottery/token', headers=headers, cookies=cookies)
        print("token", response.text)
        result = json.loads(response.text)
        _id = result["data"]["id"]
        data = {
            "token": _id,
            "sign": rsa_encrypt(f"token={_id}&userId={uid}", pubkey_str),
        }
        headers = {
            'User-Agent': UserAgent,
            'Content-Type': 'application/json;charset=utf-8',
            'Host': 'm.ximalaya.com',
            'Origin': 'https://m.ximalaya.com',
            'Referer': 'https://m.ximalaya.com/xmds-node-spa/apps/speed-ad-sweepstake-h5/home',
        }
        response = requests.post('https://m.ximalaya.com/speed/web-earn/inspire/lottery/chance',
                                 headers=headers, cookies=cookies, data=json.dumps(data))
        result = json.loads(response.text)
        print("chance", result)
        data = {
            "sign": rsa_encrypt(str(result["data"]["chanceId"]), pubkey_str),
        }

        response = requests.post('https://m.ximalaya.com/speed/web-earn/inspire/lottery/action',
                                 headers=headers, cookies=cookies, data=json.dumps(data))
        print("action", response.text)
  except Exception as e:
        print("action", str(e))


def task_label(cookies):
  print("\n【收听时长 30 60 90 】")
  headers = {
        'Host': 'm.ximalaya.com',
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'User-Agent': UserAgent,
        'Accept-Language': 'zh-cn',
        'Referer': 'https://m.ximalaya.com/growth-ssr-speed-welfare-center/page/welfare',
        'Accept-Encoding': 'gzip, deflate, br',
    }

  params = (
        ('taskLabels', '1,2'),
    )
  try:
     response = requests.get('https://m.ximalaya.com/speed/task-center/task/record',
                            headers=headers, params=params, cookies=cookies)

     result = json.loads(response.text)
     taskList = result["taskList"]
     print(taskList)
     for i in taskList:
        if i["taskId"] in [79, 80, 81]:  # 收听时长
            if i["status"] == 1:  # 可以领取
                print(i)
                taskRecordId = i["taskRecordId"]
                headers = {
                    'User-Agent': UserAgent,
                    'Host': 'm.ximalaya.com',
                    'Referer': 'https://m.ximalaya.com/growth-ssr-speed-welfare-center/page/welfare',
                    'Origin': 'https://m.ximalaya.com',
                }

                response = requests.post(
                    f'https://m.ximalaya.com/speed/task-center/task/receive/{taskRecordId}', headers=headers, cookies=cookies)
                print(response.text)
                time.sleep(1)
  except Exception as e:
        msg=str(e)
        print(msg)
  print("\n")











def ad_score(cookies, businessType, taskId,uid):
    print("\n【听书点击广告收益】")
    headers = {
        'Host': 'm.ximalaya.com',
        'Accept': 'application/json, text/plain ,*/*',
        'Connection': 'keep-alive',
        'User-Agent': UserAgent,
        'Accept-Language': 'zh-cn',
        'Content-Type': 'application/json;charset=utf-8',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    try:
       response = requests.get(
        'https://m.ximalaya.com/speed/task-center/ad/token', headers=headers, cookies=cookies)
       result = response.json()
       token = result["id"]
       data = {
        "taskId": taskId,
        "businessType": businessType,
        "rsaSign": rsa_encrypt(f"""businessType={businessType}&token={token}&uid={uid}""", pubkey_str),
          }
       response = requests.post(f'https://m.ximalaya.com/speed/task-center/ad/score',
                             headers=headers, cookies=cookies, data=json.dumps(data))

       print(response.text)
    except Exception as e:
        msg=str(e)
        print(msg)
    print("\n")




def bubble(cookies,uid):
  print("\n【听书收集气泡】")
  headers = {
        'User-Agent': UserAgent,
        'Content-Type': 'application/json;charset=utf-8',
        'Host': 'm.ximalaya.com',
        'Origin': 'https://m.ximalaya.com',
        'Referer': 'https://m.ximalaya.com/xmds-node-spa/apps/speed-growth-open-components/bubble',
    }

  data = {"listenTime": "41246", "signature": "2b1cc9ee020db596d28831cff8874d9c",
            "currentTimeMillis": "1596695606145", "uid": uid, "expire": False}
  try:
     response = requests.post('https://m.ximalaya.com/speed/web-earn/listen/bubbles',
                             headers=headers, cookies=cookies, data=json.dumps(data))
     result = response.json()
     print(result)
     for i in result["data"]["effectiveBubbles"]:
         print(i["id"])
         receive(cookies, i["id"])
         time.sleep(1)
         ad_score(cookies, 7, i["id"],uid)
     for i in result["data"]["expiredBubbles"]:
         ad_score(cookies, 6, i["id"],uid)
  except Exception as e:
        msg=str(e)
        print(msg)

def receive(cookies, taskId):
   print("\n【听书获取奖励】")
   headers = {
        'Host': 'm.ximalaya.com',
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'User-Agent': UserAgent,
        'Accept-Language': 'zh-cn',
        'Referer': 'https://m.ximalaya.com/xmds-node-spa/apps/speed-growth-open-components/bubble',
        'Accept-Encoding': 'gzip, deflate, br',
    }
   try:
      response = requests.get(
        f'https://m.ximalaya.com/speed/web-earn/listen/receive/{taskId}', headers=headers, cookies=cookies)
      print("receive: ", response.text)
   except Exception as e:
        msg=str(e)
        print(msg)

def card_draw2(cookies, drawRecordIdList):
  print("\n【每天30次抽奖获取卡】")
  headers = {
        'Host': 'm.ximalaya.com',
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'User-Agent': UserAgent,
        'Accept-Language': 'zh-cn',
        'Referer': 'https://m.ximalaya.com/xmds-node-spa/apps/speed-growth-activities/card-collection/home',
        'Accept-Encoding': 'gzip, deflate, br',
    }
  token = requests.get('https://m.ximalaya.com/speed/web-earn/card/token/1',
                         headers=headers, cookies=cookies,).json()["data"]["id"]

  data = {
        "drawType": 1,
        "drawRecordIdList": drawRecordIdList
    }
  headers = {
        'User-Agent': UserAgent,
        'Content-Type': 'application/json;charset=utf-8',
        'Host': 'm.ximalaya.com',
        'Origin': 'https://m.ximalaya.com',
        'Referer': 'https://m.ximalaya.com/xmds-node-spa/apps/speed-growth-activities/card-collection/home',
    }
  try:
    response = requests.post('https://m.ximalaya.com/speed/web-earn/card/draw',
                             headers=headers, cookies=cookies, data=json.dumps(data))
    print('抽奖',response.text)
  except Exception as e:
        msg=str(e)
        print(msg)



def get_card_coin(cookies, themeId, cardIdList,uid):
    print("\n【普通卡集卡齐全兑换】")
    headers = {
        'Host': 'm.ximalaya.com',
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'User-Agent': UserAgent,
        'Accept-Language': 'zh-cn',
        'Referer': 'https://m.ximalaya.com/xmds-node-spa/apps/speed-growth-activities/card-collection/home',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    token = requests.get('https://m.ximalaya.com/speed/web-earn/card/token/3',
                         headers=headers, cookies=cookies,).json()["data"]["id"]
    _datatime = datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y%m%d", )
    data = {
        "cardIdList": cardIdList,
        "themeId": themeId,
        "signData": rsa_encrypt(f"{_datatime}{token}{uid}", pubkey_str),
        "token": token
    }
    headers = {
        'User-Agent': UserAgent,
        'Content-Type': 'application/json;charset=utf-8',
        'Host': 'm.ximalaya.com',
        'Origin': 'https://m.ximalaya.com',
        'Referer': 'https://m.ximalaya.com/xmds-node-spa/apps/speed-growth-activities/card-collection/home',
    }
    try:
      response = requests.post('https://m.ximalaya.com/speed/web-earn/card/exchangeCoin',
                             headers=headers, cookies=cookies, data=json.dumps(data))
      print('集卡兑换金币',response.text)
    except Exception as e:
        msg=str(e)
        print(msg)


def exchangeCard(cookies, toCardAwardId, fromId):
    print("\n【万能卡兑换普通卡】")
    headers = {
        'User-Agent': UserAgent,
        'Content-Type': 'application/json;charset=utf-8',
        'Host': 'm.ximalaya.com',
        'Origin': 'https://m.ximalaya.com',
        'Referer': 'https://m.ximalaya.com/xmds-node-spa/apps/speed-growth-activities/card-collection/home',
    }
    fromRecordIdList=[]
    fromRecordIdList+=[fromId]
    print(fromRecordIdList)
    data = {
        "toCardAwardId": toCardAwardId,
        "fromRecordIdList":fromRecordIdList,
        "exchangeType": 1
    }
    print('兑换卡片toCardAwardId',toCardAwardId)

    try:
       response = requests.post('https://m.ximalaya.com/speed/web-earn/card/exchangeCard',
                             headers=headers, cookies=cookies, data=json.dumps(data))
       print('万能卡兑换',response.text)
    except Exception as e:
        msg=str(e)
        print(msg)

def fragmentExchange(cookies, toCardAwardId):
   print("\n【碎片】")
   headers = {
        'User-Agent': UserAgent,
        'Content-Type': 'application/json;charset=utf-8',
        'Host': 'm.ximalaya.com',
        'Origin': 'https://m.ximalaya.com',
        'Referer': 'https://m.ximalaya.com/xmds-node-spa/apps/speed-growth-activities/card-collection/home',
    }
   try:
      response = requests.get(
        'https://m.ximalaya.com/speed/web-earn/card/fragmentInfo', headers=headers, cookies=cookies)
      #print(response.text)
      obj=response.json()
      fraglist=obj['data']
      if len(fraglist)<2:
      	print('碎片没有一对，无法兑换')
      	return
      fromRecordIdList=[fraglist[0],fraglist[1]]
      print('碎片id:',fromRecordIdList)
      data = {
        "toCardAwardId": toCardAwardId,
        "fromRecordIdList":fromRecordIdList,
        "exchangeType": 2
      }
      print('碎片兑换卡片toCardAwardId',toCardAwardId)
   except Exception as e:
      msg=str(e)
      print(msg)
   try:
       response = requests.post('https://m.ximalaya.com/speed/web-earn/card/exchangeCard',
                             headers=headers, cookies=cookies, data=json.dumps(data))
       print('碎片兑换',response.text)
   except Exception as e:
        msg=str(e)
        print(msg)
def card(cookies,uid):
    print("\n【开始集卡】")
    headers = {
        'Host': 'm.ximalaya.com',
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'User-Agent': UserAgent,
        'Accept-Language': 'zh-cn',
        'Referer': 'https://m.ximalaya.com/xmds-node-spa/apps/speed-growth-activities/card-collection/home',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    try:
      response = requests.get(
        'https://m.ximalaya.com/speed/web-earn/card/userCardInfo', headers=headers, cookies=cookies)
      #print(response.text)
      userCardsList = response.json()["data"]["userCardsList"]
      drawRecordIdList = response.json()["data"]["drawRecordIdList"]
      if drawRecordIdList:
         drawRecordIdList=drawRecordIdList[0:1]
         print('抽奖卡:',drawRecordIdList)
         card_draw2(cookies,drawRecordIdList)

      allIds = set([i["id"] for i in userCardsList if i["id"] != 1])
      print('自己的非万能卡',allIds)
      delt = set(range(2, 19))-allIds
      print('自己没有获取的卡',delt)
      listdelt=sorted(list(delt))
      fragmentExchange(cookies,listdelt[0])
      OmnipotentCard = [i for i in userCardsList if i["id"] == 1]
      #print('自己万能卡',OmnipotentCard)
      if delt and OmnipotentCard:
         exchangeCard(cookies, choice(list(delt)),
                     OmnipotentCard[0]["recordId"])

      jixiangwu2 = [i for i in userCardsList if i["id"] in [2, 3]]
      shangsiji4 = [i for i in userCardsList if i["id"] in [4, 5, 6, 7]]
      shuiguolao5 = [i for i in userCardsList if i["id"] in [8, 9, 10, 11, 12]]
      minghuahui6 = [i for i in userCardsList if i["id"] in [13, 14, 15, 16, 17, 18]]
      sidamingzhu4 = [i for i in userCardsList if i["id"] in [19, 20, 21, 22]]
      dongwuwenhua5 = [i for i in userCardsList if i["id"] in [23,24, 25, 26, 27]]
      jiajie5 = [i for i in userCardsList if i["id"] in [28,29, 30, 31, 32]]
      dibiao5 = [i for i in userCardsList if i["id"] in [33,34, 35, 36, 37]]
      _map = {
        2: [2, 3],
        3: [4, 5, 6, 7],
        4: [8, 9, 10, 11, 12],
        5: [13, 14, 15, 16, 17, 18],
        6: [19, 20, 21, 22],
        7: [23, 24, 25, 26, 27],
        8: [28, 29, 30, 31, 32],
        9: [33, 34, 35, 36, 37],
        }
      for i in [jixiangwu2,shangsiji4,shuiguolao5,minghuahui6,sidamingzhu4,dongwuwenhua5,jiajie5,dibiao5]:
        if not i:
            continue
        card_theme = i
        themeId = card_theme[0]["themeId"]
        print(f""">>>>当前集卡所在类型{themeId} {_map[themeId]}""")
        recordIdList = []
        for _, v in groupby(card_theme, key=lambda x: x["id"]):
            recordIdList.append(list(v)[0])
        if len(recordIdList) == len(_map[themeId]):
            print("卡片凑齐满足兑换金币")
            cardIdList = [i["recordId"] for i in recordIdList]
            print('开始兑换金币:卡片类型'+str(themeId), cardIdList)
            get_card_coin(cookies, themeId, cardIdList,uid)
    except Exception as e:
          msg=str(e)
          print(msg)

def getOmnipotentCard(cookies,uid):
   print("\n 【获得万能卡信息】")
   headers = {
        'User-Agent': UserAgent,
        'Content-Type': 'application/json;charset=utf-8',
        'Host': 'm.ximalaya.com',
        'Origin': 'https://m.ximalaya.com',
        'Referer': 'https://m.ximalaya.com/xmds-node-spa/apps/speed-growth-activities/card-collection/home',
    }
   try:
     result = requests.get('https://m.ximalaya.com/speed/web-earn/card/omnipotentCardInfo',
                         headers=headers, cookies=cookies,).json()
     print(result)
     count=result["data"]["count"]
     if count == 5:
        print("万能卡获取今日已满")
        return
     token = requests.get('https://m.ximalaya.com/speed/web-earn/card/token/1',
                         headers=headers, cookies=cookies,).json()["data"]["id"]
     mins = int(time.time())
     date_stamp = (mins-57600) % 86400
     _datatime = datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y%m%d", )

     data = {
        "listenTime": mins-date_stamp,
        "signData": rsa_encrypt(f"{_datatime}{token}{uid}", pubkey_str),
        "token": token
     }

     response = requests.post('https://m.ximalaya.com/speed/web-earn/card/getOmnipotentCard',
                             headers=headers, cookies=cookies, data=json.dumps(data))
     print(response.text)
   except Exception as e:
        msg=str(e)
        print(msg)



def reportTime(cookies,uid):
    print("提交服务器本地时长\n")
    headers = {
        'User-Agent': UserAgent,
        'Content-Type': 'application/json;charset=utf-8',
        'Host': 'm.ximalaya.com',
        'Origin': 'https://m.ximalaya.com',
        'Referer': 'https://m.ximalaya.com/xmds-node-spa/apps/speed-growth-activities/card-collection/home',
    }
    mins = int(time.time())
    date_stamp = (mins-57600) % 86400
    _datatime = datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y%m%d", )
    listenTime = mins-date_stamp
    data = {"listenTime": listenTime,
            "signData": rsa_encrypt(f"{_datatime}{listenTime}{uid}", pubkey_str), }
    try:
       response = requests.post('https://m.ximalaya.com/speed/web-earn/card/reportTime',
                             headers=headers, cookies=cookies, data=json.dumps(data))
       print(response.text)
    except Exception as e:
        msg=str(e)
        print(msg)





def account(cookies,j):
  print("\n【打印账号收益】")
  headers = {
        'Host': 'm.ximalaya.com',
        'Content-Type': 'application/json;charset=utf-8',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': UserAgent,
        'Referer': 'https://m.ximalaya.com/speed/web-earn/wallet',
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'gzip, deflate, br',
    }
  try:
    response = requests.get(
        'https://m.ximalaya.com/speed/web-earn/account/coin', headers=headers, cookies=cookies)
    result = response.json()
    print(result)
    global iosrule
    dv=cookies['device_model']
    iosrule+=f"""【{j}】{result["total"]/10000}|{result["todayTotal"]/10000}|{result["historyTotal"]/10000}|{dv}"""+'\n'

  except Exception as e:
        msg=str(e)
        print(msg)

def saveListenTime(cookies,uid):
    print("\n【保存本地收听时长】")
    headers = {
        'User-Agent': UserAgent,
        'Host': 'mobile.ximalaya.com',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    mins = int(time.time())
    date_stamp = (mins-57600) % 86400
    _datatime = datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y%m%d", )
    listentime = date_stamp
    print(listentime//60)
    currentTimeMillis = int(time.time()*1000)-2
    sign = hashlib.md5(
        f'currenttimemillis={currentTimeMillis}&listentime={listentime}&uid={uid}&23627d1451047b8d257a96af5db359538f081d651df75b4aa169508547208159'.encode()).hexdigest()
    data = {
        'activtyId': 'listenAward',
        'currentTimeMillis': currentTimeMillis,
        'listenTime': str(listentime),
        'nativeListenTime': str(listentime),
        'signature': sign,
        'uid': uid
    }

    try:
        response = requests.post('http://mobile.ximalaya.com/pizza-category/ball/saveListenTime',
                             headers=headers, cookies=cookies, data=data)
        print(response.text)
    except Exception as e:
        msg=str(e)
        print(msg)

def dati_taskrecord(cookies):
    print("\n【领取答题任务各种奖励】")
    headers = {
        'User-Agent': UserAgent,

    }
    try:
       response = requests.get('https://m.ximalaya.com/speed/web-earn/task/record?taskLabels=4&showReceived=true',
                            headers=headers, cookies=cookies)
       result = response.json()
    #print(response.text)
       if len(result['taskList'])>0:
           for ls in result['taskList']:
                if ls['taskRecordId']>0:
                   response = requests.post('https://m.ximalaya.com/speed/web-earn/task/receive/'+str(ls['taskRecordId']),
                           headers=headers, cookies=cookies)
                   print(response.text)
    except Exception as e:
        msg=str(e)
        print(msg)
def homehourred(cookies,uid):
  print("\n【首页红包信息】")
  headers = {
        'User-Agent': UserAgent,}
  currentTimeMillis = int(time.time()*1000)-2
  response = requests.get(f'http://mobile.ximalaya.com/pizza-category/activity/getAward?activtyId=indexSegAward&ballKey={uid}&currentTimeMillis={currentTimeMillis}&sawVideoSignature={currentTimeMillis}+{uid}&version=2',
                            headers=headers, cookies=cookies)

  try:
    print(response.text)
    result = response.json()
    for num in range(1,3):
       xg=time.strftime("%Y%m%d", time.localtime())
       response = requests.get(f'http://mobile.ximalaya.com/pizza-category/activity/awardMultiple?activtyId=indexSegAward&awardReceiveId={uid}-{xg}-6-{num}',
                            headers=headers, cookies=cookies)
       result = response.json()
       print(response.text)
       time.sleep(1)
  except Exception as e:
        msg=str(e)
        print(msg)

def pushmsg():
  if xmly_bark_cookie.strip():
    print("\n【BARK消息】")
    purl = f'https://api.day.app/{xmly_bark_cookie}/xmly/{iosrule}'
    response = requests.post(purl)
    #print(response.text)
  if djj_tele_cookie.strip():
     print("\n【Telegram消息】")
     id=djj_tele_cookie[djj_tele_cookie.find('@')+1:len(djj_tele_cookie)]
     botid=djj_tele_cookie[0:djj_tele_cookie.find('@')]

     purl=f'''https://api.telegram.org/bot{botid}/sendMessage?chat_id={id}&text=XMLY\n{iosrule}'''

     response = requests.get(purl,timeout=5)
         

def checkin(cookies,uid):
    print("\n【连续签到】")
    headers = {
        'Host': 'm.ximalaya.com',
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'User-Agent': UserAgent,
        'Accept-Language': 'zh-cn',
        'Referer': 'https://m.ximalaya.com/growth-ssr-speed-welfare-center/page/welfare',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    params = (
        ('time', f"""{int(time.time()*1000)}"""),
    )
    try:
       response = requests.get('https://m.ximalaya.com/speed/task-center/check-in/record',
                                headers=headers, params=params, cookies=cookies)
       result = json.loads(response.text)
       print(result)
       print(f"""连续签到{result["continuousDays"]}/{result["historyDays"]}天""")
       print(result["isTickedToday"])
       if not result["isTickedToday"]:
           print("!!!开始签到")
           _datatime = datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y%m%d", )
           headers = {
            'User-Agent': UserAgent,
            'Content-Type': 'application/json;charset=utf-8',
            'Host': 'm.ximalaya.com',
            'Origin': 'https://m.ximalaya.com',
            'Referer': 'https://m.ximalaya.com/growth-ssr-speed-welfare-center/page/welfare',
        }
           data = {
            "checkData": rsa_encrypt(f"date={_datatime}&uid={uid}", pubkey_str),
            "makeUp": False
        }

           response = requests.post('https://m.ximalaya.com/speed/task-center/check-in/check',
                                 headers=headers, cookies=cookies, data=json.dumps(data))
           print(response.text)
    except Exception as e:
        msg=str(e)
        print(msg)






def m():
    currentTimeMillis = int(time.time()*1000)-2
    sign = hashlib.md5(('2'+'a45421662ad74842a3f3118aa474ac6c').encode()).hexdigest()
    print(sign)
##################################################################
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



def main(cookies,uid):
    print("#"*20)
    print("\n")
    homehourred(cookies,uid)
    listenData(cookies,uid)
    saveListenTime(cookies,uid)
    reportTime(cookies,uid)
    bubble(cookies,uid)
    card(cookies,uid)
    getOmnipotentCard(cookies,uid)
    #dati_taskrecord(cookies)
    ans_main(cookies)
    lottery_info(cookies,uid)
    checkin(cookies,uid)
    print("\n")
@clock
def start():
  check()
  j=0
  for i in cookiesList:
    j+=1
    #if j!=1:
       #continue
    print(">>>>>>>>>【账号"+str(j)+"开始】")
    cookies = str2dict(i)
    uid = cookies["1&_token"].split("&")[0]
    uuid = cookies["XUM"]
    main(cookies,uid)
    account(cookies,j)
  pushmsg()




if __name__ == '__main__':
       start()
