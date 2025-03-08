n = int(input())
dp = [1,1]

for _ in range(n):
    a = dp[1] * 2 + dp[0]
    dp[0] = dp[1]
    dp[1] = a

print(dp[1] % 9901)