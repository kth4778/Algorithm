import sys
input = sys.stdin.readline

N = int(input())
U = [int(input()) for _ in range(N)]
U.sort()
nums = set()

for i in U:
    for j in U:
        nums.add(i + j)

for i in range(N - 1, -1, -1):
    for j in range(N):
        if U[i] - U[j] in nums:
            print(U[i])
            sys.exit()