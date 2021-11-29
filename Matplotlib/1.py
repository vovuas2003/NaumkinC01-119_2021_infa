import random
import math
import numpy as np
import matplotlib.pyplot as plt
N = [100, 1000, 10000, 100000]
mu, sigma = 0, 1
sp = plt.subplot(221)
x = mu + sigma * np.random.randn(N[0])
n, bins, patches = plt.hist(x, facecolor='g')
plt.grid(True)
sp = plt.subplot(222)
x = mu + sigma * np.random.randn(N[1])
n, bins, patches = plt.hist(x, facecolor='r')
plt.grid(True)
sp = plt.subplot(223)
x = mu + sigma * np.random.randn(N[2])
n, bins, patches = plt.hist(x, facecolor='b')
plt.grid(True)
sp = plt.subplot(224)
x = mu + sigma * np.random.randn(N[3])
n, bins, patches = plt.hist(x)
plt.grid(True)
plt.show()
