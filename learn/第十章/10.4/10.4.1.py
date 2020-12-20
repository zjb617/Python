from datetime import date
halloween = date(2014, 10, 31)
print(halloween)
print(halloween.day)
print(halloween.month)
print(halloween.year)
halloween.isoformat()

now = date.today()
print(now)
from datetime import timedelta
one_day = timedelta(days=1)
tomorrow = now + one_day
print(tomorrow)
print(now + 17*one_day)
yesterday = now - one_day
print(yesterday)

from datetime import time
noon = time(12, 0, 0)
print(noon)
print(noon.hour)
print(noon.minute)
print(noon.second)
print(noon.microsecond)

from datetime import datetime
some_day = datetime(2014, 1,2,3,4,5,6)
print(some_day)
print(some_day.isoformat())#T将日期和时间分隔开

now = datetime.now()
print(now)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon)
print(noon_today)

print(noon_today.date())
print(noon_today.time())