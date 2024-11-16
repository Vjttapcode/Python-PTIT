class SinhVien:
    def __init__(self, masv, ten, lop):
        self.masv = masv
        self.ten = ten
        self.lop = lop
        self.diemcc = 10
        self.ghichu = ""

    def tinh_cc(self, dd):
        for i in dd:
            if i == 'm':
                self.diemcc -= 1
            elif i == 'v':
                self.diemcc -= 2
        if self.diemcc <= 0:
            self.diemcc = 0
            self.ghichu = 'KDDK'

    def __str__(self):
        return f"{self.masv} {self.ten} {self.lop} {self.diemcc} {self.ghichu}"

n = int(input())
danhsach = []
for _ in range(n):
    masv = input()
    ten = input()
    lop = input()
    sinhvien = SinhVien(masv, ten, lop)
    danhsach.append(sinhvien)

for _ in range(n):
    id, dd = input().split()
    for sv in danhsach:
        if id == sv.masv:
            sv.tinh_cc(dd)

for sv in danhsach:
    print(sv)
