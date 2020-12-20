import multiprocessing
import os
def do_this(what):
    whoami(what)

def whoami(what):
    print('Process %s says: %s' %(os.getpid(),what))

if __name__ == "__main__":#__name__是当前模块名，__main__是模块被直接运行时的模块名
    whoami("I'm the main program")
    for n in range(4):
        p = multiprocessing.Process(target=do_this,
            args=("I'm function %s" % n,))
        p.start()