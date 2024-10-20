import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def dfs(y,x):
    if dp[y][x]:
        return dp[y][x]
    
    dp[y][x] = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < N and 0 <= nx < N and maps[y][x] < maps[ny][nx]:
            dp[y][x] = max(dp[y][x], dfs(ny, nx) + 1)
        
    return dp[y][x]


N = int(input())
maps = [list(map(int,input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
answer = 0

dy = [1,0,0,-1]
dx = [0,1,-1,0]

for i in range(N):
    for j in range(N):
        if not dp[i][j]:
            dfs(i,j)

for i in dp:
    answer = max(answer, max(i))

print(answer)