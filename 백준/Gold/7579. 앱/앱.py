import sys
input = sys.stdin.readline

N,M = map(int,input().split())
A = list(map(int,input().split()))
C = list(map(int,input().split()))

maxCost = sum(C)
dp = [0 for _ in range(maxCost + 1)] 

for i in range(N):
    memory = A[i]
    cost = C[i]

    for j in range(maxCost, cost - 1, -1):
        dp[j] = max(dp[j], dp[j - cost] + memory)

for i in range(maxCost + 1):
    if dp[i] >= M:
        print(i)
        break