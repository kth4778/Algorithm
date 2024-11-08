import heapq
import sys
input = sys.stdin.readline

N,M = map(int,input().split())

node_info = [[] for _ in range(N + 1)]
distance = {i:float("INF") for i in range(1,N + 1)}

for _ in range(M):
    a,b,c = map(int,input().split())   
    node_info[a].append([b,c])
    node_info[b].append([a,c])

que = []
distance[1] = 0

heapq.heappush(que, [distance[1], 1])

while que:
    d,cur = heapq.heappop(que)

    if d > distance[cur]:
        continue

    for next_node, weight in node_info[cur]:
        new_distance = weight + d

        if new_distance < distance[next_node]:
            distance[next_node] = new_distance
            heapq.heappush(que, [new_distance, next_node])

print(distance[N])