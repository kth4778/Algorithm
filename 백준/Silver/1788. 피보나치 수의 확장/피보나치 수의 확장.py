n = int(input())
dp = [0,1]

for _ in range(2, abs(n) + 1):
    dp[0], dp[1] = dp[1], (dp[0] + dp[1]) % 1000000000

if n < 0 and n % 2 == 0:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)

if n == 0:
    print(0)
else:
    print(abs(dp[1]))