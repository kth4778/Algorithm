n = input()
answer = 0
n2 = n
while True:
    left = n2[-1]

    if len(n2) < 2:
        n2 = left + '0'

    p = 0
    for i in n2:
        p += int(i)
    right = str(p)[-1]
    n2 = str(int(left + right))
    answer += 1
    if n == n2:
        break
print(answer)