n = int(input())
dp = [1 for _ in range(10)]

for _ in range(n - 1):
    new_dp = [1 for _ in range(10)]

    for i in range(1, 10):
        new_dp[i] = new_dp[i - 1] + dp[i]

    dp = new_dp

print(sum(dp) % 10_007)