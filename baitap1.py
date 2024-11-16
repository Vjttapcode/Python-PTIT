a = list(map(int,input().split()))
# a = [1 2 2 3 4 4 5 6]
res = []
i = 0
while i< len(a):
    if a[i] not in res:
        res.append(a[i])
    i+=1
for x in res:
    print(x, end = ' ')