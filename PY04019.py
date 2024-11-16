class ThiSinh:
    def __init__(self, id, name, diemtb):
        self.id = id
        self.name = name
        self.diemtb = diemtb
        if diemtb < 5:
            self.rank = 'TRUOT'
        elif 5 <= diemtb < 8:
            self.rank = 'CAN NHAC'
        elif 8 <= diemtb <= 9.5:
            self.rank = 'DAT'
        elif diemtb > 9.5:
            self.rank = 'XUAT SAC'

list = []

def cmp(x):
    return (x.diemtb * (-1))

n = int(input())
for i in range(n):
    ten = input()
    lt = float(input())
    th = float(input())
    if lt > 10:
        lt /= 10.0
    if th > 10:
        th /= 10.0
    id = ''
    id += 'TS0' + str(i+1)
    list.append(ThiSinh(id, ten, (lt + th)/2.0))
list.sort(key=cmp)

for ts in list:
    print(ts.id + ' ' + ts.name + ' ' + str.format('{:.2f}', ts.diemtb) + ' ' + ts.rank)

