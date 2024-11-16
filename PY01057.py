from math import *

def check_prime(s):
    if s<2: return False
    for i in range(2, isqrt(s)+1):
        if s % i == 0:
            return False
    return True

def solve(s):
    for i in range(0, len(s)):
        tmp = ord(s[i]) - ord('0')
        if check_prime(i) and not check_prime(tmp):
            return False
        elif not check_prime(i) and check_prime(tmp):
            return False
    return True

if __name__ == '__main__':
    for i in range(int(input())):
        n = input()
        if solve(n): print('YES')
        else: print('NO')