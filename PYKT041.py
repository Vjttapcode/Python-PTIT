def count_coin_pairs(a,n):
    cnt = 0
    for i in a:
        tmp1 = i.count('C')
        cnt += (tmp1 * (tmp1 - 1))//2
    for j in range(n):
        tmp2 = sum(1 for i in a if i[j] == 'C')
        cnt += (tmp2 * (tmp2 - 1))//2
    return cnt

n = int(input())
a = [input().strip() for _ in range(n)]
print(count_coin_pairs(a,n))