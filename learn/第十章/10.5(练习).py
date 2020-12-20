from datetime import date, datetime, timedelta
now = date.today()
now_str = now.isoformat()
with open('today', 'wt') as output:
    print(now_str, file=output)

with open('today', 'rt') as input:
    today_string = input.read()

print(today_string)

fmt = '%Y-%m-%d\n'
datetime.strptime(today_string, fmt)

import os
print(os.listdir('.'))

print(os.listdir('..'))


import multiprocessing
def now(seconds):
    from datetime import datetime
    from time import sleep
    sleep(seconds)
    print('wait', seconds, 'seconds, time is', datetime.utcnow())

if __name__ == '__main__':
    import random
    for n in range(3):
        seconds = random.random()
        proc = multiprocessing.Process(target=now, args=(seconds,))



my_day = date(1982, 8, 14)

my_day.weekday()
my_day.isoweekday()
#使用函数 weekday()，周一返回 0，周日返回 6。而使用函数 isoweekday()，周一返回1，周日返回 7。

party_day = my_day + timedelta(days=10000)
print(party_day)