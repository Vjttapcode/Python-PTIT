f = [0,1,1]

for i in range(3,93):
    f.append(f[i-1] + f[i-2])

for i in range(int(input())):
    l , r = map(int,input().split())
    for j in range(l, r+1):
        print(f[j], end = ' ')
    print()
