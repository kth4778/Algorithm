import heapq
import sys
input = sys.stdin.readline

def Dikgstra(s):
    distance = {i:float("inf") for i in range(1,n+1)}
    distance[s] = 0

    queue = [[0,s]]
    while queue:
        d,cur = heapq.heappop(queue)

        if distance[cur] < d:
            continue 

        for next_node, weight in graph[cur]:
            new_distance = weight + d
            if distance[next_node] > new_distance:
                distance[next_node] = new_distance
                heapq.heappush(queue, [new_distance, next_node])

    return distance.values()
 
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])

for i in range(1,n+1):
    for j in Dikgstra(i):
        if j == float("inf"):
            print(0, end = " ")
            continue
        print(j, end = " ")
    print()