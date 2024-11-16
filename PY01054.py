for i in range(int(input())):
    n = input()
    tich = 1
    for j in range(len(n)):
        if n[j] != '0':
            tich *= int(n[j])
    print(tich)