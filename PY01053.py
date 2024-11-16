for i in range(int(input())):
    n = input()
    tong = 0
    for j in range(len(n)):
        tong += int(n[j])
    if tong%3==0: print("YES")
    else: print("NO")