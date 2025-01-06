T = int(input())

dp = [0 for _ in range(1_000_001)]

dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, 1_000_001):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3])  % 1_000_000_009

for _ in range(T):
    n = int(input())
    print(dp[n])