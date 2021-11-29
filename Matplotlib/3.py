import random
import math
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 20, 0.01)
y = []
for i in x:
    z = np.log((i**2 + 1)*math.exp(-abs(i)/10))/np.log(1 + math.tan(1/(1 + (math.sin(i))**2)))
    y.append(z)
plt.plot(x, y)
plt.grid(True, linewidth=1)
plt.minorticks_on()
plt.grid(which='minor',color='k',linestyle=':')
plt.show()
