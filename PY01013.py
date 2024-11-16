from math import *

t = int(input())

def primenumber(n):
    if n<2 : return False
    for i in range(2,isqrt(n)+1):
        if n % i == 0:
            return False
    return True

while t>0:
    a,b = map(int,input().split())
    c = gcd(a,b)
    tmp = 0
    while c>0:
        tmp += c%10
        c = c//10
    if primenumber(tmp):
        print("YES")
    else: print("NO")
    t-=1
