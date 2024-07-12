import sys
import heapq
input = sys.stdin.readline

def dijkstra(start,end):
    distance = {i:float("INF") for i in range(1,n+1)}
    distance[start] = 0
    queue = []
    heapq.heappush(queue,[distance[start],start])

    while queue:
        d,cur = heapq.heappop(queue)
        if distance[cur] < d:
            continue
        for weight,next_node in graph[cur]:
            new_distance = weight+d
            if distance[next_node] > new_distance:
                distance[next_node] = new_distance
                heapq.heappush(queue,[new_distance,next_node])
    return distance[end]

n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a,b,cost = map(int,input().split())
    graph[a].append([cost,b])
    graph[b].append([cost,a])
v1,v2 = map(int,input().split())

distance1 = dijkstra(1,v1) + dijkstra(v1,v2) + dijkstra(v2,n)
distance2 = dijkstra(1,v2) + dijkstra(v2,v1) + dijkstra(v1,n)
min_distance = min(distance1,distance2)

if min_distance == float("INF"):
    print(-1)
else:
    print(min_distance)