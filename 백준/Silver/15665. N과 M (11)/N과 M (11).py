from itertools import product

a,b = map(int,input().split())
nums = sorted(list(map(int,input().split())))

for i in sorted(list(set(list(product(nums,repeat=b))))):
    print(' '.join([str(w) for w in i]))