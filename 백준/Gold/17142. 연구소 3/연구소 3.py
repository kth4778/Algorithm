from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

def bfs(coordinates, remain_cnt):
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    que = deque()
    time = 0

    for y,x, in coordinates:
        visited[y][x] = 0
        que.append([y,x])

    while que and remain_cnt > 0:
        y,x = que.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] == -1 and maps[ny][nx] != 'W':
                    visited[ny][nx] = visited[y][x] + 1
                    if maps[ny][nx] == 0:
                        remain_cnt -= 1
                    time = max(time, visited[ny][nx])
                    que.append([ny,nx])
                    
    if remain_cnt > 0:
        return float("INF")
    return time

N,M = map(int,input().split())
maps = [[0 for _ in range(N)] for _ in range(N)]
virus = []
dy = [1,0,0,-1]
dx = [0,1,-1,0]
answer = float("inf")
empty_cnt = N ** 2

for i in range(N):
    lst = list(map(int,input().split()))
    for j in range(N):
        if lst[j] == 1:
            maps[i][j] = 'W'
            empty_cnt -= 1

        elif lst[j] == 2:
            virus.append([i,j])
            maps[i][j] = 'N'
            empty_cnt -= 1

for i in combinations(virus, M):
    answer = min(answer, bfs(list(i), empty_cnt))

if answer == float("INF"):
    print(-1)
else:
    print(answer)