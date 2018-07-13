#!/usr/bin/python
# -*- coding:utf8 -*-

import os

def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)

    if not isExists:
        os.makedirs(path)
        print(path + ' is unexist')
        return True
    else:
        return False

# 使用mode方式打开文件
def getFileMode(path,filename,mode):
    mkdir(path)
    os.chdir(path)
    if not os.path.exists(filename):
        print(filename + ' is unexist')
        f = os.open(filename,os.O_CREAT|os.O_RDWR)
        pass
    f = open(filename,mode)
    return f

# 默认使用覆盖的方式打开文件
def getFile(path,filename):
    return getFileMode(path,filename,'w+')

def getProjectPath():
    return os.getcwd()

if __name__ == '__main__':
    print('get file start')
    print(getProjectPath())
    getFile("files\p2peye","test.txt")
    # testfile = getFile('/Users/chenbin/codes/git/python/files','test.txt')
    # testfile.write('ceshi')
    # testfile.close()