from collections import deque

n = int(input())
rout = [list(map(int,input().split())) for _ in range(n-1)]

maps = [[] for _ in range(n+1)]
for a,b in rout:
    maps[a].append(b)
    maps[b].append(a)

result = [0 for _ in range(n+1)]
result[1] = 1
que = deque()
que.append(1)
while que:
    a = que.popleft()
    for i in maps[a]:
        if result[i] == 0:
            result[i] = a
            que.append(i)
for i in result[2:]:
    print(i)
