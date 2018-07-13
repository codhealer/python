#!/usr/bin/python
# -*- coding:utf8 -*-
import requests
import re
import time
import os
from utils import httpUtils
from utils import fileUtil
from lxml import etree
from bs4 import BeautifulSoup
currentPath = os.getcwd()
err_file = fileUtil.getFileMode(currentPath+'/files/p2peye','p2perror.txt','a+')
def get_links(url,index):
    # open file
    zfile = fileUtil.getFile(currentPath+'/files/p2peye/files/','p2peye'+index+'.txt')
    # get url content
    res = requests.get(url,headers=httpUtils.getHeader())
    # beautiful the html content
    selector = etree.HTML(httpUtils.decodeHttpRes(res.text))
    # find the content
    # //*[@id="nv_platform"]/div[@class="qt-w clearfix"]/ul[@class="ui-result clearfix"/li
    contents = selector.xpath('//*[@id="nv_platform"]/div[@class="qt-w clearfix"]/div[@class="qt-w890 qt-gl"]/ul[@class="ui-result clearfix"]/li')
    # write content into file
    print("xpath contents :>>>>>>>" + str(contents))
    '''
    
<a href="//tuandai.p2peye.com" class="ui-result-ablock clearfix" target="_blank" title="团贷网">
            <div class="ui-result-left">
              <p class="ui-result-text">预期利率：<strong class="ui-color-red">10.55%</strong></p>
              <p class="ui-result-text">运营状态： 正常运营6年 </p>
            </div>
            <div class="ui-result-middle">
              <div class="clearfix">
                <p class="ui-result-text ui-result-capital">注册资本：10293万 </p>
                <p class="ui-result-text ui-result-address">注册地：广东省|东莞市</p>
              </div>
              <p class="ui-result-text">用户评价 ：
                                [安全]
                                [靠谱]
                                [背景强大]
                                <span class="ui-color-blue">92%</span>好评度， <span class="ui-color-blue">4978</span>人点评</p>
            </div>
          </a>
    '''
    zfile.write("名字,资本,地址,状态,连接")
    for content in contents:
        tagNode = content.xpath("div[1]/div[2]/a[1]")[0]
        
        n_title = tagNode.xpath('string(@title)')
        n_url = "https:"+tagNode.xpath('string(@href)')
        n_rate = tagNode.xpath('string(div[@class="ui-result-left"]/p[1]/strong)')
        n_status = tagNode.xpath('string(div[@class="ui-result-left"]/p[2])')
        n_capital = tagNode.xpath('string(div[@class="ui-result-middle"]/div[1]/p[1])').replace(',','')
        n_address = tagNode.xpath('string(div[@class="ui-result-middle"]/div[1]/p[2])')

        n_result = n_title + "," + n_capital + "," + n_address + "," + n_status + "," + n_url
        zfile.write(n_result+"\n")
        if("正常" not in str(n_status)):
            err_file.write(n_result+"\n")
            pass
        # zfile.write(str(zw_name)
        #     +'|'+str(zw_xinchou)
        #     +'|'+str(zw_diqu)
        #     +'|'+str(zw_jingyan)
        #     +'|'+str(zw_xueli)
        #     +'\n')
        pass
    zfile.close()
    pass
## https://www.p2peye.com/platform/all/p217/
if __name__ == '__main__':
    for i in range(22,218):
        url = 'https://www.p2peye.com/platform/all/p{}/'.format(str(i))
        print('=====> getContent:'+url)
        get_links(url,str(i))
        time.sleep(1)
        pass
    err_file.close()