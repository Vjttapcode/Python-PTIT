s1 = input().strip()
s2 = input().strip()
p = int(input().strip())

idx = p-1

res = s1[:idx] + s2 + s1[idx:]

print(res)