import heapq
import sys
input = sys.stdin.readline

def solution(start):
    result = 0

    distance = {i:float("INF") for i in range(N)}
    distance[start] = 0

    q = []
    heapq.heappush(q,[distance[start],start])

    while q:
        d,cur = heapq.heappop(q)

        if d > distance[cur]:
            continue

        for next_node, nd in node_info[cur]:
            new_distance = d + nd
            if distance[next_node] > new_distance:
                heapq.heappush(q, [new_distance, next_node])
                distance[next_node] = new_distance

    for i in distance:
        if distance[i] <= M:
            result += items[i]
    return result

N,M,R = map(int,input().split())
items = list(map(int,input().split()))
node_info = [[] for _ in range(N)]
answer = 0

for _ in range(R):
    a,b,d = map(int,input().split())
    node_info[a - 1].append([b - 1,d])
    node_info[b - 1].append([a - 1,d])

for i in range(N):
    answer = max(answer, solution(i))

print(answer)