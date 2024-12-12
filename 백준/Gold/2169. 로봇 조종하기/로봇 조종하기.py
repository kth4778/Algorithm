import copy
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
dp = [[0 for _ in range(M)] for _ in range(N)]

dp[0] = maps[0]

for i in range(1, M):
    dp[0][i] += dp[0][i - 1]

for i in range(1, N):
    left, right = copy.deepcopy(maps[i]), copy.deepcopy(maps[i])
    for j in range(M):
        if j == 0:
            left[j] += dp[i - 1][j]
        else:
            left[j] += max(left[j - 1], dp[i - 1][j])

    for j in range(M - 1, -1, -1):
        if j == M - 1:
            right[j] += dp[i - 1][j]
        else:
            right[j] += max(right[j + 1], dp[i - 1][j])
    
    for j in range(M):
        dp[i][j] = max(left[j], right[j])
    
print(dp[N - 1][M - 1])