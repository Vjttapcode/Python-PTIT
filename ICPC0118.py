for _ in range(int(input())):
    d,m = map(int,input().split())
    if m == 1:
        if d < 20:
            print('Ma Ket')
        else: print('Bao Binh')
    if m == 2:
        if d < 19:
            print('Bao Binh')
        else: print('Song Ngu')
    if m == 3:
        if d < 21:
            print('Song Ngu')
        else: print('Bach Duong')
    if m == 4:
        if d < 20:
            print('Bach Duong')
        else: print('Kim Nguu')
    if m == 5:
        if d < 21:
            print('Kim Nguu')
        else: print('Song Tu')
    if m == 6:
        if d < 21:
            print('Song Tu')
        else: print('Cu Giai')
    if m == 7:
        if d < 23:
            print('Cu Giai')
        else: print('Su Tu')
    if m == 8:
        if d < 23:
            print('Su Tu')
        else: print('Xu Nu')
    if m == 9:
        if d < 23:
            print('Xu Nu')
        else: print('Thien Binh')
    if m == 10:
        if d < 23:
            print('Thien Binh')
        else: print('Thien Yet')
    if m == 11:
        if d < 23:
            print('Thien Yet')
        else: print('Nhan Ma')
    if m == 12:
        if d < 22: print('Nhan Ma')
        else: print('Ma Ket')
