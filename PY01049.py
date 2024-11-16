from math import *

def prime_num(n):
    if n<2: return False
    for i in range(2,isqrt(n)+1):
        if n%i==0: return False
    return True

def check1(n):
    cnt = 0
    while n>0:
        cnt += 1
        n//=10
    if prime_num(cnt): return True
    return False

def check2(n):
    cnt_prime = 0
    cnt_non = 0
    while n>0:
        if prime_num(n%10): cnt_prime += 1
        else: cnt_non += 1
        n//=10
    if cnt_prime > cnt_non: return True
    return False

t = int(input())
while t>0:
    n = int(input())
    if check1(n) and check2(n):
        print("YES")
    else: print("NO")
    t-=12