from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
Sy, Sx = map(int,input().split())
Ey, Ex = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(N)]
visited = [[[float("inf") for _ in range(2)] for _ in range(M)] for _ in range(N)]
que = deque()
dy, dx = [1,0,0,-1], [0,1,-1,0]

visited[Sy - 1][Sx - 1][0] = 0
que.append([Sy - 1, Sx - 1, 0, 0])

while que:
    y, x, is_break, move = que.popleft()

    if y == Ey - 1 and x == Ex - 1:
        print(move)
        sys.exit()

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if 0 <= ny < N and 0 <= nx < M:
            if maps[ny][nx] == 0:
                if visited[ny][nx][is_break] > move + 1:
                    visited[ny][nx][is_break] = move + 1
                    que.append([ny, nx , is_break, move + 1])
            
            else:
                if is_break == 0:
                    if visited[ny][nx][is_break] > move + 1:
                        visited[ny][nx][is_break] = move + 1
                        que.append([ny, nx, is_break + 1, move + 1])

print(-1)