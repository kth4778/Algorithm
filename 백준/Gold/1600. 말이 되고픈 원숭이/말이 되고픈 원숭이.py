import heapq
import sys
input = sys.stdin.readline

k = int(input())
m,n = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
visited = [[[False for _ in range(k+1)] for _ in range(m)] for _ in range(n)]

dx = [1,0,0,-1,1,2,2,1,-1,-2,-2,-1]
dy = [0,1,-1,0,2,1,-1,-2,-2,-1,1,2]

queue = [[0,k,0,0]]
for i in range(k+1):
    visited[0][0][i] = True
result = -1

while queue:
    move,t,y,x = heapq.heappop(queue)
    if y == n-1 and x == m-1:
        result = move
        break

    if t > 0:
        for i in range(12):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 0:
                if i < 4:
                    if not visited[ny][nx][t]:
                        heapq.heappush(queue,[move+1,t,ny,nx])
                        visited[ny][nx][t] = True
                else:
                    if not visited[ny][nx][t-1]:
                        heapq.heappush(queue,[move+1,t-1,ny,nx])
                        visited[ny][nx][t-1] = True
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 0:
                if not visited[ny][nx][t]:
                    visited[ny][nx][t] = True
                    heapq.heappush(queue,[move+1,t,ny,nx])

print(result)