from math import *

t = int(input())

while t>0:
    n,x,m = map(float,input().split())
    nam = 0
    while 1:
        n = n+(n*x/100)
        nam += 1
        if n < m:
            continue
        else: break
    print(nam)
    t-=1