import math

isPrime = [1] * 1000005
isPrime[0] = isPrime[1] = 0

for i in range(2, 1000):
    if isPrime[i] == 1:
        j = i*i
        while j < int(1e6):
            isPrime[j] = 0
            j += i

a = []

for i in range(2, int(1e6)):
    if isPrime[i] == 1:
        a.append(i)

for _ in range(int(input())):
    n = int(input())
    cnt = 0
    idx = 0
    while a[idx] <= n-6:
        num = a[idx]
        if isPrime[num + 6] == 1 and (isPrime[num + 4]== 1 or isPrime[num+2]==1):
            cnt += 1
        idx += 1
    print(cnt)
