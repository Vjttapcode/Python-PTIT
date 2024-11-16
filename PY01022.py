n = input()
step = 0
if n[0] == '-':
    n = n[1:]
while len(n) > 1:
    sum = 0
    for digit in n:
        sum += int(digit)
    n = str(sum)
    step += 1

print(step)