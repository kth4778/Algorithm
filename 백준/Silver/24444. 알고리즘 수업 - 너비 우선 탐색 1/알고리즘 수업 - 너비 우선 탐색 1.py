from collections import deque
import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)
    graph[a].append(b)
graph = [sorted(i) for i in graph]

cnt = 1
que = deque()
visited[r] = cnt
cnt += 1
que.append(r)

while que:
    cur = que.popleft()
    for node in graph[cur]:
        if not visited[node]:
            visited[node] = cnt
            cnt += 1
            que.append(node)

for i in range(1,n+1):
    p = visited[i]
    if not p:
        print(0)
    else:
        print(p)