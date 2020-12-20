# 覆盖
class Person():
    def __init__(self, name):
        self.name = name


class EmailPerson(Person):
    def __init__(self, name, email):
        # 不直接使用self.name = name的原因:如果 Person 类的定义在未来发生改变，使用 super() 可以保证这些改变会自动反映
        super().__init__(name)
        # 到 EmailPerson 类上，而不需要手动修改。
        self.email = email


bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
print(bob.name)
print(bob.email)


print('---------------------------')


# 使用属性对特性进行访问和设置
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print('inside the getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)


fowl = Duck('Howard')
print(fowl.name)  # 访问特性调用get_name()

print(fowl.get_name())  # 显式调用

fowl.name = 'Daffy'  # 对name执行赋值操作是，调用set_name()
print(fowl.name)

fowl.set_name('Daffy')  # 显式调用
print(fowl.name)


print('-------------------')


# 定义属性之修饰符
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name


# 此时不可用显式调用
fowl = Duck('Howard')
print(fowl.name)
fowl.name = 'Donald'
print(fowl.name)


print('--------------')


# 属性还可以指向一个计算结果值
class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius


c = Circle(5)
print(c.radius)
print(c.diameter)
c.radius = 7
print(c.diameter)
#c.diameter = 20  # 报错原因:没有指定其setter属性，无法从类的外部对它的值进行设置


print('------------------------')


#使用名称重整保护私有特性
class Duck():
    def __init__(self,input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self,input_name):
        print('inside the setter')
        self.__name = input_name


fowl = Duck('Howard')
print(fowl.name)
fowl.name = 'Donald'
print(fowl.name)
#fowl.__name#python将其名字重整，让外部的代码无法使用


print('----------')


#方法的类型
#   1.类方法(class method)
class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print('A has',cls.count,"little objects.")


easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()#将A传入参数cls

#   2.静态方法(static method)66666
class Coyoteweapon():
    @staticmethod
    def commerical():
        print('This CoyoteWeapon has been brought to you by Acme')


Coyoteweapon.commerical()#不用创建对象即可调用类里的方法


print('-----------------------')


#鸭子类型
#多态
class Quote():
    def __init__(self,person,words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'


hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), 'says:', hunter.says())

hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
print(hunted1.who(), 'says:',hunted1.says())

hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
print(hunted2.who(), 'says:', hunted2.says())

class BabblingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'

brook = BabblingBrook()

def who_says(obj):
    print(obj.who(), 'says:', obj.says())

who_says(hunter)
who_says(hunted1)
who_says(hunted2)
who_says(brook)


print('---------------------')


#特殊方法
class Word():
    def __init__(self, text):
        self.text = text

    def equals(self, word2):
        return self.text.lower() == word2.text.lower()


first = Word('ha')
second = Word('HA')
third = Word('eh')

print(first.equals(second))
print(first.equals(third))

class Word():
    def __init__(self,text):
        self.text = text
    def __eq__(self,word2):
        return self.text.lower() == word2.text.lower()


first = Word('ha')
second = Word('HA')
third = Word('eh')

print(first == second)
print(first == third)#除__eq__外还有很多其他的特殊方法，请参考《Python语言及其应用》P122，此处再介绍__str__()和__repr__()

class Word():
    def __init__(self,text):
        self.text = text
    def __eq__(self,word2):
        return self.text.lower() == word2.text.lower()
    def __str__(self):
        return self.text
    def __repr__(self):
        return Word( self.text )


first = Word('ha')
print(first)


print('------------')


#组合
class Bill():
    def __init__(self,description):
        self.description = description

class Tail():
    def __init__(self,length):
        self.length = length

class Duck():
    def __init__(self,bill,tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('This duck has a', bill.description, 'bill and a', tail.length, 'tail')


tail = Tail('long')
bill = Bill('wide orange')
duck = Duck(bill, tail)
duck.about()


print('----------------')


#命名元组
from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')#第一个参数为元组名称，第二个参数可以是 空格隔开的字符串，也可以是字符串组成的列表
duck = Duck('wide orange', 'long')
print(duck)
print(duck.bill)
print(duck.tail)


#也可用字典构造一个命名元组
parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)#相当于duck2 = Duck(bill = 'wide orange', tail = 'long')
print(duck2)
duck3 = duck2._replace(tail = 'magnificant', bill = 'crushing')
print(duck3)
#字典可以添加新的域(键值对)
duck_dict = {'bill':'wide orange', 'tail':'long'}
print(duck_dict)
duck_dict['color'] = 'green'
print(duck_dict)
#但是命名元组不行
#duck.color = 'green'

#命名元组总结
# 1.它无论看起来还是使用起来都和不可变对象非常相似
# 2.与使用对象相比，使用命名元组在时间和空间上效率更高
# 3.可以使用点号.对特性进行进行访问，而不需要使用字典风格的方括号
# 4.可以把它作为字典的键
