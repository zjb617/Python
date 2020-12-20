#1.使用match()进行准确匹配
import re
source = 'Young Frankenstein'
m = re.match('You', source)
if m:
    print(m.group())
    
m = re.match('^You', source)#起始描点
if m:
    print(m.group())

m = re.match('Frank', source)#match只能检测开头
if m:
    print(m.group())

m = re.search('Frank', source)#search可以检测任何位置
if m:
    print(m.group())

m = re.match('.*Frank', source)  #  . 代表任何单一字符   * 代表任意一个它之前的字符 .* 代表任意多个字符（包括 0 个）
if m:
    print(m.group())

print('---------------')

#2.使用search()寻找首次匹配
m = re.search('Frank', source)
if m:
    print(m.group())

print('-------------')

#3.使用findall()寻找所有匹配
m = re.findall('n',source)
print(m)
print('Found', len(m), 'matches')

m = re.findall('n.', source)#.的意义看上面
print(m)

m = re.findall('n.?', source)#加个?代表可选
print(m)

print('-------------')

#4.使用split()按匹配切分
m = re.split('n',source)
print(m)

print('-------------')

#5.使用sub()替换匹配
m = re.sub('n','?',source)
print(m)

print('-------------')

#6.特殊的字符
import string
printable = string.printable
len(printable)
print(printable[0:50])
print(printable[50:])

t1 = re.findall('\d', printable)
print(t1)

t2 = re.findall('\w', printable)
print(t2)

t3 = re.findall('\s', printable)
print(t3)

x = 'abc' + '-/*' + '\u00ea' + '\u0155'
t3 = re.findall('\w', x)
print(t3)

print('---------------------')

#模式:使用标识符
source = '''I wish I may, I wish I might
Have a dish of fish tonight.'''
t4 = re.findall('wish', source)
print(t4)
t5 = re.findall('wish|fish', source)
print(t5)
t6 = re.findall('^wish', source)
print(t6)
t7 = re.findall('wish$', source)
print(t7)
t8 = re.findall('fish tonight\.$', source)
print(t8)
t9 = re.findall('[wf]ish', source)#以 w 或 f 开头，后面紧接着 ish 的匹配
print(t9)
t10 = re.findall('[wsh]+', source)#以若干个 w、 s 或 h 组合的匹配
print(t10)
t11 = re.findall('ght\W', source)#r注意大写W，查询以 ght 开头，后面紧跟一个非数字非字母字符的匹配
print(t11)
t12 = re.findall('I (?=wish)', source)#查询以 I 开头，后面跟着 wish 的匹配（wish 出现次数尽量少）
print(t12)
t13 = re.findall('(?<=I) wish',source)#最后查询以 wish 结尾，前面为 I 的匹配（I 出现的次数尽量少）
print(t13)
#有时，正则表达式的语法可能会与python本身的语法冲突。例如：
t14 = re.findall('\bfish', source)#我们期望其能匹配到任何以fish开头的词
print(t14)#但是未能匹配成功
#\b，它在字符串中代表退格，但在正则表达式中，它代表一个单词的开头位置。
#所以要使用正则表达式，则：
t15 = re.findall(r'\bfish', source)#告诉python这是一个正则表达式
print(t15)

print('-------------------------')

#8.模式：定义匹配的输出
m = re.search(r'(. dish\b).*(\bfish)', source)
print(m.group())
print(m.groups())

m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
print(m.group())
print(m.groups())
print(m.group('DISH'))
print(m.group('FISH'))
