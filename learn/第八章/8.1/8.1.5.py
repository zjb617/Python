#使用with关闭文件
poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''
with open('relativity', 'wt') as fout:
    fout.write(poem)
