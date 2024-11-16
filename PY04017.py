import math

def time_in_minutes(s):
    h,m = map(int, s.split(':'))
    return h*60 + m - (6*60)

def tao_ma(ten, donvi):
    tmp1 = ten.split()
    tmp2 = donvi.split()
    ma = ''.join(u[0] for u in tmp2) + ''.join(t[0] for t in tmp1)
    return ma.upper()

n = int(input())
dist = 120
racers = []
for _ in range(n):
    ten = input()
    donvi = input()
    vedich = input()

    thoigiandua = time_in_minutes(vedich)
    vantoc = round(dist / (thoigiandua / 60))
    ma = tao_ma(ten, donvi)
    racers.append((ma,ten,donvi,vantoc))

racers.sort(key=lambda x: -x[3])
for racer in racers:
    print(f"{racer[0]} {racer[1]} {racer[2]} {racer[3]} Km/h")

