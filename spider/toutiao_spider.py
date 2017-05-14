# coding=utf-8
import json

import requests

from util import mongo_util
from util import mysql_util

# header = {
#     'X-LC-Prod':'1',
#     'X-LC-Session':'',
#     'X-LC-Id': 'mhke0kuv33myn4t4ghuid4oq2hjj12li374hvcif202y5bm6',
#     'Accept': 'application/json',
#     'Content-Type': 'application/json',
#     'User-Agent': 'AVOS Cloud android-v3.16.4 SDK',
#     'X-LC-Sign': '8ed1d122688346866173822864df30a2,1494401683768',
#     'X-Android-RS': '1',
#     'Host': 'api.leancloud.cn',
#     'Connection': 'Keep-Alive',
#     'Accept-Encoding': 'gzip'
# }

param = {
    'refer': 1,
    'count': 20,
    'min_behot_time': 1494403964,
    'last_refresh_sub_entrance_interval': 1494403967,
    'loc_mode': 7,
    'loc_time': 1494403856,
    'latitude': '39.993552831479164',
    'longitude': '116.51232601159914',
    'city': '%E5%8C%97%E4%BA%AC%E5%B8%82',
    'tt_from': 'pull',
    'lac': 4257,
    'cid': 28723,
    'cp': '58911a23cab7fq1',
    'iid': '10129229587',
    'device_id': '36255905281',
    'ac': 'wifi',
    'channel': 'xiaomi',
    'aid': 13,
    'app_name': 'news_article',
    'version_code': 612,
    'version_name': '6.1.2',
    'device_platform': 'android',
    'ab_version': '123182%2C112577%2C115754%2C114037%2C122834%2C113607%2C123191%2C114107%2C123186%2C125705%2C113608%2C122670%2C125743%2C125719%2C125503%2C125174%2C122471%2C104320%2C123176%2C112578%2C125192%2C124048%2C125391%2C122948%2C31210%2C124699%2C121011%2C114338%2C125068',
    'ab_client': 'a1%2Cc4%2Ce1%2Cf2%2Cg2%2Cf7',
    'ab_group': '100169',
    'ab_feature': '102749%2C94563',
    'abflag': 3,
    'ssmix': 'a',
    'device_type': 'HM+NOTE+1LTE',
    'device_brand': 'Xiaomi',
    'language': 'zh',
    'os_api': 19,
    'os_version': '4.4.4',
    'uuid': '866032028813695',
    'openudid': 'b11e7c8d5ef31f82',
    'manifest_version_code': 612,
    'resolution': '720*1280',
    'dpi': 320,
    'update_version_code': 6124,
    '_rticket': '1494403967410'
}


def request_host():
    r = requests.get("https://is.snssdk.com/api/news/feed/v53/", params=param, verify=False)
    data = r.json()['data']  # python 获取 data 数据部分
    # print r.text  # python 对象转 json


    # db_handle.list_insert('test', 'bbb', data)  # 数据入mongodb库

    # mysql_util.create_table()
    mysql_util.insert(data)  # 数据入库


request_host()
