import sys
sys.setrecursionlimit(10 ** 5)

def dfs(y,x):
    global is_peak
    cur_hight = farm[y][x]

    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if cur_hight < farm[ny][nx]:
                is_peak = False
            if not visited[ny][nx] and cur_hight == farm[ny][nx]:
                visited[ny][nx] = True
                dfs(ny,nx)

N,M = map(int,input().split())
farm = [list(map(int,input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
answer = 0

dy = [1, 0, 0, -1, 1, 1, -1, -1]
dx = [0, 1, -1, 0, 1, -1, 1, -1]


for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            is_peak = True
            visited[i][j] = True
            dfs(i,j)
            if is_peak:
                answer += 1

print(answer)