/*
 * @Author: shylocks https://github.com/shylocks
 * @Date: 2021-01-13 22:01:41
 * @Last Modified by:   shylocks
 * @Last Modified time: 2021-01-13 22:11:41
 */
/*
秒秒币
一天签到100币左右，100币可兑换1毛钱红包，推荐攒着配合农场一起用
活动时间：长期活动
更新地址：https://gitee.com/lxk0301/jd_scripts/raw/master/jd_ms.js


特鲁多在乔治·布朗学院的演讲
文章来源：未知 文章作者：enread 发布时间：2017-04-27 08:05 字体： [大 中 小]　 进入论坛
(单词翻译:双击或拖选)
Good morning, everyone. Thank you for coming out today.
 
Yesterday, as you all know, was the launch of our 2017 budget, and I'd like to say a few words about that before I take your questions.
 
We've delivered a budget that takes a realistic look at the challenges ahead. It reflects not only the financial realities but also the personal anxieties that so many Canadians are feeling, especially those in the middle class and those working hard to join it. I see a few of you smiling back there. You've heard me refer to the middle class before, perhaps. Maybe you think, as some of our critics have said, that this is just politicking1, just a slogan. And I want to tell you today, it's not just a slogan. These are real people we're talking about. Millions of Canadians who work hard, who struggle, who worry about their children and their parents and their livelihoods2 and who frankly3 need a break.
 
You might recall that I spent much of January on the road, meeting with Canadians in their communities. And one thing I heard over and over is that Canadians are worried about their future, their job opportunities, being able to pay their bills at the end of every month - expenses are increasing but their salaries are not.
 
In every community I visited, I met parents who worry about the kinds of opportunities their kids have or will not have when they graduate from school. That's what working Canadians - middle-class Canadians - are focused on and that's what we've focused on in this budget. To suggest that it's just politics does our fellow citizens a disservice. To dismiss their legitimate4 worries as mere5 feelings, even more so.
 
You can't spend any amount of time with Canadians, listen to them, actually hear them, and walk away thinking those feelings don't matter. They matter a lot to me, and to our government.
 
The level of confidence that Canadians have in their economic future is important, especially when it comes to getting a new job, making an offer on a house or buying a new car. As we celebrate our successes, we must also recognize that there are still many Canadians who are concerned about losing ground rather than getting ahead. Budget 2017 is focused on people, what they need to feel confident about their future. It gives Canadians the tools they need to build a better life for themselves, for their children and for their grandchildren.
 
That starts with making sure every Canadian can get the training they need to get a good, well-paying job. That's why Budget 2017 includes things like better support for lifelong learning. If you're unemployed6 or under-employed, this budget will give you better access to the training and financial support that can help you keep… find and keep a good job, including giving you the chance to go back to school without the fear of losing the EI benefits you need to put food on the table. If you currently have a job, but you want to go back to school part-time to upgrade your skills or get a new certification, this budget makes it easier for you to access Canada's Student Grants and Canada's Student Loans. If you're a student with a family to support, this budget makes it more affordable7 for you to improve your qualifications. As many as 13,000 students with dependent children will qualify for student grants under Budget 2017. And if you're a working adult who wants to get a new degree, diploma, or certificate like the ones offered here at George Brown, there's help for you, too. We're introducing a pilot project to look at new ways to make sure that Canada's Student Loans and Grants are more accessible so that your education can become more affordable.
 
Budget 2017 is, above all else, an investment in Canadians, an investment in people. Canada is home to some of the smartest, hardworking and most ambitious people in the world. With this budget, we are helping8 Canadians realize their dreams of a brighter, more secure future, and we'll all be better-off for it.



============Quantumultx===============
[task_local]
#京东秒秒币
10 7 * * * https://gitee.com/lxk0301/jd_scripts/raw/master/jd_ms.js, tag=京东秒秒币, img-url=https://raw.githubusercontent.com/yogayyy/Scripts/master/Icon/shylocks/jd_ms.jpg, enabled=true

================Loon==============
[Script]
cron "10 7 * * *" script-path=https://gitee.com/lxk0301/jd_scripts/raw/master/jd_ms.js,tag=京东秒秒币

===============Surge=================
京东秒秒币 = type=cron,cronexp="10 7 * * *",wake-system=1,timeout=200,script-path=https://gitee.com/lxk0301/jd_scripts/raw/master/jd_ms.js

============小火箭=========
京东秒秒币 = type=cron,script-path=https://gitee.com/lxk0301/jd_scripts/raw/master/jd_ms.js, cronexpr="10 7 * * *", timeout=200, enable=true
 */
const $ = new Env('京东秒秒币');

const notify = $.isNode() ? require('./sendNotify') : '';
//Node.js用户请在jdCookie.js处填写京东ck;
const jdCookieNode = $.isNode() ? require('./jdCookie.js') : '';
//IOS等用户直接用NobyDa的jd cookie
let cookiesArr = [], cookie = '', message;
if ($.isNode()) {
  Object.keys(jdCookieNode).forEach((item) => {
    cookiesArr.push(jdCookieNode[item])
  })
  if (process.env.JD_DEBUG && process.env.JD_DEBUG === 'false') console.log = () => {
  };
  if(JSON.stringify(process.env).indexOf('GITHUB')>-1) process.exit(0)
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
!(async () => {
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
        $.msg($.name, `【提示】cookie已失效`, `京东账号${$.index} ${$.nickName || $.UserName}\n请重新登录获取\nhttps://bean.m.jd.com/`, {"open-url": "https://bean.m.jd.com/"});

        if ($.isNode()) {
          await notify.sendNotify(`${$.name}cookie已失效 - ${$.UserName}`, `京东账号${$.index} ${$.UserName}\n请重新登录获取cookie`);
        }
        continue
      }
      await jdMs()
    }
  }
})()
  .catch((e) => {
    $.log('', `❌ ${$.name}, 失败! 原因: ${e}!`, '')
  })
  .finally(() => {
    $.done();
  })

async function jdMs() {
  $.score = 0
  await getActInfo()
  await getUserInfo()
  $.cur = $.score
  if ($.encryptProjectId) {
    await getTaskList()
  }
  await getUserInfo(false)
  await showMsg()
}

function getActInfo() {
  return new Promise(resolve => {
    $.post(taskPostUrl('assignmentList', {}, 'appid=jwsp'), (err, resp, data) => {
      try {
        if (err) {
          console.log(`${err},${jsonParse(resp.body)['message']}`)
          console.log(`${$.name} API请求失败，请检查网路重试`)
        } else {
          if (safeGet(data)) {
            data = JSON.parse(data)
            if (data.code === 200) {
              $.encryptProjectId = data.result.assignmentResult.encryptProjectId
              console.log(`活动名称：${data.result.assignmentResult.projectName}`)
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
function getUserInfo(info=true) {
  return new Promise(resolve => {
    $.post(taskPostUrl('homePageV2', {}, 'appid=SecKill2020'), (err, resp, data) => {
      try {
        if (err) {
          console.log(`${err},${jsonParse(resp.body)['message']}`)
          console.log(`${$.name} API请求失败，请检查网路重试`)
        } else {
          if (safeGet(data)) {
            data = JSON.parse(data)
            if (data.code === 2041) {
              $.score = data.result.assignment.assignmentPoints || 0
              if(info) console.log(`当前秒秒币${$.score}`)
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
  let body = {"encryptProjectId": $.encryptProjectId, "sourceCode": "wh5"}
  return new Promise(resolve => {
    $.post(taskPostUrl('queryInteractiveInfo', body), async (err, resp, data) => {
      try {
        if (err) {
          console.log(`${err},${jsonParse(resp.body)['message']}`)
          console.log(`${$.name} API请求失败，请检查网路重试`)
        } else {
          if (safeGet(data)) {
            data = JSON.parse(data)
            $.risk = false
            if (data.code === '0') {
              for (let vo of data.assignmentList) {
                if($.risk) break
                if (vo['completionCnt'] < vo['assignmentTimesLimit']) {
                  if (vo['assignmentType'] === 1) {
                    for (let i = vo['completionCnt']; i < vo['assignmentTimesLimit']; ++i) {
                      console.log(`去做${vo['assignmentName']}任务：${i + 1}/${vo['assignmentTimesLimit']}`)
                      let body = {
                        "encryptAssignmentId": vo['encryptAssignmentId'],
                        "itemId": vo['ext'][vo['ext']['extraType']][i]['itemId'],
                        "actionType": 1,
                        "completionFlag": ""
                      }
                      await doTask(body)
                      await $.wait(vo['ext']['waitDuration'] * 1000 + 500)
                      body['actionType'] = 0
                      await doTask(body)
                    }
                  } else if (vo['assignmentType'] === 0) {
                    for (let i = vo['completionCnt']; i < vo['assignmentTimesLimit']; ++i) {
                      console.log(`去做${vo['assignmentName']}任务：${i + 1}/${vo['assignmentTimesLimit']}`)
                      let body = {
                        "encryptAssignmentId": vo['encryptAssignmentId'],
                        "itemId": "",
                        "actionType": "0",
                        "completionFlag": true
                      }
                      await doTask(body)
                      await $.wait(1000)
                    }
                  } else if (vo['assignmentType'] === 3) {
                    for (let i = vo['completionCnt']; i < vo['assignmentTimesLimit']; ++i) {
                      console.log(`去做${vo['assignmentName']}任务：${i + 1}/${vo['assignmentTimesLimit']}`)
                      let body = {
                        "encryptAssignmentId": vo['encryptAssignmentId'],
                        "itemId": vo['ext'][vo['ext']['extraType']][i]['itemId'],
                        "actionType": 0,
                        "completionFlag": ""
                      }
                      await doTask(body)
                      await $.wait(1000)
                    }
                  }
                }
              }
            } else {
              console.log(data)
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

function doTask(body) {
  body = {...body, "encryptProjectId": $.encryptProjectId, "sourceCode": "wh5", "ext": {}}
  return new Promise(resolve => {
    $.post(taskPostUrl('doInteractiveAssignment', body), (err, resp, data) => {
      try {
        if (err) {
          console.log(`${err},${jsonParse(resp.body)['message']}`)
          console.log(`${$.name} API请求失败，请检查网路重试`)
        } else {
          if (safeGet(data)) {
            data = JSON.parse(data)
            console.log(data.msg)
            if(data.msg==='风险等级未通过') $.risk =1
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

function showMsg() {
  return new Promise(resolve => {
    message += `本次运行获得秒秒币${$.score-$.cur}枚，共${$.score}枚`;
    $.msg($.name, '', `京东账号${$.index}${$.nickName}\n${message}`);
    resolve()
  })
}


function taskPostUrl(function_id, body = {}, extra = '', function_id2) {
  let url = `${JD_API_HOST}`;
  if (function_id2) {
    url += `?functionId=${function_id2}`;
  }
  return {
    url,
    body: `functionId=${function_id}&body=${escape(JSON.stringify(body))}&client=wh5&clientVersion=9.3.2&${extra}`,
    headers: {
      "Cookie": cookie,
      "origin": "https://h5.m.jd.com",
      "referer": "https://h5.m.jd.com/babelDiy/Zeus/2NUvze9e1uWf4amBhe1AV6ynmSuH/index.html",
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
