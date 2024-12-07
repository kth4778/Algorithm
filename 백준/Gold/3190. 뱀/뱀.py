from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

maps = [[0 for _ in range(N)] for _ in range(N)] # 0: 빈 공간, 1: 지렁이, 2: 사과
dy = [0,1,0,-1]  #우하좌상
dx = [1,0,-1,0]
maps[0][0] = 1

for _ in range(K):
    y,x = map(int,input().split())
    maps[y - 1][x - 1] = 2

L = int(input())
direction_info = {}

for _ in range(L):
    a,b = input().split()
    direction_info[int(a)] = b

mode = 0
time = 0
snake = deque()
y,x = 0,0

snake.append([0,0])

while True:
    ny, nx = y + dy[mode], x + dx[mode]
    if 0 > ny or N <= ny or 0 > nx or N <= nx:
        break
    
    if maps[ny][nx] == 1:
        break

    if maps[ny][nx] != 2:
        i,j = snake.popleft()
        maps[i][j] = 0
    
    y,x = ny,nx
    maps[ny][nx] = 1
    snake.append([ny,nx])

    time += 1
    
    if time in direction_info.keys():
        if direction_info[time] == 'D':
            mode = (mode + 1) % 4
        else:
            if mode == 0:
                mode = 3
            else:
                mode -= 1

print(time + 1)