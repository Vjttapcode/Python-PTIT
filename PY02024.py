class number:
    def __init__(self,num):
        self.num = num
        self.mulDigit = 1
        while num>0:
            self.mulDigit *= num % 10
            num //= 10

def cmp(a):
    return (a.mulDigit, a.num)

for z in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    res = []
    for i in a:
        res.append(number(i))
    res.sort(key = cmp)
    for i in res:
        print(i.num, end = ' ')
    print()