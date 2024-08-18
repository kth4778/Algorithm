from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
maps = [list(input().strip()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
sy, sx, ey, ex = 0,0,0,0
water_coordinate = deque()
dy = [1,0,0,-1]
dx = [0,1,-1,0]

for i in range(n):
    for j in range(m):
        if maps[i][j] == 'S':
            sy, sx = i, j
        if maps[i][j] == 'D':
            ey, ex = i, j
        if maps[i][j] == '*':
            water_coordinate.append([i,j])
            maps[i][j] = 'X'

que = deque()
que.append([0,sy,sx])
visited[sy][sx] = True

while que:
    for _ in range(len(water_coordinate)):
        y,x = water_coordinate.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == '.':
                maps[ny][nx] = 'X'
                water_coordinate.append([ny,nx])

    for _ in range(len(que)):
        move,y,x = que.popleft()
        if y == ey and x == ex:
            print(move)
            sys.exit()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != 'X' and not visited[ny][nx]:
                visited[ny][nx] = True
                que.append([move+1, ny, nx])

print('KAKTUS')