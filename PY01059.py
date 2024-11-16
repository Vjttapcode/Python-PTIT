for z in range(int(input())):
    n = input()
    sum = 0
    tich = 1
    check = False
    for i in range(len(n)):
        tmp = ord(n[i]) - ord('0')
        if i%2==0:
            sum += tmp;
        else:
            if tmp > 0:
                tich *= tmp
                check = True
    if check:
        print(str(sum), str(tich), sep = " ")
    else: print(str(sum),0, sep = " ")
