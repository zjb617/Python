import os
uid = 5
gid = 22
os.chown('oops', uid, gid)#此方法为Unix/Linux/Mac特有，Windows没有
