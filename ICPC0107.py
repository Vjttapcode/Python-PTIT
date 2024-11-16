def resolve(p,q,s1,s2):
    s1 = s1.replace(p,q)
    s2 = s2.replace(p,q)
    return int(s1) + int(s2)

for _ in range(int(input())):
    [p,q] = input().split()
    s = input().split()
    if len(s) > 1:
        s1, s2 = s[0], s[1]
    else:
        s1 = s[0]
        s2 = input()
    x = resolve(p,q,s1,s2)
    y = resolve(q,p,s1,s2)
    print(min(x,y), max(y,x))