class Data:
    def __init__(self, val, cnt):
        self.val = val
        self.cnt = cnt

def cmp(a):
    return (a.cnt * (-1), a.val)

for _ in range(int(input())):
    n = int(input())
    a = []
    b = []
    Dic = {}
    for i in range(n):
        x = int(input())
        if x not in a:
            a.append(x)
            Dic[x] = 0
        else:
            Dic[x] += 1
    for i in a:
        b.append(Data(i, Dic[i]))
    b.sort(key=cmp)
    print(b[0].val)