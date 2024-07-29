import heapq
import sys
input = sys.stdin.readline

m,n = map(int,input().split())
maps = []
razer = []
for i in range(n):
    maps.append(list(input().rstrip()))
    for j in range(m):
        if maps[i][j] == 'C':
            razer.append([i,j])

(sy,sx),(ey,ex) = razer[0],razer[1]
dx = [1,0,0,-1]
dy = [0,1,-1,0]
distance = [[float("INF") for _ in range(m)] for _ in range(n)]
visited = [[[False]*m for _ in range(n)] for _ in range(2)]

def Digkstra(sy,sx):
    distance[sy][sx] = 0
    maps[sy][sx] = '*'
    queue = []
    for i in range(4):
        heapq.heappush(queue,[0,sy,sx,i])
        visited[i%2][sy][sx] = True
    while queue:
        dp,y,x,direction = heapq.heappop(queue)
        if distance[y][x] < dp:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not (0 <= ny < n and 0 <= nx < m) or maps[ny][nx] == '*':
                continue
            plus = 0
            if direction != i:
                plus += 1
            cost = plus + dp
            if cost < distance[ny][nx] or (cost == distance[ny][nx] and not visited[i%2][ny][nx] ):
                distance[ny][nx] = cost
                heapq.heappush(queue,[cost,ny,nx,i])
                visited[i%2][ny][nx] = True
Digkstra(sy,sx)
print(distance[ey][ex] if distance[ey][ex] != float("INF") else -1)