import heapq
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([c,b])
    graph[b].append([c,a])
graph = [sorted(i,key=lambda x: -x[0]) for i in graph]

start,end = map(int,input().split())

distance = {i:0 for i in range(1,n+1)}
queue = []
heapq.heappush(queue,[0,start])

while queue:
    w,cur = heapq.heappop(queue)
    if cur == end:
        print(-w)
        break
    w *= -1
    if distance[cur] > w:
        continue

    for weight,node in graph[cur]:
        if w == 0:
            distance[node] = weight
            heapq.heappush(queue,[-weight,node])
        elif distance[node] < weight and distance[node] < w:
            distance[node] = min(weight,w)
            heapq.heappush(queue,[-distance[node],node])