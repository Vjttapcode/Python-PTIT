class number:
    def __init__(self,val):
        self.val = val
        self.sumDigit = 0
        while val>0:
            self.sumDigit += val % 10
            val //= 10

def cmp(a):
    return (a.sumDigit, a.val)

for z in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ans = []
    for i in a:
        ans.append(number(i))
    ans.sort(key = cmp)
    for i in ans:
        print(i.val, end = ' ')
    print()