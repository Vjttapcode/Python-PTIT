from datetime import datetime

floor_bill = {
    1: 25,
    2: 34,
    3: 50,
    4: 80
}

class KhachHang:
    def __init__(self, id, name, room, checkin, checkout, service):
        self.id = f"KH{id:02d}"
        self.name = name
        self.room = room
        self.checkin = datetime.strptime(checkin.strip(), "%d/%m/%Y")
        self.checkout = datetime.strptime(checkout.strip(), "%d/%m/%Y")
        self.service = int(service)
        self.daylength = max((self.checkout - self.checkin).days+1,1)
        self.floor = int(self.room[0])
        self.bill = floor_bill.get(self.floor,0)
        self.total = self.payment()

    def payment(self):
        if self.daylength == 0:
            return self.bill + self.service
        return self.daylength * self.bill + self.service

    def __lt__(self, other):
        return self.total > other.total #sap xep giam dan theo tien

    def __str__(self):
        return f"{self.id} {self.name} {self.room} {self.daylength} {self.total}"

n = int(input())
list = []
for i in range(1, n+1):
    name = input()
    room = input()
    checkin = input()
    checkout = input()
    service = input()
    cust = KhachHang(i,name,room,checkin,checkout,service)
    list.append(cust)

list.sort()
for cust in list:
    print(cust)
