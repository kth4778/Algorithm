import sys
input = sys.stdin.readline
from collections import deque
          

N,H,D = map(int,input().split())
maps = []

visited = [[0 for _ in range(N)] for _ in range(N)]
answer = float("INF")
dx = [1,0,0,-1]
dy = [0,1,-1,0]
sy = sx = -1

for i in range(N):
    lst = list(input())
    for j in range(N):
        if lst[j] == 'S':
            sy, sx = i,j
    maps.append(lst)

que = deque()
que.append([sy,sx,0,0,H])

while que:
    y, x, umbrella, move, hp = que.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if maps[ny][nx] == 'E':
                print(move + 1)
                exit()

            Nhp, Numbrella = hp, umbrella

            if maps[ny][nx] == 'U':
                Numbrella = D

            if Numbrella > 0:
                Numbrella -= 1
            else:
                Nhp -= 1
            
            if Nhp > 0 and Numbrella + Nhp > visited[ny][nx]:
                que.append([ny, nx, Numbrella, move + 1, Nhp])
                visited[ny][nx] = Numbrella + Nhp

print(-1)