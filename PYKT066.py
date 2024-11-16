import math


def solve(n,k,a):
    min_len = float("inf")
    check = False
    for i in range(n):
        tmp = a[i]
        for k in range(i,n):
            tmp = math.gcd(tmp, a[k])
            if tmp == k:
                check = True
                min_len = min(min_len, k-i+1)
                break
            if tmp < k:
                break
    return min_len if check else -1

for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    print(solve(n,k,a))