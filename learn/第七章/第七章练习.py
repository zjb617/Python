#练习1
import unicodedata
mystery = '\U0001f4a9'
print(mystery)
print(unicodedata.name(mystery))

print('-----------------')

#练习2
pop_bytes = mystery.encode('utf-8')
print(pop_bytes)

print('-----------------')

#练习3
pop_string = pop_bytes.decode('utf-8')
print(pop_string)
print(pop_string == mystery)

print('-----------------')

#练习4
poem = '''
My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s.
'''
args = ('roast beef', 'ham', 'head','clam')
print(poem % args)

print('--------------------')

#练习5
letter = '''
Dear {salutation} {name},

Thank you for your letter.  We are sorry that our {product} {verb} in your
{room}. Please note that it should never be used in a {room}, especially
near any {animals}.

Send us your receipt and {amount} for shipping and handling. We will send
you another {product} that, in our tests, is {percent}% less likely to
have {verbed}.

Thank you for your support.

Sincerely,
{spokesman}
{job_title}
'''

print('---------------------')

#练习6
response = {
    'salutation': 'Colonel',
    'name': 'Hackenbush',
    'product': 'duck blind',
    'verb': 'imploded',
    'room': 'conservatory',
    'animals': 'emus',
    'amount': '$1.38',
    'percent': '1',
    'verbed': 'imploded',
    'spokesman': 'Edgar Schmeltz',
    'job_title': 'Licensed Podiatrist'
    }
print(letter.format(**response))

print('---------------------')

#练习7
mammoth = '''
We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.

All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.

Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.364 ｜ 附录 E

May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.

Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.

We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon.
'''

print('-----------------------')

#练习8
import re
pat = r'\bc\w*'#若不加r，则python会将\b解释为退格字符，查找不到
print(re.findall(pat, mammoth))

print('--------------------')

#练习9
pat = r'\bc\w{3}\b'#最后的\b 指明单词的结束，如果不用，则会得到所有以c开头并且至少有四个字母单词的前四个字母
print(re.findall(pat, mammoth))

print('---------------------')

#练习10
pat = r'\b\w*r\b'#对r结尾的单词得到完美结果
print(re.findall(pat, mammoth))

pat = r'\b\w*l\b'
print(re.findall(pat, mammoth))#但是这就出现问题了（ll都出来了）
#解决方法一
pat = r'\b[\w\']*l\b'
print(re.findall(pat, mammoth))
#解决方法二
pat = r"\b[\w']*l\b"#注意是双引号
print(re.findall(pat, mammoth))

print('--------------------------')

#练习11
pat = r'\b\w*[aeiou]{3}[^aeiou]\w*\b'
print(re.findall(pat, mammoth))
pat = r'\b\w*[aeiou]{3}[^aeiou\s]\w*\b'
print(re.findall(pat, mammoth))
pat = r'\b\w*[aeiou]{3}[^aeiou\s]*\w*\b'
print(re.findall(pat, mammoth))

print('--------------------------')

#练习12
import binascii
hex_str = '47494638396101000100800000000000ffffff21f9' + \
    '0401000000002c000000000100010000020144003b'
gif = binascii.unhexlify(hex_str)
print(len(gif))

print('-------------------------')

#练习13
print(gif[:6] == 'GIF89a')
print(gif[:6] == b'GIF89a')
print(type(gif))
print(type('GIF89a'))
print(type(b'GIF89a'))

print('-------------------------')

#练习14
import struct
width, height = struct.unpack('<HH', gif[6:10])
print(width,height)