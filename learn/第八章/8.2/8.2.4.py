menu = \
{
'breakfast': {
        'hours':'7-11',
        'items': {
            'breakfast burritos': '$6.00',
            'pancakes': '$4.00'
            }
        },
'lunch': {
        'hours': '11-3',
        'items': {
            'hamburger': '$5.00'
            }
        },
'dinner': {
        'hours': '3-10',
        'items': {
                'spaghetti': '$8.00'
                }
        }
}

import json
menu_json = json.dumps(menu)#将menu编码成JSON字符串
print(menu_json)

menu2 = json.loads(menu_json)#将JSON字符串解析成Python的数据结构
print(menu2)

import datetime
now = datetime.datetime.utcnow()
print(now)
#json.dumps(now)#报错原因：标准 JSON 没有定义日期或者时间类型，需要自定义处理方式。

now_str = str(now)
print(json.dumps(now_str))
from time import mktime
now_epoch = int(mktime(now.timetuple()))
print(json.dumps(now_epoch))

class DTEncoder(json.JSONEncoder):
    def default(self,obj):
        #isinstance()检查obj的类型
        if isinstance(obj, datetime.datetime):#判断obj是不是datetime.datetime的对象
            return int(mktime(obj.timetuple()))
        #否则是普通解码器知道的东西:
        return json.JSONEncoder.default(self, obj)

print(json.dumps(now, cls=DTEncoder))

print(type(now))
print(isinstance(now, datetime.datetime))
print(type(234))
print(isinstance(234, int))
print(type('hey'))
print(isinstance('hey', str))