from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __repr__(self):#使用%r时自动调用repr，%s调用str
        return 'Vector(%r, %r)' %(self.x, self.y)#%r用来做调试（debug）比较好，因为它会显示变量的原始数据（rawdata），而%s和其他的符号则是用来向用户显示输出的。

    def __abs__(self):
        return hypot(self.x, self.y)#返回欧几里得范数，一般即为向量的模长

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self,scalar):
        return Vector(self.x * scalar, self.y * scalar)