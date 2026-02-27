import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def dfs(y, x):
    if y == N - 1 and x == M - 1:
        dp[y][x] = 1
        return 
    
    if dp[y][x] != -1:
        return

    dp[y][x] = 0

    for i in range(4):
        ny, nx = dy[i] + y, dx[i] + x

        if 0 <= ny < N and 0 <= nx < M:
            if maps[y][x] > maps[ny][nx]:
                dfs(ny, nx)
                dp[y][x] += dp[ny][nx]


N, M = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
dp = [[-1 for _ in range(M)] for _ in range(N)]
dy, dx = [1, 0, 0, -1], [0, 1, -1, 0]

dfs(0, 0)

print(dp[0][0])