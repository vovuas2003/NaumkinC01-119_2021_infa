import random
import math
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return -x*x+4
x = np.arange(-2, 2, 0.01)
y = -x**2 + 4
N = 10000
su=0
for i in range(N):
    x1 = (random.random() - 0.5) * 4
    y1 = random.random() * 4
    plt.plot (x1, y1, 'go')
    su=su+f(x1)
plt.plot(x, y, 'b')
plt.show()
otv=4*su/N
print(otv)
