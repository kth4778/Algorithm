from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
truth = list(map(int,input().split()))
partys = [list(map(int,input().split())) for _ in range(m)]
party = [set() for _ in range(n+1)]

for i in partys:
    for w in i[1:]:
        for j in i[1:]:
            party[w].add(j)

set_idx = set()
for i in truth[1:]:
    que = deque()
    que.append(i)
    set_idx.add(i)
    while que:
        idx = que.popleft()
        for w in party[idx]:
            if  w not in set_idx:
                set_idx.add(w)
                que.append(w)
result = 0

for i in partys:
    switch = True
    for j in i[1:]:
        if j in set_idx:
            switch = False
            break
    if switch:
        result += 1
print(result)
