import aiohttp
import json

async def loadImgInfo(uid, cookie, sinceid):
    referer = 'https://weibo.com/' + uid + '?tabtype=album'
    url = 'https://weibo.com/ajax/profile/getImageWall?uid=' + uid + '&sinceid=' + sinceid
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': cookie,
        'referer': referer,
        'sec-ch-ua': '"\\Not\"A;Brand";v="99", "Chromium";v="84", "Google Chrome";v="84"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-1c139e096020309ee08515b68b212990-a3301d11f8d55b85-00',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.30 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': 'ay1cbLKwIOjHA2k1UZFupGJ_'
    }
    params = {
        'uid': uid,
        'sinceid': '0',
        'has_album': 'true'
    }
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url, params=params) as response:
            res_text = await response.text()
            return res_text

async def get_district(text, pidList=[]):
    dict_data = json.loads(text)
    infoList = dict_data["data"]["list"]
    for info in infoList:
        pid = info['pid']
        pidList.append(pid)
        print(len(pidList), ':', pid)
    since_id = dict_data["data"]['since_id']
    return pidList, since_id

async def load_userName(uid, cookie):
    url = 'https://weibo.com/ajax/profile/info?uid=' + uid
    referer = 'https://weibo.com/u/' + uid
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': cookie,
        'referer': referer,
        'sec-ch-ua': '"\\Not\"A;Brand";v="99", "Chromium";v="84", "Google Chrome";v="84"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-1c139e096020309ee08515b68b212990-a3301d11f8d55b85-00',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.30 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': 'ay1cbLKwIOjHA2k1UZFupGJ_'
    }
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            res_text = await response.text()
            dict_data = json.loads(res_text)
            name = dict_data['data']['user']['screen_name']
            return name
