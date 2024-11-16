for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    res = 0
    for i in range(0, n-2):
        x = a[i]
        l = i+1
        r = len(a)-1
        while l<r:
            if x + a[l] + a[r] == 0:
                res += 1
                l += 1
            elif x + a[l] + a[r] < 0:
                l += 1
            else: r -= 1
    print(res)