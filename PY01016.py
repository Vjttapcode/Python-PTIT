for z in range(int(input())):
    n = input()
    res = ""
    for i in range(len(n)-1):
        if ord('0') < ord(n[i + 1]) <= ord('9'):
            tmp = ord(n[i+1]) - ord('0')
            while tmp > 0:
                res += n[i]
                tmp -= 1
    for i in res:
        print(i,end = '')
    print()