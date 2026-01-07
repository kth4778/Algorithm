def solution(info, n, m):
    dp = [float("INF") for _ in range(m)]
    dp[0] = 0

    for A, B in info:
        switch = False 
        next_dp = [float("INF") for _ in range(m)]
        
        for i in range(m):
            if dp[i] != float("INF"):
                if dp[i] + A < n:
                    next_dp[i] = min(next_dp[i], dp[i] + A)
                    switch = True
                if i + B < m:
                    next_dp[i + B] = min(next_dp[i + B], dp[i])
                    switch = True
        dp = next_dp

        if not switch:
            return -1
    return min(dp)
