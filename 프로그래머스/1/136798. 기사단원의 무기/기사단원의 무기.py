def solution(number, limit, power):
    dp = [0 for _ in range(number + 1)]
    
    for i in range(1, number + 1):
        count = 0
        for j in range(i, number + 1, i):
            dp[j] += 1
    
    answer = 0
    
    for i in dp:
        if i > limit:
            answer += power
        else:
            answer += i
            
    return answer