import math
import numpy as np
def number1():
    return np.arange(12,43)
def number2():
    a=np.zeros(12)
    a[4]=1
    return a
def number3():
    a=np.arange(0,9,1).reshape(3, 3)
    return a
def number4():
    a=np.array([1,2,0,0,4,0])
    a=a[a>0]
    return a
def number5():
    a1=np.arange(15).reshape(5,3)
    a2=np.arange(1,12,2).reshape(3,2)
    return np.dot(a1,a2)
def number6():
    a=np.zeros(10*10).reshape(10,10)
    a[:,0]=1
    a[:,9]=1
    a[0,:]=1
    a[9,:]=1
    return  a
def number7():
    return sorted(np.random.randint(1,9,10))
def number8():
    a=np.arange(9).reshape(3,3)
    for index,value in np.ndenumerate(a):
        print(index,value)
    for index in np.ndindex(a.shape):
        print(index,a[index])
    return 0
def number9():
    a=np.random.randint(1,9,10)
    su=math.sqrt(sum(i**2 for i in a))
    a=np.array([i/su for i in a])
    return a
def number10():
    x=float(input())
    x_=np.random.randint(-10,9,10)
    z=min([abs(i-x) for i in x_])
    print(x_)
    if z+x in x_:
        return z+x
    else:
        return x-z
