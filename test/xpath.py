#!/usr/bin/python
#encoding:utf-8
from lxml import etree
 
 
s = '''<html>
        <header><title>hello world</title></header>
        <body>
            <div>
                <h1>Hello World</h1>
            </div>
            <div>
                <span>test</span>
            </div>
        </body>
        </html>'''
xpath = '/html/body/div'
selector = etree.HTML(s)
content = selector.xpath(xpath)
for i in content:
    print(i)
print(u"************ 华丽分割符1 ************")