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