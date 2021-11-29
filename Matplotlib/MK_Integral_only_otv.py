import random
def f(x):
    return -x*x+4
N = int(input())
su=0
for i in range(N):
    x1 = random.uniform(-2,2)
    su=su+f(x1)
otv=4*su/N
print(otv)
