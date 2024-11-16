from collections import Counter

def is_permutation(s1,s2):
    if len(s1) != len(s2):
        return "NO"
    elif Counter(s1) != Counter(s2):
        return "NO"
    return "YES"

t = int(input())
res = []
for i in range(t):
    s1 = input().strip()
    s2 = input().strip()
    tmp = is_permutation(s1,s2)
    res.append(f"Test {i+1}: {tmp}")

for i in res:
    print(i)

