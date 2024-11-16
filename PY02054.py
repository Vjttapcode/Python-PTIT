n,m = map(int,input().split())
a = []
for i in range(n):
    for j in range(m):
        a.append(int(input()))
if n > m:
    tmp = n - m
    while tmp > 0:
