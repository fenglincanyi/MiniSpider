# coding=utf-8
import json

import requests

from util import db_handle

header = {
    'X-LC-Prod':'1',
    'X-LC-Session':'',
    'X-LC-Id': 'mhke0kuv33myn4t4ghuid4oq2hjj12li374hvcif202y5bm6',
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'User-Agent': 'AVOS Cloud android-v3.16.4 SDK',
    'X-LC-Sign': '8ed1d122688346866173822864df30a2,1494401683768',
    'X-Android-RS': '1',
    'Host': 'api.leancloud.cn',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip'
}

param = {
    'limit': '20',
    'where': '{"type":"post"}',
    'skip': '0',
    'order': '-createdAt',
    'include': 'user'
}


def request_host():
    # 搜索 -> 专栏
    r = requests.get("https://api.leancloud.cn/1.1/classes/Entry", params=param, headers=header, verify=False)
    # data = r.json()[u'data']  # python 获取 data 数据部分
    print r.text  # python 对象转 json

    # db_handle.list_insert('test', 'bbb', data)  # 数据入库


request_host()
