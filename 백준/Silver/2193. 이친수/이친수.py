N = int(input())
dp = [0 for _ in range(N + 1)]

dp[1] = 1

if N == 1:
    print(1)
    exit()
else:
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[N])