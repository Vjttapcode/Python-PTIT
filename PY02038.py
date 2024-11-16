def count_coin_pairs(a,n):
    res = 0
    for i in a:
        count_in_row = i.count('C')
        res += (count_in_row * (count_in_row - 1))//2
    for j in range(n):
        count_in_col = sum(1 for i in a if i[j] == 'C')
        res += (count_in_col * (count_in_col - 1))//2
    return res

n = int(input())
a = [input().strip() for _ in range(n)]
print(count_coin_pairs(a,n))