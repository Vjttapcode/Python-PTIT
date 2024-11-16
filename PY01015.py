def check(a):
    for i in range(1,len(a)):
        if a[i] < a[i-1]:
            return False
    return True
t = int(input())
while t>0:
    s = input()
    if check(s):
        print("YES")
    else: print("NO")
    t-=1