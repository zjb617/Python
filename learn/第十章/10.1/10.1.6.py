import os
os.link('oops.txt', 'yikes.txt')
os.path.isfile('yikes.txt')
os.path.islink('yikes.txt')
os.symlink('oops.txt', 'jeepers.txt')
os.path.islink('jeepers.txt')