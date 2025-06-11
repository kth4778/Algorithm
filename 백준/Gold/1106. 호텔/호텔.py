C,N = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)]
dp = [float("INF") for _ in range(C + 100)]

dp[0] = 0

for cost, customer in lst:
    for i in range(customer, C + 100):
        dp[i] = min(dp[i], cost + dp[i - customer])

print(min(dp[C:]))