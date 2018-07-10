import requests
import re
import time
import os
from utils import httpUtils
from utils import fileUtil
from lxml import etree
#//*[@id="main"]/div/div[2]/ul
def get_links(url,index):
    # open file
    zfile = fileUtil.getFile('/Users/chenbin/codes/git/python/files','zhipin'+index+'.txt')
    # get url content
    res = requests.get(url,headers=httpUtils.getHeader())
    # beautiful the html content
    print(res.content.decode('utf-8'))
    selector = etree.HTML(res.content.decode('utf-8'))
    # find the content
    contents = selector.xpath('//*[@id="main"]/div/div[@class="job-list"]/ul/li')
    # write content into file
    for content in contents:
        zw_name = content.xpath('div/div[1]/h3/a/div[1]/text()')
        zw_xinchou = content.xpath('div/div[1]/h3/a/span[1]/text()')
        zw_diqu = content.xpath('div/div[1]/p/text()[1]')
        zw_jingyan = content.xpath('div/div[1]/p/text()[2]')
        zw_xueli = content.xpath('div/div[1]/p/text()[3]')
        zfile.write(str(zw_name)
            +'|'+str(zw_xinchou)
            +'|'+str(zw_diqu)
            +'|'+str(zw_jingyan)
            +'|'+str(zw_xueli)
            +'\n')
        pass
    zfile.close()
    pass

if __name__ == '__main__':
    urls = [format(str(i)) for i in range(1,10)]
    for i in range(1,10):
        url = 'https://www.zhipin.com/c101280600/?page={}&ka=page-2'.format(str(i))
        print('=====> getContent:'+url)
        get_links(url,str(i))
        time.sleep(1)
        pass