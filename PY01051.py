t = int(input())
while t>0:
    n = input()
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if str(sum) == str(sum)[::-1] and sum > 9:
        print("YES")
    else: print("NO")
    t-=1
    