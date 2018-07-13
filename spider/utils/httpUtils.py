#!/usr/bin/python
# -*- coding:utf8 -*-

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}
def getHeader():
    return headers

def decodeHttpRes(content):
    # \xa9 is  (copyright) char; unsupport to decode
    return content.decode('utf-8','ignore').replace(u'\xa9', u'')