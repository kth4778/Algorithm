import copy
from itertools import combinations
from collections import deque

N, M = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
virus = []
wall = []
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
answer = -1

for y in range(N):
    for x in range(M):
        if maps[y][x] == 2:
            virus.append([y, x])
        elif maps[y][x] == 0:
            wall.append([y, x])

def safe_size(w):
    copy_maps = copy.deepcopy(maps)
    visited = [[False for _ in range(M)] for _ in range(N)]

    for y, x in w:
        copy_maps[y][x] = 1
    
    que = deque()

    for y, x in virus:
        que.append([y, x])
    
    while que:
        y, x = que.popleft()

        for i in range(4):
            ny, nx = dy[i] + y, dx[i] + x
            if 0 <= nx < M and 0 <= ny < N:
                if not visited[ny][nx] and copy_maps[ny][nx] == 0:
                    copy_maps[ny][nx] = 2
                    visited[ny][nx] = True
                    que.append([ny, nx])

    result = 0

    for y in range(N):
        for x in range(M):
            if copy_maps[y][x] == 0:
                result += 1

    return result

for w in combinations(wall, 3):
    answer = max(answer, safe_size(w))

print(answer)