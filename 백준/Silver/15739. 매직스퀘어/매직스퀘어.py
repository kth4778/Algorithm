n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]

numbers = set()
lst = []
row = 0
col = 0

for i in range(n):
    row += maps[i][i]
    col += maps[i][n - i - 1]
    lst.append(sum(maps[i]))

for x in range(n):
    q = 0
    for y in range(n):
        q += maps[y][x]
        numbers.add(maps[y][x])
    lst.append(q)
lst.append(row)
lst.append(col)

p = n * (n ** 2 + 1) / 2

if len(numbers) != n ** 2:
    print("FALSE")
    exit()

for i in lst:
    if p != i:
        print("FALSE")
        exit()

print("TRUE")