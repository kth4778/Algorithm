from itertools import combinations_with_replacement

n,m = map(int,input().split())
for i in combinations_with_replacement([i for i in range(1,n+1)],m):
    print(' '.join([str(w) for w in i]))