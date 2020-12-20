import time
now = time.time()
time.ctime(now)

fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
t = time.localtime()
print(t)
time.strftime(fmt, t)

from datetime import date,time
some_day = date(2014, 7, 4)
fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
some_day.strftime(fmt)

some_day = time(10,35)
some_day.strftime(fmt)

import time
fmt = "%Y-%m-%d"
#time.strptime("2012 01 29", fmt)报错
time.strptime("2012-01-29", fmt)


import locale
from datetime import date
halloween = date(2014, 10, 31)
for lang_country in ['en_us','fr_fr','de_de','es_es','is_is']:
    locale.setlocale(locale.LC_TIME, lang_country)
    halloween.strftime('%A,%B,%d')

names = locale.locale_alias.keys()
good_names = [name for name in names if \
len(name)==5 and name[2]=='_']
print(good_names[:5])
de = [name for name in good_names if name.startswith('de')]
print(de)