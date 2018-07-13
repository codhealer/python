# 使用vscode说明
vscode可以很方便支持前端的开发，有点加强版的sublime。
1. 有丰富的插件以及便捷的界面管理。
2. 可以使用分栏操作来编写md文件，特别方便
3. 以工作区为管理，可以将多个文件夹添加到工作区进行管理，感觉这点比idea更好
4. 可以方便的跟svn，git版本管理工具集成

# 工程说明
1. 开始说明
- 首先从github clone对应的分支到本地
- 然后将目录导入到工作区进行进行开发了

# requests返回结构
- status_code 返回码
- content 内容

# xpath使用

- xpath需要导入etree这个包（from lxml import etree)
- 获取html结构的内容：selector = etree.HTML(res.content)
- 根据xpath表达式进行选取节点：selector.xpath('xpath表达式')
- xpath表达式返回的都是一个数组，所以最后定位的时候，通过下标去获取
- xpath表达式内部下标都是从1开始算
- xpath表达式返回的都是一个节点数组：最后要获取节点的内容时需要用 node.xpath('string(.)') 获取【.代表当前节点】
# 坑点说明
- python 文件有中文编译不过去

```
在文件头添加
#!/usr/bin/python
# -*- coding:utf8 -*-
```