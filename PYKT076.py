class TheLoai:
    def __init__(self, ma, ten):
        self.ma = ma
        self.ten = ten

class Phim:
    def __init__(self, ma, theloai, ngaykhoichieu, ten, sotap):
        self.ma = ma
        self.theloai = theloai
        self.ngaykhoichieu = ngaykhoichieu
        self.ngay = int(ngaykhoichieu[0:2])
        self.thang = int(ngaykhoichieu[3:5])
        self.nam = int(ngaykhoichieu[6:])
        self.ten = ten
        self.sotap = sotap

    def __str__(self):
        return '{} {} {} {} {}'.format(self.ma, self.theloai.ten, self.ngaykhoichieu, self.ten, self.sotap)

n,m = map(int, input().split())
a = []
b = []
for i in range(n):
    a.append(TheLoai('TL{:03}'.format(i+1), input()))

for i in range(m):
    tl = input()
    for j in a:
        if tl == j.ma:
            b.append(Phim('P{:03}'.format(i+1), j, input(), input(), int(input())))
b.sort(key=lambda e:(e.nam, e.thang, e.ngay, e.ten, -e.sotap))
print(*b, sep='\n')