from math import ceil

import sys
input = sys.stdin.readline

n = int(input())
p = [None]+list(map(int,input().split()))

dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i] = p[i]
    for j in range(i - 1, ceil(i/2) - 1, -1):
        dp[i] = max(dp[i], dp[j] + dp[i - j])

print(dp[n])