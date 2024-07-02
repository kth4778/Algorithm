from itertools import permutations

n,m = map(int,input().split())
lst = list(map(int,input().split()))
for i in sorted(list(set(list(permutations(lst,m))))):
    print(' '.join([str(w) for w in i]))