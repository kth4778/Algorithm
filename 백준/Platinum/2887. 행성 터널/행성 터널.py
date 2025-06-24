import heapq
import sys
input = sys.stdin.readline

N = int(input())
A = [[i] + list(map(int,input().split())) for i in range(N)]

A1 = sorted(A, key = lambda x : x[1])
A2 = sorted(A, key = lambda x : x[2])
A3 = sorted(A, key = lambda x : x[3])

graph = []

for i in range(1, N):
    heapq.heappush(graph, [min(abs(A1[i][1] - A1[i - 1][1]), abs(A1[i][2] - A1[i - 1][2]), abs(A1[i][3] - A1[i - 1][3])), A1[i][0], A1[i - 1][0]])

for i in range(1, N):
    heapq.heappush(graph, [min(abs(A2[i][1] - A2[i - 1][1]), abs(A2[i][2] - A2[i - 1][2]), abs(A2[i][3] - A2[i - 1][3])), A2[i][0], A2[i - 1][0]])

for i in range(1, N):
    heapq.heappush(graph, [min(abs(A3[i][1] - A3[i - 1][1]), abs(A3[i][2] - A3[i - 1][2]), abs(A3[i][3] - A3[i - 1][3])), A3[i][0], A3[i - 1][0]])

parent = [i for i in range(N)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

answer = 0

cost = 0

while graph:
    c,a,b = heapq.heappop(graph)

    if find(a) != find(b):
        union(a, b)
        cost += c

print(cost)