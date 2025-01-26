from collections import deque
from itertools import combinations
import copy
import sys
input = sys.stdin.readline

def bfs(coordinates):
    copy_maps = copy.deepcopy(maps)
    que = deque()

    for i,j in coordinates:
        copy_maps[i][j] = 'v'
        que.append([i,j])
    
    time = -1

    while que:
        for _ in range(len(que)):
            y,x = que.popleft()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < N:
                    if copy_maps[ny][nx] == 0:
                        copy_maps[ny][nx] = 'v'
                        que.append([ny,nx])
        time += 1

    for i in range(N):
        for j in range(N):
            if copy_maps[i][j] == 0:
                return float("INF")

    return time

N,M = map(int,input().split())
maps = [[0 for _ in range(N)] for _ in range(N)]
available_virus = []
dx = [1,0,0,-1]
dy = [0,1,-1,0]
answer = float("INF")


for i in range(N):
    lst = list(map(int,input().split()))
    for j in range(N):
        if lst[j] == 2:
            available_virus.append([i,j])
        elif lst[j] == 1:
            maps[i][j] = 'w'


for i in combinations(available_virus, M):
    answer = min(answer, bfs(list(i)))

if answer == float("INF"):
    print(-1)
else:
    print(answer)