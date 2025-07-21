import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())

graph = [[] for _ in range(N + 1)]
count = [0 for _ in range(N + 1)]
result = [0 for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for _ in range(M):
    a,b = map(int,input().split())
    count[b] += 1
    graph[a].append(b)

que = deque()

for i in range(1, N + 1):
    if count[i] == 0:
        que.append([i, 1])
        visited[i] = True

while que:
    n, cnt = que.popleft()
    result[n] = cnt

    for i in graph[n]:
        count[i] -= 1
    
    for i in range(1, N + 1):
        if count[i] == 0 and not visited[i]:
            que.append([i, cnt + 1])
            visited[i] = True

print(*result[1:])