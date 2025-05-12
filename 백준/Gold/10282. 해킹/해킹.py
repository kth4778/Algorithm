from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,d,c = map(int,input().split())
    visited = [float("INF") for _ in range(n + 1)]

    nodes = [[] for _ in range(n + 1)]
    for _ in range(d):
        a,b,s = map(int,input().split())
        nodes[b].append([a,s])
        
    visited[c] = 0
    que = deque()

    que.append([c,0])

    while que:
        node, t = que.popleft()

        for next_node, pt in nodes[node]:
            if visited[next_node] > t + pt:
                que.append([next_node, t + pt])
                visited[next_node] = t + pt

    print(f"{sum([1 for i in visited if i != float("INF")])} {max([i for i in visited if i != float("INF")])}")