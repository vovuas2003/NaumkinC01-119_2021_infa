import random
import math
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-2, 2, 0.01)
y = -x**2 + 4
N = 10000
n = 0
for i in range(N):
    x1 = (random.random() - 0.5) * 4
    y1 = random.random() * 4
    plt.plot (x1, y1, 'ro')
    if y1 <= -x1**2 + 4:
        n += 1
plt.plot(x, y, 'b')
plt.show()
integral = 16 * n/N
print (integral)
