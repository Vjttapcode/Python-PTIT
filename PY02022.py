import math
def ngto(n):
    if n<2: return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))
myMap = {}
for x in a:
    if x not in myMap:
        if ngto(x):
            myMap[x] = 1
    else:
        myMap[x] += 1
for i in a:
    if i in myMap and myMap[i]>0:
        print(i, myMap[i], sep=' ')
        myMap[i] = 0

