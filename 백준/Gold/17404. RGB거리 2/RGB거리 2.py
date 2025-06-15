import sys
input = sys.stdin.readline

N = int(input())
cost = [list(map(int,input().split())) for _ in range(N)]
dp = [[[float("INF") for _ in range(3)] for _ in range(3)] for _ in range(N)]

for i in range(3):
    dp[0][i][i] = cost[0][i]

for i in range(3):
    dp[0][i][i] = cost[0][i]

for house in range(1, N - 1):
    for nxt in range(3):
        for before in range(3):
            for start in range(3):
                if nxt != before and dp[house - 1][before][start] + cost[house][nxt] < dp[house][nxt][start]:
                    dp[house][nxt][start] = dp[house - 1][before][start] + cost[house][nxt]

for cur in range(3):
    for before in range(3):
        for start in range(3):
            if cur != before and start != cur:
                if dp[N - 2][before][start] + cost[N - 1][cur] < dp[N - 1][cur][start]:
                    dp[N - 1][cur][start] = dp[N - 2][before][start] + cost[N - 1][cur]

answer = float("INF")

for i in range(3):
    for j in range(3):
        answer = min(answer, dp[N - 1][i][j])

print(answer)