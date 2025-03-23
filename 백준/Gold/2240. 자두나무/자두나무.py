t,w = map(int,input().split())
fruits = [0] + [int(input()) for _ in range(t)]

dp = [[0 for _ in range(w + 1)] for _ in range(t + 1)]

for i in range(1, t + 1):
    fruit = fruits[i]
    
    if fruit == 1:
        dp[i][0] = dp[i - 1][0] + 1
    else:
        dp[i][0] = dp[i - 1][0]
    
    for j in range(1, w + 1):

        if (fruit == 1 and j % 2 == 0) or (fruit == 2 and j % 2 == 1):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])
    
print(max(dp[t]))