import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = {i:float("inf") for i in range(1,n+1)}
routs = {i:[] for i in range(1,n+1)}

for _ in range(m):
    a,b,cost = map(int,input().split())
    graph[a].append([b,cost])

start,end = map(int,input().split())
queue = []
distance[start] = 0
heapq.heappush(queue,[start,[start],distance[start]])

while queue:
    parents,rout,dist = heapq.heappop(queue)

    if distance[parents] < dist:
        continue
    for node,weight in graph[parents]:
        new_distance = dist+weight
        new_rout = rout+[node]
        if distance[node] > new_distance:
            distance[node] = new_distance
            routs[node] = new_rout
            heapq.heappush(queue,[node,new_rout,distance[node]])
print(distance[end])
print(len(routs[end]))
for i in routs[end]:
    print(i,end = ' ')
