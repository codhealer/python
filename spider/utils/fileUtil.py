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

def getFile(path,filename):
    mkdir(path)
    os.chdir(path)
    if not os.path.exists(filename):
        print(filename + ' is unexist')
        f = os.open(filename,os.O_CREAT|os.O_RDWR)
        pass
    f = open(filename,'w+')
    return f

if __name__ == '__main__':
    print('get file start')
    testfile = getFile('/Users/chenbin/codes/git/python/files','test.txt')
    testfile.write('ceshi')
    testfile.close()