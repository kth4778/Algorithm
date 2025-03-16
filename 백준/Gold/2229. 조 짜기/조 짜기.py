import sys
input = sys.stdin.readline

n = int(input())
students = list(map(int,input().split()))

dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    max_v = min_v = students[i - 1]
    
    for j in range(i, 0, -1):
        max_v = max(max_v, students[j - 1])
        min_v = min(min_v, students[j - 1])

        dp[i] = max(dp[i], dp[j - 1] + (max_v - min_v))
    
print(max(dp))