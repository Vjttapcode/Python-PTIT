from math import *;

def check_prime(s):
    if s<2: return False
    for i in range(2,isqrt(s)+1):
        if s%i==0:
            return False
    return True

def sum_prime(s):
    sum = 0
    for i in range(len(s)):
        tmp = ord(s[i]) - ord('0')
        sum += tmp
    if check_prime(sum):
        return True
    return False

def check_odd_even(s):
    for i in range(len(s)):
        if i%2==0:
            if (ord(s[i]) - ord('0')) % 2 != 0:
                return False
        elif i%2!=0:
            if (ord(s[i]) - ord('0')) % 2 == 0:
                return False
    return True

if __name__ == '__main__':
    for i in range(int(input())):
        n = input()
        if sum_prime(n) and check_odd_even(n):
            print('YES')
        else: print('NO')


