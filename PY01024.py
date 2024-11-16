t = int(input())

def tong_chu_so(n):
    tmp = 0
    while n>0:
        tmp += n%10
        n//=10
    return tmp % 10 == 0

def chu_so(n):
    s = str(n)
    for i in range(1,len(s)):
        if abs(int(s[i]) - int(s[i-1])) != 2:
            return False
    return True

while t>0:
    a = int(input())
    if tong_chu_so(a) and chu_so(a):
        print("YES")
    else: print("NO")
    t-=1