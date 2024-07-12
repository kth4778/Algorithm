import sys
import heapq
input = sys.stdin.readline

v,e = map(int,input().split())
start_node = int(input())

distance = {i:float("INF") for i in range(1,v+1)}
graph = [[] for _ in range(v+1)]

for _ in range(e):
    s,e,cost = map(int,input().split())
    graph[s].append([cost,e])

distance[start_node] = 0
queue = []
heapq.heappush(queue,[distance[start_node],start_node])

while queue:
    dist,cur = heapq.heappop(queue)
    if distance[cur] < dist:
        continue
    
    for weight, next_node in graph[cur]:
        new_distance = dist+weight
        if distance[next_node] > new_distance:
            distance[next_node] = new_distance
            heapq.heappush(queue,[new_distance,next_node])
for i in range(1,v+1):
    if distance[i] == float("INF"):
        print("INF")
    else:
        print(distance[i])