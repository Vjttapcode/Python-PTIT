from math import *

for _ in range(int(input())):
    n = input()
    s = 0
    for i in n:
        s += factorial(int(i))
    if s == int(n):
        print('Yes')
    else: print('No')