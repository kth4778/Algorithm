T, W = map(int,input().split())
plum = [None] + [int(input()) for _ in range(T)]
dp = [[0 for _ in range(W + 1)] for _ in range(T + 1)]

for i in range(1, T + 1):
    for j in range(W + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + (1 if plum[i] == 1 else 0)
        else:
            if j % 2 == 0:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + (1 if plum[i] == 1 else 0)
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + (1 if plum[i] == 2 else 0)

print(max(dp[T]))