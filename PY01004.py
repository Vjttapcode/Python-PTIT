from math import *

def gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a

def primenumber(a):
    if a<2: return False
    for i in range(2,isqrt(a)+1):
        if a%i==0:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t:
        k=0
        n = int(input())
        for i in range(1,n+1):
            if gcd(i,n) == 1:
                k+=1
        if primenumber(k): print("YES")
        else: print("NO")
        t-=1