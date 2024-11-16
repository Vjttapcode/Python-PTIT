import math

def isPrime(n):
    if n<2: return False
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))
b = {}
for i in a:
    b[i] = 1

a = list(b)
n = len(a)

for i in range(1,len(a)):
    a[i] += a[i-1]
check = False
for i in range(len(a)):
    if isPrime(a[i]) and isPrime(a[n-1] - a[i]):
        check = True
        print(i)
        break
if not check:
    print('NOT FOUND')