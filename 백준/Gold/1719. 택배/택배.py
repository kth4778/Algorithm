import heapq
import sys

input = sys.stdin.readline

def solution(start):
    weight = [float("INF") for _ in range(n + 1)]
    weight[start] = 0
    que = []
    heapq.heappush(que, [0, start, [start]])

    m = [[] for _ in range(n + 1)]

    while que:
        distance, cur, memory = heapq.heappop(que)

        if distance > weight[cur]:
            continue

        for next_node, d in nodes[cur]:
            new_distance = d + distance

            if weight[next_node] > new_distance:
                m[next_node] = memory + [next_node]
                weight[next_node] = new_distance
                heapq.heappush(que, [new_distance, next_node, memory + [next_node]])
    
    return m

n,m = map(int,input().split())
nodes = [[] for _ in range(n + 1)]
result = [["-" for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a,b,c = map(int,input().split())
    nodes[a].append([b,c])
    nodes[b].append([a,c])

for i in range(1, n + 1):
    p = solution(i)
    for j in range(i + 1, n + 1): 
        result[i - 1][j - 1] = p[j][1]
        result[j - 1][i - 1] = p[j][-2]

for i in result:
    print(*i)