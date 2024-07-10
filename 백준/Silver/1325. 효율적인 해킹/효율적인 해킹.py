import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)

def bfs(start):
    visited = [False for _ in range(n+1)]
    que = deque()
    que.append(start)
    visited[start] = True
    cnt = 1

    while que:
        node = que.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                cnt+=1
                que.append(i)
    return cnt

hacking_computers = {i:None for i in range(1,n+1)}
for i in range(1,n+1):
    hacking_computers[i] = bfs(i)
max_cnt = max(hacking_computers.values())

for i in range(1,n+1):
    if max_cnt == hacking_computers[i]:
        print(i,end = ' ')