def solve(s):
    cnt = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            print(cnt, s[i-1], sep = '', end = '')
            cnt = 1
        else:
            cnt += 1
    print(cnt,s[len(s)-1], sep = '')
for z in range(int(input())):
    s = input()
    solve(s)


