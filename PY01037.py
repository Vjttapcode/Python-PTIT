from math import *

def count(n):
    cnt = 0
    for i in range(1,isqrt(n)+1):
        if n%i == 0:
            cnt += 1
            if i!=n//i:
                cnt += 1
    return cnt

max_n = 10**7
res = []
max_divisors = 0
for i in range(1, max_n+1):
    divisors = count(i)
    if divisors > max_divisors:
        max_divisors = divisors
        res.append(i)

for _ in range(int(input())):
    x = int(input())
    l,r = 0, len(res) - 1
    while l < r:
        mid = (l + r) // 2
        if res[mid] >= x:
            r = mid
        else:
            l = mid + 1
    print(res[l])