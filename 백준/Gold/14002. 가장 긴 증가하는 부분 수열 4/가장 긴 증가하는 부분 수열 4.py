import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

max_size = max(dp)

result = [None for _ in range(max_size)]

for i in range(max_size, 0, -1):
    if i == max_size:
        result[i - 1] = A[dp.index(max_size)]
        continue

    for j in range(n):
        if dp[j] == i and result[i] > A[j]:
            result[i - 1] = A[j]
            break

print(max_size)
print(*result)