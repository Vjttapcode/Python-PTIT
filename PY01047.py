import math

def isPrime(n):
    if n<2: return False
    for i in range(2, math.isqrt(n)+1):
        if n%i==0:
            return False
    return True

def check(n):
    return isPrime(int(n[len(n)-4:]))

for i in range(int(input())):
    n = input()
    if check(n):
        print('YES')
    else: print('NO')