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


进店领豆,每天可拿四京豆
活动入口：京东APP首页-领京豆-进店领豆
更新时间：2020-11-03


===============Quantumultx===============
[task_local]
#进店领豆
10 0 * * * https://gitee.com/lxk0301/jd_scripts/raw/master/jd_shop.js, tag=进店领豆, img-url=https://raw.githubusercontent.com/58xinian/icon/master/jd_shop.png, enabled=true
================Loon============
[Script]
cron "10 0 * * *" script-path=https://gitee.com/lxk0301/jd_scripts/raw/master/jd_shop.js,tag=进店领豆
==============Surge===============
[Script]
进店领豆 = type=cron,cronexp="10 0 * * *",wake-system=1,timeout=3600,script-path=https://gitee.com/lxk0301/jd_scripts/raw/master/jd_shop.js
*/
const $ = new Env('进店领豆');
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
let message = '', subTitle = '';

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
      await jdShop();
    }
  }
})()
    .catch((e) => {
      $.log('', `❌ ${$.name}, 失败! 原因: ${e}!`, '')
    })
    .finally(() => {
      $.done();
    })
async function jdShop() {
  const taskData = await getTask();
  if (taskData.code === '0') {
    if (!taskData.data.taskList) {
      console.log(`${taskData.data.taskErrorTips}\n`);
      $.msg($.name, '', `京东账号 ${$.index} ${$.nickName}\n${taskData.data.taskErrorTips}`);
    } else {
      const { taskList } = taskData.data;
      let beanCount = 0;
      for (let item of taskList) {
        if (item.taskStatus === 3) {
          console.log(`${item.shopName} 已拿到2京豆\n`)
        } else {
          console.log(`taskId::${item.taskId}`)
          const doTaskRes = await doTask(item.taskId);
          if (doTaskRes.code === '0') {
            beanCount += 2;
          }
        }
      }
      console.log(`beanCount::${beanCount}`);
      if (beanCount > 0) {
        $.msg($.name, '', `京东账号 ${$.index} ${$.nickName}\n成功领取${beanCount}京豆`);
        // if ($.isNode()) {
        //   await notify.sendNotify(`${$.name} - 账号${$.index} - ${$.nickName}`, `京东账号${$.index} ${UserName}\n成功领取${beanCount}京豆`);
        // }
        // if ($.isNode()) {
        //   await notify.BarkNotify(`${$.name}`, `京东账号${$.index} ${UserName}\n成功领取${beanCount}京豆`);
        // }
      }
    }
  }
}
function doTask(taskId) {
  console.log(`doTask-taskId::${taskId}`)
  return new Promise(resolve => {
    const body = { 'taskId': `${taskId}` };
    const options = {
      url: `${JD_API_HOST}`,
      body: `functionId=takeTask&body=${escape(JSON.stringify(body))}&appid=ld`,
      headers: {
        'User-Agent': $.isNode() ? (process.env.JD_USER_AGENT ? process.env.JD_USER_AGENT : (require('./USER_AGENTS').USER_AGENT)) : ($.getdata('JDUA') ? $.getdata('JDUA') : "jdapp;iPhone;9.2.2;14.2;%E4%BA%AC%E4%B8%9C/9.2.2 CFNetwork/1206 Darwin/20.1.0"),
        'Host': 'api.m.jd.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': cookie,
      }
    }
    $.post(options, (err, resp, data) => {
      try {
        if (err) {
          console.log('\n进店领豆: API查询请求失败 ‼️‼️')
          $.logErr(err);
        } else {
          // console.log(data)
          data = JSON.parse(data);
        }
      } catch (e) {
        $.logErr(e, resp);
      } finally {
        resolve(data);
      }
    })
  })
}
function getTask(body = {}) {
 return new Promise(resolve => {
   const options = {
     url: `${JD_API_HOST}`,
     body: `functionId=queryTaskIndex&body=${escape(JSON.stringify(body))}&appid=ld`,
     headers: {
       'User-Agent': $.isNode() ? (process.env.JD_USER_AGENT ? process.env.JD_USER_AGENT : (require('./USER_AGENTS').USER_AGENT)) : ($.getdata('JDUA') ? $.getdata('JDUA') : "jdapp;iPhone;9.2.2;14.2;%E4%BA%AC%E4%B8%9C/9.2.2 CFNetwork/1206 Darwin/20.1.0"),
       'Host': 'api.m.jd.com',
       'Content-Type': 'application/x-www-form-urlencoded',
       'Cookie': cookie,
     }
   }
   $.post(options, (err, resp, data) => {
     try {
       if (err) {
         console.log('\n进店领豆: API查询请求失败 ‼️‼️')
         $.logErr(err);
       } else {
         // console.log(data)
         data = JSON.parse(data);
       }
     } catch (e) {
       $.logErr(e, resp);
     } finally {
       resolve(data);
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
