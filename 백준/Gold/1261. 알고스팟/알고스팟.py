import heapq

m,n = map(int,input().split())
graph = [list(input()) for _ in range(n)]
distance = [[float("INF") for _ in range(m)] for _ in range(n)]
dx = [1,0,0,-1]
dy = [0,1,-1,0]

distance[0][0] = 0
queue = []
heapq.heappush(queue,[0,0,0])

while queue:
    wall,y,x = heapq.heappop(queue)

    if distance[y][x] < wall:
        continue
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if graph[ny][nx] == '0':
                if distance[ny][nx] > wall:
                    distance[ny][nx] = wall
                    heapq.heappush(queue,[wall,ny,nx])
            else:
                if distance[ny][nx] > wall + 1:
                    distance[ny][nx] = wall+1
                    heapq.heappush(queue,[wall+1,ny,nx])

print(distance[n-1][m-1])

