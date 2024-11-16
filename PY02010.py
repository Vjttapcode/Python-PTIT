while True:
    n = int(input())
    if n == 0:
        break
    num = [input().lstrip('0') or '0' for _ in range(n)]
    min_num = min(num)
    max_num = max(num)
    if min_num == max_num:
        print('BANG NHAU')
    else: print(min_num, max_num)