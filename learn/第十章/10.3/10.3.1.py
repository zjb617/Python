import subprocess
ret = subprocess.getoutput('date')
print(ret)

ret = subprocess.getoutput('date -u')
print(ret)

ret = subprocess.getoutput('date -u | wc')
print(ret)

ret = subprocess.check_output(['date', '-u'])
print(ret)

ret = subprocess.getstatusoutput('date')
print(ret)

ret = subprocess.call('date')
print(ret)

ret = subprocess.call('date -u', 'shell=True')

ret =  subprocess.call(['date','-u'])