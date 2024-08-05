from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
maps = [list(input().strip()) for _ in range(n)]

water_visited = [[False for _ in range(m)] for _ in range(n)]
swan_visited = [[False for _ in range(m)] for _ in range(n)]
swan_coordinate = []
water_que = deque()
swan_que = deque()
dx = [1,0,0,-1]
dy = [0,1,-1,0]


for i in range(n):
    for j in range(m):
        if maps[i][j] != 'X':
            water_que.append([i,j])
            water_visited[i][j] = True
        if maps[i][j] == 'L':
            swan_coordinate.append([i,j])
            maps[i][j] = '.'
sy,sx = swan_coordinate[0]
ey,ex = swan_coordinate[1]
swan_que.append([sy,sx])
swan_visited[sy][sx] = True

def melt():
    new_water_que = deque()
    while water_que:
        y,x = water_que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < n and 0 <= nx < m and not water_visited[ny][nx]:
                if maps[ny][nx] == 'X':
                    water_visited[ny][nx] = True
                    maps[ny][nx] = '.'
                    new_water_que.append([ny,nx])
    return new_water_que

def meetable():
    new_swan_que = deque()
    while swan_que:
        y,x = swan_que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < n and 0 <= nx < m and not swan_visited[ny][nx]:
                if ny == ey and nx == ex:
                    return True
                if maps[ny][nx] == '.':
                    swan_que.append([ny,nx])
                else:
                    new_swan_que.append([ny,nx])
                swan_visited[ny][nx] = True
    swan_que.extend(new_swan_que)
    return False

result = 0

while True:
    if meetable():
        print(result)
        break
    water_que = melt()
    result += 1