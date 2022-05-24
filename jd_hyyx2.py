# 邀请好友开卡，更多礼品赠送，快去抢吧！ 
# create by doubi 通用模板 
# 15:/￥JDyBk7J7vQzt% ，【🐬マDoōδng】邀请好友开卡，更多礼品赠送，快去抢吧！
# https://lorealjdcampaign-rc.isvjcloud.com/interact/index?activityType=10006&templateId=20201228083300yqrhyl01&activityId=1520020257503784961&nodeId=101001005&&shareUserId=1523584605943877634&shareuserid4minipg=bQ+qhAPwYOTMkMknzFz4XiuuadQPA0cYqp9ZkvcOQeE9ilbo+RyNDutiw5Zsqz/pkdK3rLBQpEQH9V4tdrrh0w==&shopid=1000396688
# 使用规则
# 解析自己的口令 根据解析地址修改以下变量 templateId，activityId，authorCode，shopid，脚本默认不领取，注意看活动规则有的活动只能领取一阶段，有的可以领取所有奖品

from cgi import print_arguments
from cgitb import text
import json
import requests,random,asyncio,os,datetime
from urllib.parse import quote_plus,unquote_plus
from functools import partial

print = partial(print, flush=True)
activatyname = '会员邀新赢大礼'
templateId = '20201228083300yqrhyl01'   # 活动id
activityId = '1528968143070998529'    # 活动id
authorCode = '1529115775723180033' # 助力码
shopid = '703279'   # 店铺id
activityUrl = f'https://lzkj-isv.isvjcloud.com/prod/cc/interact/index?activityType=10006&templateId={templateId}&activityId={activityId}&nodeId=101001005&&shareUserId={authorCode}&shareuserid4minipg=wEPKomIZ4xyUGRQ1NbKOGGYBOhciOnD26Q8hnD3IPFDDEHNQnnsbyp+hKVYmbLfm&shopid={shopid}'

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

# 获取当前时间
def get_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 助力接口
async def getMember(ua,token):
    url = 'https://lzkj-isv.isvjcloud.com/prod/cc/interact/api/task/member/getMember'
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Host': 'lzkj-isv.isvjcloud.com',
    'Origin': 'https://lzkj-isv.isvjcloud.com',
    'Referer': activityUrl,
    'ua':ua,
    'token': token
}
    body = json.dumps({
  "shareUserId": authorCode
})
    result = json.loads(requests.post(url=url,headers=headers,data=body).text)
    return result


# 助力接口
async def basicInfo(ua,token):
    url = 'https://lzkj-isv.isvjcloud.com/prod/cc/interact/api/active/basicInfo'
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Host': 'lzkj-isv.isvjcloud.com',
    'Origin': 'https://lzkj-isv.isvjcloud.com',
    'Referer': activityUrl,
    'ua':ua,
    'token': token
}
    body = json.dumps({
  "activityId": activityId
})
    result = json.loads(requests.post(url=url,headers=headers,data=body).text)
    return result

# 获取Token
async def get_Token(cookie,ua):
    try:
        url = 'https://api.m.jd.com/client.action?functionId=isvObfuscator'
        headers = {
            'Host': 'api.m.jd.com',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie':cookie,
            'User-Agent': ua
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

# login
async def login(ua,token):
    try:
        url = 'https://lzkj-isv.isvjcloud.com/prod/cc/interact/api/user-info/login'
        headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Host': 'lzkj-isv.isvjcloud.com',
        'Origin': 'https://lzkj-isv.isvjcloud.com',
        'Referer': activityUrl,
        'User-Agent': ua,
    }
        body = json.dumps({
        "status": "0","activityId": activityId,"tokenPin": token,"source": "01","shareUserId": authorCode
    })
        result = json.loads(requests.post(url=url,headers=headers,data=body).text)
        if result['resp_code']==0:
            return result
        else:
            return False
            
    except Exception as f:
        return False

""" # 奖品list
async def prizeList(token,ua):
    url = 'https://lorealjdcampaign-rc.isvjcloud.com/apps/interact/api/task/member/prizeList'
    headers = {
        "Host":"lorealjdcampaign-rc.isvjcloud.com",
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        "token":token,
        "Content-Type":'application/json;charset=UTF-8',
        'Origin': 'https://lorealjdcampaign-rc.isvjcloud.com',
        "User-Agent":ua,
        "Connection":"keep-alive",
        "Referer": activityUrl
    }
    body = {}
    result = json.loads(requests.post(url=url,headers=headers,data=body).text)
    return result """

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
        response = requests.get(url=url,headers=header,timeout=5).text
        print(response)
        return json.loads(response)
    
    except Exception as e:
        if TimeoutError:
            return f'请求入会失败{e}'
        if IndexError:
            return response

# 检查开卡状态
def check_ruhui(body,cookie,ua):
    url = f'https://api.m.jd.com/client.action?appid=jd_shop_member&functionId=getShopOpenCardInfo&body={json.dumps(body)}&client=H5&clientVersion=9.2.0&uuid=88888'
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
    response = requests.get(url=url,headers=headers,timeout=5)
    return json.loads(response.text)

# check开卡
async def checkopencard(token,ua,):
    url = 'https://lzkj-isv.isvjcloud.com/prod/cc/interact/api/join/check'
    headers = {
        "Host":"lzkj-isv.isvjcloud.com",
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        "token":token,
        "Content-Type":'application/json;charset=UTF-8',
        'Origin': 'https://lzkj-isv.isvjcloud.com',
        "User-Agent":ua,
        "Connection":"keep-alive",
        "Referer": activityUrl
    }
    body = json.dumps({
        "status":"0"
        })
    response = requests.post(url=url,headers=headers,data=body).text
    return response

# check
async def myself(token,ua,):
    url = 'https://lzkj-isv.isvjcloud.com/prod/cc/interact/api/task/bargain/guest/myself'
    headers = {
        "Host":"lzkj-isv.isvjcloud.com",
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        "token":token,
        "Content-Type":'application/json;charset=UTF-8',
        'Origin': 'https://lzkj-isv.isvjcloud.com',
        "User-Agent":ua,
        "Connection":"keep-alive",
        "Referer": activityUrl
    }
    body = json.dumps({
        "shareUserId":authorCode
        })
    response = requests.post(url=url,headers=headers,data=body).text
    return response


""" # 检查pin
def checkpin(cks:list,pin):
    for ck in cks:
        if pin in ck:
            return ck
        else:
            None """

# 主程序
async def main():
    try:
        cks = os.environ["JD_COOKIE"].split("&")
    except:
        f = open("cklist.txt", "r", encoding='utf-8')
        cks = f.read().split('\n')
        f.close()
    success = 0   # 计算成功数
    needinviteNum = [] # 需要助力次数
    print(f'🔔{activatyname}')
    print(f'=============== 共{len(cks)}个京东账号Cookie ===============')
    print(f'================== 脚本执行-{get_time()} ==================\n')
    ua = randomuserAgent()  # 获取ua
    for n,ck in enumerate(cks,1):
        print(f'****** 开始【京东账号{n}】*********\n')
        result = await check(ua, ck) # 检测ck
        if result['code'] == 200:
            await asyncio.sleep(1)
            token = await get_Token(ck,ua) # 获取Token
            if token:
                await asyncio.sleep(1)
                cklogin = await login(ua,token) # 进入活动
                if cklogin:
                    if n == 1:
                        token = cklogin['data']['token'] # 活动ck
                        result = await basicInfo(ua,token)
                        actName = result['data']['actName'] # 活动名字
                        nickName = cklogin['data']['nickName'] # 用户名
                        print(f'你好{nickName}，已开启{actName}')
                        await asyncio.sleep(1)
                        result = await getMember(ua,token) # 活动详情信息
                        await asyncio.sleep(1)
                    else:
                        await asyncio.sleep(1)
                        result= check_ruhui({"venderId":str(707261), "channel": "401" },ck,ua) # 检查入会状态
                        if result['result']['userInfo']['openCardStatus']==0: # 0 未开卡
                            print('您还不是会员诶，去帮助队友开活动吧！\n')
                            token = await get_Token(ck,ua)
                            if token:
                                await asyncio.sleep(1)
                                cklogin = await login(ua,token) # 进入活动
                                if cklogin:
                                    token = cklogin['data']['token']
                                    await getMember(ua,token)
                                    await asyncio.sleep(1)
                                    result = await bindWithVender(ua,ck,{"venderId":'707261',"shopId":'703279',"bindByVerifyCodeFlag":1,"registerExtend":{},"writeChildFlag":0,"channel":9006})
                                    await checkopencard(token,ua)
                                    await getMember(ua,token)
                                    await myself(token,ua)
                                    if result['busiCode']=='201':
                                        print(result['message'])
                                    if '加入店铺会员成功' in str(result):
                                        success += 1
                                        print(f'已入会成功\n助力成功，当前助力{success}次\n')
                                    await asyncio.sleep(1)
                                    continue
                                else:
                                    print('没有获取到活动信息，走了\n')
                                    continue
                            else:
                                print('可惜！黑号\n')
                                continue
                        else:
                            print('您已经是会员啦，不去开活动啦\n')
                            continue
                else:
                    print('没有获取到活动信息，走了\n')
                    continue
            else:
                print('没有获取到用户信息退出了\n')
                continue
        else:
            print(result['data'])
            continue

asyncio.run(main())
