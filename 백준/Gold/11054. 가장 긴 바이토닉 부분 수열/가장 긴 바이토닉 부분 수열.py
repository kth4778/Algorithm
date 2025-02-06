n = int(input())
A1 = list(map(int,input().split()))
A2 = A1[::-1]

dp1 = [1 for _ in range(n)]
dp2 = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if A1[i] > A1[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

for i in range(n):
    for j in range(i):
        if A2[i] > A2[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

dp2 = dp2[::-1]

result = [dp1[i] + dp2[i] - 1 for i in range(n)]

print(max(result))