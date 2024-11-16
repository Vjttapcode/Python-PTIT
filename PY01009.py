s = input()

cntup = 0
cntlow = 0

for i in range(len(s)):
    if s[i].isupper():
        cntup += 1
    else: cntlow += 1

if cntup > cntlow:
    print(s.upper())
elif cntlow >= cntup:
    print(s.lower())
