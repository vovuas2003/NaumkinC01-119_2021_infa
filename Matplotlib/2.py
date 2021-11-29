import random
import math
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 20, 0.01)
plt.plot(x, x*x - x - 6)
plt.grid(True, linewidth = 1)
plt.minorticks_on()
plt.grid(which='minor',color='k',linestyle=':')
plt.show()
