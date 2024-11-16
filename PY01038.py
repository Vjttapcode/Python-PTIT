def solve(n):
    for i in range(1000):
        if n % 7 == 0:
            return n
        reversed_n = int(str(n)[::-1])
        n += reversed_n
    return -1

for _ in range(int(input())):
    n = int(input())
    print(solve(n))