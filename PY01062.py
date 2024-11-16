from math import *
def isPrime(n):
    if n<2:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def solve(n):
    if not isPrime(len(n)):
        return 'NO'
    cnt_Prime = 0
    cnt_NotPrime = 0
    for i in n:
        if isPrime(ord(i) - ord('0')):
            cnt_Prime += 1
        else: cnt_NotPrime += 1
    if cnt_Prime > cnt_NotPrime:
        return 'YES'
    return 'NO'

for z in range(int(input())):
    n = input()
    print(solve(n))
