class KhachHang:
    def __init__(self, makh, tenkh, chisocu, chisomoi):
        self.makh = makh
        self.tenkh = tenkh
        self.chisocu = chisocu
        self.chisomoi = chisomoi
        self.tongtien = self.TinhTien()
    def TinhTien(self):
        tieuthu = self.chisomoi - self.chisocu
        tien = 0
        if tieuthu <= 50:
            tien = tieuthu * 100
            phuphi = 0.02
        elif tieuthu <= 100:
            tien = 50 * 100 + (tieuthu-50) * 150
            phuphi = 0.03
        elif tieuthu > 100:
            tien = 50 * 100 + 50 * 150 + (tieuthu-100) * 200
            phuphi = 0.05
        tongtien = tien * (1 + phuphi)
        return round(tongtien)
    def __str__(self):
        return f"{self.makh} {self.tenkh} {self.tongtien}"

n = int(input())
list = []
for i in range(n):
    a = input().strip()
    b = int(input())
    c = int(input())
    makh = f"KH{str(i+1).zfill(2)}"
    kh = KhachHang(makh,a,b,c)
    list.append(kh)

list.sort(key = lambda x : x.tongtien, reverse = True)

for kh in list:
    print(kh)
