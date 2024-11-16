for _ in range(int(input())):
    s = input().strip()
    letters = []
    sum = 0

    for char in s:
        if char.isdigit():
            sum += int(char)
        elif char.isalpha():
            letters.append(char)

    letters.sort()
    res = ''.join(letters)
    if sum > 0:
        res += str(sum)

    print(res)