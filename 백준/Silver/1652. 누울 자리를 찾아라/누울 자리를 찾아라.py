N = int(input())
maps1 = [input() for _ in range(N)]
maps2 = ['' for _ in range(N)]

for i in range(N):
    for j in range(N):
        maps2[i] += maps1[j][i]

a = 0
b = 0

for i in maps1:
    for j in i.split('X'):
        if len(j) > 1:
            a += 1


for i in maps2:
    for j in i.split('X'):
        if len(j) > 1:
            b += 1

print(f"{a} {b}")