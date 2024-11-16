def solve(n):
    s = n[::-1]
    for i in range(1, len(n)):
        if abs(ord(n[i]) - ord(n[i-1])) != abs(ord(s[i]) - ord(s[i-1])):
            return 'NO'
    return 'YES'

for z in range(int(input())):
    n = input()
    print(solve(n))