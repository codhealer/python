#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import requests
from bs4 import BeautifulSoup
#from spider.httpUtil import getHeader
from utils import httpUtil
#也可以写程from spider.httpUtil import getHeader


def get_links(url,pattern):
    wb_data = requests.get(url,headers=httpUtil.getHeader())
    print(wb_data)
get_links('http://www.baidu.com','')