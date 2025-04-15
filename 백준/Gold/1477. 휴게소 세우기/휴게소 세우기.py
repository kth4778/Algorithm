from math import ceil
import sys
input = sys.stdin.readline

n,m,l = map(int,input().split())
p = list(map(int,input().split()))
p.sort()

p = [0] + p + [l]

dp = []

for i in range(1, n + 2):
    dp.append(p[i] - p[i - 1])

size= len(dp)
count = [1 for _ in range(size)]

for _ in range(m):
    new_dp = [ceil(dp[i] / count[i]) for i in range(size)]
    
    max_num_index = new_dp.index(max(new_dp))
    count[max_num_index] += 1

print(max([ceil(dp[i] / count[i]) for i in range(size)]))