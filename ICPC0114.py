from math import *

def isPrime(n):
    if n<2:
        return False
    for i in range(2, isqrt(n)+1):
        if n%i == 0:
            return False
    return True

def checkPerfectPrime(n):
    if not isPrime(int(n)):
        return 'No'
    if not isPrime(int(n[::-1])):
        return 'No'
    sum = 0
    for i in n:
        sum += int(i)
    if not isPrime(sum):
        return 'No'
    for i in n:
        if not isPrime(int(i)):
            return 'No'
    return 'Yes'

for z in range(int(input())):
    n = input()
    print(checkPerfectPrime(n))
