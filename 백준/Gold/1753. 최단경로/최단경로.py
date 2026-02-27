import heapq
import sys
input = sys.stdin.readline

V, E = map(int,input().split())
K = int(input())

graph = [[] for _ in range(V)]

for _ in range(E):
    s, e, c = map(int,input().split())
    graph[s - 1].append([e - 1, c])

def dijkstra(graph, s):
    distance = [float("INF") for _ in range(len(graph))]
    distance[s] = 0

    que = []
    
    heapq.heappush(que, [0, s])

    while que:
        dist, cur = heapq.heappop(que)

        if distance[cur] < dist:
            continue

        for next_node, cost in graph[cur]:
            if distance[next_node] > cost + dist:
                distance[next_node] = cost + dist
                heapq.heappush(que, [cost + dist, next_node])
    
    return distance

for i in dijkstra(graph, K - 1):
    if i == float('inf'):
        print("INF")
    else:
        print(i)