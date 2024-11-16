a, k ,n = map(int, input().split())
i = k - (a%k)
n -= a
b = []
while i<=n:
    b.append(i)
    i += k

if len(b) == 0:
    print(-1)
else:
    for i in b:
        print(i, end = ' ')