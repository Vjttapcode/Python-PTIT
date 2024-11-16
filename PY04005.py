class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def findParameter(self):
        return self.a + self.b + self.c

for _ in range(int(input())):
    