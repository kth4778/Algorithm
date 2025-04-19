n = int(input())

dp = [0 for _ in range(31)]
dp[2] = 3

for i in range(4,n + 1):
    if i % 2 != 0:
        continue

    dp[i] += dp[i - 2] * 3
    dp[i] += sum(dp[:i - 2]) * 2
    dp[i] += 2

print(dp[n])