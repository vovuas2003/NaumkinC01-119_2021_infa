import numpy as np
from math import *
import matplotlib.pyplot as plt

def func(x):
  return np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)

def print_func(y):
  x = np.linspace(0,16,100)
  fig = plt.figure()
  y = y(x)
  y2 = func(x)
  plt.plot(x, y, 'r')
  plt.plot(x, y2, 'g')
  plt.show()

k_array = np.array([[1, 1],
                    [15, 1]])
res = [func(1), func(15)]

k, b = np.linalg.solve(k_array, res)
print_func(lambda x: k * x + b)

k_array = np.array([[1, 1, 1],
                    [64, 8, 1],
                    [225, 15, 1]])
res = [func(1), func(8), func(15)]

k1, k2, b = np.linalg.solve(k_array, res)
print_func(lambda x: k1 * (x ** 2) + k2 * x + b)

k_array = np.array([[1, 1, 1, 1],
                    [4 ** 3, 4 ** 2, 4, 1],
                    [10 ** 3, 10 ** 2, 10, 1],
                    [15 ** 3, 15 ** 2, 15, 1]])
res = [func(1), func(4), func(10), func(15)]

k1, k2, k3, b = np.linalg.solve(k_array, res)
print_func(lambda x: k1 * (x ** 3) + k2 * (x ** 2) + k3 * x + b)
