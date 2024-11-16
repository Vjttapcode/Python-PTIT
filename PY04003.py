from math import *

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def rutGon(self):
        ucln = gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln
    def __str__(self):
        return f'{self.tu}/{self.mau}'
tu, mau = list(map(int, input().split()))
a = PhanSo(tu, mau)
a.rutGon()
print(a)