/*

杰昆·菲尼克斯的奥斯卡演讲中英对照全文
文章来源：未知 文章作者：enread 发布时间：2020-03-18 08:25 字体： [大 中 小]　 进入论坛
(单词翻译:双击或拖选)
“I’m full of so much gratitude1 now. I do not feel elevated above any of my fellow nominees2 or anyone in this room, because we share the same love – that’s the love of film. And this form of expression has given me the most extraordinary life. I don’t know where I’d be without it. But I think the greatest gift that it’s given me, and many people in [this industry] is the opportunity to use our voice for the voiceless. 

“我现在心里充满了感激之情。 我并不觉得自己比任何其他提名者或在座的任何人都要高尚，因为我们分享着同样的爱——这就是对电影的热爱。 这种表达方式给了我最不平凡的生活。 我不知道没有它我会在哪里。 但是我认为它给予我和这个行业的许多人的最大的礼物，就是让我们有机会为那些没有发言权的人发声。

 

“I’ve been thinking about some of the distressing3 issues that we’ve been facing collectively. I think at times we feel or are made to feel that we champion different causes. But for me, I see commonality. I think, whether we’re talking about gender4 inequality or racism5 or queer rights or indigenous6 rights or animal rights, we’re talking about the fight against injustice7.

“我一直在思考我们共同面临的一些令人沮丧的问题。 我认为有时我们感觉或被迫感觉我们支持不同的事业。 但对我来说，我看到了共性。 我认为，无论我们谈论的是性别不平等、种族歧视、酷儿权利、土著权利或动物权利，我们谈论的是反对不公正的斗争。

 

“We’re talking about the fight against the belief that one nation, one people, one race, one gender, one species, has the right to dominate, use and control another with impunity8.

“我们讨论的是反对一个国家、一个民族、一个种族、一个性别、一个物种有权支配、使用和控制另一个物种而不受惩罚的信念。

 

“I think we’ve become very disconnected from the natural world. Many of us are guilty of an egocentric world view, and we believe that we’re the centre of the universe. We go into the natural world and we plunder9 it for its resources. 

“我认为我们已经变得非常脱离自然世界。 我们中的许多人都对自我中心的世界观感到内疚，我们相信我们是宇宙的中心。 我们进入自然世界，掠夺它的资源。

 

“We feel entitled to artificially inseminate a cow and steal her baby, even though her cries of anguish10 are unmistakeable. Then we take her milk that’s intended for her calf11 and we put it in our coffee and our cereal.

“我们觉得自己有权利让一头奶牛人工受精，并偷走她的婴儿，尽管她痛苦的哭声是明白无误的。 然后，我们把准备给她的小牛喝的牛奶，放进我们的咖啡和麦片里。

 

“We fear the idea of personal change, because we think we need to sacrifice something; to give something up. But human beings at our best are so creative and inventive, and we can create, develop and implement12 systems of change that are beneficial to all sentient13 beings and the environment.

“我们害怕个人的改变，因为我们认为我们需要牺牲一些东西，放弃一些东西。 但是处于最佳状态的人类是如此具有创造性和创造性，我们可以创造、发展和实施对所有有情众生和环境有益的变化系统。

 

“I have been a scoundrel all my life, I’ve been selfish. I’ve been cruel at times, hard to work with, and I’m grateful that so many of you in this room have given me a second chance. I think that’s when we’re at our best: when we support each other. Not when we cancel each other out for our past mistakes, but when we help each other to grow. When we educate each other; when we guide each other to redemption.

“我一辈子都是个无赖，我很自私。 我有时很残忍，很难相处，我很感激在座的诸位给了我第二次机会。 我认为那是我们最好的时候: 当我们互相支持的时候。 不是当我们互相抵消过去的错误，而是当我们帮助彼此成长。 当我们彼此教育，当我们引导彼此救赎。

 

When he was 17, my brother [River] wrote this lyric14. He said: “run to the rescue with love and peace will follow.”

我哥哥[雷芙]17岁时写了这首歌词。 他说: “用爱去营救，和平就会随之而来。”


摇钱树 ：https://gitee.com/lxk0301/jd_scripts/raw/master/jd_moneyTree.js
更新时间：2020-11-16
活动入口：京东APP我的-更多工具-摇钱树

注：如果使用Node.js, 需自行安装'crypto-js,got,http-server,tough-cookie'模块. 例: npm install crypto-js http-server tough-cookie got --save
===============Quantumultx===============
[task_local]
#京东摇钱树
3 0-23/2 * * * https://gitee.com/lxk0301/jd_scripts/raw/master/jd_moneyTree.js, tag=京东摇钱树, img-url=https://raw.githubusercontent.com/58xinian/icon/master/jdyqs.png, enabled=true

==============Loon===========
[Script]
cron "3 0-23/2 * * *" script-path=https://gitee.com/lxk0301/jd_scripts/raw/master/jd_moneyTree.js,tag=京东摇钱树

===============Surge===========
京东摇钱树 = type=cron,cronexp="3 0-23/2 * * *",wake-system=1,timeout=3600,script-path=https://gitee.com/lxk0301/jd_scripts/raw/master/jd_moneyTree.js

============小火箭=========
京东摇钱树 = type=cron,script-path=https://gitee.com/lxk0301/jd_scripts/raw/master/jd_moneyTree.js, cronexpr="3 0-23/2 * * *", timeout=3600, enable=true
*/

const $ = new Env('京东摇钱树');
const notify = $.isNode() ? require('./sendNotify') : '';
//Node.js用户请在jdCookie.js处填写京东ck;
const jdCookieNode = $.isNode() ? require('./jdCookie.js') : '';

//IOS等用户直接用NobyDa的jd cookie
let cookiesArr = [], cookie = '';
if ($.isNode()) {
  Object.keys(jdCookieNode).forEach((item) => {
    cookiesArr.push(jdCookieNode[item])
  })
  if (process.env.JD_DEBUG && process.env.JD_DEBUG === 'false') console.log = () => {};
} else {
  let cookiesData = $.getdata('CookiesJD') || "[]";
  cookiesData = jsonParse(cookiesData);
  cookiesArr = cookiesData.map(item => item.cookie);
  cookiesArr.reverse();
  cookiesArr.push(...[$.getdata('CookieJD2'), $.getdata('CookieJD')]);
  cookiesArr.reverse();
  cookiesArr = cookiesArr.filter(item => item !== "" && item !== null && item !== undefined);
}

let jdNotify = true;//是否开启静默运行，默认true开启
let sellFruit = false;//是否卖出金果得到金币，默认'false'不卖
const JD_API_HOST = 'https://ms.jr.jd.com/gw/generic/uc/h5/m';
let userInfo = null, taskInfo = [], message = '', subTitle = '', fruitTotal = 0;
!(async () => {
  if (!cookiesArr[0]) {
    $.msg($.name, '【提示】请先获取cookie\n直接使用NobyDa的京东签到获取', 'https://bean.m.jd.com/bean/signIndex.action', {"open-url": "https://bean.m.jd.com/bean/signIndex.action"});
  }
  for (let i = 0; i < cookiesArr.length; i++) {
    if (cookiesArr[i]) {
      cookie = cookiesArr[i];
      $.UserName = decodeURIComponent(cookie.match(/pt_pin=(.+?);/) && cookie.match(/pt_pin=(.+?);/)[1])
      $.index = i + 1;
      $.isLogin = true;
      $.nickName = '';
      await TotalBean();
      console.log(`\n开始【京东账号${$.index}】${$.nickName || $.UserName}\n`);
      if (!$.isLogin) {
        $.msg($.name, `【提示】cookie已失效`, `京东账号${$.index} ${$.nickName || $.UserName}\n请重新登录获取\nhttps://bean.m.jd.com/bean/signIndex.action`, {"open-url": "https://bean.m.jd.com/bean/signIndex.action"});

        if ($.isNode()) {
          await notify.sendNotify(`${$.name}cookie已失效 - ${$.UserName}`, `京东账号${$.index} ${$.UserName}\n请重新登录获取cookie`);
        }
        continue
      }
      message = '';
      subTitle = '';
      await jd_moneyTree();
    }
  }
})()
    .catch((e) => {
      $.log('', `❌ ${$.name}, 失败! 原因: ${e}!`, '')
    })
    .finally(() => {
      $.done();
    })
async function jd_moneyTree() {
  try {
    const userRes = await user_info();
    if (!userRes || !userRes.realName) return
    await signEveryDay();
    await dayWork();
    await harvest();
    await sell();
    await myWealth();
    await stealFriendFruit()

    $.log(`\n${message}\n`);
    if (!jdNotify || jdNotify === 'false') {
      $.msg($.name, subTitle, message);
    }
  } catch (e) {
    $.logErr(e)
  }
}
function user_info() {
  console.log('初始化摇钱树个人信息');
  const params = {
    "sharePin":"",
    "shareType":1,
    "channelLV":"",
    "source":0,
    "riskDeviceParam":{"eid":"","dt":"","ma":"","im":"","os":"","osv":"","ip":"","apid":"","ia":"","uu":"","cv":"","nt":"","at":"1","fp":"","token":""}
  }
  params.riskDeviceParam = JSON.stringify(params.riskDeviceParam);
  // await $.wait(5000); //歇口气儿, 不然会报操作频繁
  return new Promise((resolve, reject) => {
    $.post(taskurl('login', params), async (err, resp, data) => {
      try {
        if (err) {
          console.log("\n摇钱树京东API请求失败 ‼️‼️")
          console.log(JSON.stringify(err));
        } else {
          if (data) {
            const res = JSON.parse(data);
            if (res && res.resultCode === 0) {
              $.isLogin = true;
              console.log('resultCode为0')
              if (res.resultData.data) {
                userInfo = res.resultData.data;
                // userInfo.realName = null;
                if (userInfo.realName) {
                  // console.log(`助力码sharePin为：：${userInfo.sharePin}`);
                  $.treeMsgTime = userInfo.sharePin;
                  subTitle = `【${userInfo.nick}】${userInfo.treeInfo.treeName}`;
                  // message += `【我的金果数量】${userInfo.treeInfo.fruit}\n`;
                  // message += `【我的金币数量】${userInfo.treeInfo.coin}\n`;
                  // message += `【距离${userInfo.treeInfo.level + 1}级摇钱树还差】${userInfo.treeInfo.progressLeft}\n`;
                } else {
                  $.log(`京东账号${$.index}${$.UserName}运行失败\n此账号未实名认证或者未参与过此活动\n①如未参与活动,请先去京东app参加摇钱树活动\n入口：我的->游戏与互动->查看更多\n②如未实名认证,请进行实名认证`)
                  // $.msg($.name, `【提示】京东账号${$.index}${$.UserName}运行失败`, '此账号未实名认证或者未参与过此活动\n①如未参与活动,请先去京东app参加摇钱树活动\n入口：我的->游戏与互动->查看更多\n②如未实名认证,请进行实名认证', {"open-url": "openApp.jdMobile://"});
                }
              }
            } else {
              console.log(`其他情况::${JSON.stringify(res)}`);
            }
          } else {
            console.log(`京豆api返回数据为空，请检查自身原因`)
          }
        }
      } catch (eor) {
        $.msg("摇钱树-初始化个人信息" + eor.name + "‼️", JSON.stringify(eor), eor.message)
      } finally {
        resolve(userInfo)
      }
    })
  })
}

function dayWork() {
  console.log(`开始做任务userInfo了\n`)
  return new Promise(async resolve => {
    const data = {
      "source":0,
      "linkMissionIds":["666","667"],
      "LinkMissionIdValues":[7,7],
      "riskDeviceParam":{"eid":"","dt":"","ma":"","im":"","os":"","osv":"","ip":"","apid":"","ia":"","uu":"","cv":"","nt":"","at":"1","fp":"","token":""}
    };
    let response = await request('dayWork', data);
    // console.log(`获取任务的信息:${JSON.stringify(response)}\n`)
    let canTask = [];
    taskInfo = [];
    if (response && response.resultCode === 0) {
      if (response.resultData.code === '200') {
        response.resultData.data.map((item) => {
          if (item.prizeType === 2) {
            canTask.push(item);
          }
          if (item.workType === 7 && item.prizeType === 0) {
            // missionId.push(item.mid);
            taskInfo.push(item);
          }
          // if (item.workType === 7 && item.prizeType === 0) {
          //   missionId2 = item.mid;
          // }
        })
      }
    }
    console.log(`canTask::${JSON.stringify(canTask)}\n`)
    console.log(`浏览任务列表taskInfo::${JSON.stringify(taskInfo)}\n`)
    for (let item of canTask) {
      if (item.workType === 1) {
        //  签到任务
        // let signRes = await sign();
        // console.log(`签到结果:${JSON.stringify(signRes)}`);
        if (item.workStatus === 0) {
          // const data = {"source":2,"workType":1,"opType":2};
          // let signRes = await request('doWork', data);
          let signRes = await sign();
          console.log(`三餐签到结果:${JSON.stringify(signRes)}`);
        } else if (item.workStatus === 2) {
          console.log(`三餐签到任务已经做过`)
        } else if (item.workStatus === -1) {
          console.log(`三餐签到任务不在时间范围内`)
        }
      } else if (item.workType === 2) {
        // 分享任务
        if (item.workStatus === 0) {
          // share();
          const data = {"source":0,"workType":2,"opType":1};
          //开始分享
          // let shareRes = await request('doWork', data);
          let shareRes = await share(data);
          console.log(`开始分享的动作:${JSON.stringify(shareRes)}`);
          const b = {"source":0,"workType":2,"opType":2};
          // let shareResJL = await request('doWork', b);
          let shareResJL = await share(b);
          console.log(`领取分享后的奖励:${JSON.stringify(shareResJL)}`)
        } else if (item.workStatus === 2) {
          console.log(`分享任务已经做过`)
        }
      }
    }
    for (let task of taskInfo) {
      if (task.mid && task.workStatus === 0) {
        console.log('开始做浏览任务');
        // yield setUserLinkStatus(task.mid);
        let aa = await setUserLinkStatus(task.mid);
        console.log(`aaa${JSON.stringify(aa)}`);
      } else if (task.mid && task.workStatus === 1){
        console.log(`workStatus === 1开始领取浏览后的奖励:mid:${task.mid}`);
        let receiveAwardRes = await receiveAward(task.mid);
        console.log(`领取浏览任务奖励成功：${JSON.stringify(receiveAwardRes)}`)
      } else if (task.mid && task.workStatus === 2) {
        console.log('所有的浏览任务都做完了')
      }
    }
    resolve();
  });
}

function harvest() {
  console.log(`收获的操作:${JSON.stringify(userInfo)}\n`)
  if (!userInfo) return
  const data = {
    "source": 2,
    "sharePin": "",
    "userId": userInfo.userInfo,
    "userToken": userInfo.userToken
  }
  return new Promise((rs, rj) => {
    request('harvest', data).then((harvestRes) => {
      if (harvestRes && harvestRes.resultCode === 0 && harvestRes.resultData.code === '200') {
        console.log('收获金果')
        let data = harvestRes.resultData.data;
        message += `【距离${data.treeInfo.level + 1}级摇钱树还差】${data.treeInfo.progressLeft}\n`;
        fruitTotal = data.treeInfo.fruit;
      }
      rs()
      // gen.next();
    })
  })
  // request('harvest', data).then((harvestRes) => {
  //   if (harvestRes.resultCode === 0 && harvestRes.resultData.code === '200') {
  //     let data = harvestRes.resultData.data;
  //     message += `【距离${data.treeInfo.level + 1}级摇钱树还差】${data.treeInfo.progressLeft}\n`;
  //     fruitTotal = data.treeInfo.fruit;
  //     gen.next();
  //   }
  // })
}
//卖出金果，得到金币
function sell() {
  return new Promise((rs, rj) => {
    const params = {
      "source": 2,
      "riskDeviceParam":{"eid":"","dt":"","ma":"","im":"","os":"","osv":"","ip":"","apid":"","ia":"","uu":"","cv":"","nt":"","at":"1","fp":"","token":""}
    }
    params.riskDeviceParam = JSON.stringify(params.riskDeviceParam);//这一步，不可省略，否则提交会报错（和login接口一样）
    console.log(`目前金果数量${fruitTotal}`)
    sellFruit = $.isNode() ? (process.env.MONEY_TREE_SELL_FRUIT ? process.env.MONEY_TREE_SELL_FRUIT : `${sellFruit}`) : ($.getdata('MONEY_TREE_SELL_FRUIT') ? $.getdata('MONEY_TREE_SELL_FRUIT') : `${sellFruit}`);
    if (sellFruit && sellFruit === 'false') {
      console.log(`\n设置的不卖出金果\n`)
      rs()
      return
    }
    if (fruitTotal > 380) {
      request('sell', params).then((sellRes) => {
        console.log(`卖出金果结果:${JSON.stringify(sellRes)}\n`)
        rs()
      })
    } else {
      rs()
    }
    // request('sell', params).then(response => {
    //   rs(response);
    // })
  })
  // request('sell', params).then((sellRes) => {
  //   console.log(`卖出金果结果:${JSON.stringify(sellRes)}\n`)
  //   gen.next();
  // })
}
//获取金币和金果数量
function myWealth() {
  return new Promise((resolve) => {
    const params = {
      "source": 2,
      "riskDeviceParam":{"eid":"","dt":"","ma":"","im":"","os":"","osv":"","ip":"","apid":"","ia":"","uu":"","cv":"","nt":"","at":"1","fp":"","token":""}
    }
    params.riskDeviceParam = JSON.stringify(params.riskDeviceParam);//这一步，不可省略，否则提交会报错（和login接口一样）
    request('myWealth', params).then(res=> {
      if (res && res.resultCode === 0 && res.resultData.code === '200') {
        console.log(`金币数量和金果：：${JSON.stringify(res)}`);
        message += `【我的金果数量】${res.resultData.data.gaAmount}\n`;
        message += `【我的金币数量】${res.resultData.data.gcAmount}\n`;
      }
      resolve();
    })
  });
}
function sign() {
  console.log('开始三餐签到')
  const data = {"source":2,"workType":1,"opType":2};
  return new Promise((rs, rj) => {
    request('doWork', data).then(response => {
      rs(response);
    })
  })
}
function signIndex() {
  const params = {
    "source":0,
    "riskDeviceParam":{"eid":"","dt":"","ma":"","im":"","os":"","osv":"","ip":"","apid":"","ia":"","uu":"","cv":"","nt":"","at":"1","fp":"","token":""}
  }
  return new Promise((rs, rj) => {
    request('signIndex', params).then(response => {
      rs(response);
    })
  })
}
function signEveryDay() {
  return new Promise(async (resolve) => {
    try {
      let signIndexRes = await signIndex();
      if (signIndexRes.resultCode === 0) {
        console.log(`每日签到条件查询:${signIndexRes.resultData.data.canSign === 2 ? '可以签到' : '已经签到过了'}`);
        if (signIndexRes.resultData && signIndexRes.resultData.data.canSign == 2) {
          console.log('准备每日签到')
          let signOneRes = await signOne(signIndexRes.resultData.data.signDay);
          console.log(`第${signIndexRes.resultData.data.signDay}日签到结果:${JSON.stringify(signOneRes)}`);
          if (signIndexRes.resultData.data.signDay === 7) {
            let getSignAwardRes = await getSignAward();
            console.log(`店铺券（49-10）领取结果：${JSON.stringify(getSignAwardRes)}`)
            if (getSignAwardRes.resultCode === 0 && getSignAwardRes.data.code === 0) {
              message += `【7日签到奖励领取】${getSignAwardRes.datamessage}\n`
            }
          }
        }
      }
    } catch (e) {
      $.logErr(e);
    } finally {
      resolve()
    }
  })
}
function signOne(signDay) {
  const params = {
    "source":0,
    "signDay": signDay,
    "riskDeviceParam":{"eid":"","dt":"","ma":"","im":"","os":"","osv":"","ip":"","apid":"","ia":"","uu":"","cv":"","nt":"","at":"1","fp":"","token":""}
  }
  return new Promise((rs, rj) => {
    request('signOne', params).then(response => {
      rs(response);
    })
  })
}
// 领取七日签到后的奖励(店铺优惠券)
function getSignAward() {
  const params = {
    "source":2,
    "awardType": 2,
    "deviceRiskParam": 1,
    "riskDeviceParam":{"eid":"","dt":"","ma":"","im":"","os":"","osv":"","ip":"","apid":"","ia":"","uu":"","cv":"","nt":"","at":"1","fp":"","token":""}
  }
  return new Promise((rs, rj) => {
    request('getSignAward', params).then(response => {
      rs(response);
    })
  })
}
// 浏览任务
async function setUserLinkStatus(missionId) {
  let index = 0;
  do {
    const params = {
      "missionId": missionId,
      "pushStatus": 1,
      "keyValue": index,
      "riskDeviceParam":{"eid":"","dt":"","ma":"","im":"","os":"","osv":"","ip":"","apid":"","ia":"","uu":"","cv":"","nt":"","at":"1","fp":"","token":""}
    }
    let response = await request('setUserLinkStatus', params)
    console.log(`missionId为${missionId}：：第${index + 1}次浏览活动完成: ${JSON.stringify(response)}`);
    // if (resultCode === 0) {
    //   let sportRevardResult = await getSportReward();
    //   console.log(`领取遛狗奖励完成: ${JSON.stringify(sportRevardResult)}`);
    // }
    index++;
  } while (index < 7) //不知道结束的条件，目前写死循环7次吧
  console.log('浏览店铺任务结束');
  console.log('开始领取浏览后的奖励');
  let receiveAwardRes = await receiveAward(missionId);
  console.log(`领取浏览任务奖励成功：${JSON.stringify(receiveAwardRes)}`)
  return new Promise((resolve, reject) => {
    resolve(receiveAwardRes);
  })
  // gen.next();
}
// 领取浏览后的奖励
function receiveAward(mid) {
  if (!mid) return
  mid = mid + "";
  const params = {
    "source":0,
    "workType": 7,
    "opType": 2,
    "mid": mid,
    "riskDeviceParam":{"eid":"","dt":"","ma":"","im":"","os":"","osv":"","ip":"","apid":"","ia":"","uu":"","cv":"","nt":"","at":"1","fp":"","token":""}
  }
  return new Promise((rs, rj) => {
    request('doWork', params).then(response => {
      rs(response);
    })
  })
}
function share(data) {
  if (data.opType === 1) {
    console.log(`开始做分享任务\n`)
  } else {
    console.log(`开始做领取分享后的奖励\n`)
  }
  return new Promise((rs, rj) => {
    request('doWork', data).then(response => {
      rs(response);
    })
  })
  // const data = 'reqData={"source":0,"workType":2,"opType":1}';
  // request('doWork', data).then(res => {
  //   console.log(`分享111:${JSON.stringify(res)}`)
  //   setTimeout(() => {
  //     const data2 = 'reqData={"source":0,"workType":2,"opType":2}';
  //     request('doWork', data2).then(res => {
  //       console.log(`分享222:${JSON.stringify(res)}`)
  //     })
  //   }, 2000)
  // })
  // await sleep(3);
}
function msgControl() {
  return new Promise((resolve) => {
    let time = $.getdata($.treeMsgTime) * 1;
    time ++;
    $.setdata(`${time}`, $.treeMsgTime);
    resolve();
  })
}
async function stealFriendFruit() {
  await friendRank();
  if ($.friendRankList && $.friendRankList.length > 0) {
    const canSteal = $.friendRankList.some((item) => {
      const boxShareCode = item.steal
      return (boxShareCode === true);
    });
    if (canSteal) {
      $.amount = 0;
      for (let item of $.friendRankList) {
        if (!item.self && item.steal) {
          await friendTreeRoom(item.encryPin);
          const stealFruitRes = await stealFruit(item.encryPin, $.friendTree.stoleInfo);
          if (stealFruitRes && stealFruitRes.resultCode === 0 && stealFruitRes.resultData.code === '200') {
            $.amount += stealFruitRes.resultData.data.amount;
          }
        }
      }
      message += `【偷取好友金果】共${$.amount}个\n`;
    } else {
      console.log(`今日已偷过好友的金果了，暂无好友可偷，请明天再来\n`)
    }
  } else {
    console.log(`您暂无好友，故跳过`);
  }
}
//获取好友列表API
async function friendRank() {
  await $.wait(1000); //歇口气儿, 不然会报操作频繁
  const params = {
    "source": 2,
    "riskDeviceParam":{"eid":"","dt":"","ma":"","im":"","os":"","osv":"","ip":"","apid":"","ia":"","uu":"","cv":"","nt":"","at":"1","fp":"","token":""}
  }
  params.riskDeviceParam = JSON.stringify(params.riskDeviceParam);//这一步，不可省略，否则提交会报错（和login接口一样）
  return new Promise((resolve, reject) => {
    $.post(taskurl('friendRank', params), (err, resp, data) => {
      try {
        if (err) {
          console.log("\n摇钱树京东API请求失败 ‼️‼️");
          console.log(JSON.stringify(err));
          $.logErr(err);
        } else {
          if (data) {
            data = JSON.parse(data);
            $.friendRankList = data.resultData.data;
          } else {
            console.log(`京豆api返回数据为空，请检查自身原因`)
          }
        }
      } catch (eor) {
        $.msg("摇钱树-初始化个人信息" + eor.name + "‼️", JSON.stringify(eor), eor.message)
      } finally {
        resolve()
      }
    })
  })
}
// 进入好友房间API
async function friendTreeRoom(friendPin) {
  await $.wait(1000); //歇口气儿, 不然会报操作频繁
  const params = {
    "source": 2,
    "friendPin": friendPin,
    "riskDeviceParam":{"eid":"","dt":"","ma":"","im":"","os":"","osv":"","ip":"","apid":"","ia":"","uu":"","cv":"","nt":"","at":"1","fp":"","token":""}
  }
  params.riskDeviceParam = JSON.stringify(params.riskDeviceParam);//这一步，不可省略，否则提交会报错（和login接口一样）
  return new Promise((resolve, reject) => {
    $.post(taskurl('friendTree', params), (err, resp, data) => {
      try {
        if (err) {
          console.log("\n摇钱树京东API请求失败 ‼️‼️");
          console.log(JSON.stringify(err));
          $.logErr(err);
        } else {
          if (data) {
            data = JSON.parse(data);
            $.friendTree = data.resultData.data;
          } else {
            console.log(`京豆api返回数据为空，请检查自身原因`)
          }
        }
      } catch (eor) {
        $.msg("摇钱树-初始化个人信息" + eor.name + "‼️", JSON.stringify(eor), eor.message)
      } finally {
        resolve()
      }
    })
  })
}
//偷好友金果API
async function stealFruit(friendPin, stoleId) {
  await $.wait(1000); //歇口气儿, 不然会报操作频繁
  const params = {
    "source": 2,
    "friendPin": friendPin,
    "stoleId": stoleId,
    "riskDeviceParam":{"eid":"","dt":"","ma":"","im":"","os":"","osv":"","ip":"","apid":"","ia":"","uu":"","cv":"","nt":"","at":"1","fp":"","token":""}
  }
  params.riskDeviceParam = JSON.stringify(params.riskDeviceParam);//这一步，不可省略，否则提交会报错（和login接口一样）
  return new Promise((resolve, reject) => {
    $.post(taskurl('stealFruit', params), (err, resp, data) => {
      try {
        if (err) {
          console.log("\n摇钱树京东API请求失败 ‼️‼️");
          console.log(JSON.stringify(err));
          $.logErr(err);
        } else {
          if (data) {
            data = JSON.parse(data);
          } else {
            console.log(`京豆api返回数据为空，请检查自身原因`)
          }
        }
      } catch (eor) {
        $.msg("摇钱树-初始化个人信息" + eor.name + "‼️", JSON.stringify(eor), eor.message)
      } finally {
        resolve(data)
      }
    })
  })
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
async function request(function_id, body = {}) {
  await $.wait(1000); //歇口气儿, 不然会报操作频繁
  return new Promise((resolve, reject) => {
    $.post(taskurl(function_id,body), (err, resp, data) => {
      try {
        if (err) {
          console.log("\n摇钱树京东API请求失败 ‼️‼️");
          console.log(JSON.stringify(err));
          $.logErr(err);
        } else {
          if (data) {
            data = JSON.parse(data);
          } else {
            console.log(`京豆api返回数据为空，请检查自身原因`)
          }
        }
      } catch (eor) {
        $.msg("摇钱树-初始化个人信息" + eor.name + "‼️", JSON.stringify(eor), eor.message)
      } finally {
        resolve(data)
      }
    })
  })
}

function taskurl(function_id, body) {
  return {
    url: JD_API_HOST + '/' + function_id + '?_=' + new Date().getTime()*1000,
    body: `reqData=${function_id === 'harvest' || function_id === 'login' || function_id === 'signIndex' || function_id === 'signOne' || function_id === 'setUserLinkStatus' || function_id === 'dayWork' || function_id === 'getSignAward' || function_id === 'sell' || function_id === 'friendRank' || function_id === 'friendTree' || function_id === 'stealFruit' ? encodeURIComponent(JSON.stringify(body)) : JSON.stringify(body)}`,
    headers: {
      'Accept' : `application/json`,
      'Origin' : `https://uua.jr.jd.com`,
      'Accept-Encoding' : `gzip, deflate, br`,
      'Cookie' : cookie,
      'Content-Type' : `application/x-www-form-urlencoded;charset=UTF-8`,
      'Host' : `ms.jr.jd.com`,
      'Connection' : `keep-alive`,
      'User-Agent' : $.isNode() ? (process.env.JD_USER_AGENT ? process.env.JD_USER_AGENT : (require('./USER_AGENTS').USER_AGENT)) : ($.getdata('JDUA') ? $.getdata('JDUA') : "jdapp;iPhone;9.2.2;14.2;%E4%BA%AC%E4%B8%9C/9.2.2 CFNetwork/1206 Darwin/20.1.0"),
      'Referer' : `https://uua.jr.jd.com/uc-fe-wxgrowing/moneytree/index/?channel=yxhd&lng=113.325896&lat=23.204600&sid=2d98e88cf7d182f60d533476c2ce777w&un_area=19_1601_50258_51885`,
      'Accept-Language' : `zh-cn`
    }
  }
}
function jsonParse(str) {
  if (typeof str == "string") {
    try {
      return JSON.parse(str);
    } catch (e) {
      console.log(e);
      $.msg($.name, '', '请勿随意在BoxJs输入框修改内容\n建议通过脚本去获取cookie')
      return [];
    }
  }
}
// prettier-ignore
function Env(t,e){"undefined"!=typeof process&&JSON.stringify(process.env).indexOf("GITHUB")>-1&&process.exit(0);class s{constructor(t){this.env=t}send(t,e="GET"){t="string"==typeof t?{url:t}:t;let s=this.get;return"POST"===e&&(s=this.post),new Promise((e,i)=>{s.call(this,t,(t,s,r)=>{t?i(t):e(s)})})}get(t){return this.send.call(this.env,t)}post(t){return this.send.call(this.env,t,"POST")}}return new class{constructor(t,e){this.name=t,this.http=new s(this),this.data=null,this.dataFile="box.dat",this.logs=[],this.isMute=!1,this.isNeedRewrite=!1,this.logSeparator="\n",this.startTime=(new Date).getTime(),Object.assign(this,e),this.log("",`🔔${this.name}, 开始!`)}isNode(){return"undefined"!=typeof module&&!!module.exports}isQuanX(){return"undefined"!=typeof $task}isSurge(){return"undefined"!=typeof $httpClient&&"undefined"==typeof $loon}isLoon(){return"undefined"!=typeof $loon}toObj(t,e=null){try{return JSON.parse(t)}catch{return e}}toStr(t,e=null){try{return JSON.stringify(t)}catch{return e}}getjson(t,e){let s=e;const i=this.getdata(t);if(i)try{s=JSON.parse(this.getdata(t))}catch{}return s}setjson(t,e){try{return this.setdata(JSON.stringify(t),e)}catch{return!1}}getScript(t){return new Promise(e=>{this.get({url:t},(t,s,i)=>e(i))})}runScript(t,e){return new Promise(s=>{let i=this.getdata("@chavy_boxjs_userCfgs.httpapi");i=i?i.replace(/\n/g,"").trim():i;let r=this.getdata("@chavy_boxjs_userCfgs.httpapi_timeout");r=r?1*r:20,r=e&&e.timeout?e.timeout:r;const[o,h]=i.split("@"),n={url:`http://${h}/v1/scripting/evaluate`,body:{script_text:t,mock_type:"cron",timeout:r},headers:{"X-Key":o,Accept:"*/*"}};this.post(n,(t,e,i)=>s(i))}).catch(t=>this.logErr(t))}loaddata(){if(!this.isNode())return{};{this.fs=this.fs?this.fs:require("fs"),this.path=this.path?this.path:require("path");const t=this.path.resolve(this.dataFile),e=this.path.resolve(process.cwd(),this.dataFile),s=this.fs.existsSync(t),i=!s&&this.fs.existsSync(e);if(!s&&!i)return{};{const i=s?t:e;try{return JSON.parse(this.fs.readFileSync(i))}catch(t){return{}}}}}writedata(){if(this.isNode()){this.fs=this.fs?this.fs:require("fs"),this.path=this.path?this.path:require("path");const t=this.path.resolve(this.dataFile),e=this.path.resolve(process.cwd(),this.dataFile),s=this.fs.existsSync(t),i=!s&&this.fs.existsSync(e),r=JSON.stringify(this.data);s?this.fs.writeFileSync(t,r):i?this.fs.writeFileSync(e,r):this.fs.writeFileSync(t,r)}}lodash_get(t,e,s){const i=e.replace(/\[(\d+)\]/g,".$1").split(".");let r=t;for(const t of i)if(r=Object(r)[t],void 0===r)return s;return r}lodash_set(t,e,s){return Object(t)!==t?t:(Array.isArray(e)||(e=e.toString().match(/[^.[\]]+/g)||[]),e.slice(0,-1).reduce((t,s,i)=>Object(t[s])===t[s]?t[s]:t[s]=Math.abs(e[i+1])>>0==+e[i+1]?[]:{},t)[e[e.length-1]]=s,t)}getdata(t){let e=this.getval(t);if(/^@/.test(t)){const[,s,i]=/^@(.*?)\.(.*?)$/.exec(t),r=s?this.getval(s):"";if(r)try{const t=JSON.parse(r);e=t?this.lodash_get(t,i,""):e}catch(t){e=""}}return e}setdata(t,e){let s=!1;if(/^@/.test(e)){const[,i,r]=/^@(.*?)\.(.*?)$/.exec(e),o=this.getval(i),h=i?"null"===o?null:o||"{}":"{}";try{const e=JSON.parse(h);this.lodash_set(e,r,t),s=this.setval(JSON.stringify(e),i)}catch(e){const o={};this.lodash_set(o,r,t),s=this.setval(JSON.stringify(o),i)}}else s=this.setval(t,e);return s}getval(t){return this.isSurge()||this.isLoon()?$persistentStore.read(t):this.isQuanX()?$prefs.valueForKey(t):this.isNode()?(this.data=this.loaddata(),this.data[t]):this.data&&this.data[t]||null}setval(t,e){return this.isSurge()||this.isLoon()?$persistentStore.write(t,e):this.isQuanX()?$prefs.setValueForKey(t,e):this.isNode()?(this.data=this.loaddata(),this.data[e]=t,this.writedata(),!0):this.data&&this.data[e]||null}initGotEnv(t){this.got=this.got?this.got:require("got"),this.cktough=this.cktough?this.cktough:require("tough-cookie"),this.ckjar=this.ckjar?this.ckjar:new this.cktough.CookieJar,t&&(t.headers=t.headers?t.headers:{},void 0===t.headers.Cookie&&void 0===t.cookieJar&&(t.cookieJar=this.ckjar))}get(t,e=(()=>{})){t.headers&&(delete t.headers["Content-Type"],delete t.headers["Content-Length"]),this.isSurge()||this.isLoon()?(this.isSurge()&&this.isNeedRewrite&&(t.headers=t.headers||{},Object.assign(t.headers,{"X-Surge-Skip-Scripting":!1})),$httpClient.get(t,(t,s,i)=>{!t&&s&&(s.body=i,s.statusCode=s.status),e(t,s,i)})):this.isQuanX()?(this.isNeedRewrite&&(t.opts=t.opts||{},Object.assign(t.opts,{hints:!1})),$task.fetch(t).then(t=>{const{statusCode:s,statusCode:i,headers:r,body:o}=t;e(null,{status:s,statusCode:i,headers:r,body:o},o)},t=>e(t))):this.isNode()&&(this.initGotEnv(t),this.got(t).on("redirect",(t,e)=>{try{if(t.headers["set-cookie"]){const s=t.headers["set-cookie"].map(this.cktough.Cookie.parse).toString();s&&this.ckjar.setCookieSync(s,null),e.cookieJar=this.ckjar}}catch(t){this.logErr(t)}}).then(t=>{const{statusCode:s,statusCode:i,headers:r,body:o}=t;e(null,{status:s,statusCode:i,headers:r,body:o},o)},t=>{const{message:s,response:i}=t;e(s,i,i&&i.body)}))}post(t,e=(()=>{})){if(t.body&&t.headers&&!t.headers["Content-Type"]&&(t.headers["Content-Type"]="application/x-www-form-urlencoded"),t.headers&&delete t.headers["Content-Length"],this.isSurge()||this.isLoon())this.isSurge()&&this.isNeedRewrite&&(t.headers=t.headers||{},Object.assign(t.headers,{"X-Surge-Skip-Scripting":!1})),$httpClient.post(t,(t,s,i)=>{!t&&s&&(s.body=i,s.statusCode=s.status),e(t,s,i)});else if(this.isQuanX())t.method="POST",this.isNeedRewrite&&(t.opts=t.opts||{},Object.assign(t.opts,{hints:!1})),$task.fetch(t).then(t=>{const{statusCode:s,statusCode:i,headers:r,body:o}=t;e(null,{status:s,statusCode:i,headers:r,body:o},o)},t=>e(t));else if(this.isNode()){this.initGotEnv(t);const{url:s,...i}=t;this.got.post(s,i).then(t=>{const{statusCode:s,statusCode:i,headers:r,body:o}=t;e(null,{status:s,statusCode:i,headers:r,body:o},o)},t=>{const{message:s,response:i}=t;e(s,i,i&&i.body)})}}time(t,e=null){const s=e?new Date(e):new Date;let i={"M+":s.getMonth()+1,"d+":s.getDate(),"H+":s.getHours(),"m+":s.getMinutes(),"s+":s.getSeconds(),"q+":Math.floor((s.getMonth()+3)/3),S:s.getMilliseconds()};/(y+)/.test(t)&&(t=t.replace(RegExp.$1,(s.getFullYear()+"").substr(4-RegExp.$1.length)));for(let e in i)new RegExp("("+e+")").test(t)&&(t=t.replace(RegExp.$1,1==RegExp.$1.length?i[e]:("00"+i[e]).substr((""+i[e]).length)));return t}msg(e=t,s="",i="",r){const o=t=>{if(!t)return t;if("string"==typeof t)return this.isLoon()?t:this.isQuanX()?{"open-url":t}:this.isSurge()?{url:t}:void 0;if("object"==typeof t){if(this.isLoon()){let e=t.openUrl||t.url||t["open-url"],s=t.mediaUrl||t["media-url"];return{openUrl:e,mediaUrl:s}}if(this.isQuanX()){let e=t["open-url"]||t.url||t.openUrl,s=t["media-url"]||t.mediaUrl;return{"open-url":e,"media-url":s}}if(this.isSurge()){let e=t.url||t.openUrl||t["open-url"];return{url:e}}}};if(this.isMute||(this.isSurge()||this.isLoon()?$notification.post(e,s,i,o(r)):this.isQuanX()&&$notify(e,s,i,o(r))),!this.isMuteLog){let t=["","==============📣系统通知📣=============="];t.push(e),s&&t.push(s),i&&t.push(i),console.log(t.join("\n")),this.logs=this.logs.concat(t)}}log(...t){t.length>0&&(this.logs=[...this.logs,...t]),console.log(t.join(this.logSeparator))}logErr(t,e){const s=!this.isSurge()&&!this.isQuanX()&&!this.isLoon();s?this.log("",`❗️${this.name}, 错误!`,t.stack):this.log("",`❗️${this.name}, 错误!`,t)}wait(t){return new Promise(e=>setTimeout(e,t))}done(t={}){const e=(new Date).getTime(),s=(e-this.startTime)/1e3;this.log("",`🔔${this.name}, 结束! 🕛 ${s} 秒`),this.log(),(this.isSurge()||this.isQuanX()||this.isLoon())&&$done(t)}}(t,e)}
