N = int(input())
box = list(map(int,input().split()))

dp = [0 for _ in range(N)]

for i in range(N):
    dp[i] = 1
    for j in range(0,i):
        if box[i] > box[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))