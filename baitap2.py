N = int(input())

S = 0
if N % 2 != 0:
    i = 1
    dau = 1
    while i <= N:
        S += dau * (1 / i)
        dau *= -1
        i += 2
else:
    i = 2
    dau = 1
    while i <= N:
        S += dau * (1 / i)
        dau *= -1
        i += 2
print(S)