# coding=utf-8
import requests
import json

param = {
    'action': 'pull',
    'before_id': 1000,
    'limit': 20,
    'action_feed': True,
    'session_token': '9743215cbfdec3dd94ce1686'
}

header = {
    'Cache-Control': 'no-cache',
    'Accept-Encoding': 'gzip',
    'Authorization': 'Bearer gt2.0AAAAAATpzHELPBksK0JwAAAAAAxNVQJgAgCZkl1SJEn_kzNS0HydXjWc8Wb4cg==',
    'Cookie': 'acw_tc=AQAAAA/1+V8XrwcAJTUscfHQSwrYk7SJ; aliyungf_tc=AQAAAO5bYn8WnAcAJTUscZPP4wmiIsR8',
    'User-Agent': 'Futureve/4.50.0 Mozilla/5.0 (Linux; Android 4.4.4; HM NOTE 1LTE Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 Google-HTTP-Java-Client/1.22.0 (gzip)',
    'x-api-version': '3.0.57',
    'x-app-version': '4.50.0',
    'x-app-za': 'OS=Android&Release=4.4.4&Model=HM+NOTE+1LTE&VersionName=4.50.0&VersionCode=481&Width=720&Height=1280&Installer=%E5%B0%8F%E7%B1%B3%E5%95%86%E5%BA%97&WebView=33.0.0.0',
    'x-app-build': 'release',
    'x-udid': 'AHBCKywZPAtLBVjPnrywfqxyTPwNAbEmLIc=',
    'Host': 'api.zhihu.com',
    'Connection': 'Keep-Alive'
}

# while(True):


r = requests.get("https://api.zhihu.com/topstory", params=param, headers=header, verify=False)
data = r.json()[u'data']  # python 获取 data 数据部分
print json.dumps(data)  # python 对象转 json
