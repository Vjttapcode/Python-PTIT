from math import *
def prime_num(n):
    if n<2: return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0: return False
    return True

t = int(input())
while t>0:
    n = input()
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if prime_num(sum): print("YES")
    else: print("NO")
    t-=1