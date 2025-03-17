import sys
import heapq

input = sys.stdin .readline

def solution(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, [0, start])

    while q:
        cur_distance, cur = heapq.heappop(q)

        for next_node, weight in graph[cur]:
            new_distance = cur_distance + weight
            if distance[next_node] > new_distance:
                distance[next_node] = new_distance
                heapq.heappush(q, [new_distance, next_node])


n,d = map(int,input().split())
graph = [[] for _ in range(d + 1)]
distance = [float("INF") for _ in range(d + 1)]

for i in range(d):
    graph[i].append([i + 1, 1])

for _ in range(n):
    start, end, dis = map(int,input().split())
    if end - start < dis:
        continue

    if start > d or end > d:
        continue

    graph[start].append([end, dis])

solution(0)

print(distance[-1])