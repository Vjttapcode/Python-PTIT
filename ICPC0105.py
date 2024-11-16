for _ in range(int(input())):
    s = input()
    s += '*'
    res = 0
    tmp = 0
    for i in range(0, len(s)-1):
        if s[i].isdigit():
            tmp = tmp*10 + int(s[i])
            if s[i+1].isalpha():
                res = max(res, tmp)
                tmp = 0
    print(res)