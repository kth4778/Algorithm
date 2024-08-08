import sys
import heapq
input = sys.stdin.readline

n,m,a,b,c = map(int,input().split())
graph = [[] for _ in range(n+1)]
costs = []

for _ in range(m):
    s,e,cost = map(int,input().split())
    graph[s].append([e,cost])
    graph[e].append([s,cost])
    costs.append(cost)

costs = sorted(list(set(costs)))

def Dijsktra(limit):
    distance = {i:float("INF") for i in range(1,n+1)}
    distance[a] = 0
    queue = [[0,a]]

    while queue:
        d,cur = heapq.heappop(queue)
        if distance[cur] < d:
            continue
        for node,weight in graph[cur]:
            if weight > limit:
                continue
            new_distance = weight + d
            if distance[node] > new_distance:
                distance[node] = new_distance
                heapq.heappush(queue,[new_distance,node])
    if distance[b] > c:
        return float("INF")
    return distance[b]

l = 0
r = len(costs) - 1
answers = float("INF")

while l <= r:
    mid = (l + r) // 2
    total = Dijsktra(costs[mid])
    if total == float("INF"):
        l = mid + 1

    else:
        r = mid - 1
        answers = min(costs[mid],answers)

if answers == float("INF"):
    print(-1)
else:
    print(answers)