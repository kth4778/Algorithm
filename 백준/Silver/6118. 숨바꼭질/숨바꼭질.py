import heapq
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = []
distance = {i:float("inf") for i in range(1,n+1)}
heapq.heappush(queue,[1,0])
distance[1] = 0

while queue:
    node,dist = heapq.heappop(queue)
    if distance[node] < dist:
        continue

    for i in graph[node]:
        new_distance = dist + 1
        if new_distance < distance[i]:
            distance[i] = new_distance
            heapq.heappush(queue,[i,new_distance])
max_node_num = max(distance.values())
max_node = [i for i in distance if distance[i] == max_node_num]

print(max_node[0],max_node_num,len(max_node))