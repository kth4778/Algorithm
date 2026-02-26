c, n = map(int,input().split())
dp = [float("INF") for _ in range(100001)]
info = []

for _ in range(n):
    cost, count = map(int,input().split())
    info.append([cost, count])
    dp[count] = min(cost, dp[count])

for _ in range(n):
    for i in range(c + 1):
        if dp[i] != float("INF"):
            for cost, count in info:
                if i + count <= 100000:
                    dp[i + count] = min(dp[i + count], dp[i] + cost)

print(min(dp[c:]))