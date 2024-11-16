for z in range(int(input())):
    n = input()
    sum = 0
    tich = 1
    check = False
    for i in range(len(n)):
        tmp = ord(n[i]) - ord('0')
        if i%2==0:
            if tmp > 0:
                tich *= tmp
                check = True
        else:
            sum += tmp
    if check:
        print(tich, sum, sep = ' ')
    else:
        print(tich, 0, sep = ' ')
