import sys
input = sys.stdin.readline

V,E = map(int,input().split())
distance = [[float("INF") for _ in range(V + 1)] for _ in range(V + 1)]

for _ in range(E):
    a,b,c = map(int,input().split())
    distance[a][b] = c

for i in range(1, V + 1):
    for j in range(1, V + 1):
        for k in range(1, V + 1):
            distance[j][k] = min(distance[j][k], distance[j][i] + distance[i][k])
        
answer = float("INF")

for i in range(1, V + 1):
    answer = min(answer, distance[i][i])

if answer == float("INF"):
    print(-1)
else:
    print(answer)