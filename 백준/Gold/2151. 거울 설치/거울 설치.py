from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
maps = []
door = [None, None]

distance = [[[float("INF") for _ in range(4)] for _ in range(N)] for _ in range(N)]
dy = [0,0,-1,1]  # 좌 우 상 하
dx = [-1,1,0,0]

for y in range(N):
    road = list(input().strip())
    maps.append(road)

    for x in range(N):
        if road[x] == "#":
            if door[0] == None:
                door[0] = [y,x]
            else:
                door[1] = [y,x]

modes = []

for i in range(4):
    ny, nx = door[0][0] + dy[i], door[0][1] + dx[i]
    if 0 <= ny < N and 0 <= nx < N:
        if maps[ny][nx] != '*':
            modes.append(i)

que = deque()

for mode in modes:
    que.append([door[0][0], door[0][1], mode, 0])
    distance[door[0][0]][door[0][1]][mode] = 0

answer = float("INF")

while que:
    y, x, m, move = que.popleft()

    if y == door[1][0] and x == door[1][1]:
        answer = min(answer, move)
        continue

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if maps[ny][nx] != "*":
                if maps[y][x] == ".":
                    if m == i and distance[ny][nx][m] > move:
                        que.append([ny, nx, m, move])
                        distance[ny][nx][m] = move
                else:
                    if i == m and distance[ny][nx][m] > move:
                        que.append([ny, nx, m, move])
                        distance[ny][nx][m] = move
                    else:
                        if distance[ny][nx][i] > move + 1:
                            que.append([ny, nx, i, move + 1])
                            distance[ny][nx][i] = move + 1

print(answer)