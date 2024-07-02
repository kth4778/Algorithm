from itertools import combinations_with_replacement

n,m = map(int,input().split())
lst = sorted(list(set(list(map(int,input().split())))))
for i in sorted(list(combinations_with_replacement(lst,m))):
    print(' '.join([str(w) for w in i]))