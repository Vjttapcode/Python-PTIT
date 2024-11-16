def findIdx(n):
    for i in range(1, len(n)):
        if n[i] == n[i-1]:
            return -1
        if n[i] < n[i-1]:
            return i
    return -1
def solve(n):
    if len(n) < 3:
        return False
    idx = findIdx(n)
    if idx == -1:
        return False
    for i in range(idx+1, len(n)):
        if n[i] > n[i-1]:
            return False
    return True

for z in range(int(input())):
    n = input()
    if(solve(n)):
        print('YES')
    else: print('NO')