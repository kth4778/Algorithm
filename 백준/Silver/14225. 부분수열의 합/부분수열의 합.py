from itertools import combinations

N = int(input())
S = list(map(int,input().split()))
m = set()

p = [i for i in range(N)]

for i in range(1,N + 1):
    for j in combinations(p,i):
        a = 0
        for q in j:
            a += S[q]
        m.add(a)
m = sorted(list(m))

index = 0

while index < len(m):
    if index + 1 != m[index]:
        print(index + 1)
        exit()

    index += 1

print(m[-1] + 1)