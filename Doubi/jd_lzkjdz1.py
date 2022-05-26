# lzkjdz-isv.isvjcloud.com/m/common 通用开卡模板 create by doubi
# 18:/復自￥ZAOTW1Lz0V%，【⤴️ī🆖ㅗ涷】，邀请开卡有礼
# https://lzkjdz-isv.isvjcloud.com/m/common/nestle/invite/?venderId=1000017162&activityId=12a061bd2ee34eb58663e01e18af6dd8&helpUuid=9123cee5524a427d9a3a456b17fd7d54
# new Env('邀请开卡有礼')

import asyncio
import requests,re,random,json,time,os
from urllib.parse import quote_plus, unquote_plus
from functools import partial
print = partial(print, flush=True)

shopid = '1000017162'
activityId = '12a061bd2ee34eb58663e01e18af6dd8'
authorCode = 'eee92737816a441dbf73851b46957e4e'
activityUrl = f'https://lzkjdz-isv.isvjcloud.com/m/common/nestle/invite/?venderId={shopid}&activityId={activityId}&helpUuid={authorCode}'

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
        result = requests.get(url=url, headers=header, timeout=20).text
        codestate = json.loads(result)
        if codestate['retcode'] == '1001':
            msg = "当前ck已失效，请检查"
            return {'code': 1001, 'data': msg}
        elif codestate['retcode'] == '0' and 'userInfo' in codestate['data']:
            nickName = codestate['data']['userInfo']['baseInfo']['nickname']
            return {'code': 200, 'name': nickName, 'ck': ck}
    except Exception as e:
        return {'code': 0, 'data': e}

# 获取当前时间
def get_time():
    time_now = round(time.time()*1000)
    return time_now

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
        body = 'body=%7B%22url%22%3A%20%22https%3A//lzkj-isv.isvjcloud.com%22%2C%20%22id%22%3A%20%22%22%7D&uuid=hjudwgohxzVu96krv&client=apple&clientVersion=9.4.0&st=1620476162000&sv=111&sign=f9d1b7e3b943b6a136d54fe4f892af05'
        result = requests.post(url=url,headers=headers,data=body).text
        result_res = json.loads(result)
        if result_res['code'] == '0':
            return result_res['token']
        else:
            return False
    except Exception as f:
        print(f)

async def wxCommonInfo(ua):
    try:
        url = 'https://lzkjdz-isv.isvjcloud.com/wxCommonInfo/token'
        headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'lzkjdz-isv.isvjcloud.com',
        'Referer': activityUrl,
        'User-Agent': ua
        }
        result = requests.get(url=url, headers=headers, timeout=20).text
        res = json.loads(result)
        if res['result']:
            LZ_TOKEN_KEY = res['data']['LZ_TOKEN_KEY']
            LZ_TOKEN_VALUE = res['data']['LZ_TOKEN_VALUE']
            return f"LZ_TOKEN_KEY={LZ_TOKEN_KEY};LZ_TOKEN_VALUE={LZ_TOKEN_VALUE};"
        else:
            return None
    except Exception as e:
        print(e)

# 获取 getMyping
async def getMyPing(ua,Cookie,token):
    url = 'https://lzkjdz-isv.isvjcloud.com/customer/getMyPing'
    headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': Cookie,
    'Host': 'lzkjdz-isv.isvjcloud.com',
    'Origin': 'https://lzkjdz-isv.isvjcloud.com',
    'Referer': activityUrl,
    'User-Agent': ua,
    }
    data = f'userId={shopid}&token={token}&fromType=APP&pin='
    result = requests.post(url=url,headers=headers,data=data,timeout=10).text
    res = json.loads(result)
    if res['result']:
        return res

async def getShopInfoVO(Cookie,ua,pin):
    url = 'https://lzkjdz-isv.isvjcloud.com/wxActionCommon/getShopInfoVO'
    headers = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': Cookie,
        'Host': 'lzkjdz-isv.isvjcloud.com',
        'Origin': 'https://lzkjdz-isv.isvjcloud.com',
        'Referer': activityUrl,
        'User-Agent': ua,
    }
    data = f'userId={shopid}&pin={pin}'
    result = requests.post(url=url,headers=headers,data=data,timeout=10).text
    res = json.loads(result)
    if res['result']:
        return res

# 获取 ad
async def accessLogWithAD(ua,Cookie,pin):
    url = 'https://lzkjdz-isv.isvjcloud.com/common/accessLogWithAD'
    headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': Cookie,
    'Host': 'lzkjdz-isv.isvjcloud.com',
    'Origin': 'https://lzkjdz-isv.isvjcloud.com',
    'Referer': activityUrl,
    'User-Agent': ua,
    }
    body = f'venderId={shopid}&code=40&activityId={activityId}&pageUrl={activityUrl}&pin={pin}'
    result = requests.post(url=url,headers=headers,data=body,timeout=30).text
    return result

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


async def getSimpleActInfoVo(ua,cookie):
    url = f'https://lzkjdz-isv.isvjcloud.com/common/brand/getFullActInfoVo?activityId={activityId}'
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

# 加入店铺会员
async def bindWithVender(ua,cookie,body):
    try:
        url = f'https://api.m.jd.com/client.action?appid=jd_shop_member&functionId=bindWithVender&body={json.dumps(body)}&client=H5&clientVersion=9.2.0&uuid=88888&h5st=20220412164645241%3B3634d1aeada6d9cd11a7526a3a6ac63e%3B169f1%3Btk02wd66f1d7418nXuLjsmO3oJMCxUqKVwIf4q1WRptKRT3nJSrx01oYYBAylbSuyg4sipnEzyEJOZuFjfG2QERcBtzd%3B6b455234e93be4ec963cd7c575d70882b838ba588149a1f54b69c8d0dacf14da%3B3.0%3B1649753205241'
        header = {
            'Host': 'api.m.jd.com',
            'Cookie': cookie,
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'User-Agent': ua,
            'Referer': f'https://shopmember.m.jd.com/shopcard/?venderId={shopid}&venderType=1&channel=7891&sceneval=2&jxsid=16346939349370206900&returnUrl={json.dumps(activityUrl)}',
        }
        response = requests.get(url=url,headers=header,timeout=30).text
        return json.loads(response)
    except Exception as e:
        print(e)

async def content(ua,Cookie,activityId,pin):
    url = 'https://lzkjdz-isv.isvjcloud.com/nestle/invite/activityContent'
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
    body = f'activityId={activityId}&pin={pin}&helpUuid={authorCode}'
    result = requests.post(url=url,headers=headers,data=body,timeout=30)
    return json.loads((result.text))

# 检查开卡状态
async def check_ruhui(body,cookie,ua):
    url = f'https://api.m.jd.com/client.action?appid=jd_shop_member&functionId=getShopOpenCardInfo&body={json.dumps(body)}&client=H5&clientVersion=9.2.0&uuid=88888&h5st=20220316103927741%3B4917820034065113%3B8adfb%3Btk02wac471c5018nzfjQ07QMnzYF7aGYN8INh7pOROYvT9xfhNG4WoAlspfC9wo4vdX6Q79yOggjkDKhiadrPg2z%2B9k%2B%3B034fb6c85703cf98cb40dfa9ecc91fe0c5aefbd69d361721c900544597f535df%3B3.0%3B1647398367741'
    headers =  {
        'Host': 'api.m.jd.com',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Cookie': cookie,
        'User-Agent': ua,
        'Accept-Language': 'zh-cn',
        'Referer': f'https://shopmember.m.jd.com/shopcard/?venderId={shopid}&channel=801&returnUrl={json.dumps(activityUrl)}',
        'Accept-Encoding': 'gzip, deflate'
    }
    response = requests.get(url=url,headers=headers,timeout=5).text
    return json.loads(response)

# 主程序
async def main():
    try:
        cks = os.environ["JD_COOKIE"].split("&")
    except:
        f = open("cklist.txt", "r", encoding='utf-8')
        cks = f.read().split('\n')
        f.close()
    success = 0   # 计算成功数
    print(f'=============== 共{len(cks)}个京东账号Cookie ===============')
    print(f'================== 脚本执行-{get_time()} ==================\n')
    for n,ck in enumerate(cks,1):
        ua = randomuserAgent()  # 获取ua
        print(f'******开始【京东账号【{n}】*********\n')
        result = await check(ua, ck) # 检测ck
        if result['code'] == 200:
            token = await get_Token(ck)
            lz_token = await wxCommonInfo(ua)
            getMe = await getMyPing(ua,lz_token,token)
            if getMe['result']:
                nickname = getMe['data']['nickname']
                secretPin = quote_plus(getMe['data']['secretPin'])
                result = await getShopInfoVO(lz_token,ua,secretPin)
                shopName = result['data']['shopName']
                result = await getSimpleActInfoVo(ua,lz_token)
                actName = result['data']['actName']
                print(f'你好[{nickname}],已获取到用户信息,店铺:{shopName},活动[{actName}]\n')
                await accessLogWithAD(ua,lz_token,secretPin)
                print('京东没返回任何东西\n')
                await content(ua,lz_token,activityId,secretPin)
                await crmCard(ua,lz_token,activityId,secretPin)
                result= await check_ruhui({"venderId":str(shopid), "channel": "401" },ck,ua) # 检查入会状态
                try:
                    if result['result']['userInfo']['openCardStatus']==0: # 0 未开卡
                        print('您还不是会员哦，快去开卡助力好友咯\n')
                        await asyncio.sleep(1)
                        ruhui = await bindWithVender(ua,ck,{"venderId":str(shopid),"shopId":str(shopid),"bindByVerifyCodeFlag":1,"registerExtend":{},"writeChildFlag":0,"activityId":2356734,"channel":7891})
                        print(ruhui)
                        await asyncio.sleep(5)
                        token = await get_Token(ck)
                        lz_token = await wxCommonInfo(ua)
                        result = await crmCard(ua,lz_token,activityId,secretPin)
                        print(result)
                        result = await content(ua,lz_token,activityId,secretPin)
                        if ruhui['busiCode']=='201':
                            pass
                        else:
                            success += 1
                            print(f'助力成功，当前助力{success}次\n')
                        await asyncio.sleep(5)
                    else:
                        print('您已经是会员了无法助力好友了\n')
                        continue
                except TypeError:
                    print('可能是黑号\n')
                    continue
            else:
                print('获取用户信息失败\n   ')
                continue
        else:
            print(result['data'])
            continue
asyncio.run(main())