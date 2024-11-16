class Student:
    def __init__(self, id, name, total):
        self.id = id
        self.name = name
        self.avg = round(total/12+0.01,1)

    def Tongket(self):
        if self.avg >= 9:
            return 'XUAT SAC'
        elif self.avg >= 8:
            return 'GIOI'
        elif self.avg >= 7:
            return 'KHA'
        elif self.avg >= 5:
            return 'TB'
        else:
            return 'YEU'

    def __str__(self):
        return '{} {} {} {}'.format(self.id, self.name, self.avg, self.Tongket())

a = []
for i in range(int(input())):
    id = 'HS{:02}'.format(i+1)
    name = input()
    p = [float(i) for i in input().split()]
    total = sum(p) + p[0] +p[1]
    a.append(Student(id, name, total))

a.sort(key=lambda x: (-x.avg, x.id))
for i in a:
    print(i)