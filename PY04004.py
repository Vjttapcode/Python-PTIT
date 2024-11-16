from math import *

class Fract:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def reduce(self):
        ucln = gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln
        return self
    def add(self, other):
        mau = self.mau * other.mau // gcd(self.mau, other.mau)
        res = Fract(self.tu * mau // self.mau + other.tu * mau // other.mau, mau)
        return res.reduce()

x,y,z,t = map(int, input().split())
A = Fract(x,y)
B = Fract(z,t)
C = A.add(B)
print(str(C.tu) + '/' + str(C.mau))