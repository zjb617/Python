#练习1
class Thing:
    pass
print(Thing)
example = Thing()
print(example)

print('-----------')

#练习2
class Thing2:
    letters = 'abc'

print(Thing2.letters)

print('-----------')

#练习3
class Thing3:
    def __init__(self):
        self.letters = 'xyz'

#print(Thing3.letters)报错原因，letters是实例对象的特性，而不是类Thing的
something = Thing3()
print(something.letters)

print('-----------')

#练习4
class Element:
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number

hydrogen = Element('Hydrogen', 'H', 1)

print('-----------')

#练习5
el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(el_dict['name'],el_dict['symbol'],el_dict['number'])
print(hydrogen.name)
#第二行可以写成
hydrogen = Element(**el_dict)

print(hydrogen.name)

print('-----------')

#练习6
class Element:
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print('name=%s, symbol=%s, number=%s' %(self.name,self.symbol,self.number))

hydrogen = Element(**el_dict)
hydrogen.dump()

print('-----------')

#练习7
print(hydrogen)
class Element:
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return ('name=%s,symbol = %s,number = %s' %(self.name, self.symbol,self.number))

hydrogen = Element(**el_dict)
print(hydrogen)

print('-----------------------')

#练习8
class Element:
    def __init__(self,name,symbol,number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    @property
    def name(self):
        return self.__name
    @property
    def symbol(self):
        return self.__symbol
    @property
    def number(self):
        return self.__number

hydrogen = Element('Hydrogen', 'H', 1)
hydrogen.name
hydrogen.symbol
hydrogen.number

print('--------------')

#练习9
class Bear:
    def eats(self):
        return 'berries'

class Rabbit:
    def eats(self):
        return 'clover'

class Octothorpe:
    def eats(self):
        return  'campers'

b = Bear()
r = Rabbit()
o = Octothorpe()
print(b.eats())
print(r.eats())
print(o.eats())

print('--------------')

#练习10
class  Laser:
    def does(self):
        return 'disintegrate'

class Claw:
    def does(self):
        return 'crush'

class SmartPhone:
    def does(self):
        return 'ring'

class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone  = SmartPhone()
    def does(self):
        return '''I have many attachments:
My laser, to %s.
My claw, to %s.
My smartphone, to %s.'''% (
    self.laser.does(),
    self.claw.does(),
    self.smartphone.does() )

robbie = Robot()
print(robbie.does())
