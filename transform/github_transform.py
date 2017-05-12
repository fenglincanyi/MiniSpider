# coding=utf-8
import copy
import re


def data_transform(source):
    # 存储方式:
    # [{A:{},B:[{},{}]}, {...}]

    resultList = []

    if source:
        for element in source:
            contributors = copy.copy(element.get('contributors'))

            if not element.get('language'):
                element[u'language'] = u'unknown'

            del element['contributors']

            resultList.append({u'project': element, u'contributors': contributors})

    return resultList


# 去表情
emoji_pattern = re.compile(
    u"(\ud83d[\ude00-\ude4f])|"  # emoticons
    u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
    u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
    u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
    u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
    "+", flags=re.UNICODE)

def remove_emoji(text):
    return emoji_pattern.sub(r'', text)