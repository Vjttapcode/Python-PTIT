class student:
    def __init__(self, name, bd, mon1, mon2, mon3):
        self.name = name
        self.bd = bd
        self.mon1 = mon1
        self.mon2 = mon2
        self.mon3 = mon3
    def tongdiem(self):
        return self.mon1 + self.mon2 + self.mon3

a = input()
b = input()
c = input()
d = input()
e = input()
A = student(str(a), str(b), float(c), float(d), float(e))
print(str(A.name) + ' ' + str(A.bd) + ' ' + str(A.tongdiem()))
