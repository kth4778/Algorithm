from itertools import combinations

a,b = map(int,input().split())
nums = sorted(list(map(int,input().split())))

for i in sorted(list(set(list(combinations(nums,b))))):
    print(' '.join([str(w) for w in i]))