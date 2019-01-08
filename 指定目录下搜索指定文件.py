#只能找到一个，不能找到该目录下所有的文件
import os


def sefile(spath, sfile):
    for sdir, sudir, file in os.walk(spath):
        a = sdir
        b = sudir
        c = file
        print(a)
        if sfile in file:
            return sfile, sdir
    return None


spath = input('请输入路径:')
sfile = input('请输入要查找的文件名：')
f = sefile(spath, sfile)
if f:
    print('文件%s在%s中被发现' % (f[0], f[1]))
else:
    print('未找到文件%s' % sfile)