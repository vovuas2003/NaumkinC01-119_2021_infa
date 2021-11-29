import random
import math
import numpy as np
import matplotlib.pyplot as plt
eq = input()
x = np.arange(-20, 20, 0.01)
plt.plot(x, eval(eq))
plt.grid(True, linewidth = 1)
plt.minorticks_on()
plt.grid(which='minor',color='k',linestyle=':')
plt.show()
