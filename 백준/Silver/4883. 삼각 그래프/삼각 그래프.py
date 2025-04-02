import sys
input = sys.stdin.readline

test_count = 1

while True:
    n = int(input())

    if n == 0:
        sys.exit()
    
    else:
        dp = [list(map(int,input().split())) for _ in range(n)]

        dp[1][0] += dp[0][1]
        dp[1][1] += min(dp[0][1], dp[1][0], dp[0][1] + dp[0][2])
        dp[1][2] += min(dp[0][1], dp[1][1], dp[0][1] + dp[0][2])
    
        for i in range(2, n):
            dp[i][0] += min(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] += min(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2], dp[i][0])
            dp[i][2] += min(dp[i - 1][1], dp[i - 1][2], dp[i][1])
        
        print(f"{test_count}. {dp[n - 1][1]}")
        test_count += 1
