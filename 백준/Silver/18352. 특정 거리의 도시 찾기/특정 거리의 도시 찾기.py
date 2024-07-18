import heapq
import sys
input = sys.stdin.readline

n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = {i:float("INF") for i in range(1,n+1)}

for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append([1,e])

distance[x] = 0
queue = []
heapq.heappush(queue,[distance[x],x])

while queue:
    w,cur = heapq.heappop(queue)
    if w > distance[cur]:
        continue
    for weight,node in graph[cur]:
        new_distance = weight+w
        if new_distance < distance[node]:
            distance[node] = new_distance
            heapq.heappush(queue,[distance[node],node])

result = [i for i in distance if distance[i] == k]
if not result:
    print(-1)
else:
    for i in result:
        print(i)