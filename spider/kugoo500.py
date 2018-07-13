#!/usr/bin/python
# -*- coding:utf8 -*-

import requests
from bs4 import BeautifulSoup
import time
from utils import httpUtil
def get_info(url):
    wb_data = requests.get(url,headers=httpUtil.getHeader())
    soup = BeautifulSoup(wb_data.text,'lxml')
    ranks = soup.select('span.pc_temp_num')
    titles = soup.select('div.pc_temp_songlist > ul > li > a')
    #print(titles)
    times = soup.select('span.pc_temp_time')
    #print(times)
    print("{}_{}_{}".format(ranks.__len__(),titles.__len__(),times.__len__()))
    for rank,title,time in zip(ranks,titles,times):
        #获取某个属性使用get
        data = {
            'rank':rank.get_text().strip(),
            'url':title.get("href"),
            'singer':title.get_text().split('-')[0],
            'song':title.get_text().split('-')[1],
            'time':time.get_text().strip()
        }
        print(data)

if __name__ == '__main__':
    urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html'.format(str(i)) for i in range(1,24)]
    for url in urls:
        get_info(url)
    time.sleep(1) #睡眠1秒