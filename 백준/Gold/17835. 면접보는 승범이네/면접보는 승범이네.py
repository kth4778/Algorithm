import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    distance[start] = 0
    queue = []
    heapq.heappush(queue,[distance[start],start])

    while queue:
        d,cur = heapq.heappop(queue)
        if distance[cur] < d:
            continue
        for weight, next_node in graph[cur]:
            new_distance = weight+d
            if distance[next_node] > new_distance:
                distance[next_node] = new_distance
                heapq.heappush(queue,[new_distance,next_node])
    return distance

n,m,k = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = {i:float("INF") for i in range(1,n+1)}

for _ in range(m):
    s,e,d = map(int,input().split())
    graph[e].append([d,s])

cities = list(map(int,input().split()))

for i in cities:
    dijkstra(i)
for i in cities:
    distance[i] = 0
max_distance = max(distance.values())
for i in distance:
    if distance[i] == max_distance:
        print(i)
        print(distance[i])
        break