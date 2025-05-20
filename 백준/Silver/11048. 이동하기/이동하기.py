import sys
input = sys.stdin.readline

N,M = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
distance = [[0 for _ in range(M)] for _ in range(N)]
distance[0][0] = maps[0][0]
dy = [-1,0,-1]
dx = [0,-1,-1]


for i in range(N):
    for j in range(M):
        for k in range(3):
            ny, nx = i + dy[k], j + dx[k]
            if 0 <= ny < N and 0 <= nx < M:
                distance[i][j] = max(distance[i][j], maps[i][j] + distance[ny][nx])

print(distance[N - 1][M - 1])