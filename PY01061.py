from math import *
def isPrime(n):
    if n<2: return False
    for i in range(2, isqrt(n)+1):
        if n%i == 0:
            return False
    return True

for z in range(int(input())):
    n = input()
    if isPrime(int(n[:3])) and isPrime(int(n[len(n)-3:])):
        print("YES")
    else: print("NO")