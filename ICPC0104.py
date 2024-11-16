for z in range(int(input())):
    s = input()
    s += '*'
    res = 10**19
    x = 0
    for i in range(0, len(s)-1):
        if s[i].isdigit():
            x = x*10 + int(s[i])
            if s[i+1].isalpha():
                res = min(res, x)
                x = 0
    print(res)

