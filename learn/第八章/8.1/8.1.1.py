poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''
print(len(poem))
fout = open('relativity', 'wt')
fout.write(poem)#返回字节数
fout.close()
fout = open('relativity', 'wt')
print(poem, file=fout)#同样返回字节数，但是print() 默认会在每个参数后面添加空格， 在每行结束处添加换行。
fout.close()
#除非自定义参数，否则print()会使用默认参数
fout = open('relativity', 'wt')
print(poem, file=fout, sep='',end='')
fout.close()

#如果源字符串非常大，可以将数据分块，直到所有字符串被写入
fout = open('relativity', 'wt')
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset:offset+chunk])
    offset += chunk

fout.close()
#如果'relativity'文件已经存在，使用模式x可以避免重写文件
#fout = open('relativity', 'xt')
#加一个异常处理
try:
    fout = open('relativity', 'xt')
    fout.write('stomp stomp stomp')
except FileExistsError:
    print('relativity already exists!. That was a close one.')

