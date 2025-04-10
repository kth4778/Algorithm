from math import sqrt

n = int(input())
dp = [i for i in range(n + 1)]
 
for i in range(1, n + 1):
    if (i ** 0.5) % 1 == 0:
        dp[i] = 1
    else:
        for j in range(2, int(sqrt(i)) + 1):
            dp[i] = min(dp[i], dp[i - j ** 2] + 1)
print(dp[n])