import os
name = 'oops.txt'
os.path.isfile(name)
os.path.isdir(name)
os.path.isdir('.')#一个.表示当前目录
os.path.isdir('..')#两个.表示上层目录
os.path.isabs(name)#isabs判断是否是一个绝对路径名
os.path.isabs('/big/fake/name')
os.path.isabs('big/fake/name/without/a/leading/slash')
