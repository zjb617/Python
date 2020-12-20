fin = open('bfile', 'rb')
bdata = fin.read()
print(len(bdata))
fin.close()