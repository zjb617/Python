bdata = bytes(range(0,256))
print(len(bdata))

fout = open('bfile', 'wb')#文件模式字符串中包含'b'(例如：'wb')，那么文件会以二进制模式打开，这时读写的是字节而不是字符串
fout.write(bdata)
fout.close()

fout = open('bfile', 'wb')
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(bdata[offset:offset+chunk])
    offset += chunk

fout.close()