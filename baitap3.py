text = input()
k = int(input())
res = ""
for c in text:
    if c.isalpha():
        tmp = k%26
        if c.islower():
            new_c = chr((ord(c) - ord('a') + tmp) % 26 + ord('a'))
        elif c.isupper():
            new_c = chr((ord(c) - ord('A') + tmp) % 26 + ord('A'))
        res += new_c
    else:
        res += c
print(res)