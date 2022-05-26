# cretre by doubi 
# 通用模板

import asyncio
from time import time
import requests,json,random,os
from urllib.parse import quote_plus, unquote_plus
from functools import partial

print = partial(print, flush=True)

activatname = '邀新助力赢好礼'
helpNickName = 'Didiheyh'
helpUuid = '2fe7f41ef9454626b11e783c935a625d' # 助力码
activityUrl = f'https://lzkjdz-isv.isvjcloud.com/m/1000411104/99/2205100041110402/?activityId=2205100041110402&helpUuid={helpUuid}&helpNickName={helpNickName}'
shopid = '1000411104'

# 随机ua
def randomuserAgent():
    global uuid, addressid, iosVer, iosV, clientVersion, iPhone, area, ADID, lng, lat
    uuid = ''.join(random.sample(
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'z'], 40))
    addressid = ''.join(random.sample('1234567898647', 10))
    iosVer = ''.join(random.sample(["15.1.1", "14.5.1", "14.4", "14.3", "14.2", "14.1", "14.0.1"], 1))
    iosV = iosVer.replace('.', '_')
    clientVersion = ''.join(random.sample(["10.3.0", "10.2.7", "10.2.4"], 1))
    iPhone = ''.join(random.sample(["8", "9", "10", "11", "12", "13"], 1))
    area = ''.join(random.sample('0123456789', 2)) + '_' + ''.join(random.sample('0123456789', 4)) + '_' + ''.join(
        random.sample('0123456789', 5)) + '_' + ''.join(random.sample('0123456789', 4))
    ADID = ''.join(random.sample('0987654321ABCDEF', 8)) + '-' + ''.join(
        random.sample('0987654321ABCDEF', 4)) + '-' + ''.join(random.sample('0987654321ABCDEF', 4)) + '-' + ''.join(
        random.sample('0987654321ABCDEF', 4)) + '-' + ''.join(random.sample('0987654321ABCDEF', 12))
    lng = '119.31991256596' + str(random.randint(100, 999))
    lat = '26.1187118976' + str(random.randint(100, 999))
    UserAgent = ''
    if not UserAgent:
        return f'jdapp;iPhone;10.0.4;{iosVer};{uuid};network/wifi;ADID/{ADID};model/iPhone{iPhone},1;addressid/{addressid};appBuild/167707;jdSupportDarkMode/0;Mozilla/5.0 (iPhone; CPU iPhone OS {iosV} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/null;supportJDSHWK/1'
    else:
        return UserAgent


# 获取Token
async def get_Token(cookie):
    try:
        url = 'https://api.m.jd.com/client.action?functionId=isvObfuscator'
        headers = {
            'Host': 'api.m.jd.com',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie':cookie,
            'User-Agent': 'JD4iPhone/168014 (iPhone; iOS; Scale/3.00)'
    }
        body = 'body=%7B%22url%22%3A%22https%3A%5C/%5C/jyds-isv.isvjcloud.com%5C/page%5C/index-20220430.php?member_id%3D3403726%26nick%3DAAFiei4pADAchjH1pPrBRYE6Q_nM0XT9LL9wRMmHnIYD_PFd7zQUONjmMj_QFBeC3P6GG_R1Pvk%26activity_id%3D266%26invite_url_id%3D%26platform_open_id%3DhVVjbDOf6oEeoHnz7_ZNlSWLyOE9OkFDSTUKUEi-_qU%26_wvUseWKWebView%3DYES%26merchantNum%3D2000062%26instId%3D39%26type%3D0%26sid%3D8ff880cb962b7e7e49759bb3e43d52dw%26un_area%3D16_1332_1336_59151%22%2C%22id%22%3A%22%22%7D&build=168014&client=apple&clientVersion=10.4.6&d_brand=apple&d_model=iPhone13%2C1&ef=1&eid=eidI6bf3812088s3ecjXNJkaR3SsJLEP23h%2BVHnI2K9M5HaVE2J6h8REjD7tNeZy715QizBG1uMdEvb4GAs6HMG/Xyh2h6n4b%2BGp/Mb9zxqU9qnbwKhL&ep=%7B%22ciphertype%22%3A5%2C%22cipher%22%3A%7B%22screen%22%3A%22CJOyDIeyDNC2%22%2C%22wifiBssid%22%3A%22DtUyZtc4YwS0DJGnEJK0YtUnCQOyZtDuCtvtDWS3Y2Y%3D%22%2C%22osVersion%22%3A%22CJUkDG%3D%3D%22%2C%22area%22%3A%22CJZpCJCzCv8nCzC2XzU5CJUn%22%2C%22openudid%22%3A%22ZwO4ZQO4ZJDwDWU5YtqnYJc1DWC1CNZsD2PrY2YmYJu3DWU1YzSyDm%3D%3D%22%2C%22uuid%22%3A%22aQf1ZRdxb2r4ovZ1EJZhcxYlVNZSZz09%22%7D%2C%22ts%22%3A1652180385%2C%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22version%22%3A%221.0.3%22%2C%22appname%22%3A%22com.360buy.jdmobile%22%2C%22ridx%22%3A-1%7D&ext=%7B%22prstate%22%3A%220%22%2C%22pvcStu%22%3A%221%22%7D&isBackground=N&joycious=117&lang=zh_CN&networkType=wifi&networklibtype=JDNetworkBaseAF&partner=apple&rfs=0000&scope=10&sign=1d5341cdf68a364678682892ba61fa14&st=1652180391940&sv=120&uemps=0-0&uts=0f31TVRjBStTMMMVdx/6coevBdXhbSIifopQageUhS/zTLdcrpETDOhFP34L6Sn7mr5dwU7LXgIFptoCqDGwsTpV6R4rDNdE/pRXTMN0iZfG7yQTTWF/y0OarqJUWhs2cKKu081h288awnyStYFgK4rs9gRYLqhan4MYGECajSemqCAr%2Bgd%2BnTec5dgBOiLWd5Mbz7fTBA4ptdJ4xs%2Bj3Q%3D%3D'
        result = requests.post(url=url,headers=headers,data=body).text
        result_res = json.loads(result)
        if result_res['code'] == '0':
            return result_res['token']
        else:
            return False
    except Exception as f:
        print(f)


# 加入店铺会员
async def bindWithVender(ua,cookie,body):
    try:
        url = f'https://api.m.jd.com/client.action?appid=jd_shop_member&functionId=bindWithVender&body={json.dumps(body)}&clientVersion=9.2.0&uuid=88888&h5st=20220412164645241%3B3634d1aeada6d9cd11a7526a3a6ac63e%3B169f1%3Btk02wd66f1d7418nXuLjsmO3oJMCxUqKVwIf4q1WRptKRT3nJSrx01oYYBAylbSuyg4sipnEzyEJOZuFjfG2QERcBtzd%3B6b455234e93be4ec963cd7c575d70882b838ba588149a1f54b69c8d0dacf14da%3B3.0%3B1649753205241'
        header = {
            'Host': 'api.m.jd.com',
            'Cookie': cookie,
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'User-Agent': ua,
            'Referer': f'https://shopmember.m.jd.com/shopcard/?venderId={shopid}&channel=401&returnUrl={json.dumps(activityUrl)}',
        }
        response = requests.get(url=url,headers=header,timeout=10).text
        return json.loads(response)
    
    except Exception as e:
        if TimeoutError:
            return f'请求入会失败{e}'
        if IndexError:
            return response

# 检测ck状态
async def check(ua, ck):
    try:
        url = 'https://me-api.jd.com/user_new/info/GetJDUserInfoUnion'
        header = {
            "Host": "me-api.jd.com",
            "Accept": "*/*",
            "Connection": "keep-alive",
            "Cookie": ck,
            "User-Agent": ua,
            "Accept-Language": "zh-cn",
            "Referer": "https://home.m.jd.com/myJd/newhome.action?sceneval=2&ufc=&",
            "Accept-Encoding": "gzip, deflate",
        }
        result = requests.get(url=url, headers=header).text
        codestate = json.loads(result)
        if codestate['retcode'] == '1001':
            msg = "当前ck已失效，请检查"
            return {'code': 1001, 'data': msg}
        elif codestate['retcode'] == '0' and 'userInfo' in codestate['data']:
            nickName = codestate['data']['userInfo']['baseInfo']['nickname']
            return {'code': 200, 'name': nickName, 'ck': ck}
    except Exception as e:
        return {'code': 0, 'data': e}

async def lztoken(ua):
    url = 'https://lzkjdz-isv.isvjcloud.com/wxCommonInfo/token'
    headers ={
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'lzkjdz-isv.isvjcloud.com',
    'Referer': activityUrl,
    'User-Agent': ua
    }
    response = requests.get(url=url,headers=headers,timeout=30).text
    response_res = json.loads(response)
    if response_res['result']:
        LZ_TOKEN_KEY = response_res['data']['LZ_TOKEN_KEY']
        LZ_TOKEN_VALUE = response_res['data']['LZ_TOKEN_VALUE']
        return f"LZ_TOKEN_KEY={LZ_TOKEN_KEY};LZ_TOKEN_VALUE={LZ_TOKEN_VALUE};"
    else:
        None

# 获取 getMyping
async def get_myping(ua,Cookie,token):
    url = 'https://lzkjdz-isv.isvjcloud.com/customer/getMyPing'
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': Cookie,
    'Host': 'lzkjdz-isv.isvjcloud.com',
    'Origin': 'https://lzkjdz-isv.isvjcloud.com',
    'Referer': activityUrl,
    'User-Agent': ua,
    'X-Requested-With': 'XMLHttpRequest',
    }
    data = f'token={token}&fromType=APP&userId={shopid}&pin='
    result = requests.post(url=url,headers=headers,data=data,timeout=30).text
    return json.loads(result)

# 获取 getSimpleActInfoVo
async def getSimpleActInfoVo(ua,cookie):
    url = 'https://lzkjdz-isv.isvjcloud.com/common/brand/getSimpleActInfoVo?activityId=2205100041110402'
    hedaers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': cookie,
        'Host': 'lzkjdz-isv.isvjcloud.com',
        'Referer': activityUrl,
        'User-Agent': ua
    }
    result = requests.get(url=url,headers=hedaers,timeout=10).text
    return json.loads(result)

# 获取 ad
async def accessLogWithAD(ua,Cookie,pin,activityId):
    url = 'https://lzkjdz-isv.isvjcloud.com/common/accessLogWithAD'
    headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-cn',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': Cookie,
    'Host': 'lzkjdz-isv.isvjcloud.com',
    'Origin': 'https://lzkjdz-isv.isvjcloud.com',
    'Referer': activityUrl,
    'User-Agent': ua,
    'X-Requested-With': 'XMLHttpRequest'
    }
    body = f'venderId={shopid}&code=99&pin={pin}&activityId={activityId}&pageUrl={activityUrl}&subType=app&adSource=null'
    result = requests.post(url=url,headers=headers,data=body,timeout=30).text
    return result

async def content(ua,Cookie,activityId,pin):
    url = 'https://lzkjdz-isv.isvjcloud.com/jomalone/invite/activityContent'
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'zh-cn',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        "Cookie":Cookie,
        'Host': 'lzkjdz-isv.isvjcloud.com',
        'Origin': 'https://lzkjdz-isv.isvjcloud.com',
        'Referer': activityUrl,
        'User-Agent': ua,
    }
    body = f'activityId={activityId}&helpUuid={helpUuid}&pin={pin}'
    result = requests.post(url=url,headers=headers,data=body,timeout=30)
    return json.loads((result.text))


async def crmCard(ua,cookie,activityId,pin):
    url = 'https://lzkjdz-isv.isvjcloud.com/crmCard/common/coupon/getOpenCardStatusWithOutSelf'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': cookie,
        'Host': 'lzkjdz-isv.isvjcloud.com',
        'Referer': activityUrl,
        'User-Agent': ua
    }
    body = f'venderId={shopid}&activityId={activityId}&pin={pin}'   
    result = requests.post(url=url,headers=headers,data=body,timeout=30)
    return json.loads((result.text))

async def main():
    try:
        cks = os.environ["JD_COOKIE"].split("&")
    except:
        f = open("cklist.txt", "r", encoding='utf-8')
        cks = f.read().split('\n')
        f.close()
        
    print(f'=============== 共{len(cks)}个京东账号Cookie ===============')
    success = 0
    for ck in cks:
        ua = randomuserAgent()
        result = await check(ua, ck) # 检测ck
        if result['code'] == 200:
            token = await get_Token(ck)
            cookie = await lztoken(ua)
            myping = await get_myping(ua,cookie,token)
            if myping['result']:
                nickname = myping['data']['nickname']
                pin = quote_plus(myping['data']['secretPin'])
                result = await getSimpleActInfoVo(ua,cookie)
                if result['result']:
                    actName = result['data']['actName']
                    activityId = result['data']['activityId']
                    await asyncio.sleep(1)
                    print(f'您好{nickname},已开启{actName}活动')
                    await accessLogWithAD(ua,cookie,pin,activityId)
                    print('京东没有返回任务东西')
                    await asyncio.sleep(1)
                    await content(ua,cookie,activityId,pin)
                    result = await crmCard(ua,cookie,activityId,pin)
                    if result['openCard']==False:
                        print('您还不是会员哦，快去开卡助力好友咯')
                        await asyncio.sleep(1)
                        ruhui = await bindWithVender(ua,ck,{"venderId":str(shopid),"bindByVerifyCodeFlag":1,"registerExtend":{},"writeChildFlag":0,"channel":7035})
                        print(ruhui)
                        cookie = await lztoken(ua)
                        result = await crmCard(ua,cookie,activityId,pin)
                        print(result)
                        await content(ua,cookie,activityId,pin)
                        success += 1
                        print(f'助力成功，当前助力{success}次')
                        await asyncio.sleep(5)
                    else:
                        print('您已经是会员了无法助力好友了')
                else:
                    print('没有获取到活动信息')
                    break

            else:
                print('获取用户信息失败')
                continue
        else:
            print(result['data'])
            continue
print(asyncio.run(main()))