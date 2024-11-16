class SinhVien:
    def __init__(self, hoten, correct, submit):
        self.hoten = hoten
        self.correct = correct
        self.submit = submit

def cmp(x):
    return (-1) * x.correct, x.submit, x.hoten

list = []

for _ in range(int(input())):
    n = input()
    c,t = map(int, input().split())
    list.append(SinhVien(n, c, t))

list.sort(key = cmp)
for sv in list:
    print(f"{sv.hoten} {sv.correct} {sv.submit}")