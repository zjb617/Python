import os
os.chmod('oops.txt', 0o400)#设置只能被拥有者读
import stat
os.chmod('oops.txt', stat.S_IRUSR)
