for z in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * 100001
    for i in a:
        cnt[i] += 1
    for i in a:
        if cnt[i]%2==1:
            print(i)
            break
