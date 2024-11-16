from math import *;

def check_odd(n):
    if len(n) % 2 != 0:
        return True
    return False

def check_first_second(n):
    if n[0] != n[1]:
        return True
    return False

def check_num(n):
    for i in range(0,len(n)-2,2):
        if n[i] != n[i+2]:
            return False
    return True

if __name__ == '__main__':
    for i in range(int(input())):
        n = input()
        if(check_odd(n) and check_first_second(n) and check_num(n)):
            print('YES')
        else: print('NO')

