import pickle
import datetime
now1 = datetime.datetime.utcnow()#获取世界标准时区的当前时间
pickled = pickle.dumps(now1)
now2 = pickle.loads(pickled)
print(now1)
print(now2)

class Tiny():
    def __str__(self):
        return 'tiny'

obj1 = Tiny()
print(obj1)
print(str(obj1))
pickled = pickle.dumps(obj1)
print(pickled)
obj2 = pickle.loads(pickled)
print(obj2)
print(str(obj2))