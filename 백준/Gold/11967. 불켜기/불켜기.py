from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())

info = [[[] for _ in range(N + 1)] for _ in range(N + 1)]
visited = [[False for _ in range(N + 1)] for _ in range(N + 1)]
ligths_on = [[False for _ in range(N + 1)] for _ in range(N + 1)]

dy = [1,0,0,-1]
dx = [0,1,-1,0]
answer = 1

for _ in range(M):
    y,x,a,b = map(int,input().split())
    info[y][x].append([a,b])


visited[1][1] = True
ligths_on[1][1] = True

que = deque()
que.append([1,1])

while que:
    y,x = que.popleft()

    for a,b in info[y][x]:
        if not ligths_on[a][b]:
            ligths_on[a][b] = True
            answer += 1

            for i in range(4):
                ny, nx = a + dy[i], b + dx[i]
                if 0 < ny <= N and 0 < nx <= N:
                    if visited[ny][nx]:
                        que.append([ny, nx])
                        visited[ny][nx] = True

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 < ny <= N and 0 < nx <= N:
            if not visited[ny][nx] and ligths_on[ny][nx]:
                visited[ny][nx] = True
                que.append([ny,nx])


print(answer)