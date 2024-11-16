with open("TepC.txt", 'w') as fileC:
    with open("TepA.txt") as fileA:
        with open("TepB.txt") as fileB:
            for x,y in zip(fileA,fileB):
                try:
                    ans = int(x)**int(y)
                except:
                    print("loi dinh dang")
                else:
                    fileC.write(str(ans))




