from math import *

for z in range(int(input())):
    n = int(input())
    print(1, end = "")
    for i in range(2,isqrt(n)+1):
        if n%i == 0:
            cnt = 0
            while n%i == 0:
                cnt += 1
                n//=i
            print(" *", end = " ")
            print(str(i) + "^" + str(cnt), end = '')
    if n>1:
        print(" *", end = " ")
        print(str(n) + '^' + str(1), end = '')
    print()