from itertools import product

n = int(input())
m = int(input())
if m > 0:
    break_botton = list(map(int,input().split()))
else:
    break_botton = []

case1 = abs(n - 100)
case2 = float("INF")

if m == 10:
    print(case1)
    exit()

botton = []
for i in range(10):
    if i not in break_botton:
        botton.append(i)

size = len(str(n))

for i in range(size-1, size+2):
    if i == 0:
        continue
    for j in product(botton, repeat=i):
        case2 = min(case2, abs(n - int(''.join([str(q) for q in j]))) + i)

print(min(case1, case2))