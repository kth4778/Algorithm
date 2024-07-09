import heapq
import sys
input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(v):
    a = list(map(int,input().split()))
    set_idx = a[0]
    for i in range(1,len(a)-1,2):
        graph[set_idx].append([a[i],a[i+1]])

def dijkstra(graph,node,v):
    distance = {i:float("inf") for i in range(1,v+1)}
    queue = []
    distance[node] = 0
    heapq.heappush(queue,[node,distance[node]])
    
    while queue:
        parents,dist = heapq.heappop(queue)
        if distance[parents] < dist:
            continue
        for node,weight in graph[parents]:
            new_distance = weight+dist
            if distance[node] > new_distance:
                distance[node] = new_distance
                heapq.heappush(queue,[node,distance[node]])
    max_dist = max(distance.values())
    for i in distance:
        if distance[i] == max_dist:
            return i,max_dist
start_node,_ = dijkstra(graph,1,v)
_,end_dist = dijkstra(graph,start_node,v)
print(end_dist)