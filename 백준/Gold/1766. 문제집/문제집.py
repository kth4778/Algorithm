import heapq
import sys
input = sys.stdin.readline

N,M = map(int,input().split())

graph = [[] for _ in range(N + 1)]
count = [0 for _ in range(N + 1)]
que = []
result = []

for _ in range(M):
    A,B = map(int,input().split())
    count[B] += 1
    graph[A].append(B)

for i in range(1, N + 1):
    if count[i] == 0:
        heapq.heappush(que, i)

while que:
    p = heapq.heappop(que)
    result.append(p)

    for i in graph[p]:
        count[i] -= 1
        if count[i] == 0:
            heapq.heappush(que, i)

print(*result)