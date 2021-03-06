/*

TED演讲：你刷手机的时间其实可以让你很出色
文章来源：未知 文章作者：enread 发布时间：2020-05-14 13:36 字体： [大 中 小]　 进入论坛
(单词翻译:双击或拖选)
　　你有时常感觉无聊吗?你无聊的时候会做什么呢?刷微博?给别人的票圈点赞?有没有想过这些无聊的时间也可以产生新创意?今天就来看看，——如何利用无聊的时光迸发出灵感
　　——How boredom1 can lead to your most brilliant ideas

　　演讲原文节选
 
　　And anyway, don’t only boring people get bored? But then I started to wonder: What actually happens to us when we get bored? Or, more importantly: What happens to us if we never get bored? And what could happen if we got rid of this human emotion entirely2? I started talking to neuroscientists and cognitive3 psychologists, and what they told me was fascinating. It turns out that when you get bored, you ignite a network in your brain called the "default mode." So our body, it goes on autopilot while we’re folding the laundry or we’re walking to work, but actually that is when our brain gets really busy.
 
　　不是只有无聊的人才会无聊吗?但我接着开始想：当我们无聊时，会发生什么事?或更重要的：当我们从不无聊时，会发生什么事?如果我们完全摆脱这种人类情绪，又会发生什么事?我开始和神经科学家及认知心理学家谈这个话题，他们给我的回复很棒。结果是，当你无聊时，你会点燃你脑中的一个网路，叫做「预设模式」。所以当我们在折洗好的衣服、或是走路去上班时，我们的身体会自动驾驶，但其实那时我们的大脑才真的很忙。
 
　　So before challenge week, we were averaging two hours a day on our phones and 60 pickups, you know, like, a quick check, did I get a new email? Here’s what Tina, a student at Bard4 College, discovered about herself?(Audio)Tina: So far, I’ve been spending between 150 and 200 minutes on my phone per day, and I’ve been picking up my phone 70 to 100 times per day. And it’s really concerning, because that’s so much time that I could have spent doing something more productive, more creative, more towards myself, because when I’m on my phone, I’m not doing anything important.
 
　　在挑战周之前，我们平均是一天花2小时在手机上，拿起手机 60 次，比如拿起来看一下有没有新邮件。以下是巴德学院学生蒂娜对她自己的发现。(语音)蒂娜：目前，我每天会花 150 到 200 分钟在手机上，每天拿起手机 70 到 100 次。这很让人担忧，因为这么多时间我本来可以用来做比较有生产力、有创意、对我自己有助益的事，因为当我用手机时，我并没有在做重要的事。
 
　　If you have never known life without connectivity, you may never have experienced boredom. And there could be consequences. Researchers at USC have found they’re studying, teenagers who are on social media while they’re talking to their friends or they’re doing homework and two years down the road, they are less creative and imaginative about their own personal futures5 and about solving societal problems, like violence in their neighborhoods. And we really need this next generation to be able to focus on some big problems: climate change, economic disparity, massive cultural differences.
 
　　如果你从来就不知道没有连结的人生是怎样的，你可能从来没有体验过无聊。那是可能会有后果的。南加大的研究者发现——他们的研究对象是会在和朋友说话或做功课时，同时用社交媒体的青少年，两年时间过去后，他们对于自己的未来会比较没创意和想像力，对于解决社会问题，如街坊暴力，也比较没创意和想像力。我们真的需要下一个世代能够专注在大问题上：气候改变、经济失衡、大量文化差异。
 
　　So the next time you go to check your phone, remember that if you don’t decide how you’re going to use the technology, the platforms will decide for you. And ask yourself: What am I really looking for? Because if it’s to check email, that’s fine -- do it and be done. But if it’s to distract yourself from doing the hard work that comes with deeper thinking, take a break, stare out the window and know that by doing nothing, you are actually being your most productive and creative self. It might feel weird6 and uncomfortable at first, but boredom truly can lead to brilliance7.
 
　　切记，如果你没有决定你要如何用那科技，下次你再去看你的手机，平台就会为你做决定。记得自问：我到底在找什么?因为如果是去看邮件，没问题，去做，然后做完就好。但如果是让自己从需要深刻思考的努力工作中分心，休息一下，看看窗外，要知道，什么都不做时，其实是最有生产力及创意的时候。一开始可能感觉很怪且不舒服，但无聊真的可以带来出色。


京东赚赚
可以做随机互助
活动入口：京东赚赚小程序
长期活动，每日收益2毛左右，多号互助会较多

============Quantumultx===============
[task_local]
# 京东赚赚
10 0 * * * https://gitee.com/lxk0301/jd_scripts/raw/master/jd_jdzz.js, tag=京东赚赚, img-url=https://raw.githubusercontent.com/58xinian/icon/master/jdzz.png, enabled=true

================Loon==============
[Script]
cron "10 0 * * *" script-path=https://gitee.com/lxk0301/jd_scripts/raw/master/jd_jdzz.js,tag=京东赚赚

===============Surge=================
京东赚赚 = type=cron,cronexp="10 0 * * *",wake-system=1,timeout=3600,script-path=https://gitee.com/lxk0301/jd_scripts/raw/master/jd_jdzz.js

============小火箭=========
京东赚赚 = type=cron,script-path=https://gitee.com/lxk0301/jd_scripts/raw/master/jd_jdzz.js, cronexpr="10 0 * * *", timeout=3600, enable=true
 */
const $ = new Env('京东赚赚');
const notify = $.isNode() ? require('./sendNotify') : '';
//Node.js用户请在jdCookie.js处填写京东ck;
const jdCookieNode = $.isNode() ? require('./jdCookie.js') : '';
let helpAuthor=false; // 帮助作者
const randomCount = $.isNode() ? 20 : 5;
let jdNotify = true; // 是否关闭通知，false打开通知推送，true关闭通知推送
//IOS等用户直接用NobyDa的jd cookie
let cookiesArr = [], cookie = '', message;
if ($.isNode()) {
  Object.keys(jdCookieNode).forEach((item) => {
    cookiesArr.push(jdCookieNode[item])
  })
  if (process.env.JD_DEBUG && process.env.JD_DEBUG === 'false') console.log = () => {
  };
} else {
  let cookiesData = $.getdata('CookiesJD') || "[]";
  cookiesData = jsonParse(cookiesData);
  cookiesArr = cookiesData.map(item => item.cookie);
  cookiesArr.reverse();
  cookiesArr.push(...[$.getdata('CookieJD2'), $.getdata('CookieJD')]);
  cookiesArr.reverse();
  cookiesArr = cookiesArr.filter(item => item !== "" && item !== null && item !== undefined);
}
const JD_API_HOST = 'https://api.m.jd.com/client.action';
const inviteCodes = [``]
!(async () => {
  $.tuanList = []
  await requireConfig();
  if (helpAuthor) await getAuthorShareCode('https://gitee.com/shylocks/updateTeam/raw/main/jd_zz.json');
  if (helpAuthor) await getAuthorShareCode('https://gitee.com/lxk0301/updateTeam/raw/master/shareCodes/jd_zz.json');
  if (!cookiesArr[0]) {
    $.msg($.name, '【提示】请先获取京东账号一cookie\n直接使用NobyDa的京东签到获取', 'https://bean.m.jd.com/bean/signIndex.action', {"open-url": "https://bean.m.jd.com/bean/signIndex.action"});
    return;
  }
  for (let i = 0; i < cookiesArr.length; i++) {
    if (cookiesArr[i]) {
      cookie = cookiesArr[i];
      $.UserName = decodeURIComponent(cookie.match(/pt_pin=(.+?);/) && cookie.match(/pt_pin=(.+?);/)[1])
      $.index = i + 1;
      $.isLogin = true;
      $.nickName = '';
      message = '';
      await TotalBean();
      console.log(`\n******开始【京东账号${$.index}】${$.nickName || $.UserName}*********\n`);
      if (!$.isLogin) {
        $.msg($.name, `【提示】cookie已失效`, `京东账号${$.index} ${$.nickName || $.UserName}\n请重新登录获取\nhttps://bean.m.jd.com/bean/signIndex.action`, {"open-url": "https://bean.m.jd.com/bean/signIndex.action"});

        if ($.isNode()) {
          await notify.sendNotify(`${$.name}cookie已失效 - ${$.UserName}`, `京东账号${$.index} ${$.UserName}\n请重新登录获取cookie`);
        }
        continue
      }
      await shareCodesFormat()
      await jdWish()
    }
  }
  for (let i = 0; i < cookiesArr.length; i++) {
    $.canHelp = true
    if (cookiesArr[i]) {
      cookie = cookiesArr[i];
      for (let j = 0; j < $.tuanList.length; ++j) {
        await helpFriendTuan($.tuanList[j])
        if(!$.canHelp) break
      }
    }
  }
})()
  .catch((e) => {
    $.log('', `❌ ${$.name}, 失败! 原因: ${e}!`, '')
  })
  .finally(() => {
    $.done();
  })

async function jdWish() {
  $.bean = 0
  $.tuan = null
  $.hasOpen = false
  await getUserTuanInfo()
  if (!$.tuan) {
    await openTuan()
    if ($.hasOpen) await getUserTuanInfo()
  }
  if ($.tuan) $.tuanList.push($.tuan)

  await helpFriends()
  await getUserInfo()
  await getTaskList()
  $.nowBean = parseInt($.totalBeanNum)
  $.nowNum = parseInt($.totalNum)
  for (let i = 0; i < $.taskList.length; ++i) {
    let task = $.taskList[i]
    if (task['taskId'] === 1 && task['status'] !== 2) {
      console.log(`去做任务：${task.taskName}`)
      await doTask({"taskId": task['taskId'],"mpVersion":"3.4.0"})
    } else if (task['taskId'] !== 3 && task['status'] !== 2) {
      console.log(`去做任务：${task.taskName}`)
      if(task['itemId'])
        await doTask({"itemId":task['itemId'],"taskId":task['taskId'],"mpVersion":"3.4.0"})
      else
        await doTask({"taskId": task['taskId'],"mpVersion":"3.4.0"})
      await $.wait(3000)
    }
  }
  await getTaskList();
  await showMsg();
}

function showMsg() {
  return new Promise(async resolve => {
    message += `本次获得${parseInt($.totalBeanNum) - $.nowBean}京豆，${parseInt($.totalNum) - $.nowNum}金币\n`
    message += `累计获得${$.totalBeanNum}京豆，${$.totalNum}金币\n可兑换${$.totalNum / 10000}元无门槛红包`
    if (parseInt($.totalBeanNum) - $.nowBean > 0) {
      $.msg($.name, '', `京东账号${$.index} ${$.nickName}\n${message}`);
    } else {
      $.log(message)
    }
    // 云端大于10元无门槛红包时进行通知推送
    if ($.isNode() && $.totalNum >= 1000000) await notify.sendNotify(`${$.name} - 京东账号${$.index} - ${$.nickName}`, `京东账号${$.index} ${$.nickName}\n当前金币：${$.totalNum}个\n可兑换无门槛红包：${parseInt($.totalNum) / 10000}元\n`,)
    resolve();
  })
}
function getAuthorShareCode(url) {
  return new Promise(resolve => {
    $.get({url: `${url}?${new Date()}`,
      headers:{
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/87.0.4280.88"
      }}, async (err, resp, data) => {
      try {
        if (err) {
        } else {
          $.tuanList = $.tuanList.concat(JSON.parse(data))
          console.log(`作者助力码获取成功`)
        }
      } catch (e) {
        $.logErr(e, resp)
      } finally {
        resolve();
      }
    })
  })
}
function helpFriendTuan(body) {
  return new Promise(resolve => {
    $.get(taskTuanUrl("vvipclub_distributeBean_assist", body), async (err, resp, data) => {
      try {
        if (err) {
          console.log(`${JSON.stringify(err)}`)
          console.log(`${$.name} API请求失败，请检查网路重试`)
        } else {
          if (safeGet(data)) {
            data = JSON.parse(data);
            if (data.success) {
              console.log('助力成功')
            } else {
              if (data.resultCode === '9200008') console.log('不能助力自己')
              else if (data.resultCode === '9200011') console.log('已经助力过')
              else if (data.resultCode === '2400205') console.log('团已满')
              else if (data.resultCode === '2400203') {console.log('助力次数已耗尽');$.canHelp = false}
              else console.log(`未知错误`)
            }
          }
        }
      } catch (e) {
        $.logErr(e, resp)
      } finally {
        resolve(data);
      }
    })
  })
}

function getUserTuanInfo() {
  let body = {"paramData": {"channel": "FISSION_BEAN"}}
  return new Promise(resolve => {
    $.get(taskTuanUrl("distributeBeanActivityInfo", body), async (err, resp, data) => {
      try {
        if (err) {
          console.log(`${JSON.stringify(err)}`)
          console.log(`${$.name} API请求失败，请检查网路重试`)
        } else {
          if (safeGet(data)) {
            data = JSON.parse(data);
            if (data.data && !data.data.canStartNewAssist) {
              $.tuan = {
                "activityIdEncrypted": data.data.id,
                "assistStartRecordId": data.data.assistStartRecordId,
                "assistedPinEncrypted": data.data.encPin,
                "channel": "FISSION_BEAN"
              }
              $.tuanActId = data.data.id
            }
          }
        }
      } catch (e) {
        $.logErr(e, resp)
      } finally {
        resolve(data);
      }
    })
  })
}

function openTuan() {
  let body = {"activityIdEncrypted": $.tuanActId, "channel": "FISSION_BEAN"}
  return new Promise(resolve => {
    $.get(taskTuanUrl("vvipclub_distributeBean_startAssist", body), async (err, resp, data) => {
      try {
        if (err) {
          console.log(`${JSON.stringify(err)}`)
          console.log(`${$.name} API请求失败，请检查网路重试`)
        } else {
          if (safeGet(data)) {
            data = JSON.parse(data);
            if (data['success']) {
              $.hasOpen = true
            }
          }
        }
      } catch (e) {
        $.logErr(e, resp)
      } finally {
        resolve(data);
      }
    })
  })
}

function getUserInfo() {
  return new Promise(resolve => {
    $.get(taskUrl("interactIndex"), async (err, resp, data) => {
      try {
        if (err) {
          console.log(`${JSON.stringify(err)}`)
          console.log(`${$.name} API请求失败，请检查网路重试`)
        } else {
          if (safeGet(data)) {
            data = JSON.parse(data);
            if (data.data.shareTaskRes) {
              console.log(`\n【京东账号${$.index}（${$.nickName || $.UserName}）的${$.name}好友互助码】${data.data.shareTaskRes.itemId}\n`);
            } else {
              console.log(`\n\n已满5人助力或助力功能已下线,故暂时无${$.name}好友助力码\n\n`)
            }
          }
        }
      } catch (e) {
        $.logErr(e, resp)
      } finally {
        resolve(data);
      }
    })
  })
}

function getTaskList() {
  return new Promise(resolve => {
    $.get(taskUrl("interactTaskIndex"), async (err, resp, data) => {
      try {
        if (err) {
          console.log(`${JSON.stringify(err)}`)
          console.log(`${$.name} API请求失败，请检查网路重试`)
        } else {
          if (safeGet(data)) {
            data = JSON.parse(data);
            $.taskList = data.data.taskDetailResList
            $.totalNum = data.data.totalNum
            $.totalBeanNum = data.data.totalBeanNum
          }
        }
      } catch (e) {
        $.logErr(e, resp)
      } finally {
        resolve(data);
      }
    })
  })
}

// 完成
function doTask(body, func = "doInteractTask") {
  // console.log(taskUrl("doInteractTask", body))
  return new Promise(resolve => {
    $.get(taskUrl(func, body), async (err, resp, data) => {
      try {
        if (err) {
          console.log(`${JSON.stringify(err)}`)
          console.log(`${$.name} API请求失败，请检查网路重试`)
        } else {
          if (safeGet(data)) {
            data = JSON.parse(data);
            // console.log(data)
            if (func === "doInteractTask") {
              if (data.subCode === "S000") {
                console.log(`任务完成，获得 ${data.data.taskDetailResList[0].incomeAmountConf} 金币，${data.data.taskDetailResList[0].beanNum} 京豆`)
                $.bean += parseInt(data.data.taskDetailResList[0].beanNum)
              } else {
                console.log(`任务失败，错误信息：${data.message}`)
              }
            } else {
              console.log(`${data.data.helpResDesc}`)
            }
          }
        }
      } catch (e) {
        $.logErr(e, resp)
      } finally {
        resolve(data);
      }
    })
  })
}

async function helpFriends() {
  for (let code of $.newShareCodes) {
    if (!code) continue
    await doTask({"itemId": code, "taskId": "3", "mpVersion": "3.4.0"}, "doHelpTask")
  }
}
getArrRandomly = (arr) => {
  var len = arr.length;
  for (var i = len - 1; i >= 0; i--) {
    var randomIndex = Math.floor(Math.random() * (i + 1));
    var itemIndex = arr[randomIndex];
    arr[randomIndex] = arr[i];
    arr[i] = itemIndex;
  }
  return arr;
}


getRandomArr = (arr=[],num) => {
  const tmpArr = getArrRandomly(arr);
  let arrList = [];
  for (let i = 0; i < num; i++) {
    arrList.push(tmpArr[i]);
  };
  return arrList;
}


function readShareCode() {
console.log(`开始读取朱丽娜。。。`)
return new Promise(async resolve => {
  $.get({url: `https://raw.githubusercontent.com/jd1994527314/iosrule/cs/JD_TG/ZZ.json`, 'timeout': 10000}, (err, resp, data) => {
    try {
      if (err) {
        console.log(`${JSON.stringify(err)}`)
        console.log(`${$.name} API请求失败，请检查网路重试`)
      } else {
        if (data) {
          console.log(`随机取${randomCount}个码放到您固定的互助码后面(不影响已有固定互助)`)
          data = JSON.parse(data);
        }
      }
    } catch (e) {
      $.logErr(e, resp)
    } finally {
      resolve(data);
    }
  })
  await $.wait(10000);
  resolve()
})
}
//格式化助力码
function shareCodesFormat() {
return new Promise(async resolve => {
  // console.log(`第${$.index}个京东账号的助力码:::${$.shareCodesArr[$.index - 1]}`)
  $.newShareCodes = [];
  
  const readShareCodeRes = await readShareCode();
  
  if (readShareCodeRes && readShareCodeRes.code === 200) {
$.newShareCodes = [...new Set([...$.newShareCodes, ...(getRandomArr(getArrRandomly(readShareCodeRes.data),randomCount)|| [])])];
  }
  
  console.log(`第${$.index}个京东账号将要助力的好友${JSON.stringify($.newShareCodes)}`)





  resolve();
})
}

function requireConfig() {
  return new Promise(resolve => {
    console.log(`开始获取${$.name}配置文件\n`);
    //Node.js用户请在jdCookie.js处填写京东ck;
    let shareCodes = [];
    if ($.isNode()) {
      if (process.env.JDZZ_SHARECODES) {
        if (process.env.JDZZ_SHARECODES.indexOf('\n') > -1) {
          shareCodes = process.env.JDZZ_SHARECODES.split('\n');
        } else {
          shareCodes = process.env.JDZZ_SHARECODES.split('&');
        }
      }
    }
    console.log(`共${cookiesArr.length}个京东账号\n`);
    $.shareCodesArr = [];
    if ($.isNode()) {
      Object.keys(shareCodes).forEach((item) => {
        if (shareCodes[item]) {
          $.shareCodesArr.push(shareCodes[item])
        }
      })
    }
    console.log(`您提供了${$.shareCodesArr.length}个账号的${$.name}助力码\n`);
    resolve()
  })
}

function taskUrl(functionId, body = {}) {
  return {
    url: `${JD_API_HOST}?functionId=${functionId}&body=${escape(JSON.stringify(body))}&client=wh5&clientVersion=9.1.0`,
    headers: {
      'Cookie': cookie,
      'Host': 'api.m.jd.com',
      'Connection': 'keep-alive',
      'Content-Type': 'application/json',
      'Referer': 'http://wq.jd.com/wxapp/pages/hd-interaction/index/index',
      'User-Agent': $.isNode() ? (process.env.JD_USER_AGENT ? process.env.JD_USER_AGENT : (require('./USER_AGENTS').USER_AGENT)) : ($.getdata('JDUA') ? $.getdata('JDUA') : "jdapp;iPhone;9.2.2;14.2;%E4%BA%AC%E4%B8%9C/9.2.2 CFNetwork/1206 Darwin/20.1.0"),
      'Accept-Language': 'zh-cn',
      'Accept-Encoding': 'gzip, deflate, br',
    }
  }
}

function taskTuanUrl(function_id, body = {}) {
  return {
    url: `${JD_API_HOST}?functionId=${function_id}&body=${escape(JSON.stringify(body))}&appid=swat_miniprogram&osVersion=5.0.0&clientVersion=3.1.3&fromType=wxapp&timestamp=${new Date().getTime() + new Date().getTimezoneOffset() * 60 * 1000 + 8 * 60 * 60 * 1000}`,
    headers: {
      "Accept": "*/*",
      "Accept-Encoding": "gzip, deflate, br",
      "Accept-Language": "zh-cn",
      "Connection": "keep-alive",
      "Content-Type": "application/x-www-form-urlencoded",
      "Host": "api.m.jd.com",
      "Referer": "https://servicewechat.com/wxa5bf5ee667d91626/108/page-frame.html",
      "Cookie": cookie,
      "User-Agent": $.isNode() ? (process.env.JD_USER_AGENT ? process.env.JD_USER_AGENT : (require('./USER_AGENTS').USER_AGENT)) : ($.getdata('JDUA') ? $.getdata('JDUA') : "jdapp;iPhone;9.2.2;14.2;%E4%BA%AC%E4%B8%9C/9.2.2 CFNetwork/1206 Darwin/20.1.0"),
    }
  }
}

function taskPostUrl(function_id, body = {}) {
  return {
    url: `${JD_API_HOST}?functionId=${function_id}`,
    body: body,
    headers: {
      "Cookie": cookie,
      'Content-Type': 'application/x-www-form-urlencoded',
      "User-Agent": $.isNode() ? (process.env.JD_USER_AGENT ? process.env.JD_USER_AGENT : (require('./USER_AGENTS').USER_AGENT)) : ($.getdata('JDUA') ? $.getdata('JDUA') : "jdapp;iPhone;9.2.2;14.2;%E4%BA%AC%E4%B8%9C/9.2.2 CFNetwork/1206 Darwin/20.1.0"),
    }
  }
}

function TotalBean() {
  return new Promise(async resolve => {
    const options = {
      "url": `https://wq.jd.com/user/info/QueryJDUserInfo?sceneval=2`,
      "headers": {
        "Accept": "application/json,text/plain, */*",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-cn",
        "Connection": "keep-alive",
        "Cookie": cookie,
        "Referer": "https://wqs.jd.com/my/jingdou/my.shtml?sceneval=2",
        "User-Agent": $.isNode() ? (process.env.JD_USER_AGENT ? process.env.JD_USER_AGENT : (require('./USER_AGENTS').USER_AGENT)) : ($.getdata('JDUA') ? $.getdata('JDUA') : "jdapp;iPhone;9.2.2;14.2;%E4%BA%AC%E4%B8%9C/9.2.2 CFNetwork/1206 Darwin/20.1.0")
      }
    }
    $.post(options, (err, resp, data) => {
      try {
        if (err) {
          console.log(`${JSON.stringify(err)}`)
          console.log(`${$.name} API请求失败，请检查网路重试`)
        } else {
          if (data) {
            data = JSON.parse(data);
            if (data['retcode'] === 13) {
              $.isLogin = false; //cookie过期
              return
            }
            $.nickName = data['base'].nickname;
          } else {
            console.log(`京东服务器返回空数据`)
          }
        }
      } catch (e) {
        $.logErr(e, resp)
      } finally {
        resolve();
      }
    })
  })
}

function safeGet(data) {
  try {
    if (typeof JSON.parse(data) == "object") {
      return true;
    }
  } catch (e) {
    console.log(e);
    console.log(`京东服务器访问数据为空，请检查自身设备网络情况`);
    return false;
  }
}

function jsonParse(str) {
  if (typeof str == "string") {
    try {
      return JSON.parse(str);
    } catch (e) {
      console.log(e);
      $.msg($.name, '', '不要在BoxJS手动复制粘贴修改cookie')
      return [];
    }
  }
}
// prettier-ignore
function Env(t,e){"undefined"!=typeof process&&JSON.stringify(process.env).indexOf("GITHUB")>-1&&process.exit(0);class s{constructor(t){this.env=t}send(t,e="GET"){t="string"==typeof t?{url:t}:t;let s=this.get;return"POST"===e&&(s=this.post),new Promise((e,i)=>{s.call(this,t,(t,s,r)=>{t?i(t):e(s)})})}get(t){return this.send.call(this.env,t)}post(t){return this.send.call(this.env,t,"POST")}}return new class{constructor(t,e){this.name=t,this.http=new s(this),this.data=null,this.dataFile="box.dat",this.logs=[],this.isMute=!1,this.isNeedRewrite=!1,this.logSeparator="\n",this.startTime=(new Date).getTime(),Object.assign(this,e),this.log("",`🔔${this.name}, 开始!`)}isNode(){return"undefined"!=typeof module&&!!module.exports}isQuanX(){return"undefined"!=typeof $task}isSurge(){return"undefined"!=typeof $httpClient&&"undefined"==typeof $loon}isLoon(){return"undefined"!=typeof $loon}toObj(t,e=null){try{return JSON.parse(t)}catch{return e}}toStr(t,e=null){try{return JSON.stringify(t)}catch{return e}}getjson(t,e){let s=e;const i=this.getdata(t);if(i)try{s=JSON.parse(this.getdata(t))}catch{}return s}setjson(t,e){try{return this.setdata(JSON.stringify(t),e)}catch{return!1}}getScript(t){return new Promise(e=>{this.get({url:t},(t,s,i)=>e(i))})}runScript(t,e){return new Promise(s=>{let i=this.getdata("@chavy_boxjs_userCfgs.httpapi");i=i?i.replace(/\n/g,"").trim():i;let r=this.getdata("@chavy_boxjs_userCfgs.httpapi_timeout");r=r?1*r:20,r=e&&e.timeout?e.timeout:r;const[o,h]=i.split("@"),n={url:`http://${h}/v1/scripting/evaluate`,body:{script_text:t,mock_type:"cron",timeout:r},headers:{"X-Key":o,Accept:"*/*"}};this.post(n,(t,e,i)=>s(i))}).catch(t=>this.logErr(t))}loaddata(){if(!this.isNode())return{};{this.fs=this.fs?this.fs:require("fs"),this.path=this.path?this.path:require("path");const t=this.path.resolve(this.dataFile),e=this.path.resolve(process.cwd(),this.dataFile),s=this.fs.existsSync(t),i=!s&&this.fs.existsSync(e);if(!s&&!i)return{};{const i=s?t:e;try{return JSON.parse(this.fs.readFileSync(i))}catch(t){return{}}}}}writedata(){if(this.isNode()){this.fs=this.fs?this.fs:require("fs"),this.path=this.path?this.path:require("path");const t=this.path.resolve(this.dataFile),e=this.path.resolve(process.cwd(),this.dataFile),s=this.fs.existsSync(t),i=!s&&this.fs.existsSync(e),r=JSON.stringify(this.data);s?this.fs.writeFileSync(t,r):i?this.fs.writeFileSync(e,r):this.fs.writeFileSync(t,r)}}lodash_get(t,e,s){const i=e.replace(/\[(\d+)\]/g,".$1").split(".");let r=t;for(const t of i)if(r=Object(r)[t],void 0===r)return s;return r}lodash_set(t,e,s){return Object(t)!==t?t:(Array.isArray(e)||(e=e.toString().match(/[^.[\]]+/g)||[]),e.slice(0,-1).reduce((t,s,i)=>Object(t[s])===t[s]?t[s]:t[s]=Math.abs(e[i+1])>>0==+e[i+1]?[]:{},t)[e[e.length-1]]=s,t)}getdata(t){let e=this.getval(t);if(/^@/.test(t)){const[,s,i]=/^@(.*?)\.(.*?)$/.exec(t),r=s?this.getval(s):"";if(r)try{const t=JSON.parse(r);e=t?this.lodash_get(t,i,""):e}catch(t){e=""}}return e}setdata(t,e){let s=!1;if(/^@/.test(e)){const[,i,r]=/^@(.*?)\.(.*?)$/.exec(e),o=this.getval(i),h=i?"null"===o?null:o||"{}":"{}";try{const e=JSON.parse(h);this.lodash_set(e,r,t),s=this.setval(JSON.stringify(e),i)}catch(e){const o={};this.lodash_set(o,r,t),s=this.setval(JSON.stringify(o),i)}}else s=this.setval(t,e);return s}getval(t){return this.isSurge()||this.isLoon()?$persistentStore.read(t):this.isQuanX()?$prefs.valueForKey(t):this.isNode()?(this.data=this.loaddata(),this.data[t]):this.data&&this.data[t]||null}setval(t,e){return this.isSurge()||this.isLoon()?$persistentStore.write(t,e):this.isQuanX()?$prefs.setValueForKey(t,e):this.isNode()?(this.data=this.loaddata(),this.data[e]=t,this.writedata(),!0):this.data&&this.data[e]||null}initGotEnv(t){this.got=this.got?this.got:require("got"),this.cktough=this.cktough?this.cktough:require("tough-cookie"),this.ckjar=this.ckjar?this.ckjar:new this.cktough.CookieJar,t&&(t.headers=t.headers?t.headers:{},void 0===t.headers.Cookie&&void 0===t.cookieJar&&(t.cookieJar=this.ckjar))}get(t,e=(()=>{})){t.headers&&(delete t.headers["Content-Type"],delete t.headers["Content-Length"]),this.isSurge()||this.isLoon()?(this.isSurge()&&this.isNeedRewrite&&(t.headers=t.headers||{},Object.assign(t.headers,{"X-Surge-Skip-Scripting":!1})),$httpClient.get(t,(t,s,i)=>{!t&&s&&(s.body=i,s.statusCode=s.status),e(t,s,i)})):this.isQuanX()?(this.isNeedRewrite&&(t.opts=t.opts||{},Object.assign(t.opts,{hints:!1})),$task.fetch(t).then(t=>{const{statusCode:s,statusCode:i,headers:r,body:o}=t;e(null,{status:s,statusCode:i,headers:r,body:o},o)},t=>e(t))):this.isNode()&&(this.initGotEnv(t),this.got(t).on("redirect",(t,e)=>{try{if(t.headers["set-cookie"]){const s=t.headers["set-cookie"].map(this.cktough.Cookie.parse).toString();s&&this.ckjar.setCookieSync(s,null),e.cookieJar=this.ckjar}}catch(t){this.logErr(t)}}).then(t=>{const{statusCode:s,statusCode:i,headers:r,body:o}=t;e(null,{status:s,statusCode:i,headers:r,body:o},o)},t=>{const{message:s,response:i}=t;e(s,i,i&&i.body)}))}post(t,e=(()=>{})){if(t.body&&t.headers&&!t.headers["Content-Type"]&&(t.headers["Content-Type"]="application/x-www-form-urlencoded"),t.headers&&delete t.headers["Content-Length"],this.isSurge()||this.isLoon())this.isSurge()&&this.isNeedRewrite&&(t.headers=t.headers||{},Object.assign(t.headers,{"X-Surge-Skip-Scripting":!1})),$httpClient.post(t,(t,s,i)=>{!t&&s&&(s.body=i,s.statusCode=s.status),e(t,s,i)});else if(this.isQuanX())t.method="POST",this.isNeedRewrite&&(t.opts=t.opts||{},Object.assign(t.opts,{hints:!1})),$task.fetch(t).then(t=>{const{statusCode:s,statusCode:i,headers:r,body:o}=t;e(null,{status:s,statusCode:i,headers:r,body:o},o)},t=>e(t));else if(this.isNode()){this.initGotEnv(t);const{url:s,...i}=t;this.got.post(s,i).then(t=>{const{statusCode:s,statusCode:i,headers:r,body:o}=t;e(null,{status:s,statusCode:i,headers:r,body:o},o)},t=>{const{message:s,response:i}=t;e(s,i,i&&i.body)})}}time(t,e=null){const s=e?new Date(e):new Date;let i={"M+":s.getMonth()+1,"d+":s.getDate(),"H+":s.getHours(),"m+":s.getMinutes(),"s+":s.getSeconds(),"q+":Math.floor((s.getMonth()+3)/3),S:s.getMilliseconds()};/(y+)/.test(t)&&(t=t.replace(RegExp.$1,(s.getFullYear()+"").substr(4-RegExp.$1.length)));for(let e in i)new RegExp("("+e+")").test(t)&&(t=t.replace(RegExp.$1,1==RegExp.$1.length?i[e]:("00"+i[e]).substr((""+i[e]).length)));return t}msg(e=t,s="",i="",r){const o=t=>{if(!t)return t;if("string"==typeof t)return this.isLoon()?t:this.isQuanX()?{"open-url":t}:this.isSurge()?{url:t}:void 0;if("object"==typeof t){if(this.isLoon()){let e=t.openUrl||t.url||t["open-url"],s=t.mediaUrl||t["media-url"];return{openUrl:e,mediaUrl:s}}if(this.isQuanX()){let e=t["open-url"]||t.url||t.openUrl,s=t["media-url"]||t.mediaUrl;return{"open-url":e,"media-url":s}}if(this.isSurge()){let e=t.url||t.openUrl||t["open-url"];return{url:e}}}};if(this.isMute||(this.isSurge()||this.isLoon()?$notification.post(e,s,i,o(r)):this.isQuanX()&&$notify(e,s,i,o(r))),!this.isMuteLog){let t=["","==============📣系统通知📣=============="];t.push(e),s&&t.push(s),i&&t.push(i),console.log(t.join("\n")),this.logs=this.logs.concat(t)}}log(...t){t.length>0&&(this.logs=[...this.logs,...t]),console.log(t.join(this.logSeparator))}logErr(t,e){const s=!this.isSurge()&&!this.isQuanX()&&!this.isLoon();s?this.log("",`❗️${this.name}, 错误!`,t.stack):this.log("",`❗️${this.name}, 错误!`,t)}wait(t){return new Promise(e=>setTimeout(e,t))}done(t={}){const e=(new Date).getTime(),s=(e-this.startTime)/1e3;this.log("",`🔔${this.name}, 结束! 🕛 ${s} 秒`),this.log(),(this.isSurge()||this.isQuanX()||this.isLoon())&&$done(t)}}(t,e)}
