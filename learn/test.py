a = ['apple', 'student', 'banana']
choice = 'apple'
if choice in a:
    print(f'Yes,{choice}')
else:
    print('Invalid choice')
print('apple' in a)


def info():
    print(666)


info()


def add(a,b):
    print(a+b)
    
    
add(1,3)

a = [x*y for x in range(1,10) for y in range(1,10)]
print(a)


import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0.05, 10, 1000)
y = np.sin(x)
plt.plot(x, y, ls="-.", lw=2, c="c", label="plot figure")
plt.legend()
plt.text(3.10, 0.09, "y=sin(x)", weight="bold", color="b")
plt.show()