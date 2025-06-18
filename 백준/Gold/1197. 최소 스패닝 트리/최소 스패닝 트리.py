import heapq
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

V,E = map(int,input().split())
graph = [i for i in range(V + 1)]
que = []

for _ in range(E):
    a,b,c = map(int,input().split())
    heapq.heappush(que, [c, a, b])

def find(x):
    if x != graph[x]:
        graph[x] = find(graph[x])

    return graph[x]

def union(a, b):
    a = graph[a]
    b = graph[b]

    if a > b:
        graph[a] = b
    else:
        graph[b] = a

answer = 0

while que:
    cost, a, b = heapq.heappop(que)

    if find(a) != find(b):
        answer += cost
        union(a,b)

print(answer)