import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = {i:float("inf") for i in range(1,n+1)}

for _ in range(m):
    s,e,c = map(int,input().split())
    graph[s].append([e,c])
start,end = map(int,input().split())

distance[start] = 0
queue = []
heapq.heappush(queue,[start,distance[start]])

while queue:
    parents , dist = heapq.heappop(queue)
    if distance[parents] < dist:
        continue

    for node,weight in graph[parents]:
        new_distance = weight+dist
        if distance[node] > new_distance:
            distance[node] = new_distance
            heapq.heappush(queue,[node,distance[node]])
print(distance[end])