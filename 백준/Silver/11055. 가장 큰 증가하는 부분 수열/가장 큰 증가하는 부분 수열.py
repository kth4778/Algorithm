N = int(input())
A = list(map(int,input().split()))
dp = [i for i in A]

for i in range(N):
    for j in range(0, i):
        if A[i] > A[j] and dp[i] < A[i] + dp[j]:
            dp[i] = A[i] + dp[j]

print(max(dp))