from collections import deque
import sys
input = sys.stdin.readline

def dfs(n, Rcnt, Gcnt, lst):
    global answer
    if n == TC:
        if Rcnt == R and Gcnt == G:
            answer = max(answer, bfs(lst))
        return
    
    dfs(n + 1, Rcnt + 1, Gcnt, lst + [-1])
    dfs(n + 1, Rcnt, Gcnt + 1, lst + [1])
    dfs(n + 1, Rcnt, Gcnt, lst + [0])

def bfs(lst):
    que = deque()
    new_garden = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0

    for i in range(TC):
        if lst[i] == 0:
            continue
        ly, lx = land[i]
        new_garden[ly][lx] = lst[i]
        que.append([ly, lx])

    while que:
        y, x = que.popleft()

        if new_garden[y][x] == 2500:
            continue
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < M and 0 <= ny < N and garden[ny][nx] != 0:
                if new_garden[ny][nx] == 0:
                    if new_garden[y][x] < 0:
                        new_garden[ny][nx] = new_garden[y][x] - 1
                        que.append([ny, nx])
                    else:
                        new_garden[ny][nx] = new_garden[y][x] + 1
                        que.append([ny, nx])
                else:
                    if new_garden[y][x] < 0:
                        if new_garden[y][x] - 1 + new_garden[ny][nx] == 0:
                            new_garden[ny][nx] = 2500
                            cnt += 1
                    else:
                        if new_garden[y][x] + 1 + new_garden[ny][nx] == 0:
                            new_garden[ny][nx] = 2500
                            cnt += 1

    return cnt

N, M, G, R = map(int,input().split())
garden = [list(map(int,input().split())) for _ in range(N)]
land = []
answer = 0

dx = [1,0,0,-1]
dy = [0,1,-1,0]

for i in range(N):
    for j in range(M):
        if garden[i][j] == 2:
            land.append([i,j])

TC = len(land)
dfs(0, 0, 0, [])
print(answer) 