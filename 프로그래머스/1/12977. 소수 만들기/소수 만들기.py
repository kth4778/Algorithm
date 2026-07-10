from itertools import combinations

def solution(nums):
    nums.sort()
    
    result = 0
    l = sum(nums[-3:])
    
    dp = [0 for _ in range(l + 1)]
    
    for i in range(1, l + 1):
        for j in range(i, l + 1, i):
            dp[j] += 1
    
    for i in combinations(nums, 3):
        if dp[sum(i)] == 2:
            result += 1
    
    return result