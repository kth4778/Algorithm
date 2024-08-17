import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
sy, sx, sdir = map(int,input().split())
ey, ex, edir = map(int,input().split())

dx = [0,1,-1,0,0]
dy = [0,0,0,1,-1]
visited = [[[False for _ in range(5)] for _ in range(m)] for _ in range(n)]
sy -= 1
sx -= 1
ey -= 1
ex -= 1

que = deque()
que.append([0,sy,sx,sdir])
visited[sy][sx][sdir] = True

while que:
    move,y,x,dir = que.popleft()

    if y == ey and x == ex and dir == edir:
        print(move)
        break

    for q in range(1,4):
        nx = x + dx[dir] * q
        ny = y + dy[dir] * q

        if 0 > ny or 0 > nx or n <= ny or m <= nx or maps[ny][nx] == 1:
            break

        if not visited[ny][nx][dir] and maps[ny][nx] == 0:
            que.append([move+1, ny, nx, dir])
            visited[ny][nx][dir] = True
    
    if dir == 1 or dir == 2:
        if not visited[y][x][3]:
            visited[y][x][3] = True
            que.append([move+1,y,x,3])
        if not visited[y][x][4]:
            visited[y][x][4] = True
            que.append([move+1,y,x,4])
    else:
        if not visited[y][x][1]:
            visited[y][x][1] = True
            que.append([move+1,y,x,1])
        if not visited[y][x][2]:
            visited[y][x][2] = True
            que.append([move+1,y,x,2])