from collections import deque
import sys
input = sys.stdin.readline

def bfs(k,p):
    que = deque()
    visited = [False for _ in range(n+1)]
    visited[p] = True
    answer = 0

    que.append([p,float("INF")])
    while que:
        cur, distance = que.popleft()
        for next_node, d in graph[cur]:
            if not visited[next_node] and next_node != p:
                new_distance = min(distance, d)
                if new_distance >= k:
                    answer += 1
                que.append([next_node, new_distance])
                visited[next_node] = True
    return answer

n,q = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,cost = map(int,input().split())
    graph[a].append([b, cost])
    graph[b].append([a, cost])

for _ in range(q):
    k,p = map(int,input().split())
    print(bfs(k,p))