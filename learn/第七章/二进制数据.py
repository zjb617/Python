blist = [1,2,3,255]
the_bytes = bytes(blist)
print(the_bytes)
the_byte_array = bytearray(blist)
print(the_byte_array)
print(b'\x61')
print(b'\x01abc\xff')

#the_bytes[1] = 127#报错说明bytes类型的不可变性
#但是bytearray类型的变量是可变的
the_byte_array = bytearray(blist)
print(the_byte_array)
the_byte_array[1] = 127
print(the_byte_array)

the_bytes = bytes(range(0,256))
the_byte_array = bytearray(range(0,256))
print(the_bytes)
print(the_byte_array)

print('------------------')

#使用struct转换二进制数据
import struct
valid_png_header = b'\x89PNG\r\n\x1a\n'
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
    b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
if data[:8] == valid_png_header:
    width, height = struct.unpack('>LL', data[16:24])#>LL也可以写成>2L
    print('Valid PNG, width', width, 'height', height)
else:
    print('Not a valid PNG')

print(data[16:20])
print(data[20:24])
print(0x9a, 0x8d)

import struct
print(struct.pack('>L', 154))
print(struct.pack('>L', 141))

struct.unpack('>16x2L6x', data)


# 使用大端方案（>）
# 跳过 16 个字节（16x）
# 读取 8 字节内容——两个无符号长整数（2L）
# 跳过最后 6 个字节（6x）

#其他二进制数据工具
# from construct import Struct, Magic, UBInt32, Const, String
# fmt = Struct('png',
#     Magic(b'\x89PNG\r\n\x1a\n'),
#     UBInt32('length'),
#     Const(String('type', 4), b'IHDR'),
#     UBInt32('width'),
#     UBInt32('height')
#     )
# data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
#     b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
# result = fmt.parse(data)
# print(result)
# print(result.width, result.height)#不知为什么此模块无用

#使用binascii()转换字节/字符串
import binascii
valid_png_header = b'\x89PNG\r\n\x1a\n'
print(binascii.hexlify(valid_png_header))
#反过来转换也可以:
print(binascii.unhexlify(b'89504e470d0a1a0a'))

#位运算符------>参考《Python语言及其运用》P149  位运算符


print('------------BIG--------------')