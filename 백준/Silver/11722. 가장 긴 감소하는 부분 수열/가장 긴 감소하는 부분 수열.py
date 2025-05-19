N = int(input())
A = list(map(int,input().split()))
p = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if A[i] < A[j]:
            p[i] = max(p[i], p[j] + 1)

print(max(p))