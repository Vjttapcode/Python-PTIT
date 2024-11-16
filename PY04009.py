class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao
    def cong(self, other):
        return SoPhuc(self.thuc + other.thuc, self.ao + other.ao)
    def nhan(self, other):
        thuc = self.thuc * other.thuc - self.ao * other.ao
        ao = self.thuc * other.ao + other.thuc * self.ao
        return SoPhuc(thuc, ao)
    def __str__(self):
        if self.ao >= 0:
            return f"{self.thuc} + {self.ao}i"
        else:
            return f"{self.thuc} - {-self.ao}i"

for _ in range(int(input())):
    a,b,c,d = map(int, input().split())
    A = SoPhuc(a,b)
    B = SoPhuc(c,d)
    tong = A.cong(B)
    C = tong.nhan(A)
    D = tong.nhan(tong)
    print(f"{C}, {D}")