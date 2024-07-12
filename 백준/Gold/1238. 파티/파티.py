import copy
import heapq
import sys
input = sys.stdin.readline

def dijkstra(start,end):
    distance = {i:float("inf") for i in range(1,n+1)}
    queue = []
    distance[start] = 0
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

n,m,x = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s,e,t = map(int,input().split())
    graph[s].append([t,e])

results = []

for i in range(1,n+1):
    results.append(dijkstra(i,x)+dijkstra(x,i))
print(max(results))