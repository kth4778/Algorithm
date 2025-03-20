n = int(input())

dp = [0,1,1,1,1,1,1,1,1,1]
index = 1

while index < n:
    new_dp = [0 for _ in range(10)]
    
    for i in range(10):
        li = i - 1
        ri = i + 1

        if 0 <= li < 10:
            new_dp[i] += dp[li]
        
        if 0 <= ri < 10:
            new_dp[i] += dp[ri]
    
    dp = new_dp
    index += 1

print(sum(dp) % 1000000000)