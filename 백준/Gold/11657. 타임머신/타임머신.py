import sys
input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
distance = {i:float("inf") for i in range(1,n+1)}
distance[1] = 0

for _ in range(m):
    s,e,cost = map(int,input().split())
    graph[s].append([e,cost])

length = len(graph)
switch = True

for _ in range(1,length-1):
    for i in range(1,length):
        for next_node,weight in graph[i]:
            if distance[i]+weight < distance[next_node]:
                distance[next_node] = distance[i] + weight
            
for i in range(1,length):
    for next_node,weight in graph[i]:
        if distance[i] + weight < distance[next_node]:
            switch = False
            break
    if not switch:
        break

if not switch:
    print(-1)
else:
    for i in range(2,n+1):
        if distance[i] == float('inf'):
            print(-1)
        else:
            print(distance[i])

