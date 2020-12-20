import time
now = time.time()
print(now)

time.ctime(now)

time.localtime(now)
time.gmtime(now)
tm = time.localtime(now)
time.mktime(tm)
