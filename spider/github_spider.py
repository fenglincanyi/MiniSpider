# coding=utf-8
import json

import requests

from util import mongo_util
from util import mysql_util
from transform import github_transform

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
#
# param = {
#     'limit': '20',
#     'where': '{"type":"post"}',
#     'skip': '0',
#     'order': '-createdAt',
#     'include': 'user'
# }


def request_host():
    # github trends app 启动拉取的，本月
    r = requests.get("http://github.laowch.com/json/_monthly")
    # data = r.json()[u'data']  # python 获取 data 数据部分
    # print r.text  # python 对象转 json

    result = github_transform.data_transform(r.json())


    # db_handle.list_insert('test', 'bbb', data)  # 数据入库
    mysql_util.insert(result)
    # mysql_util.create_table()

request_host()
