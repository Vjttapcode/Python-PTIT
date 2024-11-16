from math import *

def phanTichThuaSoNgto(n):
    tmp = 0
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            while n % i == 0:
                tmp += i
                n //= i
    if n>1: tmp += n
    return tmp

n = int(input())
sum = 0
for i in range(1,n+1):
    x = int(input())
    sum += phanTichThuaSoNgto(x)
print(sum)