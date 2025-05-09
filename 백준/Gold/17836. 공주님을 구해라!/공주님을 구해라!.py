from collections import deque
import sys

input = sys.stdin.readline

N,M,T = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]


visited = [[[float("INF") for _ in range(2)] for _ in range(M)] for _ in range(N)]
dy, dx = [1,0,0,-1], [0,1,-1,0]
que = deque()
que.append([0, 0, 0, False])
answer = float("INF")
visited[0][0][0] = 0

while que:
    y,x,move,gram = que.popleft()

    if y == N - 1 and x == M - 1:
        if move <= T:
            print(move)
            sys.exit()
        else:
            continue

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if gram:
                if visited[ny][nx][1] > move + 1:
                    visited[ny][nx][1] = move + 1
                    que.append([ny, nx, move + 1, gram])
            else:
                if visited[ny][nx][0] > move + 1 and maps[ny][nx] != 1:
                    visited[ny][nx][0] = move + 1
                    if maps[ny][nx] == 2:
                        que.append([ny, nx, move + 1, not gram])
                    else:
                        que.append([ny, nx, move + 1, gram])

print("Fail")