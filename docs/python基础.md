# 基本语法
- 设置编码
```
#!/usr/bin/python
# -*- coding: UTF-8 -*-
```
- 内置库，方法，对象
```
库：
    操作系统：os，shutil（文件管理）
    文件通配符：glob
    命令行：sys
    字符串正则：re，json
    数学工具：math，random
    日期时间：date，time
    数据压缩：zlib，gzip，bz2，zipfile，以及 tarfile
    性能度量：Timer
    测试：doctest，unittest
方法：
    控制台：print，input
    文件：open，file，dir，
    长度范围：len，range，reverse(反向)，next(下一个)，dict，slice，sort
    类型转换：tuple，set，list，map，repr（解释器读取的格式），iter（迭代器），eval
    数学方法：max，min，cmp，abs，pow，sum，hex，long，float，bin(二进制)，int，compile(复数)
    字符串：format，str，chr
```

- 条件判断
```
if 判断条件1:
    执行语句1……
elif 判断条件2:
    执行语句2……
elif 判断条件3:
    执行语句3……
else:
    执行语句4……
```
- 循环语句
```
while循环，for循环，嵌套循环
控制：break，continue，pass（占位符）
```
- 基本数据类型

1. Number（数字）
2. String（字符串）
```
拼接
格式化
```
3. List（数组）
4. Tuple（元组）：相当于final的数组
5. Dictionary（字典）：key-value结构
```
常用方法：
删除 del dict['KEY]
清空 dict.clear()
对比 dict.cmp(key1,key2)
长度 len(dict)
获取 dict.keys(),dict.values(),dict.items()
```
6. 日期和时间
```
需要import time对象
time对象>>
获取当前时间戳：time.time()
格式化：time.strftime(fmt[,tupletime])
calendar对象>>

```
7. 关键词
```
包，模块导入：
import [module] 和from ... import [导入包所有模块 from ... import *]

系统方法（前后双下划线）：
__name__，__init__，__main__，__del__，__setitem__，__getitem__，
__len__，__cmp__，__call__，
__add__，__sub__，__mul__，__div__，__mod__，__pow__

异常处理：
try:
    ...
except **Error:
    ...
    raise #重新抛出异常
finally:
    ...

面向对象：
    类：class xxx(super class):，方法 def f(args):
    类属性访问：self(推荐用self)，this
```
8. 包的引用
```
1.如果导入的模块和主程序在同个目录下，直接import就行了
2.如果导入的模块是在主程序所在目录的子目录下，可以在子目录中增加一个空白的__init__.py文件，该文件使得python解释器将子目录整个也当成一个模块，然后直接通过“import 子目录.模块”导入即可。
3.如果导入的模块是在主程序所在目录的父目录下，则要通过修改path来解决，有两种方法：
(1)通过”import sys，sys.path.append('父目录的路径')“来改变，这种方法属于一次性的，只对当前的python解释器进程有效，关掉python重启后就失效了。
(2)直接修改环境变量：在windows中是 “ set 变量=‘路径’  ” 例如：set PYTHONPATH=‘C:\test\...’ 查看是否设置成功用echo %PYTHONPATH%,而且进到python解释器中查看sys.path,会发现已经有了新增加的路径了。这　种方式是永久的，一次设置以后一直都有效。在linux中是 "export 变量=‘路径’ “，查看是" echo $变量 "
通过修改path是通用的方法，因为python解释器就是通过sys.path去一个地方一个地方的寻找模块的。
```