import sys
import heapq
input = sys.stdin.readline

n,m,k = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = {i:[float("INF") for _ in range(k+1)] for i in range(1,n+1)}

for _ in range(m):
    a,b,cost = map(int,input().split())
    graph[a].append([cost,b])
    graph[b].append([cost,a])

for i in range(k+1):
    distance[1][i] = 0

queue = []
heapq.heappush(queue,[0,1,0])

while queue:
    d,cur,cnt = heapq.heappop(queue)
    if distance[cur][cnt] < d:
        continue

    for weight,next_node in graph[cur]:
        new_distance = weight+d
        if distance[next_node][cnt] > new_distance:
            distance[next_node][cnt] = new_distance
            heapq.heappush(queue,[new_distance,next_node,cnt])
        if cnt < k and distance[next_node][cnt+1] > d:
            distance[next_node][cnt+1] = d
            heapq.heappush(queue,[d,next_node,cnt+1])
print(min(distance[n]))
