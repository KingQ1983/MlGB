#2021.4.1update

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


btlist1=[]
btlist2=[]
btlist3=[]
btlist4=[]
treeId=''
dreamtown_house=0
dreamtown_car=0


hd1={"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Content-Type":"application/json","Connection": "close","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 WUBA/10.12.5","X-Requested-With": "XMLHttpRequest",}
hd2={"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Content-Type":"application/json","Connection": "close","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 WUBA/10.12.5","X-Requested-With": "XMLHttpRequest",}

hd3={"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Content-Type":"application/x-www-form-urlencoded","Connection": "close","User-Agent":"58tongcheng/10.12.5 (iPhone; iOS 14.4.1; Scale/2.00)"}


nockhd={"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-Hans-CN;q=1, en-US;q=0.9, zh-Hant-CN;q=0.8","Content-Type": "application/json","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 WUBA/10.12.5",}


lookhd={"58idfa": "B38160D2-DC94-4414-905B-D15F395FD787","58mac": "02:00:00:00:00:00","58openudid": "DD2629B4-5657-4186-B020-B32B0AC2F6FE","58ua": "58app","Accept": "*/*","Accept-Encoding": "deflate, gzip","Accept-Language": "zh-Hans-CN;q=1, en-US;q=0.9, zh-Hant-CN;q=0.8","Connection": "keep-alive","Host": "app.58.com","User-Agent": "58tongcheng/10.12.5 (iPhone; iOS 14.4.1; Scale/2.00)","adnop": "46001","apn": "WWAN","areaid": "","bangbangid": "152168948486","brand": "Apple","bundle": "com.taofang.iphone","channelid": "80000","charset": "UTF-8","cid": "3","coordinateType": "10","coordinatesystem": "GCJ-02","currentcid": "3","deny": "2.000000","dirname": "gz","f": "58","firstopentime": "1617072776087","id58": "103492657670395","idfv": "6259C25D-61ED-4A43-9A0B-0B3108352D32","imei": "0f607264fc6318a92b9e13c65db7cd3c","netType": "3g","nop": "46001","openudid": "6a6229c4f9ad8d0ffb976189a5d65feab14ef46d","os": "ios","osv": "14.4.1","owner": "google","platform": "iphone","ppu": "UID=152168948486&UN=%E4%BA%BF%E4%B8%87%E4%B8%8D%E6%98%AF%E6%A2%A6ABC&TT=343fcdd75d810471689b37c98a1d8230&PBODY=VM847Ec2G_oaxg_LsWaMaExpQVgIdYVQWYoIkrIgG8DHjuMBoNKhnEJOLNn2iwogfmTS7zwM3zfvZesXV4oTMHCnCcrHFcMY4GDnDBuQi-vKJtFYpfmwDCOB-bCHd_cIrkyorlwAFUMsfUb0IxjdXLY3gWwxi1Nk2NIuGliZcOI&VER=1","productorid": "3","push": "0","r": "1792_828","scale": "1","sh": "848","sid": "0","sw": "414","townlocalid": "","uid": "152168948486","uniqueid": "B38160D2-DC94-4414-905B-D15F395FD787","uploadtime": "20210331093638","uuid": "4F4A0BC5-9134-40E7-A44C-C94CCE009A76","version": "10.12.5","vlat": "23.120049","vlocalid": "","vlon": "113.30765","wbuversion": "10.12.5","webua": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 WUBA/10.12.5","xxaqrid": "eaad036ea7","xxzl-cid": "8dfe55e157944307b332ef7806793476","xxzl_cid": "8dfe55e157944307b332ef7806793476","xxzl_deviceid": "jMGPHnBPvx3LSO+FUaxKAtpbAq7BG6SO5gvyh6yqRMVmNqtxxDWhEtVAHV41k67G","xxzl_smartid": "6693cacc83d53bcd6ca2356e427266bd","xxzlcid": "8dfe55e157944307b332ef7806793476","xxzlsid": "6KIVjz-SgH-LRP-Qsm-1hSLbqyuA",}

videobody='{"message":"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","cypher": 2}'


mission_body='{"message":"2wppMZ6ijrGp8GLM20D8nDgFz42r2vATlHEpAU7c90GhJuBA15MTIA3s4YomPXVerLS4V75mj5uyGkyjgSA6rRy\/a2MOJnGMD3QB8ivNeLkRqCrWNk3scw2GWeu\/Hhd3M8QZPXCq+lIhnC4LS+6rTbLnqTcsPAfL4qdO0+60WNT7pgG59ZJBI0DW9ml9zyOGjN1aNJ0MF\/7byTC1xnSz0lV65N1tEEVBEzCenP\/U9UaDn69wjD8Ijg2GpZeEbf2zE5w8BVQRzoAmWhrRlrmVrsD3WU2HMOFK3MEk+DD0ma4gZ\/3LFhVzgP3\/vAX2SCxzrLlEPdxN3rIpDkZ8DjLG8tHKbcaPviEfd4aXGgam02pu83NhkwSn+6s12vmoSYhWUBTSCz0hT1\/I4c\/Xol73dJke7w4kpS4Yn3y9LsXt0soZ7TChqjyqncjfcFWLPdb\/zszmt\/vJMZshAC8JBK+Yu7HiwNEbdwrINzEydGbjJ02qL98umoSiddGF+A7RrJKthgkVDmiKuYuS8gOzfsyiQdXWMqQaSH94QXKJ6OLopOPDTVKs\/rdjlf1KtAZdTmcmuv586BqrfJsEbLx3gNH5F5epviPcC1B6N6VwK4Vc\/uecDxTDbCUFihrnasFcw4Z7u2vC\/wpcURd6o3tVPcH+\/Gks3eilG2C+ViyN9ocZvV3nHqk5HjA+wgJn4NJHmbKTD\/avANIkr5HW53aNgHGUbwTGa1m\/LGsNKbgPoxlpkHcLJpILwzc\/oSa9RFBg0mXk4vU3mytLp9noMzl3xe8+gq3UrDHYqdqA5i\/0eVaKQy6ZwbWtSAfqltnqjnxLVRum8PiYUpGhpS5pXcAQ5eZ41zyshMlWvZpyMOKrnYQkxjpEYWYg1RE3+F1Wi6guaizUKu+BJcMi6d4uNeAu0dd4qHJKFEcmC8UAcq3ydt1dAgljYT6nK3TEadsPwdxlTMm7cu+cWv4Q1U1FCldS426+1zllANyzVHmXGsFArQMcAPLfrHtVA6DrJMyy98joocu71xInIjpyh\/BytinoypUZkEZY6aGzSvH3J8lRbTKmsoeZf69Sa1K5zN64kf6Pu9hSvjXSpUJh3wp5P+Vw26+PxJXHzXLFP9xpKo84qeglmNxL3PlnowWsWK55hJJoo8+wM4DFF5jTs7pL3HnB\/SjR89D8tkY47KpOCWeScLZNRknCSYKzWHCMqIIsnlvEZE8koQm8XmGp0G6ebHoXELaYajjBgnGBicvR05x9RJMME+tngAZn8pQ6ZUZ9lOBZCc+9uOCVXPwlkgaVK\/\/X66e8K2Rx2KMPUo4IbJhSmvW9bJH3d3KsgRREN4kx3REfIXreVviUV3ANHbuiIeOXeoQYX2qIXbpucNUwhJuIw9NWhWROzYoHtxBfCHdj+eEO6\/nCA730olvRsE1I7dysA6DlNj0fwCQ1nDmlBYWxr2uqR\/suXK49XneQ+oSfolI5Q+JrV487n2edGfF3be8QbGCVborvLMr44BnAXm8M1nCvIe\/R9iDCg3WL5sfKj1gXJAjKPPbl3Q5mSRfeWPyeSU17T3mK\/kEVlopFkDou5muCDbz5+WACpPL++nasLhW5vZSfjHe94s4s4\/JrPRAJNDwYtiDe4O1PFqkWD3EazWN5fqcRLbrm7WE1J88fxDBbBeYOfXObtlbUOr7w5WCLiSkJfa8NnAGGjGvOUv7KedFk7BtoIMtYNPPUsvmGu\/QlZx4kRQWV+5kUDyHUyDgheITQ6hRAuQxuEAPmdY3Y9QUAkXVZC1HYJfAREviUY27FCMsa0tXhtVukkJ2g6PyK0Tsb0GbFNlByzCqgjBFQO1Tkc+gAxE2jYZ3VgJnD0AeclHPuHz25hPDtR3BZCvX\/dUrVHlEsgLEUCXa2rcFJ1mkGdV3nt\/nWfGq9qS3aH0AQjJV8rSlh4pQipWuSU\/aEBBhKF\/S7x+P9LIUXWJ7SNUsA4ExLbhTNURsY7\/g0ywdh9IzlzJDrG+rzb+0Ywdxw8kY62wxrBw61SfY3vHC5Nw4Ad0X2Gb6wZyaHH6BAEpRX8s6HNeio2F1RS4Um8uMUHun4Xl226OO\/AuJMH7HjOxVnLOgrInPzhyrqOdAzJQu6LuMOLt4sK8iLznyxc1mSZH2ZGH3yftC\/9Z2CvhUVNlR6DoA0WiUd4W42xQGhniY9JNQX9yywkfJ62TFZ\/ObaXTGLqCbVMtyCXBpMnPmUUrD3L\/jVozWNL5kWadZg9PWrpfyqMXt\/A+PJgO0G\/Bnkf\/zbptu83FLx4A5WvMc2TTA0GQdpZDJeELRKPoeb8KqFfGsoYmxvOQ4FjmzCwbyixCUvy6B2BUwA6KhxewM4R6cwy49Y\/VTDN3+XU+9xFhnE9UDbYhz4CRgcc7dqnPM96vMY5tL7V8AIpj11kWeweX77\/kU0+B7u4EymwIsM0Ua0iaJQ5eeFyqNp9SCPdVLi8RymEh0N8tqixSxLCTrTFFX9Uov8K3\/CXLlcrCTeexatPZNN1rrPVoWAHQ8ZX7oO7iTsYIqm8lN8JTdbtTmCLyccjfdJIPB6y4cgdOVN8kq3V87vvmZXsRUqhmblLykrL0B\/MpxohWX0N\/AiNseyM8OyTQbBtSnUFIsjJcwg\/lMNX091KfOxzfEoQhcQp1vMTviWoH9TNFsVtiLOJoZJfScOqzeFp9PdyT9Tw8SpechMEh4522yvwzwVmyXNrRli3Lude9UwYYi\/H0QVyTns9YTw09MpuvURQfsryB0np8u62RyI3koDKOKMSIuUfq8NJjPyY3UnvPQtqsrtzdstdsGftCBlAbxt6KP5ZK7ROZQnGjopnkAasD9DftVXoKBIiP6teIV\/znQc9lIyPaGhtZB3ErnIxiVqvffF07O+Rqvtbq5FbTAm1r0DIkvjeT1zz8DriL9rb1Ta6aJFSDoAxVxRUhbvYXSwFPbA97YNVhWN49xTVjen9VBee6ZQISvn9Q1LubWPoSJ44M2KQB25QUwcUtArdjiyVMDr+r2a00OchAMVYlZCzTDxFuATbcY65XwBwzcHQqDMKrziwXv2BXCXfPPeLBkbt9k7TrbdmPLTxspUg1Zzf3X0dt6WtpVG7PJWuhtzLVlkNE8nDMsRjAPZCvQScyPNuZ3lKYrUcNGla9FCU7eDioRi\/LlaGHRcT4VOtKdwGSdfB5dMSa+2nScdOpYllQa3z8Ym+sL1bniYuqmpDppgbUMuhVH+EEVM67J0NbSQuOl0+sd9UijBCeT0en0gwTw1zdasd9KG7NOXlrO9JFKzdSSFcQX8uQPT5N8Ca2an6SK9kSxdvtGUoMYv1ubq7J0ATesYooRFbhktoUddiZjrpkociZfP3N2REhevPe1v6yhStnSL7ZAu60h3cL7PGf\/7pF8dP2gZqCcKeJfj\/09r0Kwpa3BrRJceQ36Z2X\/xySsn67p7KFj52Rqhtj0bbOUcRMqvVzTAiJm3qMgJu5H8u3aErmhaXIth4fPSnHhIG\/T7ibRDM2XTwYEf5ijLoYff7cx6aKzuhZKqjVaTy\/RN+aALUrgfHHjuY8H0mgf\/BIuwhhShItWq0EaK6iUZQBVvOvNC9F8qsYRu67rPsfBZfitO\/IRVIZmZ3ZXAYvsrd9VoVmrU87lTxmLWn6z\/suynbjSrN2kvw61LZAxClGx9Q3g6VsbDZG3T8OOaoykDyODgzs\/GrEM1HK08MWrzHuQ2UzoeqbJ4cVohwQWZtZFQGJ7TUDxFAItCYlX58RXTEd78d\/iMhDFs9GjRKF19p\/dXnUQX5O61SwOQVTcszV+IDhEcx6mAWTEk8OR5QL1kHuMA2dgxe9YVYvrllNQv2dd3Z6w2ZGpih7h1ziDyjLFod5IACq7d90BQED4E+vSXmS2sMjXGubAFaUhC+tMBYAQM7t+opab\/8ia8QYc8\/07A2VuHUnGjP5N9d9gr7r5dC3WLrgwUwd5Ohr33vbaR9+t1IqUAPvWpE\/ac7grFeMDi7EwHtDRe4rMIcwoydCqOQHQzCH5tzouoHY7JDkcQk3C1z3r1LLrLxuNYOKwO6Ru\/ukbTJKdxKI6bGdIPgOB61q871ITUYOwl+HA==","cypher":2}'





def TC58():
  
  try:
   
   
   
   dreamtown_monopoly()
   mineral_attendance()

   mission_jianglijin()
   activityTreeMoney()
   dreamtown()
   mineral()
   print('通知========🔔🔔')
   activityTreeMoney_getConfig(1)
   dreamtown_maininfo(1)
   mineral_main(1)
  except Exception as e:
      print(str(e))


def activityTreeMoney():
  try:
     activityTreeMoney_getActivityTaskList()
     activityTreeMoney_getConfig()
     activityTreeMoney_watering()
     activityTreeMoney_receiveDayWelfare()
     lotteryMachine_drawLuck()
  except Exception as e:
      print(str(e))
      
def dreamtown():
  try:
     dreamtown_maininfo()
     dreamtown_buy()
  except Exception as e:
      print(str(e))

def mineral():
  try:
     mineral_signInfo()
     mineral_main()
     mineral_strangerInfo()
  except Exception as e:
      print(str(e))
      
      
def mineral_attendance():
   print('\n 【mineral_attendance打卡】')
   try:
          response = requests.get('https://magicisland.58.com/web/attendance/detail/info?productorid=3',headers=hd3,timeout=10)
          userRes=json.loads(response.text)
          number=userRes['result']['infoList'][0]['number']
          if userRes['result']['infoList'][0]['userState']==0:
             attendance_signIn(number)
          else:
             print(number+'单日打卡已报名,打卡时间5-8点')
             msg=number+'单日打卡已报名|'
             loger(msg)
          
          if not userRes['result']['attendSituationList'][0]:
             attendance_attend(number)
          else:
            msg='已打卡(5-8点)|'
            loger(msg)
   except Exception as e:
      print(str(e))
      

def attendance_signIn(number):
   print('\n 【signIn报名】')
   try:
       print(number)
       hd3['Referer']='https://magicisland.58.com/web/v/client'
       response = requests.post('https://magicisland.58.com/web/attendance/signIn',headers=hd3,data='number='+number+'&category=oneDay&productorid=3',timeout=10)
       userRes=json.loads(response.text)
       print(userRes['message'])
   except Exception as e:
      print(str(e))
      
def attendance_attend(number):
   print('\n 【attend打卡】')
   try:
       hd3['Referer']='https://magicisland.58.com/web/v/client'
       response = requests.post('https://magicisland.58.com/web/attendance/attend',headers=hd3,data='productorid=3&number='+number,timeout=10)
       userRes=json.loads(response.text)
       print(userRes['message'])
   except Exception as e:
      print(str(e))
      
      

def dreamtown_monopoly():
   print('\n 【dreamtown_monopoly大富翁】')
   try:
          response = requests.post('https://dreamtown.58.com/web/dreamtown/monopoly/rolldice',headers=hd3,timeout=10)
          userRes=json.loads(response.text)
          print(userRes['message'])
          
   except Exception as e:
      print(str(e))
      
      
      
def mission_jianglijin():
   print('\n 【mission_jianglijin奖励金】')
   try:
          response = requests.get('https://wxcvip.58.com/api/mission/index?bizId=INCENTIVE_VIDEO',headers=hd3,timeout=10)
          userRes=json.loads(response.text)
          #print(userRes)
          msg1=userRes['data']['amount']
          #签到
          if not userRes['data']['tractSignProgress']['todaySignStatus']:
              mission_sign()
          #看视频
          
          for v in userRes['data']['inventiveVideo']:
             if not v['taskState']==1:
                _reward_video(mission_body)
                time.sleep(5)
          response = requests.get('https://wxcvip.58.com/api/mission/index?bizId=INCENTIVE_VIDEO',headers=hd3,timeout=10)
          userRes=json.loads(response.text)
          msg2=f'''奖励金{userRes['data']['amount']}元,本次增加{userRes['data']['amount']-msg1}元'''
          print(msg2)
   except Exception as e:
      print(str(e))
def mission_sign():
   print('\n 【mission_sign】')
   try:
          response = requests.get('https://wxcvip.58.com/api/mission/user/sign',headers=hd3,timeout=10)
          userRes=json.loads(response.text)
          print(userRes)            
   except Exception as e:
      print(str(e))
      
      
      
      
      
      
def mineral_strangerInfo():
   print('\n 【mineral_strangerInfo】')
   try:
       
          response = requests.get('https://magicisland.58.com/web/mining/strangerInfo',headers=hd3,timeout=10)
          userRes=json.loads(response.text)
          #print(userRes)
          for id in userRes['result']['strangerList']:
             
             if id['status']==0:
                print(id['nickname'])
                response = requests.get('https://magicisland.58.com/web/mining/stealStranger?id='+id['id'],headers=hd3,timeout=10)
                userRes=json.loads(response.text)
                print(userRes['message'])
                time.sleep(1)
          
                
   except Exception as e:
      print(str(e))
      
      

def mineral_signInfo():
   print('\n 【mineral_signInfo】')
   try:
        response = requests.get('https://magicisland.58.com/web/sign/signInfo',headers=hd3,timeout=10)
        userRes=json.loads(response.text)
        #print(userRes)
        
        for sg in userRes['result']['cardInfo']:
          print(f'''{sg['number']}-{'已完成' if sg['cardStatus']==2 else '未完成'}''')
        msg=f'''我的矿石{userRes['result']['minerOre']}mg(约{userRes['result']['minerOreValue']}元),本轮已连续签到{userRes['result']['signCount']}天'''
        print(msg)
   except Exception as e:
      print(str(e))

def mineral_sign():
   print('\n 【mineral_sign】')
   try:
         # if userRes['result']['todayStatus']==0:
          response = requests.get('https://magicisland.58.com/web/sign/signInV2?sessionId=&successToken=&scene=null',headers=hd3,timeout=10)
          userRes=json.loads(response.text)
          print(userRes)
       
   except Exception as e:
      print(str(e))
def mineral_main(push=0):
   print('\n 【mineral_main】')
   try:
        response = requests.get('https://magicisland.58.com/web/mineral/main?openSettings=1',headers=hd3,timeout=10)
        userRes=json.loads(response.text)
        #print(userRes)
        game=userRes['result']['games']
        gameProcess=f'''游戏进度{game['gameProcess']['joinedNum']}-{game['gameProcess']['gameNum']}'''
        print(gameProcess)
        
        userInfo=f'''{userRes['result']['userInfo']['nickName']}|{userRes['result']['userInfo']['minerOre']}({userRes['result']['userInfo']['minerOreValue']})|'''
        #print(userInfo)
        if push==1:
           loger(userInfo)
           return
        task=userRes['result']['tasks']
        for key in task:
          if task[key]:
             print(f'''任务【{task[key]['name']}】-进度{task[key]['data']}-数量{task[key]['taskCount']}-{'已完成✓👌🏻' if task[key]['state']==1 else '未完成❌'}''')
        if task['video']['state']==0:
           mineral_reward_video()
        if task['sign']['state']==0:
           mineral_sign()
        if task['usedCar']['state']==0:
           mineral_ershouche_look()
   except Exception as e:
      print(str(e))
def mineral_reward_video():
   print('\n 【mineral_reward_video】')
   try:
        
        response = requests.get('https://magicisland.58.com/web/video/reward/ore',headers=hd3,timeout=10)
        userRes=json.loads(response.text)
        print(userRes)
        time.sleep(5)
        _reward_video(videobody)
   except Exception as e:
      print(str(e))
      
def _reward_video(body):
   print('\n 【_reward_video】')
   try:
        #https://api-access.pangolin-sdk-toutiao.com/api/ad/union/sdk/reward_video/reward/
        response = requests.post('https://api-access.pangolin-sdk-toutiao.com/api/ad/union/sdk/reward_video/reward/',headers=nockhd,data=body,timeout=10)
        userRes=json.loads(response.text)
        print(userRes)
        
        
   except Exception as e:
      print(str(e))
      
      
def mineral_ershouche_look():
   print('\n 【mineral_ershouche_look】')
   try:
        response = requests.get('https://wireless.58.com/api/list/ershouche/?data_source=shenqikuangche&ct=filter&params=%7B%22data_source%22%3A%22shenqikuangche%22%7D&curVer=10.12.5&appId=3&reentries=%7B%22reentry_id%22%3A%22519337e7-edec-4de7-aa2a-ca47c9d5aa8a%22%2C%22feed_page%22%3A%221%22%2C%22hasnext%22%3Atrue%2C%22feed_last_count%22%3A35%7D&os=ios&action=getListInfo&isNeedAd=1&localname=gz&tabkey=allcity&page=2&pid=&needcpt=true',headers=hd3,timeout=10)
        userRes=json.loads(response.text)
        #print(userRes)
        infoIdlist=[]
        if userRes['status']==0:
          for i in range(len(userRes['result']['getListInfo']['infolist'])):
             infoIdlist.append(userRes['result']['getListInfo']['infolist'][i]['infoID'])
        
        print(infoIdlist)
        nm=0
        for infoId in infoIdlist:
           print(infoId)
           nm+=1
           if num==11:
              break
           infoId=str(infoId)
           response = requests.post('https://app.58.com/api/detail/car/ux/ifUX',headers=hd3,data='infoId='+infoId,timeout=10)
           userRes=json.loads(response.text)
           print(userRes)
           time.sleep(10)
           response = requests.get('https://app.58.com/api/detail/ershouche/'+infoId+'?format=json&typos=topinfo_l15&sidDict=%7B%22pgtid%22%3A%22%22%2C%22gtid%22%3A%22171038444211963652871649195%22%2C%22TID%22%3A%221faecfd8-1c68-43f8-b055-1daff437bb7d%22%7D&locationcity=3&platform=ios&params=%7B%22carinfolog%22%3A%7B%22userid%22%3A%2238017143199760%22%2C%22abtest348%22%3A%22WBERSHOUCHE_348_628172700%22%2C%22abtest389%22%3A%22WBERSHOUCHE_389_851313131%22%2C%22page_id%22%3A%22514%22%2C%22clickfrom%22%3A%22other%22%2C%22dianpu_type%22%3A%22feidianpu%22%2C%22abtest398%22%3A%22%22%2C%22business_type%22%3A%22z%22%2C%22pgtid%22%3A%22171038444211963652871649195%22%2C%22cateid%22%3A%2229%22%2C%22fxc_type%22%3A%22feifangxinche%22%2C%22discityname%22%3A%22%E5%B9%BF%E5%B7%9E%22%2C%22isCoupon%22%3Afalse%2C%22abtest373%22%3A%22WBERSHOUCHE_373_2129393547%22%2C%22discityid%22%3A%223%22%2C%22reco_type%22%3A%22feituijian%22%2C%22SFXSJ%22%3A%22%22%2C%22pos%22%3A%2214%22%2C%22abtest356%22%3A%22WBERSHOUCHE_356_1657472220%22%2C%22productid%22%3A%2210003%22%2C%22abtest395%22%3A%22WBERSHOUCHE_395_1806390698%22%2C%22TID%22%3A%221faecfd8-1c68-43f8-b055-1daff437bb7d%22%2C%22page%22%3A%221%22%2C%22infoid%22%3A%2245286883288225%22%2C%22data_source%22%3A%22shenqikuangche%22%2C%22is_def_list%22%3A%221%22%7D%7D&appId=3&version=10.12.5&localname=gz',headers=lookhd,timeout=10)
           userRes=json.loads(response.text)
           print(userRes['msg'])
   except Exception as e:
      print(str(e))
      
      
########################
def activityTreeMoney_getActivityTaskList():
   print('\n  【activityTreeMoney_getActivityTaskList】')
   try:
        
        response = requests.get('https://xzd.hswchangdu.com/activityTask/getActivityTaskList',headers=hd1,timeout=10)
        userRes=json.loads(response.text)
        #print(userRes)
        msg='【签到任务】\n'
        status='未开始'
        task=userRes['data']['signTask']
        for i in range(len(task)):
          if task[i]['status']==1:
             status='完成'
          elif task[i]['status']==0:
             status='未开始'
          msg+=f'''{i+1}.{task[i]['taskSubTitle']}-{task[i]['btnTxt']}-{task[i]['finishNum']}/{task[i]['needNum']}({task[i]['rewardList'][0]['rewardNum']}{task[i]['rewardList'][0]['rewardName']}-{status})\n'''
          if task[i]['taskSubTitle']=='今日' and status=='未开始':
            taskType=task[i]['taskType']
            taskConfigId=task[i]['taskConfigId']
            activityTreeMoney_receiveSign(taskType,taskConfigId)
        print(msg)
        msg='【领水滴任务】\n'
        task=userRes['data']['taskList']
        for i in range(len(task)):
           if task[i]['status']==2:
             status='完成'
           else:
             status='未完成'
           msg+=f'''{i+1}.{task[i]['taskTitle']}-{task[i]['btnTxt']}-{task[i]['finishNum']}/{task[i]['needNum']}({task[i]['rewardList'][0]['rewardNum']}{task[i]['rewardList'][0]['rewardName']}-{status})\n'''
           taskType=task[i]['taskType']
           taskConfigId=task[i]['taskConfigId']
           if status=='未完成':
             #if taskType==101:
               activityTreeMoney_finishTask(taskType,taskConfigId)
               time.sleep(1)
               activityTreeMoney_receiveTaskList(taskType,taskConfigId)
            # else:
               #activityTreeMoney_receiveTaskList(taskType,taskConfigId)
               #time.sleep(1)
        print(msg)
   except Exception as e:
      print(str(e))
def activityTreeMoney_getConfig(push=0):
   print('\n 【activityTreeMoney_getConfig】')
   global treeId
   try:
        response = requests.get('https://xzd.hswchangdu.com/activityTreeMoney/getConfig',headers=hd1,timeout=10)
        userRes=json.loads(response.text)
        
        #print(userRes)
        treeId=userRes['data']['treeConfig']['treeId']
        msg=f'''{userRes['data']['treeConfig']['treeTag']}-<可用水滴{userRes['data']['usableEnergy']}g💧|(水桶{userRes['data']['treeConfig']['bottleConfig']['bottleEnergy']}/{userRes['data']['treeConfig']['bottleConfig']['bottleVolume']})>(等级{userRes['data']['treeConfig']['treeLevelNo']}/{userRes['data']['treeConfig']['treeLevelMax']})[{userRes['data']['treeConfig']['wateringTips']},{userRes['data']['treeConfig']['upUpgradeRewardTips']},{userRes['data']['treeConfig']['rewardTips']}]|'''
        print(msg)
        if push==1:
           loger(msg)
           return
        taskType=userRes['data']['treeConfig']['upgradeReward']['taskType']
        taskConfigId=userRes['data']['treeConfig']['upgradeReward']['taskConfigId']
        if userRes['data']['treeConfig']['upgradeReward']['status']==1:
           activityTreeMoney_receiveUpgrade(taskType,taskConfigId)
        else:
          print('\n Not enough for Upgrade')
        
        if userRes['data']['treeConfig']['bottleConfig']['bottleEnergy']==20:
          activityTreeMoney_receiveBottle()
        if userRes['data']['treeConfig']['bottleConfig']['canQuicken']==1:
          activityTreeMoney_quickenBottle()
        
   except Exception as e:
      print(str(e))
      
      
def activityTreeMoney_watering():
   print('\n 【activityTreeMoney_watering】')
   try:
        response = requests.post('https://xzd.hswchangdu.com/activityTreeMoney/watering',headers=hd1,data=json.dumps({"treeId":treeId}),timeout=10)
        userRes=json.loads(response.text)
        
        print(userRes['desc'])
        
   except Exception as e:
      print(str(e))

def activityTreeMoney_receiveBottle():
   print('\n 【activityTreeMoney_receiveBottle】')
   try:
        response = requests.post('https://xzd.hswchangdu.com/activityTreeMoney/receiveBottle',headers=hd1,data=json.dumps({"treeId":treeId,"multiple":1}),timeout=10)
        userRes=json.loads(response.text)
        
        print(userRes['desc'])
        
   except Exception as e:
      print(str(e))
def activityTreeMoney_receiveSign(taskType,taskConfigId):
   print('\n 【activityTreeMoney_receiveSign】')
   try:
        response = requests.post('https://xzd.hswchangdu.com/activityTreeMoney/receiveSign',headers=hd1,data=json.dumps({"taskType":taskType,"taskConfigId":taskConfigId}),timeout=10)
        userRes=json.loads(response.text)
        
        print(userRes)
        
   except Exception as e:
      print(str(e))
      
      
def activityTreeMoney_receiveUpgrade(taskType,taskConfigId):
   print('\n 【activityTreeMoney_receiveUpgrade】')
   try:
        response = requests.post('https://xzd.hswchangdu.com/activityTreeMoney/receiveUpgrade',headers=hd1,data=json.dumps({"taskType":taskType,"taskConfigId":taskConfigId,"treeId":treeId}),timeout=10)
        userRes=json.loads(response.text)
        
        print(userRes)
        if userRes['code']==0:
          activityTreeMoney_watering()
          
        
   except Exception as e:
      print(str(e))
      
def activityTreeMoney_receiveTaskList(taskType,taskConfigId):
   print('\n 【activityTreeMoney_receiveTaskList】')
   try:
        response = requests.post('https://xzd.hswchangdu.com/activityTask/receiveTaskList',headers=hd1,data=json.dumps({"taskType":taskType,"taskConfigId":taskConfigId}),timeout=10)
        userRes=json.loads(response.text)
        
        print(userRes)
        
   except Exception as e:
      print(str(e))

def activityTreeMoney_finishTask(taskType,taskConfigId):
   print('\n 【activityTreeMoney_finishTask】')
   try:
        response = requests.post('https://xzd.hswchangdu.com/activityTask/finishTask',headers=hd1,data=json.dumps({"taskType":taskType,"taskConfigId":taskConfigId}),timeout=10)
        userRes=json.loads(response.text)
        
        print(userRes['desc'])
        
   except Exception as e:
      print(str(e))
def activityTreeMoney_quickenBottle():
   print('\n 【activityTreeMoney_quickenBottle】')
   try:
        response = requests.post('https://xzd.hswchangdu.com/activityTreeMoney/quickenBottle',headers=hd1,data=json.dumps({"treeId":treeId}),timeout=10)
        userRes=json.loads(response.text)
        
        print(userRes['desc'])
        
   except Exception as e:
      print(str(e))
      
      
def activityTreeMoney_receiveDayWelfare():
   print('\n 【activityTreeMoney_receiveDayWelfare】')
   try:
        response = requests.get('https://xzd.hswchangdu.com/activityTreeMoney/receiveDayWelfare',headers=hd1,timeout=10)
        userRes=json.loads(response.text)
        
        print(userRes['desc'])
        
   except Exception as e:
      print(str(e))
      
def lotteryMachine_drawLuck():
   print('\n 【lotteryMachine_drawLuck】')
   try:
        
        response = requests.post('https://xzd.hswchangdu.com/lotteryMachine/drawLuck',headers=hd3,timeout=10)
        userRes=json.loads(response.text)
        
        print(userRes)
        if userRes['code']==0:
           lotteryMachine_drawLuck()
           time.sleep(2)
   except Exception as e:
      print(str(e))
      
##############################
def dreamtown_maininfo(push=0):
   print('\n 【dreamtown_maininfo】')
   try:
        global dreamtown_house,dreamtown_car
        response = requests.get('https://dreamtown.58.com/web/dreamtown/maininfo',headers=hd3,timeout=10)
        userRes=json.loads(response.text)
        #print(userRes)
        userInfo=userRes['result']['userInfo']
        msg=f'''{userInfo['nickName']}_{userInfo['level']}|{userInfo['coin']}/{userInfo['offlineCoin']}|'''
        if push==1:
           loger(msg)
           return
        if int(userInfo['offlineCoin'])>10000:
           dreamtown_offlineicons()
        dreamtown_house=userRes['result']['levelInfo']['house']
        dreamtown_car=userRes['result']['levelInfo']['car']
        msg=f'''{dreamtown_house}|{dreamtown_car}'''
        print(msg)
        
        levelInfo=userRes['result']['locationInfo']
        #print(levelInfo)
        lev_list=[]
        for key in levelInfo:
          lev_list.append(key)
        print(lev_list)
        for i in range(0,11):
           if levelInfo[lev_list[i]]:
              print(lev_list[i]+'@'+str(levelInfo[lev_list[i]]['level']))
           if not levelInfo[lev_list[i]]:
               print(lev_list[i]+'@'+str(levelInfo[lev_list[i]]))
               continue
           for j in range(i+1,12):
             #if levelInfo[lev_list[j]]:
                 #print('......'+lev_list[j]+'#'+str(levelInfo[lev_list[j]]['level']))
             if not levelInfo[lev_list[j]]:
               # print('......'+lev_list[j]+'#'+str(levelInfo[lev_list[j]]))
                continue
             if levelInfo[lev_list[i]]['level']==levelInfo[lev_list[j]]['level']:
               print(lev_list[i]+'------>'+lev_list[j])
               dreamtown_compound(lev_list[j],lev_list[i])
               time.sleep(10)
               print('break====')
               break
             
   except Exception as e:
      print(str(e))
      
def dreamtown_buy():
   print('\n 【dreamtown_buy】')
   try:
        response = requests.get('https://dreamtown.58.com/web/dreamtown/maininfo',headers=hd3,timeout=10)
        userRes=json.loads(response.text)
        levelInfo=userRes['result']['locationInfo']
        lev_list=[]
        for key in levelInfo:
          lev_list.append(key)
        for i in range(len(lev_list)):
           if not levelInfo[lev_list[i]]:
             response = requests.post('https://dreamtown.58.com/web/dreamtown/buy',headers=hd3,data='type=quick&level=1',timeout=10)
             userRes=json.loads(response.text)
             print(userRes['message'])
             time.sleep(2)
   except Exception as e:
      print(str(e))

def dreamtown_compound(toId,fromId):
   print('\n 【dreamtown_compound】')
   try:
        dat=f'''toId={toId}&fromId={fromId}'''
        response = requests.post('https://dreamtown.58.com/web/dreamtown/compound',headers=hd3,data=dat,timeout=10)
        userRes=json.loads(response.text)
        print(userRes['message'])
        
   except Exception as e:
      print(str(e))

def dreamtown_offlineicons():
   print('\n 【dreamtown_offlineicons】')
   try:
        response = requests.get('https://dreamtown.58.com/web/dreamtown/icons',headers=hd3,timeout=10)
        userRes=json.loads(response.text)
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
    
    
    
    
@clock
def start():
   global result,hd1,hd2,hd3,hd,lookhd
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('tc58_tree_ck',btlist1)
   watch('tc58_lot_ck',btlist2)
   watch('tc58_dream_ck',btlist3)
   result=''
   for cc in range(len(btlist1)):
        result+='【'+str(cc+1)+'】'
        print('账号【'+str(cc+1)+'】开始运行==')
        hd1['Cookie']=btlist1[cc]
        hd2['Cookie']=btlist2[cc]
        hd3['Cookie']=btlist3[cc]
        lookhd['Cookie']=btlist3[cc]
        TC58()
        print('【'+str(cc+1)+'】-'+'🏆🏆🏆🏆运行完毕')
        result+='\n'
   #print('\n'+result)
   pushmsg('58',result)
    
    
   
     
if __name__ == '__main__':
       start()
    
