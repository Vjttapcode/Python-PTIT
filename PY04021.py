class Gamer:
    def __init__(self, id, name, checkin, checkout):
        self.id = id
        self.name = name
        self.checkin = checkin
        self.checkout = checkout

    def calculate_hour(self):
        h_in = self.checkin.split(':')[0]
        m_in = self.checkin.split(':')[1]
        h_out = self.checkout.split(':')[0]
        m_out = self.checkout.split(':')[1]
        tmp1 = int(h_in) * 60 + int(m_in)
        tmp2 = int(h_out) * 60 + int(m_out)
        m_total = tmp2 - tmp1
        return m_total//60

    def calculate_min(self):
        h_in = self.checkin.split(':')[0]
        m_in = self.checkin.split(':')[1]
        h_out = self.checkout.split(':')[0]
        m_out = self.checkout.split(':')[1]
        tmp1 = int(h_in) * 60 + int(m_in)
        tmp2 = int(h_out) * 60 + int(m_out)
        m_total = tmp2 - tmp1
        return m_total % 60

    def __lt__(self, other):
        return self.calculate_hour() > other.calculate_hour()

    def __str__(self):
        return '{} {} {} gio {} phut'.format(self.id, self.name, self.calculate_hour(), self.calculate_min())

gamers = []
for i in range(int(input())):
    id = input()
    name = input()
    checkin = input()
    checkout = input()
    gamers.append(Gamer(id, name, checkin, checkout))
gamers.sort()
for g in gamers:
    print(g)