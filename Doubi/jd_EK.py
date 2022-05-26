# 戴森会员赢好礼！ 18人 20E卡 
# create by doubi 通用模板 
# 15:/￥ABBEh97xdJ￥ ，达开最新倞〣Dσδδng邀请好友赢好礼
# https://jyds-isv.isvjcloud.com/page/index-20220430.php?member_id=3350047&nick=AAFieiztADB3TvRy5JFgZbb-MZkokEtAK9Ti9VaMeERN3Q7D_leoTUvQP8Vt0kpGKqwytPcBkb8&activity_id=268&invite_url_id=&platform_open_id=Aq1FEZEEfhQv8gLrS32zp9B+EJMtpWbH1cLlicWmwb7xRJup55uZv3h71r12lqDP&_wvUseWKWebView=YES&merchantNum=2000062&instId=39&type=0
# new Env('戴森会员赢好礼')

from urllib import response
import requests,random,asyncio,os,datetime,json,time,random,re
from urllib.parse import quote_plus,unquote_plus
from functools import partial

print = partial(print, flush=True)
activatyname = '戴森会员赢好礼！'
member_id = '3962925'    # 助力id
nick = 'AAFiheQyADBbFXYO9d-dCsc4A3UpCWKeDbU2Zg6ymHkpr-sK0vhK2thV2Q73lZBtNZlKG2aiPK4' # token
platform_open_id = 'jLAqojA%2BYTi95giY7h51X3awUSXeKB30w8KOFuW60Vjj1O2f3b6ctAodeLnmTR9mkdK3rLBQpEQH9V4tdrrh0w%3D%3D' # open_id
activity_id = '269'
activityUrl = f'https://jyds-isv.isvjcloud.com/page/index-20220430.php?member_id={member_id}&nick={nick}&activity_id={activity_id}&invite_url_id=&platform_open_id={platform_open_id}&_wvUseWKWebView=YES&merchantNum=2000062&instId=39&type=0' 
shopid = '100000000000417'

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

# 格式化时间
def get_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 时间戳
def get_now():
    return round(time.time()*1000)

# 随机位数
def random_str(num=16):
    uln = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    rs = random.sample(uln, num)  # 生成一个 指定位数的随机字符串
    return ''.join(rs)  # 返回随机字符串

# 登录活动 获取Token
async def loginjingdong(token,ua):
    url = f'https://vip.zkyai.com/apis/user/loginjingdong?account={token}&merchantNum=2000062&traceId={random_str()}&refresh=0&protocol=https&_={get_now()}'
    header = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'vip.zkyai.com',
        'Origin': 'https://jyds-isv.isvjcloud.com',
        'Referer': 'https://jyds-isv.isvjcloud.com/',
        'User-Agent': ua
    }
    response = json.loads(requests.get(url=url,headers=header).text)
    return response


# 获取first ck
async def memberinfo(ua,account):
    url = f'https://vip.zkyai.com/apis/member/memberinfo?account={quote_plus(account)}&merchantNum=2000062&traceId={random_str()}&refresh=0&protocol=https&jd_token={quote_plus(account)}&_={get_now()}'
    header = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'vip.zkyai.com',
        'Origin': 'https://jyds-isv.isvjcloud.com',
        'Referer': 'https://jyds-isv.isvjcloud.com/',
        'User-Agent': ua
    }
    response = requests.get(url=url,headers=header).text
    response_res =  json.loads(response)
    if response_res['code']==0:
        return response_res
    else:
        False

# 提交邀请
async def invited(ua,account):
    url = f'https://vip.zkyai.com/apis/fission/update-invited-record'
    header = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        'Connection': 'keep-alive',
        'Host': 'vip.zkyai.com',
        'Origin': 'https://jyds-isv.isvjcloud.com',
        'Referer': 'https://jyds-isv.isvjcloud.com/',
        'User-Agent': ua
    }
    body = {f"activity_id={activity_id}&merchantNum=2000062&traceId={random_str()}&refresh=0&protocol=https&jd_token={account}"}
    response = requests.post(url=url,headers=header,data=body).text
    return json.loads(response)

async def visit(def_id,ua,body):
    url = 'https://vip.zkyai.com/apis/'+def_id
    headers = {
        'Host': 'vip.zkyai.com',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://jyds-isv.isvjcloud.com',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': ua,
        'Referer': 'https://jyds-isv.isvjcloud.com/',
        'Accept-Language': 'zh-cn'
    }
    response = requests.post(url=url,headers=headers,data=body).text
    print(response)
    return response

# 活动接口
async def activity(ua,token):
    url = f'https://vip.zkyai.com/apis/fission/get-activity-detail?activity_id={activity_id}&mixnick={token}&merchantNum=2000062&traceId={random_str()}&refresh=0&protocol=https&__={get_now()}'
    header = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        'Connection': 'keep-alive',
        'Host': 'vip.zkyai.com',
        'Origin': 'https://jyds-isv.isvjcloud.com',
        'Referer': 'https://jyds-isv.isvjcloud.com/',
        'User-Agent': ua
    }
    response = requests.get(url=url,headers=header).text
    response_res =  json.loads(response)
    if response_res['code'] == 0:
        return response_res
    else:
        False

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
            'Referer': f'https://shopmember.m.jd.com/shopcard/?venderId={shopid}&channel=401&returnUrl={json.dumps(activityUrl)}',
        }
        response = requests.get(url=url,headers=header,timeout=30).text
        return json.loads(response)
    
    except Exception as e:
        print(e)

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
    print(f'🔔{activatyname}')
    print(f'=============== 共{len(cks)}个京东账号Cookie ===============')
    print(f'================== 脚本执行-{get_time()} ==================\n')
    ua = randomuserAgent()  # 获取ua
    for n,ck in enumerate(cks,1):
        print(f'****** 开始【京东账号{n}】*********\n')
        result = await check(ua, ck) # 检测ck
        if result['code'] == 200:
            token = await get_Token(ck)
            account = await loginjingdong(token,ua) 
            print(account)
            result= await check_ruhui({"venderId":str(shopid), "channel": "401" },ck,ua) # 检查入会状态
            try:
                if result['result']['userInfo']['openCardStatus']==0: # 0 未开卡
                    print('你还不是会员，去帮好友助力吧！')
                    if token:
                        await loginjingdong(token,ua)
                        await asyncio.sleep(1)
                        account = await loginjingdong(token,ua) 
                        await asyncio.sleep(2)
                        result = await activity(ua,token)
                        if result:
                            name = result['data']['activity_info']['name']
                            print(f'已开启{name}活动\n')
                            await visit('activity/visit',ua,f'activity_id={activity_id}&platform_open_id={token}&platform_type=2&merchantNum=2000062&traceId={random_str()}&refresh=0&protocol=https'.encode('UTF-8'))
                            await visit('fission/report-hd-trace',ua,f'activity_id={activity_id}&mix_nick={token}&action=5&relation_open_id={account}&merchantNum=2000062&traceId={random_str()}&refresh=0&protocol=https'.encode('UTF-8'))
                            await visit('invite/invites',ua,f'act_id={activity_id}&invited_id={token}&invited_member_id=&act_type=29&type=19&member_id={member_id}&timestamp=1652191201296&invite_url_id=&merchantNum=2000062&traceId={random_str()}&refresh=0&protocol=https'.encode('UTF-8'))
                            print('去入会')
                            ruhui = await bindWithVender(ua,ck,{"venderId":str(shopid),"shopId":str(shopid),"bindByVerifyCodeFlag":1,"registerExtend":{},"writeChildFlag":0,"channel":9006})
                            print(ruhui)
                            await asyncio.sleep(2)
                            await loginjingdong(token,ua)
                            await activity(ua,token)
                            if ruhui['busiCode']=='0':
                                success += 1
                                print(f'已入会成功\n助力成功，当前助力{success}次\n')
                            await asyncio.sleep(1)
                            continue
                else:
                    print('您已经是会员啦，不去开活动啦\n')
                    continue
            except TypeError as e:
                print('可能是黑号')
                continue
        else:
            print(result['data'])
            continue

asyncio.run(main())