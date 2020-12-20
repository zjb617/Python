fin = open('relativity', 'rt')
poem = fin.read()#无参数则一次性读完
fin.close()
print(len(poem))

poem = ''
fin = open('relativity', 'rt')
chunk = 100
while True:
    fragment = fin.read(chunk)#一次读取100个字符
    if not fragment:
        break
    poem += fragment

fin.close()
print(len(poem))

poem = ''
fin = open('relativity', 'rt')
while True:
    line = fin.readline()#每次读取一行，空行也读（\n）
    if not line:
        break
    poem  += line

fin.close()
print(len(poem))

#18~27可简化为
poem = ''
fin = open('relativity', 'rt')
for line in fin:
    poem += line

fin.close()
print(len(poem))

#
fin = open('relativity', 'rt')
lines = fin.readlines()#readlines以列表形式返回
fin.close()
print(len(lines), 'lines read')
for line in lines:
    print(line, end='')