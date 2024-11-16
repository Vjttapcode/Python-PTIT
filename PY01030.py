from math import *

n,k = map(int,input().split())

a = 10 ** (k-1)
b = 10 ** k
cnt = 0
for i in range(a,b):
    if gcd(i,n) == 1:
        cnt+=1
        print(i, end = ' ')
        if cnt%10==0:
            print()