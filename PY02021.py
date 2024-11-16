for z in range(int(input())):
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    check = False
    for i in a:
        if i in b and i in c:
            print(i, end = " ")
            check = True
    if check == False:
        print("NO")