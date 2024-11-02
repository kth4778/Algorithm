import sys
input = sys.stdin.readline

N = int(input())
lst = list(int(input().strip()) for _ in range(N))
arr = [0 for _ in range(N)]

arr[0] = lst[0]

if N > 1:
    arr[1] = lst[0] + lst[1]

if N > 2:
    arr[2] = max((lst[0] + lst[2]), (lst[1] + lst[2]), arr[1])

for i in range(3, N):
    arr[i] = max(arr[i - 1], arr[i - 3] + lst[i - 1] + lst[i], arr[i - 2] + lst[i])

print(arr[N - 1])