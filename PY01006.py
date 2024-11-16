def check(s):
    s = str(s)
    for i in range(len(s)):
        if s[i] != '4' and s[i] != '7':
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t>0:
        n = input()
        if check(n): print("YES")
        else : print("NO")
        t-=1