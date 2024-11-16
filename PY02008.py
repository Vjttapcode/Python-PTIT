from math import *

def nguyento(n):
    if n<2: return False
    for i in range(2, isqrt(n)+1):
        if n%i==0:
            return False
    return True

a = [2]
for i in range(3,8000,2):
    if nguyento(i):
        a.append(i)
n,x = list(map(int,input().split()))
print(x, end = ' ')
for i in range(n):
    print(x + a[i], end = ' ')
    x = x + a[i]