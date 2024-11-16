priority_point = {
    1: 2.0,
    2: 1.5,
    3: 1.0,
    4: 0.0
}

list_subject = {
    "A": "TOAN",
    "B": "LY",
    "C": "HOA"
}

class Teacher:
    def __init__(self, teacher_id, name, apply_id, sub1, sub2):
        self.teacher_id = f"GV{teacher_id:02d}"
        self.name = name
        self.apply_id = apply_id
        self.sub1 = sub1
        self.sub2 = sub2
        self.subject = list_subject.get(self.apply_id[0])
        self.priority_id = int(self.apply_id[1])
        self.point = float(priority_point.get(self.priority_id))
        self.total = self.calculate()
        self.status = self.solve()

    def calculate(self):
        return self.sub1 * 2 + self.sub2 + self.point

    def solve(self):
        if self.total >= 18.0:
            return "TRUNG TUYEN"
        return "LOAI"

    def __lt__(self, other):
        return self.total > other.total

    def __str__(self):
        return f"{self.teacher_id} {self.name} {self.subject} {self.total} {self.status}"

n = int(input())
list_gv = []
for i in range(1,n+1):
    name = input()
    apply_id = input()
    sub1 = float(input())
    sub2 = float(input())
    gv = Teacher(i, name, apply_id, sub1, sub2)
    list_gv.append(gv)

list_gv.sort()
for gv in list_gv:
    print(gv)
