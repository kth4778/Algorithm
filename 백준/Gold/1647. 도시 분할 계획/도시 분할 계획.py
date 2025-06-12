import heapq
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
answer = 0
maxCost = 0
count = 1

for _ in range(M):
    a,b,cost = map(int,input().split())
    graph[a].append([cost, b])
    graph[b].append([cost, a])

def prim(start):
    global answer
    global maxCost
    global count

    visited[start] = True
    candidate = graph[start]
    heapq.heapify(candidate)

    while candidate and count < N:
        cost, b  = heapq.heappop(candidate)

        if not visited[b]:
            visited[b] = True
            answer += cost
            maxCost = max(maxCost, cost)
            count += 1

            for cost, nxt in graph[b]:
                if not visited[nxt]:
                    heapq.heappush(candidate, [cost, nxt])

prim(1)
print(answer - maxCost)