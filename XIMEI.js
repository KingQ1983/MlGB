/*
软件名称:西梅 微信扫码下载
更新时间：2021-05-25 @肥皂
脚本说明：西梅自动任务
脚本为自动完成西梅的阅读任务
5.25更新。加入视频任务。现在每天可撸2.05元。


扫码打开 https://ae01.alicdn.com/kf/U8c71c1ac1f47422788561b0be3d4ea2ah.jpg
微信扫码打开可领红包



本脚本以学习为主！
使用方法:打开西梅，首页推荐下拉刷新获得数据

TG电报群: https://t.me/hahaha8028

4.3更新西梅加入自动提现功能,不用再去微信提现了,请确保自己的账号已绑定微信
5.25更新加入视频任务
boxjs地址 :  

https://raw.githubusercontent.com/age174/-/main/feizao.box.json


西梅
圈X配置如下，其他软件自行测试，定时可以多设置几次，没任务会停止运行的
[task_local]
#西梅
20 9 * * * https://raw.githubusercontent.com/age174/-/main/ximei.js, tag=西梅, img-url=https://ae01.alicdn.com/kf/Ucd02ea79ef22473daf3576486d134509Q.jpg, enabled=true


[rewrite_local]
#西梅
https://app.hubonews.com/.+/articles/list url script-request-body https://raw.githubusercontent.com/age174/-/main/ximei.js



#loon
https://app.hubonews.com/.+/articles/list script-path=https://raw.githubusercontent.com/age174/-/main/ximei.js, requires-body=true, timeout=10, tag=西梅



#surge

西梅 = type=http-request,pattern=https://app.hubonews.com/.+/articles/list,requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/age174/-/main/ximei.js,script-update-interval=0




[MITM]
hostname = app.hubonews.com


*/

const $ = new Env('西梅');
let status;
status = (status = ($.getval("ximeistatus") || "1") ) > 1 ? `${status}` : ""; // 账号扩展字符
let ximeiurlArr = [], ximeihdArr = [],ximeicount = ''
let times = Math.round(Date.now())
let ximeiurl = $.getdata('ximeiurl')
let ximeihd = $.getdata('ximeihd')
let st = '@123hb#*^&xiMEI99'
let ximeikey = '',id = '',uid='',tid='',name='',uuid=''
!(async () => {
  if (typeof $request !== "undefined") {
    await ximeick()
   
  } else {ximeiurlArr.push($.getdata('ximeiurl'))
    ximeihdArr.push($.getdata('ximeihd'))
    let ximeicount = ($.getval('ximeicount') || '1');
  
  
  
  
  for (let i = 2; i <= ximeicount; i++) {
    ximeiurlArr.push($.getdata(`ximeiurl${i}`))
    ximeihdArr.push($.getdata(`ximeihd${i}`))
  }
  
  if ($.isNode()) {
   ximeihdArr=[];
if (process.env.XIMEIHD && process.env.XIMEIHD.indexOf('\n') > -1) 
   ximeihdArr = process.env.XIMEIHD.split('\n');
   else
ximeihdArr = process.env.XIMEIHD.split();
  }
  
  
    console.log(`------------- 共${ximeihdArr.length}个账号-------------\n`)
      for (let i = 0; i < ximeihdArr.length; i++) {
        if (ximeihdArr[i]) {
         
          ximeiurl = ximeiurlArr[i];
          ximeihd = ximeihd = JSON.stringify(ximeihdArr[i]);
          $.index = i + 1;
          console.log(`\n开始【西梅${$.index}】`)
          await ximei1()
          await ximeiid();
          await ximeixx()

  }
}}

})()
  .catch((e) => $.logErr(e))
  .finally(() => $.done())
//西梅数据获取


function ximeick() {
   if ($request.url.indexOf("list") > -1) {
 const ximeiurl = $request.url
  if(ximeiurl)     $.setdata(ximeiurl,`ximeiurl${status}`)
    $.log(ximeiurl)
  const ximeihd = JSON.stringify($request.headers)
        if(ximeihd)    $.setdata(ximeihd,`ximeihd${status}`)
$.log(ximeihd)
   $.msg($.name,"",'西梅'+`${status}` +'数据获取成功！')
  }
}



//西梅文章列表
function ximei1(timeout = 0) {
  return new Promise((resolve) => {
    setTimeout( ()=>{
     // if (typeof $.getdata('ximeihd') === "undefined") {
        //$.msg($.name,"",'请先获取西梅数据!😓',)
        //$.done()
     // }

let url = {
        url : "https://app.hubonews.com/v3/articles/list",
        headers : JSON.parse(ximeihd),
        body : `{"limit": 20,"page": 1}`,
}
      $.post(url, async (err, resp, data) => {
        try {
          //console.log(data)
    const result = JSON.parse(data)
        if(result.code == 0){
id = result.data[0].data.articleId
name = result.data[0].data.translatedTitle
        console.log(`\n西梅获取文章列表成功\n文章ID:${id}\n文章标题:${name}\n执行阅读任务`) 
await ximeiyd()
        
} else {
console.log('西梅获取用户信息失败 已停止当前账号运行!')

}
        } catch (e) {
          //$.logErr(e, resp);
        } finally {
          resolve()
        }
      })
    },timeout)
  })
}


//西梅用户id
function ximeiid(timeout = 0) {
  return new Promise((resolve) => {

let url = {
        url : "https://app.hubonews.com/v1/activity/tasks",
        headers : JSON.parse(ximeihd),
        
}
      $.get(url, async (err, resp, data) => {

        try {
    const result = JSON.parse(data)

        if(result.code == 0){
uuid = result.data.user_id
        console.log('\n西梅用户id获取成功:'+uuid+'执行视频任务')
   
        
      for (let i = 1; i < 21; i++) {
$.log('\n执行第'+i+'次视频任务,共20次')
        await $.wait(200);
        await ximeisp();
}
} else {
       console.log('\n西梅用户id失败  '+result.msg)
await $.wait(1000);
        await ximeipl();
}
   
        } catch (e) {
          //$.logErr(e, resp);
        } finally {
          resolve()
        }
    },timeout)
  })
}

//西梅任务视频
function ximeisp(timeout = 0) {
  return new Promise((resolve) => {

let url = {
        url : "http://app.qubiankeji.com:8084/callbacks/v1/reward",
        headers : JSON.parse(ximeihd),
       body :`{"positionId":"1391594488677285923","reward":true,"userKey":"${uuid}"}`,
}
      $.post(url, async (err, resp, data) => {

        try {
    

        if(resp.statusCode == 200){

        console.log('\n西梅视频观看成功')
        await $.wait(1000);
        
} else {
       console.log('\n西梅视频观看失败  '+data)
await $.wait(1000);
       
}
   
        } catch (e) {
          //$.logErr(e, resp);
        } finally {
          resolve()
        }
    },timeout)
  })
}

//西梅任务阅读
function ximeiyd(timeout = 0) {
  return new Promise((resolve) => {
tid = md5(`action_time=${times}&action_type=101&business_id=${id}&secret=${st}`)
let url = {
        url : "https://app.hubonews.com/v1/activity/points/update",
        headers : JSON.parse(ximeihd),
        body : `{"sign":"${tid}","action_time":${times},"business_id":"${id}","action_type": 101}`,
}
      $.post(url, async (err, resp, data) => {

        try {
    const result = JSON.parse(data)

        if(result.code == 0){

        console.log('\n西梅阅读成功,获得梅子:'+result.data.point)
        await $.wait(1000);
        await ximei1();
} else {
       console.log('\n西梅阅读失败  '+result.msg)
await $.wait(1000);
        
}
   
        } catch (e) {
          //$.logErr(e, resp);
        } finally {
          resolve()
        }
    },timeout)
  })
}



//西梅信息
function ximeixx(timeout = 0) {
  return new Promise((resolve) => {
let url = {
        url : "https://app.hubonews.com/v1/activity/tasks",
        headers : JSON.parse(ximeihd),
        
}
      $.get(url, async (err, resp, data) => {

        try {
    const result = JSON.parse(data)

        if(result.code == 0){

        console.log('\n西梅用户信息获取成功\n当前梅子:'+result.data.point+'\n当前金币:'+result.data.coin)
if(result.data.point >=100){
$.log('西梅-检测到当前梅子可提现,执行提现任务')
await ximeitx();
}
        
} else {
       console.log('\n西梅用户信息获取失败  '+result.msg)
}
   
        } catch (e) {
          //$.logErr(e, resp);
        } finally {
          resolve()
        }
    },timeout)
  })
}

//西梅任务提现
function ximeitx(timeout = 0) {
  return new Promise((resolve) => {

let url = {
        url : "https://app.hubonews.com/v1/credit/cashout/apply",
        headers : JSON.parse(ximeihd),
        body : `{"cashout_credits":100,"assets_type":0}`,
}
      $.post(url, async (err, resp, data) => {

        try {
    const result = JSON.parse(data)

        if(result.code == 0){

        console.log('\n西梅提现成功:'+result.data.order_status)

        
} else {
       console.log('\n西梅提现失败  '+result.msg)

}
   
        } catch (e) {
          //$.logErr(e, resp);
        } finally {
          resolve()
        }
    },timeout)
  })
}


//封装md5
function md5(a) {
    function b(a, b) {
        return a << b | a >>> 32 - b
    }

    function c(a, b) {
        var c, d, e, f, g;
        return e = 2147483648 & a,
            f = 2147483648 & b,
            c = 1073741824 & a,
            d = 1073741824 & b,
            g = (1073741823 & a) + (1073741823 & b),
            c & d ? 2147483648 ^ g ^ e ^ f : c | d ? 1073741824 & g ? 3221225472 ^ g ^ e ^ f : 1073741824 ^ g ^ e ^ f : g ^ e ^ f
    }

    function d(a, b, c) {
        return a & b | ~a & c
    }

    function e(a, b, c) {
        return a & c | b & ~c
    }

    function f(a, b, c) {
        return a ^ b ^ c
    }

    function g(a, b, c) {
        return b ^ (a | ~c)
    }

    function h(a, e, f, g, h, i, j) {
        return a = c(a, c(c(d(e, f, g), h), j)),
            c(b(a, i), e)
    }

    function i(a, d, f, g, h, i, j) {
        return a = c(a, c(c(e(d, f, g), h), j)),
            c(b(a, i), d)
    }

    function j(a, d, e, g, h, i, j) {
        return a = c(a, c(c(f(d, e, g), h), j)),
            c(b(a, i), d)
    }

    function k(a, d, e, f, h, i, j) {
        return a = c(a, c(c(g(d, e, f), h), j)),
            c(b(a, i), d)
    }

    function l(a) {
        for (var b, c = a.length, d = c + 8, e = (d - d % 64) / 64, f = 16 * (e + 1), g = new Array(f - 1), h = 0, i = 0; c > i;)
            b = (i - i % 4) / 4,
                h = i % 4 * 8,
                g[b] = g[b] | a.charCodeAt(i) << h,
                i++;
        return b = (i - i % 4) / 4,
            h = i % 4 * 8,
            g[b] = g[b] | 128 << h,
            g[f - 2] = c << 3,
            g[f - 1] = c >>> 29,
            g
    }

    function m(a) {
        var b, c, d = "", e = "";
        for (c = 0; 3 >= c; c++)
            b = a >>> 8 * c & 255,
                e = "0" + b.toString(16),
                d += e.substr(e.length - 2, 2);
        return d
    }

    function n(a) {
        a = a.replace(/\r\n/g, "\n");
        for (var b = "", c = 0; c < a.length; c++) {
            var d = a.charCodeAt(c);
            128 > d ? b += String.fromCharCode(d) : d > 127 && 2048 > d ? (b += String.fromCharCode(d >> 6 | 192),
                b += String.fromCharCode(63 & d | 128)) : (b += String.fromCharCode(d >> 12 | 224),
                b += String.fromCharCode(d >> 6 & 63 | 128),
                b += String.fromCharCode(63 & d | 128))
        }
        return b
    }

    var o, p, q, r, s, t, u, v, w, x = [], y = 7, z = 12, A = 17, B = 22, C = 5, D = 9, E = 14, F = 20, G = 4, H = 11,
        I = 16, J = 23, K = 6, L = 10, M = 15, N = 21;
    for (a = n(a),
             x = l(a),
             t = 1732584193,
             u = 4023233417,
             v = 2562383102,
             w = 271733878,
             o = 0; o < x.length; o += 16)
        p = t,
            q = u,
            r = v,
            s = w,
            t = h(t, u, v, w, x[o + 0], y, 3614090360),
            w = h(w, t, u, v, x[o + 1], z, 3905402710),
            v = h(v, w, t, u, x[o + 2], A, 606105819),
            u = h(u, v, w, t, x[o + 3], B, 3250441966),
            t = h(t, u, v, w, x[o + 4], y, 4118548399),
            w = h(w, t, u, v, x[o + 5], z, 1200080426),
            v = h(v, w, t, u, x[o + 6], A, 2821735955),
            u = h(u, v, w, t, x[o + 7], B, 4249261313),
            t = h(t, u, v, w, x[o + 8], y, 1770035416),
            w = h(w, t, u, v, x[o + 9], z, 2336552879),
            v = h(v, w, t, u, x[o + 10], A, 4294925233),
            u = h(u, v, w, t, x[o + 11], B, 2304563134),
            t = h(t, u, v, w, x[o + 12], y, 1804603682),
            w = h(w, t, u, v, x[o + 13], z, 4254626195),
            v = h(v, w, t, u, x[o + 14], A, 2792965006),
            u = h(u, v, w, t, x[o + 15], B, 1236535329),
            t = i(t, u, v, w, x[o + 1], C, 4129170786),
            w = i(w, t, u, v, x[o + 6], D, 3225465664),
            v = i(v, w, t, u, x[o + 11], E, 643717713),
            u = i(u, v, w, t, x[o + 0], F, 3921069994),
            t = i(t, u, v, w, x[o + 5], C, 3593408605),
            w = i(w, t, u, v, x[o + 10], D, 38016083),
            v = i(v, w, t, u, x[o + 15], E, 3634488961),
            u = i(u, v, w, t, x[o + 4], F, 3889429448),
            t = i(t, u, v, w, x[o + 9], C, 568446438),
            w = i(w, t, u, v, x[o + 14], D, 3275163606),
            v = i(v, w, t, u, x[o + 3], E, 4107603335),
            u = i(u, v, w, t, x[o + 8], F, 1163531501),
            t = i(t, u, v, w, x[o + 13], C, 2850285829),
            w = i(w, t, u, v, x[o + 2], D, 4243563512),
            v = i(v, w, t, u, x[o + 7], E, 1735328473),
            u = i(u, v, w, t, x[o + 12], F, 2368359562),
            t = j(t, u, v, w, x[o + 5], G, 4294588738),
            w = j(w, t, u, v, x[o + 8], H, 2272392833),
            v = j(v, w, t, u, x[o + 11], I, 1839030562),
            u = j(u, v, w, t, x[o + 14], J, 4259657740),
            t = j(t, u, v, w, x[o + 1], G, 2763975236),
            w = j(w, t, u, v, x[o + 4], H, 1272893353),
            v = j(v, w, t, u, x[o + 7], I, 4139469664),
            u = j(u, v, w, t, x[o + 10], J, 3200236656),
            t = j(t, u, v, w, x[o + 13], G, 681279174),
            w = j(w, t, u, v, x[o + 0], H, 3936430074),
            v = j(v, w, t, u, x[o + 3], I, 3572445317),
            u = j(u, v, w, t, x[o + 6], J, 76029189),
            t = j(t, u, v, w, x[o + 9], G, 3654602809),
            w = j(w, t, u, v, x[o + 12], H, 3873151461),
            v = j(v, w, t, u, x[o + 15], I, 530742520),
            u = j(u, v, w, t, x[o + 2], J, 3299628645),
            t = k(t, u, v, w, x[o + 0], K, 4096336452),
            w = k(w, t, u, v, x[o + 7], L, 1126891415),
            v = k(v, w, t, u, x[o + 14], M, 2878612391),
            u = k(u, v, w, t, x[o + 5], N, 4237533241),
            t = k(t, u, v, w, x[o + 12], K, 1700485571),
            w = k(w, t, u, v, x[o + 3], L, 2399980690),
            v = k(v, w, t, u, x[o + 10], M, 4293915773),
            u = k(u, v, w, t, x[o + 1], N, 2240044497),
            t = k(t, u, v, w, x[o + 8], K, 1873313359),
            w = k(w, t, u, v, x[o + 15], L, 4264355552),
            v = k(v, w, t, u, x[o + 6], M, 2734768916),
            u = k(u, v, w, t, x[o + 13], N, 1309151649),
            t = k(t, u, v, w, x[o + 4], K, 4149444226),
            w = k(w, t, u, v, x[o + 11], L, 3174756917),
            v = k(v, w, t, u, x[o + 2], M, 718787259),
            u = k(u, v, w, t, x[o + 9], N, 3951481745),
            t = c(t, p),
            u = c(u, q),
            v = c(v, r),
            w = c(w, s);
    var O = m(t) + m(u) + m(v) + m(w);
    return O.toLowerCase()
}


function Env(t,e){class s{constructor(t){this.env=t}send(t,e="GET"){t="string"==typeof t?{url:t}:t;let s=this.get;return"POST"===e&&(s=this.post),new Promise((e,i)=>{s.call(this,t,(t,s,r)=>{t?i(t):e(s)})})}get(t){return this.send.call(this.env,t)}post(t){return this.send.call(this.env,t,"POST")}}return new class{constructor(t,e){this.name=t,this.http=new s(this),this.data=null,this.dataFile="box.dat",this.logs=[],this.isMute=!1,this.isNeedRewrite=!1,this.logSeparator="\n",this.startTime=(new Date).getTime(),Object.assign(this,e),this.log("",`\ud83d\udd14${this.name}, \u5f00\u59cb!`)}isNode(){return"undefined"!=typeof module&&!!module.exports}isQuanX(){return"undefined"!=typeof $task}isSurge(){return"undefined"!=typeof $httpClient&&"undefined"==typeof $loon}isLoon(){return"undefined"!=typeof $loon}toObj(t,e=null){try{return JSON.parse(t)}catch{return e}}toStr(t,e=null){try{return JSON.stringify(t)}catch{return e}}getjson(t,e){let s=e;const i=this.getdata(t);if(i)try{s=JSON.parse(this.getdata(t))}catch{}return s}setjson(t,e){try{return this.setdata(JSON.stringify(t),e)}catch{return!1}}getScript(t){return new Promise(e=>{this.get({url:t},(t,s,i)=>e(i))})}runScript(t,e){return new Promise(s=>{let i=this.getdata("@chavy_boxjs_userCfgs.httpapi");i=i?i.replace(/\n/g,"").trim():i;let r=this.getdata("@chavy_boxjs_userCfgs.httpapi_timeout");r=r?1*r:20,r=e&&e.timeout?e.timeout:r;const[o,h]=i.split("@"),a={url:`http://${h}/v1/scripting/evaluate`,body:{script_text:t,mock_type:"cron",timeout:r},headers:{"X-Key":o,Accept:"*/*"}};this.post(a,(t,e,i)=>s(i))}).catch(t=>this.logErr(t))}loaddata(){if(!this.isNode())return{};{this.fs=this.fs?this.fs:require("fs"),this.path=this.path?this.path:require("path");const t=this.path.resolve(this.dataFile),e=this.path.resolve(process.cwd(),this.dataFile),s=this.fs.existsSync(t),i=!s&&this.fs.existsSync(e);if(!s&&!i)return{};{const i=s?t:e;try{return JSON.parse(this.fs.readFileSync(i))}catch(t){return{}}}}}writedata(){if(this.isNode()){this.fs=this.fs?this.fs:require("fs"),this.path=this.path?this.path:require("path");const t=this.path.resolve(this.dataFile),e=this.path.resolve(process.cwd(),this.dataFile),s=this.fs.existsSync(t),i=!s&&this.fs.existsSync(e),r=JSON.stringify(this.data);s?this.fs.writeFileSync(t,r):i?this.fs.writeFileSync(e,r):this.fs.writeFileSync(t,r)}}lodash_get(t,e,s){const i=e.replace(/\[(\d+)\]/g,".$1").split(".");let r=t;for(const t of i)if(r=Object(r)[t],void 0===r)return s;return r}lodash_set(t,e,s){return Object(t)!==t?t:(Array.isArray(e)||(e=e.toString().match(/[^.[\]]+/g)||[]),e.slice(0,-1).reduce((t,s,i)=>Object(t[s])===t[s]?t[s]:t[s]=Math.abs(e[i+1])>>0==+e[i+1]?[]:{},t)[e[e.length-1]]=s,t)}getdata(t){let e=this.getval(t);if(/^@/.test(t)){const[,s,i]=/^@(.*?)\.(.*?)$/.exec(t),r=s?this.getval(s):"";if(r)try{const t=JSON.parse(r);e=t?this.lodash_get(t,i,""):e}catch(t){e=""}}return e}setdata(t,e){let s=!1;if(/^@/.test(e)){const[,i,r]=/^@(.*?)\.(.*?)$/.exec(e),o=this.getval(i),h=i?"null"===o?null:o||"{}":"{}";try{const e=JSON.parse(h);this.lodash_set(e,r,t),s=this.setval(JSON.stringify(e),i)}catch(e){const o={};this.lodash_set(o,r,t),s=this.setval(JSON.stringify(o),i)}}else s=this.setval(t,e);return s}getval(t){return this.isSurge()||this.isLoon()?$persistentStore.read(t):this.isQuanX()?$prefs.valueForKey(t):this.isNode()?(this.data=this.loaddata(),this.data[t]):this.data&&this.data[t]||null}setval(t,e){return this.isSurge()||this.isLoon()?$persistentStore.write(t,e):this.isQuanX()?$prefs.setValueForKey(t,e):this.isNode()?(this.data=this.loaddata(),this.data[e]=t,this.writedata(),!0):this.data&&this.data[e]||null}initGotEnv(t){this.got=this.got?this.got:require("got"),this.cktough=this.cktough?this.cktough:require("tough-cookie"),this.ckjar=this.ckjar?this.ckjar:new this.cktough.CookieJar,t&&(t.headers=t.headers?t.headers:{},void 0===t.headers.Cookie&&void 0===t.cookieJar&&(t.cookieJar=this.ckjar))}get(t,e=(()=>{})){t.headers&&(delete t.headers["Content-Type"],delete t.headers["Content-Length"]),this.isSurge()||this.isLoon()?(this.isSurge()&&this.isNeedRewrite&&(t.headers=t.headers||{},Object.assign(t.headers,{"X-Surge-Skip-Scripting":!1})),$httpClient.get(t,(t,s,i)=>{!t&&s&&(s.body=i,s.statusCode=s.status),e(t,s,i)})):this.isQuanX()?(this.isNeedRewrite&&(t.opts=t.opts||{},Object.assign(t.opts,{hints:!1})),$task.fetch(t).then(t=>{const{statusCode:s,statusCode:i,headers:r,body:o}=t;e(null,{status:s,statusCode:i,headers:r,body:o},o)},t=>e(t))):this.isNode()&&(this.initGotEnv(t),this.got(t).on("redirect",(t,e)=>{try{if(t.headers["set-cookie"]){const s=t.headers["set-cookie"].map(this.cktough.Cookie.parse).toString();this.ckjar.setCookieSync(s,null),e.cookieJar=this.ckjar}}catch(t){this.logErr(t)}}).then(t=>{const{statusCode:s,statusCode:i,headers:r,body:o}=t;e(null,{status:s,statusCode:i,headers:r,body:o},o)},t=>{const{message:s,response:i}=t;e(s,i,i&&i.body)}))}post(t,e=(()=>{})){if(t.body&&t.headers&&!t.headers["Content-Type"]&&(t.headers["Content-Type"]="application/x-www-form-urlencoded"),t.headers&&delete t.headers["Content-Length"],this.isSurge()||this.isLoon())this.isSurge()&&this.isNeedRewrite&&(t.headers=t.headers||{},Object.assign(t.headers,{"X-Surge-Skip-Scripting":!1})),$httpClient.post(t,(t,s,i)=>{!t&&s&&(s.body=i,s.statusCode=s.status),e(t,s,i)});else if(this.isQuanX())t.method="POST",this.isNeedRewrite&&(t.opts=t.opts||{},Object.assign(t.opts,{hints:!1})),$task.fetch(t).then(t=>{const{statusCode:s,statusCode:i,headers:r,body:o}=t;e(null,{status:s,statusCode:i,headers:r,body:o},o)},t=>e(t));else if(this.isNode()){this.initGotEnv(t);const{url:s,...i}=t;this.got.post(s,i).then(t=>{const{statusCode:s,statusCode:i,headers:r,body:o}=t;e(null,{status:s,statusCode:i,headers:r,body:o},o)},t=>{const{message:s,response:i}=t;e(s,i,i&&i.body)})}}time(t){let e={"M+":(new Date).getMonth()+1,"d+":(new Date).getDate(),"H+":(new Date).getHours(),"m+":(new Date).getMinutes(),"s+":(new Date).getSeconds(),"q+":Math.floor(((new Date).getMonth()+3)/3),S:(new Date).getMilliseconds()};/(y+)/.test(t)&&(t=t.replace(RegExp.$1,((new Date).getFullYear()+"").substr(4-RegExp.$1.length)));for(let s in e)new RegExp("("+s+")").test(t)&&(t=t.replace(RegExp.$1,1==RegExp.$1.length?e[s]:("00"+e[s]).substr((""+e[s]).length)));return t}msg(e=t,s="",i="",r){const o=t=>{if(!t)return t;if("string"==typeof t)return this.isLoon()?t:this.isQuanX()?{"open-url":t}:this.isSurge()?{url:t}:void 0;if("object"==typeof t){if(this.isLoon()){let e=t.openUrl||t.url||t["open-url"],s=t.mediaUrl||t["media-url"];return{openUrl:e,mediaUrl:s}}if(this.isQuanX()){let e=t["open-url"]||t.url||t.openUrl,s=t["media-url"]||t.mediaUrl;return{"open-url":e,"media-url":s}}if(this.isSurge()){let e=t.url||t.openUrl||t["open-url"];return{url:e}}}};this.isMute||(this.isSurge()||this.isLoon()?$notification.post(e,s,i,o(r)):this.isQuanX()&&$notify(e,s,i,o(r)));let h=["","==============\ud83d\udce3\u7cfb\u7edf\u901a\u77e5\ud83d\udce3=============="];h.push(e),s&&h.push(s),i&&h.push(i),console.log(h.join("\n")),this.logs=this.logs.concat(h)}log(...t){t.length>0&&(this.logs=[...this.logs,...t]),console.log(t.join(this.logSeparator))}logErr(t,e){const s=!this.isSurge()&&!this.isQuanX()&&!this.isLoon();s?this.log("",`\u2757\ufe0f${this.name}, \u9519\u8bef!`,t.stack):this.log("",`\u2757\ufe0f${this.name}, \u9519\u8bef!`,t)}wait(t){return new Promise(e=>setTimeout(e,t))}done(t={}){const e=(new Date).getTime(),s=(e-this.startTime)/1e3;this.log("",`\ud83d\udd14${this.name}, \u7ed3\u675f! \ud83d\udd5b ${s} \u79d2`),this.log(),(this.isSurge()||this.isQuanX()||this.isLoon())&&$done(t)}}(t,e)}
