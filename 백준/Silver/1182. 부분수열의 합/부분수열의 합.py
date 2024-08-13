from itertools import combinations

n,s = map(int,input().split())
nums = list(map(int,input().split()))
answer = 0

for i in range(1,n+1):
    for j in combinations([p for p in range(n)], i):
        if sum([nums[w] for w in j]) == s:
            answer += 1

print(answer)