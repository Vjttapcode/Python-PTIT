def gen_permutations(s):
    if len(s) == 1:
        return [s]
    permutations = []
    for i in range(len(s)):
        fixed_char = s[i]
        remaining_chars = s[:i] + s[i+1:]
        for perm in gen_permutations(remaining_chars):
            permutations.append([fixed_char] + perm)
    return permutations

def find_largest_smaller_num(n):
    permutations = sorted(set(gen_permutations(n)))
    for perm in permutations:
        if perm < n and not perm.startswith('0'):
            return perm

    return "-1"

t = int(input())
for i in range(1,t+1):
    n = input()
    res = find_largest_smaller_num(n)
    print(res)