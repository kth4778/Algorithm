from collections import deque
import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())
sequence = {i:0 for i in range(1,n+1)}
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

graph = [sorted(i, reverse = True) for i in graph]
p = 2

que = deque([r])
sequence[r] = 1

while que:
    cur = que.popleft()

    for next_node in graph[cur]:
        if sequence[next_node] != 0:
            continue

        sequence[next_node] = p
        p += 1
        que.append(next_node)

for i in sequence.values():
    print(i)