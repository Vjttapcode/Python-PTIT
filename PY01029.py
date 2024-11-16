t = int(input())
def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a

while t>0:
    a = int(input())
    b = int(str(a)[::-1])
    if gcd(a,b) == 1:
        print("YES")
    else: print("NO")
    t-=1
