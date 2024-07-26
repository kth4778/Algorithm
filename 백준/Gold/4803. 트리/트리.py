import sys
from collections import deque
input = sys.stdin.readline

def bfs(cur):
    isTree = True
    que = deque()
    que.append(cur)
    while que:
        x = que.popleft()
        if visited[x]:
            isTree = False
        visited[x] = True

        for i in graph[x]:
            if not visited[i]:
                que.append(i)
    return isTree


case = 1

while True:
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        exit()
    else:
        graph = [[] for _ in range(n+1)]
        for _ in range(m):
            a,b = map(int,input().split())
            graph[a].append(b)
            graph[b].append(a)
        
        visited = {i:0 for i in range(1,n+1)}
        result = 0
        for i in range(1,n+1):
            if visited[i]:
                continue
            else:
                if bfs(i):
                    result += 1

        if result == 0:
            print(f"Case {case}: No trees.")
        elif result == 1:
            print(f"Case {case}: There is one tree.")
        else:
            print(f"Case {case}: A forest of {result} trees.")
        case += 1