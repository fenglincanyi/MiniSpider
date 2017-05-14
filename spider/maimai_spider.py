# coding=utf-8
import requests

from util import mongo_util
from util import timer_scheduler
from util import mysql_util

param = {
    'u': '37378145',
    'access_token': '1.f04a06ada5c1c51770cde4117d8389c8',
    'version': '4.16.10',
    'ver_code': 'android_1202',
    'channel': 'XiaoMi',
    'vc': 'Android%204.4.4%2F19',
    'push_permit': 1,
    'net': 'wifi',
    'open': 'icon',
    'appid': 3,
    'device': 'Xiaomi%20HM%20NOTE%201LTE',
    'imei': '866032028813695',
    'density': '2.0',
    'action': 'out_date',
    'page': 9
}

# header = {
#     'Cache-Control': 'no-cache',
#     'Accept-Encoding': 'gzip',
#     'Authorization': 'Bearer gt2.0AAAAAATpzHELPBksK0JwAAAAAAxNVQJgAgCZkl1SJEn_kzNS0HydXjWc8Wb4cg==',
#     'Cookie': 'acw_tc=AQAAAA/1+V8XrwcAJTUscfHQSwrYk7SJ; aliyungf_tc=AQAAAO5bYn8WnAcAJTUscZPP4wmiIsR8',
#     'User-Agent': 'Futureve/4.50.0 Mozilla/5.0 (Linux; Android 4.4.4; HM NOTE 1LTE Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 Google-HTTP-Java-Client/1.22.0 (gzip)',
#     'x-api-version': '3.0.57',
#     'x-app-version': '4.50.0',
#     'x-app-za': 'OS=Android&Release=4.4.4&Model=HM+NOTE+1LTE&VersionName=4.50.0&VersionCode=481&Width=720&Height=1280&Installer=%E5%B0%8F%E7%B1%B3%E5%95%86%E5%BA%97&WebView=33.0.0.0',
#     'x-app-build': 'release',
#     'x-udid': 'AHBCKywZPAtLBVjPnrywfqxyTPwNAbEmLIc=',
#     'Host': 'api.zhihu.com',
#     'Connection': 'Keep-Alive'
# }


END_FLAG = 3  # 默认5次，就停止
count = 0


def request_host():
    global count
    if count < END_FLAG:
        r = requests.get("https://open.taou.com/maimai/gossip/v3/feed", params=param, verify=False)
        # data = r.json()[u'data']  # python 获取 data 数据部分
        # print json.dumps(data) # python 对象转 json

        # mongo_util.list_insert('test', 'aaa', data)  # 数据入库
        # param['page'] += 1 # 页码自增
        # count += 1

        # mysql_util.create_table()
        mysql_util.insert(r.json()['data'])

    else:
        timer_scheduler.timer_stop()


# timer_scheduler.timer(request_host, 5)
# timer_scheduler.timer(res, 1)


request_host()