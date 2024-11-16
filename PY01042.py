def check(n):
    for i in range(len(n)):
        if n[i] != '0' and n[i] != '1' and n[i] != '2':
            return False
    return True
t = int(input())
while t>0:
    s = input()
    if check(s): print("YES")
    else: print("NO")
    t-=1