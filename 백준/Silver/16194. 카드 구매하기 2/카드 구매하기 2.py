from math import ceil
import sys
input = sys.stdin.readline

N = int(input())
nums = [None] + list(map(int,input().split()))

for i in range(1, N + 1):
    for j in range(i - 1, ceil(i / 2) - 1, -1):
        nums[i] = min(nums[i], nums[j] + nums[i - j])

print(nums[N])