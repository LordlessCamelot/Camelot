# cretre by doubi
# new Env('欧莱雅-用对心只对你')
# 欧莱雅日常活动

import asyncio
import requests
import json
import random
import os
from functools import partial

print = partial(print, flush=True)

activatname = '欧莱雅-用对心只对你'
shareOpenId = 'ER7H6c62EYmTTuQKgpxV6aygi-zfSEO6oSMc40Ppndc'
shopid = '1000002662'
activityId = '2396254'
activityUrl = f'https://hd-zex-isv.isvjcloud.com/zex-jd-web/newJD/loreal18/index.html?brand=5012622631&campaignId=718&shareOpenId={shareOpenId}&ruleId=476&shopId={shopid}&activityId={activityId}'
# 随机ua


def randomuserAgent():
    global uuid, addressid, iosVer, iosV, clientVersion, iPhone, area, ADID, lng, lat
    uuid = ''.join(random.sample(
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'z'], 40))
    addressid = ''.join(random.sample('1234567898647', 10))
    iosVer = ''.join(random.sample(
        ["15.1.1", "14.5.1", "14.4", "14.3", "14.2", "14.1", "14.0.1"], 1))
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


async def getMemberInfo(token, ua):
    url = f'https://hd-zex-isv.isvjcloud.com/zex-jd-srv/user/v2/getMemberInfo?token={token}&brand=5012622631&openid=&source=01'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'hd-zex-isv.isvjcloud.com',
        'Referer': activityUrl,
        'User-Agent': ua,
        'X-Requested-With': 'XMLHttpRequest'
    }
    result = requests.get(url=url, headers=headers).text
    result_res = json.loads(result)
    return result_res

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
            'Cookie': cookie,
            'User-Agent': 'JD4iPhone/168014 (iPhone; iOS; Scale/3.00)'
        }
        body = 'body=%7B%22url%22%3A%22https%3A%5C/%5C/jyds-isv.isvjcloud.com%5C/page%5C/index-20220430.php?member_id%3D3403726%26nick%3DAAFiei4pADAchjH1pPrBRYE6Q_nM0XT9LL9wRMmHnIYD_PFd7zQUONjmMj_QFBeC3P6GG_R1Pvk%26activity_id%3D266%26invite_url_id%3D%26platform_open_id%3DhVVjbDOf6oEeoHnz7_ZNlSWLyOE9OkFDSTUKUEi-_qU%26_wvUseWKWebView%3DYES%26merchantNum%3D2000062%26instId%3D39%26type%3D0%26sid%3D8ff880cb962b7e7e49759bb3e43d52dw%26un_area%3D16_1332_1336_59151%22%2C%22id%22%3A%22%22%7D&build=168014&client=apple&clientVersion=10.4.6&d_brand=apple&d_model=iPhone13%2C1&ef=1&eid=eidI6bf3812088s3ecjXNJkaR3SsJLEP23h%2BVHnI2K9M5HaVE2J6h8REjD7tNeZy715QizBG1uMdEvb4GAs6HMG/Xyh2h6n4b%2BGp/Mb9zxqU9qnbwKhL&ep=%7B%22ciphertype%22%3A5%2C%22cipher%22%3A%7B%22screen%22%3A%22CJOyDIeyDNC2%22%2C%22wifiBssid%22%3A%22DtUyZtc4YwS0DJGnEJK0YtUnCQOyZtDuCtvtDWS3Y2Y%3D%22%2C%22osVersion%22%3A%22CJUkDG%3D%3D%22%2C%22area%22%3A%22CJZpCJCzCv8nCzC2XzU5CJUn%22%2C%22openudid%22%3A%22ZwO4ZQO4ZJDwDWU5YtqnYJc1DWC1CNZsD2PrY2YmYJu3DWU1YzSyDm%3D%3D%22%2C%22uuid%22%3A%22aQf1ZRdxb2r4ovZ1EJZhcxYlVNZSZz09%22%7D%2C%22ts%22%3A1652180385%2C%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22version%22%3A%221.0.3%22%2C%22appname%22%3A%22com.360buy.jdmobile%22%2C%22ridx%22%3A-1%7D&ext=%7B%22prstate%22%3A%220%22%2C%22pvcStu%22%3A%221%22%7D&isBackground=N&joycious=117&lang=zh_CN&networkType=wifi&networklibtype=JDNetworkBaseAF&partner=apple&rfs=0000&scope=10&sign=1d5341cdf68a364678682892ba61fa14&st=1652180391940&sv=120&uemps=0-0&uts=0f31TVRjBStTMMMVdx/6coevBdXhbSIifopQageUhS/zTLdcrpETDOhFP34L6Sn7mr5dwU7LXgIFptoCqDGwsTpV6R4rDNdE/pRXTMN0iZfG7yQTTWF/y0OarqJUWhs2cKKu081h288awnyStYFgK4rs9gRYLqhan4MYGECajSemqCAr%2Bgd%2BnTec5dgBOiLWd5Mbz7fTBA4ptdJ4xs%2Bj3Q%3D%3D'
        result = requests.post(url=url, headers=headers, data=body).text
        result_res = json.loads(result)
        if result_res['code'] == '0':
            return result_res['token']
        else:
            return False
    except Exception as f:
        print(f)

# 助力


async def join(ua, openid, shareOpenId,participateSource=11):
    try:
        url = 'https://hd-zex-isv.isvjcloud.com/zex-jd-srv/campaign/join?brand=5012622631'
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Host': 'hd-zex-isv.isvjcloud.com',
            'Origin': 'https://hd-zex-isv.isvjcloud.com',
            'Referer': activityUrl,
            'User-Agent': ua,
            'X-Requested-With': 'XMLHttpRequest'
        }
        body = json.dumps({
            "openid": openid,
            "campaignId": "718",
            "ruleId": "476",
            "ruleDetailId": "",
            "shareOpenId": shareOpenId,
            "pageScene": "",
            "description": "",
            "participateSource": participateSource,
            "businessId": 1,
            "businessPass": ""
        })
        result = requests.post(url=url, headers=headers, data=body).text
        result_res = json.loads(result)
        print(result_res)
        return result_res

    except Exception as f:
        print(f)


async def task(eventId, openid, ua):
    try:
        url = 'https://hd-zex-isv.isvjcloud.com/zex-jd-srv/monitor/data/submit?brand=5012622631'
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Host': 'hd-zex-isv.isvjcloud.com',
            'Origin': 'https://hd-zex-isv.isvjcloud.com',
            'Referer': activityUrl,
            'User-Agent': ua,
            'X-Requested-With': 'XMLHttpRequest'
        }
        body = json.dumps({
            "eventId": eventId,
            "openid": openid,
            "pageScene": f"brand=5012622631&campaignId=718&shareOpenId={shareOpenId}&ruleId=476&shopId=1000002662&activityId=2396254&sid=8ff880cb962b7e7e49759bb3e43d52dw&un_area=16_1332_1336_59151",
            "pageUrl": "https://hd-zex-isv.isvjcloud.com//zex-jd-web/newJD/loreal17/index.html",
            "externalId": "",
            "bizDesc": ""
        })
        result = requests.post(url=url, headers=headers, data=body).text
        result_res = json.loads(result)
        print(result_res)
        return result_res['msg']

    except Exception as f:
        print(f)

# 加入店铺会员


async def bindWithVender(ua, cookie, body):
    try:
        url = f'https://api.m.jd.com/client.action?appid=jd_shop_member&functionId=bindWithVender&body={json.dumps(body)}&clientVersion=9.2.0&client=H5&uuid=88888&h5st=20220525013418422%3B6557296343586533%3B169f1%3Btk02w99281b4e18n0dRulgUl8od3rb6UXQxFWpV2lZ%2FErHMN2CyKhYN8ww9JaI8EYCLJoiL%2FG0M64JvSWd1pSeWWKiSF%3Bfbe4fb1cae722483a1e78d37d09e883e59ebe371d641db4388376f04cb2bcecc%3B3.0%3B1653413658422'
        header = {
            'Host': 'api.m.jd.com',
            'Cookie': cookie,
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'User-Agent': ua,
            'Referer': f'https://shopmember.m.jd.com/shopcard/?venderId={shopid}&channel=401&returnUrl={json.dumps(activityUrl)}',
        }
        response = requests.get(url=url, headers=header, timeout=5).text
        print(response)
        response_res = str(response).split('(')[1].split(')')[0]
        return json.loads(response_res)

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


async def main():
    try:
        cks = os.environ["JD_COOKIE"].split("&")
    except:
        f = open("cklist.txt", "r", encoding='utf-8')
        cks = f.read().split('\n')
        f.close()
    print(f'=============== 共{len(cks)}个京东账号Cookie ===============')
    for ck in cks:
        ua = randomuserAgent()
        result = await check(ua, ck)  # 检测ck
        try:
            if result['code'] == 200:
                token = await get_Token(ck)
                if token:
                    result = await getMemberInfo(token, ck)
                    openid = result['result']['openid']
                    nickName = result['result']['nickName']
                    print(f'你好![{nickName}],开启[{activatname}]活动\n')
                    result = await join(ua, openid, shareOpenId)
                    if result['msg'] == 'success' or '请入会' in result['msg']:
                        await bindWithVender(ua, ck, {"venderId": str(shopid), "shopId": str(shopid), "bindByVerifyCodeFlag": 1, "registerExtend": {}, "writeChildFlag": 0, "channel": 9006})
                        result = await getMemberInfo(token, ua)
                        result = await join(ua, openid, shareOpenId)
                        print(result)
                    else:
                        print(result['msg'])
                    print('去做日常任务\n')
                    await asyncio.sleep(2)
                    await join(ua,openid,shareOpenId,14)
                    await asyncio.sleep(2)
                    await join(ua,openid,shareOpenId,7)
                    await asyncio.sleep(2)
                    await join(ua,openid,shareOpenId,10)
                    await asyncio.sleep(2)
                    await join(ua,openid,shareOpenId,4)
                    await asyncio.sleep(10)
                else:
                    print('黑号吧\n')
                    continue
            else:
                print(result['data'])
                continue

        except TypeError as e:
            print(e)
            continue
print(asyncio.run(main()))