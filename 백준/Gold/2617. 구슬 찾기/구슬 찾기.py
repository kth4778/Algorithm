from collections import deque
import sys
input = sys.stdin.readline

def bfs(start,n,graph):
    visited = [False for _ in range(n+1)]
    que = deque()
    result = 0
    que.append(start)
    visited[start] = True
    
    while que:
        s = que.popleft()
        for i in graph[s]:
            if not visited[i]:
                visited[i] = True
                que.append(i)
                result += 1
    return result

n,m = map(int,input().split())
graph1 = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph1[a].append(b)
    graph2[b].append(a)
answer = 0

for i in range(1,n+1):
    a = bfs(i,n,graph1)
    b = bfs(i,n,graph2)
    if a > n//2 or b > n//2:
        answer += 1

print(answer)