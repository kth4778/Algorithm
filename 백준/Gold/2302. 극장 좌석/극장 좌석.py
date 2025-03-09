n = int(input())
m = int(input())
seats = [int(input()) for _ in range(m)]

if n == 1:
    print(1)
    exit()

dp = [0 for _ in range(n + 1)]
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

nums = [False for _ in range(n + 1)]

for i in seats:
    nums[i] = True

s = ""

for i in range(1, n + 1):
    if not nums[i]:
        s += "t"
    else:
        s += "f"

answer = 1

for i in s.split("f"):
    answer *= dp[len(i)]

print(answer)