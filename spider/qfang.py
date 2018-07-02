#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import requests
from bs4 import BeautifulSoup
#from spider.httpUtil import getHeader
from spider import httpUtil
#也可以写程from spider.httpUtil import getHeader
def init():
    pypath = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../utils')
    sys.path.append(pypath)
init()

def get_links(url,pattern):
    wb_data = requests.get(url,headers=httpUtil.getHeader())
    print(wb_data)
get_links('http://www.baidu.com','')