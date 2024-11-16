n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
A = []
B = []
res1 = []
res2 = []
res3 = []
for i in a:
    if a.count(i) == 1:
        A.append(i)
for i in b:
    if b.count(i) == 1:
        B.append(i)
for i in A:
    if i in B:
        res1.append(i)
res1 = sorted(res1)
for i in A:
    if i not in B:
        res2.append(i)
res2 = sorted(res2)
for i in B:
    if i not in A:
        res3.append(i)
res3 = sorted(res3)
for i in res1:
    print(i, end = " ")
print()
for i in res2:
    print(i, end = " ")
print()
for i in res3:
    print(i, end = " ")
