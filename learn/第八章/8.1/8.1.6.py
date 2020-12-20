fin = open('bfile', 'rb')
print(fin.tell())
print(fin.seek(255))#seek还有第二个参数origin，若为0则从开头偏移255个字节；若为1，则从当前位置偏移255字节；若为2，则从末尾开始倒着偏移255字节(此时第一个参数一般为-255)

bdata = fin.read()
print(len(bdata))
print(bdata[0])

import os
print(os.SEEK_SET)#相当于seek第二个参数为0时
print(os.SEEK_CUR)#相当于seek第二个参数为1时
print(os.SEEK_END)#相当于seek第二个参数为2时

#读取最后一个字节的两种方法
#方法一
fin = open('bfile', 'rb')
print(fin.seek(-1, 2))
print(fin.tell())

bdata = fin.read()
print(len(bdata))
print(bdata[0])

#方法二 
fin = open('bfile', 'rb')
print(fin.seek(254,0))
print(fin.tell())
print(fin.seek(1,1))
print(fin.tell())
bdata = fin.read()
print(len(bdata))
print(bdata[0])